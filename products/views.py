
from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.db.models.functions import Lower
from django.db.models import Avg
from django.core.paginator import Paginator

from .models import Product, Category
from .forms import ProductForm
from reviews.models import Review


def all_products(request):
    """
    This view returns all the products on the site with
    sorting and search queries too.
    Got a hand with the pagination,
    here https://www.youtube.com/watch?v=wmYSKVWOOTM
    """
    products = Product.objects.all().order_by('id')
    search = None
    categories = None
    sort = None
    direction = None

    if request.GET:
        if 'sort' in request.GET:
            sortkey = request.GET['sort']
            sort = sortkey
            if sortkey == 'name':
                sortkey = 'lower_name'
                products = products.annotate(lower_name=Lower('name'))
            if sortkey == 'category':
                sortkey = 'category__name'

            if 'direction' in request.GET:
                direction = request.GET['direction']
                if direction == 'desc':
                    sortkey = f'-{sortkey}'
            products = products.order_by(sortkey)

        if 'category' in request.GET:
            categories = request.GET['category'].split(',')
            print(products)
            products = products.filter(category__name__in=categories)
            categories = Category.objects.filter(name__in=categories)

        if 'search' in request.GET:
            search = request.GET['search']
            if not search:
                messages.error(request,
                               "Please enter a search Criteria \
                               to search our products!")
                return redirect(reverse('products'))

            queries = Q(
                        name__icontains=search) | Q(
                        description__icontains=search)
            products = products.filter(queries)

    products_paginator = Paginator(products, 10)
    page_num = request.GET.get('page')
    page = products_paginator.get_page(page_num)
    sorting = f'{sort}_{direction}'

    context = {
        'page': page,
        'products': products,
        'search_term': search,
        'current_categories': categories,
        'sorting': sorting,
    }

    return render(request, 'products/products.html', context)


def product_details(request, product_id):
    """
    view returns all the details of each individual
    item on the site from the product_id
    Got a hand with the aggregation, here
    https://stackoverflow.com/questions/19138609/django-aggregation-sum-return-value-only
    Got a hand with the pagination,
    here https://www.youtube.com/watch?v=wmYSKVWOOTM
    """

    product = get_object_or_404(Product, pk=product_id)
    reviews = Review.objects.filter(product=product_id).order_by("id")
    avg_rating = Review.objects.filter(
                                        product=product_id).aggregate(
                                        avg=Avg('rating'))['avg']
    reviews_paginator = Paginator(reviews, 5)
    page_num = request.GET.get('page')
    page = reviews_paginator.get_page(page_num)

    context = {
        'product': product,
        'reviews': reviews,
        'page': page,
        'avg_rating': avg_rating,
    }

    return render(request, 'products/product_details.html', context)


@login_required
def add_product(request):
    """ Adds a product to the store """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that')
        return redirect(reverse('home'))

    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            product = form.save()
            messages.success(request, 'Successfully added product!')
            return redirect(reverse('product_details', args=[product.id]))
        else:
            messages.error(request,
                           'Could not add product to site. \
                           Please ensure form is valid!')
    else:
        form = ProductForm()

    template = 'products/add_product.html'
    context = {
        'form': form,
    }

    return render(request, template, context)


@login_required
def edit_product(request, product_id):
    """ edits a product on the site """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    product = get_object_or_404(Product, pk=product_id)
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            messages.success(request, f'Successfully updated {product.name}!')
            return redirect(reverse('product_details', args=[product.id]))
        else:
            messages.error(request,
                           f'Failed to update {product.name}. \
                           Please ensure form is valid!')
    else:
        form = ProductForm(instance=product)
        messages.info(request, f'You are editing {product.name}')

    template = 'products/edit_product.html'
    context = {
        'form': form,
        'product': product,
    }

    return render(request, template, context)


@login_required
def delete_product(request, product_id):
    """ deletes a product on the site """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    product = get_object_or_404(Product, pk=product_id)
    product.delete()
    messages.success(request, 'Product deleted!')

    return redirect(reverse('products'))