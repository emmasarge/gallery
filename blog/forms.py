from django import forms
from .widgets import CustomClearableFileInput
from .models import BlogPost, BlogComment


class BlogForm(forms.ModelForm):
    """ Create form for blog posts """

    class Meta:
        model = BlogPost
        fields = (
            'blog_title',
            'blog_preview',
            'blog_content',
            'image_url',
            'image',
            )

    image = forms.ImageField(
                label='Image', required=False, widget=CustomClearableFileInput)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'border-full rounded-0'


class CommentForm(forms.ModelForm):
    """ Create comment form for blog posts """

    class Meta:
        # which model and which fields
        model = BlogComment
        fields = (
            'comment_title',
            'comment',
            )
