# Testing #
---


## Table of Contents ##
---

* 1. [Validation](#validation)
* 2. [Manual testing](#manual)
        * [Viewing and Navigation](#viewing)
        * [Registration and Accounts](#registration)
        * [Product sorting and searching](#searching)
        * [Purchase and Checkout](#purchase)
        * [Admin and Store Management](#admin)
        * [Stripe](#stripe)
        * [Security](#security)
        * [Acessibility](#acessibility)
* 3. [Issues](#issues)


<a name="validation"></a>
## Validation ## 
---
This project was created on Chrome but has been tried on a Samsung galaxy, iphone, Macbook Pro, MacBook Air, Lenovo and large desktop. It works on Explorer and Safari too though I have been having issues with styling on Safari. 

**HTML**

[**W3C Markup Validator Service**](https://validator.w3.org/) for testing HTML.
![HTML](readme/html-test.png)

**CSS**

[**W3C CSS Validator Service**](https://jigsaw.w3.org/css-validator/) to test CSS.

![CSS](readme/css-test.png)

**Javascript**

[**JSHint**]() to validate Javascript files.



**Python**

Gitpod built-in linter and [**PEP8**] to test Python files.
[pip3 -m flake8](readme/pep8.png)


<a name="manual"></a>
## Manual Testing ## 
---

**1. Viewing and Navigation**

As a a visitor I want this site to intuitive

* Expected: Site is clean with easy-to-use flow.
* Testing: Found navigation bar and homepage cta to see products and create purchase
* Result: site had everything visible and accessible. Safari not displaying same as Chrome.

**2. Registration**

I want to easily find where to register and for the process to be fast

* Expected: Admin icon or cta
* Testing: Found icon and registered easily with form
* Result: Registration was quick and an email was sent to my account to validate the username_email

**3. Product Search**

User can search site for any product with filter and search bar

* Expected: Search bar in a visible location
* Testing: Looked up benign words like nude and is and the search bar worked
* Result: Search bar works and detects categories and text in details

**4. Purchase and Checkout**

User can securely purchase their item or save item to cart

* Expected: Intuitive funnel to checkout
* Testing: Logged in and out of account to see if my products would still be in cart, they were. Added multiple products, deleted products from cart
* Result: Functionality is successful

**5. Admin and Store management**

Admin and super user can log into the site or visit the admin page to use CRUD on projects
* Expected: admin can have access to more secure functions
* Testing: Logged in as admin, had more access than regular user, added products and edited products. 
* Result: Admin and super user can adjust products and blogs in admin settings.
* [superuser](readme/superuser.png)

**6. Stripe** 
Secure payment

* Expected: user can log in credit card details to secure a payment 
* Testing: User completes checkout funnel and adds payment with false card 42424242424242 424 4242. Payment is successful and email is sent. Checked webhooks in stripe and they are successful. Checked webhook success on [stripe](readme/webook.png)
* Result: functioning and secure payment method


**7. Security** 
* Expected: Admin and superusers have privelged and secure access to security
* Testing: Log out of admin account and force page in url. Luckily when logged out, I could not access admin priveleges
* Result: Secure site for business owners and admin.

**8. Accessibility** 
* Expected: site performs well on various devices but with a mobile-first focus
* Testing: used an ipad 6, iphone 10, iphone7, macbook pro, lenovo think pad.
* Result: the site was looking fine but some input forms aren't translating to desktop. 

* [Product page mobile](readme/product-mobile.png)
* [Product page desktop](readme/product-page.png)
* [Forms](readme/forms.png)