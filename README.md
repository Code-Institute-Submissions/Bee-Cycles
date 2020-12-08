# Bee Cycles
## [Live Heroku App Link](https://bee-cycles.herokuapp.com/)
## [GitHub repository Link](https://github.com/todorr92/Bee-Cycles) 
#### Bee Cycles webshop was designed, built and deployed by Slobodan Todorovic as his final project for the Code Institute Full Stack Web Development diploma. The purpose of Bee Cycles online shop is to be the first website built for this shop. This website is designed to create a beautifully intuitive, smooth and effortless online shopping experience.
## Table of Contents
1. UX
2. Features
3. Information Architecture
4. Technologies Used
5. Testing
6. Deployment
7. Credits

## UX
### Goal
### User Stories
### As a Shopper
1. As a shopper I want to view list of products and services.
2. As a shopper I want to view product and service details so that I can identify price, description, product rating and product image.
3. As a shopper I want to easily view total of my purchases at any time.
4. As a shopper I want to sort the list of available products by best rated, price and categorically.
5. As a shopper I want to search for a product/service by name or description.
6. As a shopper I want to view items in my bag to be puchased.
7. As a shopper I want to adjust the quantity of individual items in my bag.
8. As a shopper I want to easily enter my payment information.
9. As a shopper I want to feel my personal and payment information is safe and secure.
10. As a shopper I want to view an order confirmation after checkout.
11. As a shopper I want to recieve an email confirmation after checking out.
### As a Site User
1. As a user I want to easily register for an account.
2. As a user I want to easily log in or out.
3. As a user I want to easily recover my password in case I forget it.
4. As a user I want to recieve and email confirmation after registering.
5. As a user I want to have a personalized user profile.
### As a Shop Owner
1. As a owner I want to add a product.
2. As a owner I want to edit a product.
3. As a owner I want to delete a product.

## Design Choices
### Font
[](/media/readme-images/fonts.png)
+ Primary font 'Arial' was chosen for the main text of the site because of it clear readability, clean style and complementary contrast with the secondary font. This font also looks good in uppercase with a little extra letter spacing, and so could serve nicely as a sub heading as well.
+ The secondary font 'Permanent Marker' was chosen for the site name as it helps site name to stand out, but yet keep that simplicity.
### Icons
+ In order to keep the site uncluttered only a few icons were utilized.
[](/media/readme-images/nav-icons.png)
+ The search icon, shopping cart and user icons were used in the navigation bar as they are conventionally used in this setting and would be what the user expects to see.
+ If the user is logged in as Admin, user icon is changing to njinja user icon
[](/media/readme-images/nav-icons.png)
+ The Facebook and Yelp logo icon is included in the footer to lead visitors to Bee Cycles facebook and Yelp page.
[](/media/readme-images/products-icons.png)
+ Euro icon was used as currency, Tag icon was used for Category, star as a product rating, and some basic edit and delete icons.
[](/media/readme-images/quantity-icons.png)
+ Basic plus and minus icons were used for quantity.
### Colours
[](/media/readme-images/quantity-icons.png)
+ Orange: #FFC107
+ Smoky White: #E3E1E1
+ Dark Grey: #343A40
+ Black: #000000
+ Above colour palette was chosen based on owners chosen logo and catchy site name, so I've decided to keep everything in those colours.
### Styling
+ Curved cornes were applied on Buttons and Product cards.
+ Text shaddow and brightness were applied on Category cards on Home Page to make text more easier to read. 
### Wireframes
#### These wireframes were created using [Balsamiq](https://balsamiq.com/) during the Scope Plane part of the design and planning process for this project.
+ [Home](/media/wireframes/Home.png)
+ [Products](/media/wireframes/Products.png)
+ [Product Details](/media/wireframes/)
+ [Shopping Bag](/media/wireframes/Shopping-Bag.png)
+ [Checkout](/media/wireframes/Checkout.png)
+ [Checkout Success](/media/wireframes/)
+ [Profile](/media/wireframes/Profile.png)
## Features
### Existing Features
#### Elements on every page
##### Navbar:
[](/media/readme-images/navbar.png)
+ The navbar features on every page
+ The navigation bar features Bee Cycles logo on the far left, and site name Bee Cycles in the middle of the page which both links to the home page of the site.
+ In desktop view on the center of the navbar is a list of the product pages: All Products, Bikes, Accessories and Special Offers. All of the links apart of All Products are a dropdown menu which lists out the categories of shop products.
+ Beside navigation links, on desktop view a search bar is located just on the top of navigation links, searched word will be searched in both product name and description.
+ On the right side of the navbar are the links to shopping cart and dropdown on user icon.
+ A user who is currently logged out will also see options to register or log into the website.
+ A user who is logged in will see options to view their account page or log out.
+ Superuser or Admin will have additional option Product Managment where new product can be added.
+ The shopping cart icon is located to the far right of the navigation bar. Once a user has added at least one item to their cart a bold font will be applied to cart and amount for specific product or products.
[](/media/readme-images/mobile-nav.png)
+ In tablet and mobile view the logo and site name Bee Cycles are hidden, and Home link is added to burger menu.
+ The shopping cart icon is displayed at the right of the navigation bar, and the burger icon to display the full navigation menu is on the far left, with search bar and user icon in the middle of navigation bar because that is where a user would expect to find it.
##### Footer
[](/media/readme-images/footer.png)
+ The footer features on every page.
+ The footer background of dark grey and orange text was chosen to maintain same colour palette.
+ Location shown in footer is linked to Google Maps, email can be sent using default mail provider and telephone is just for information.
+ The footer also includes a link to Bee Cycle active social media channel on Facebook and Yelp. If/When Bee Cycles activates their other social medial channels on twitter/instagram/pinterest then these can be added to the icons in the footer.
## Hero images taken from Pixabay, freeimages, Pexels
## TinyPNG used to compress images
## Logo font is Permanent Marker