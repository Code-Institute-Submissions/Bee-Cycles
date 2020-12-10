# Bee Cycles - Testing details

### [README.md](readme.md)
### [Bee Cycles](https://bee-cycles.herokuapp.com/)
## Table of Contents
1. [User Stories Testing](#user-stories-testing)
2. [Manual Testing](#manual-testing)
3. [Code Validation](#code-validation)
4. [Browser Testing](#browser-testing)
5. [Bugs Discovered](#bugs-discovered)
6. [Further Testing](#further-testing)

## Code Validation
### [Autoprefixer](https://autoprefixer.github.io/)
+ Added prefixes to CSS for different browsers.
### [CSS Validator](https://jigsaw.w3.org/css-validator/)
+ Couple of errors showed on base.css.
![](media/testing-images/css-errors.png)
+ Errors appeared because I wanted to override default `ul` styling as shown on image.
![](media/testing-images/default-ul.png)
+ Also couple of warnings were shown but all of them were due to prefix vendors.
### [CSS Formatter](https://www.cleancss.com/css-beautify/)
+ Formatted base.css.
### [HTML Validator](https://validator.w3.org/nu/)
#### Home Page
+ Had a few errors due to `li` item being direct child of `nav` element.
![](media/testing-images/home.png)
+ Fixed that by wrapping `li` elements in one `ul` element and added custom css styling.
![](media/testing-images/home-fixed.png)
#### Products Page
![](media/testing-images/products-warnings.png)
+ Had a two warnings regarding script type.
![](media/testing-images/products-fixed.png)
+ Fixed that by removing script type from code.
#### Product Details Page
![](media/testing-images/product-details-warning.png)
+ Only one warning regarding script type.
![](media/testing-images/product-details-fixed.png)
+ Fixed that by removing script type from code.
#### Cart Page
![](media/testing-images/cart-warning.png)
+ One warning regarding script type.
![](media/testing-images/cart-fixed.png)
+ Fixed that by removing script type from code.
#### Checkout Page
![](media/testing-images/checkout.png)
+ No errors there.
![](media/testing-images/checkout-success.png)
+ No errors on checkout-success page.
#### Add/Edit Page
![](media/testing-images/add-product.png)
![](media/testing-images/edit-product.png)
+ No errors here.
#### Profile Page
![](media/testing-images/profile-page.png)
+ No errors.
#### Sign Up/Login Page
![](media/testing-images/sign-up.png)
![](media/testing-images/login.png)
+ No errors.