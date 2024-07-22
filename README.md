# Cuppa Cake

Cuppa Cake is an e-commerce platform that sells a variety of cakes, cake jars, cupcakes, and cake pops. The website allows customers to browse through a range of items, place orders, and contact the business for enquiries.

The live site can be viewed [here](https://cuppa-cake-66d9c1594728.herokuapp.com/).

![Landing Page](/README_files/img/cuppa-cake-landing-page.png)

## Overview
Cuppa Cake is built with Django, a high-level Python web framework, and uses PostgreSQL for the database. The platform is hosted on Heroku and uses Cloudinary for static and media files storage.

## Table of Contents
- [Cuppa Cake](#cuppa-cake)
  - [Overview](#overview)
  - [Table of Contents](#table-of-contents)
  - [User Experience](#user-experience)
    - [Agile Methodology](#agile-methodology)
    - [User Epics \& User Stories](#user-epics--user-stories)
  - [Design](#design)
    - [Wireframes](#wireframes)
    - [Database Schema](#database-schema)
    - [Typography](#typography)
    - [Color Scheme](#color-scheme)
    - [Icons](#icons)
  - [Features](#features)
    - [Existing Features](#existing-features)
      - [General Navigation](#general-navigation)
        - [Navigation Bar](#navigation-bar)
        - [Landing Page](#landing-page)
        - [Header](#header)
        - [Footer](#footer)
          - [404 Page](#404-page)
      - [Authentication](#authentication)
        - [Registration](#registration)
        - [Login](#login)
        - [Logout](#logout)
      - [Profile](#profile)
        - [Profile Page](#profile-page)
        - [Edit Profile](#edit-profile)
      - [Products](#products)
        - [Product Page](#product-page)
        - [Search Products](#search-products)
        - [Filter Products](#filter-products)
        - [Product Details](#product-details)
        - [Add Product](#add-product)
        - [Edit Product](#edit-product)
        - [Delete Product](#delete-product)
      - [Bag](#bag)
        - [Bag Page](#bag-page)
        - [Add to Bag](#add-to-bag)
        - [Remove from Bag](#remove-from-bag)
        - [Adjust Quantity](#adjust-quantity)
      - [Checkout](#checkout)
        - [Checkout Page](#checkout-page)
        - [Payment](#payment)
        - [Order Form](#order-form)
        - [Order Confirmation](#order-confirmation)
      - [Contact](#contact)
        - [Contact Page](#contact-page)
        - [Contact Form](#contact-form)
      - [Newsletter](#newsletter)
        - [Newsletter Signup](#newsletter-signup)
  - [Future Features](#future-features)
  - [Technologies Used](#technologies-used)
    - [Languages](#languages)
    - [Libraries \& Frameworks](#libraries--frameworks)
    - [Tools](#tools)
    - [Databases](#databases)
    - [Hosting](#hosting)
    - [Version Control](#version-control)
  - [Testing](#testing)
    - [Manual Testing](#manual-testing)
    - [Automated Testing](#automated-testing)
    - [User Stories Testing](#user-stories-testing)
    - [Bugs](#bugs)
      - [Resolved Bugs](#resolved-bugs)
      - [Known Bugs](#known-bugs)
  - [Web Marketing](#web-marketing)
    - [Advantages](#advantages)
    - [Target Audience](#target-audience)
    - [Marketing Strategy](#marketing-strategy)
  - [SEO](#seo)
    - [Meta Tags](#meta-tags)
    - [Sitemap](#sitemap)
    - [robots.txt](#robotstxt)
  - [Deployment](#deployment)
    - [Heroku Deployment](#heroku-deployment)
  - [Credits](#credits)
    - [Content](#content)
    - [Media](#media)
    - [Acknowledgements](#acknowledgements)

## User Experience
### Agile Methodology
Cuppa Cake was developed using the Agile methodology, which emphasizes iterative development, collaboration, and flexibility. The site was divided into sprints, with each sprint focusing on specific features and user stories. The Agile methodology allowed for continuous feedback and improvements, ensuring that the final product meets user requirements and expectations.

### User Epics & User Stories
During the planning stage, several key epics were identified to structure the development process and ensure a comprehensive and user-centric design. Each epic is home to a series of user stories that define the scope and direction of the project. These stories are pivotal in guiding the development and ensuring that every feature contributes to a seamless and enjoyable user experience.

Each user story addresses the needs and expectations of our users and is organized within the project's kanban board, offering a detailed view of the development progress and priorities.

Below are the epics and user stories developed for Cuppa Cake, each aimed at enhancing the user experience and functionality of the platform:
1. User Registration & Authentication
    - User Registration
    - User Login
    - User Logout
    - Password Reset
2. Product Browsing & Search Functionality
    - Product Categories
    - Product Listing
    - Product Search
    - Product Filters
    - View Product Details
3. Product Reviews
    - View Customer Reviews
    - Review a Product
    - Edit a Review
    - Delete a Review
4. Shopping Cart & Checkout
    - Add to Cart
    - View Shopping Cart
    - Remove from Cart
    - Adjust Quantity
    - Proceed to Checkout
    - Enter Shipping Information
    - Enter Payment Information
    - Order Confirmation
5. Order Management
    - View Order History
    - View Order Details
    - Track Order Status
    - Cancel Order
    - Return Order
6. Admin Management
    - View Orders
    - Add Products
    - Remove Products
    - Edit Products
    - Manage User Accounts
7. Customer Support
    - Contact Form
    - FAQ Page
8. Marketing & Promotions
    - Email Newsletter Signup
    - Apply Discount Codes
    - Special Offers Page

## Design
### Wireframes

Wireframes were created using Figma to visualize the layout and design of the website. The wireframes provide a clear representation of the site's structure, navigation, and content, ensuring a consistent and user-friendly design.

![Wireframe Landing Page](/README_files/img/wireframe-landing-page.png)
![Wireframe Homepage](/README_files/img/wireframe-homepage.png)

### Database Schema
The database schema was created using dbdiagram.io. The schema was created to show the relationships between the different models in the database.
![Database Schema](/README_files/img/database-schema.png)

### Typography

The primary font used for Cuppa Cake is 'Lato', a sans-serif typeface that offers a clean and modern look. The font is used throughout the site for headings, paragraphs, and buttons, ensuring a consistent and professional design.

### Color Scheme

The color scheme for Cuppa Cake is inspired by the colors of cakes and desserts. The primary colors used are aqua, grey, pink, and white, creating a warm and inviting atmosphere. The colors are used throughout the site to highlight important elements, create contrast, and enhance the overall design.

### Icons

- [Font Awesome](https://fontawesome.com/) - Used for all icons on the site.

## Features
### Existing Features
#### General Navigation
##### Navigation Bar
The navigation bar is located at the top of the page and provides easy access to the main sections of the site. The navigation bar includes links to the home page, product categories, search functionality, user account, shopping cart, and contact page.
##### Landing Page
The landing page is the first page users see when they visit the site. The landing page includes a hero image, featured categories, and a call-to-action button to encourage users to explore the site.
##### Header
The header is located at the top of the page and includes the site logo, search bar, and user account options. The header is fixed at the top of the page, ensuring easy access to important features as users scroll through the site.
##### Footer
The footer is located at the bottom of the page and includes social media icons, address, and contact information.
###### 404 Page
A custom 404 page is displayed when users navigate to a page that does not exist. The 404 page includes a message informing users that the page is not found and a link to return to the home page.

#### Authentication
##### Registration
Users can create an account by providing their username, email address, and password. After registration, users can log in to their account to access additional features such as adding products to the shopping cart and placing orders.
##### Login
Users can log in to their account by providing their username and password. After logging in, users can access their account information, view order history, and manage their shopping cart.
##### Logout
Users can log out of their account by clicking the logout button. After logging out, users are redirected to the home page and must log in again to access their account.

#### Profile
##### Profile Page
Users can view and edit their profile information, including their contact number and address. The profile page also displays the user's order history and allows users to manage their shopping cart.
##### Edit Profile
Users can edit their profile information, including their contact number and address. After editing their profile, users can save the changes and update their account information.

#### Products
##### Product Page
The product page displays a list of products available for purchase. Users can view product details, add products to the shopping cart, and filter products by category.
##### Search Products
Users can search for products by entering keywords in the search bar. The search functionality allows users to find specific products quickly and easily.
##### Filter Products
Users can filter products by category to narrow down their search results. The filter functionality allows users to browse products by category, price, and other criteria.
##### Product Details
Users can view detailed information about each product, including product name, description, price, and images. The product details page also includes customer ratings.
##### Add Product
Admin users can add new products to the site by providing product information, including product name, description, price, and images. After adding a product, admin users can publish the product to the site.
##### Edit Product
Admin users can edit existing products by updating product information, including product name, description, price, and images. After editing a product, admin users can save the changes and update the product details.
##### Delete Product
Admin users can delete products from the site by removing the product from the database. After deleting a product, admin users can confirm the deletion and remove the product from the site.

#### Bag
##### Bag Page
The bag page displays a list of products added to the shopping bag. Users can view product details, adjust product quantities, and remove products from the bag.
##### Add to Bag
Users can add products to the shopping bag by clicking the "Add to Bag" button on the product details page. After adding a product to the bag, users can view the product in the shopping bag.
##### Remove from Bag
Users can remove products from the shopping bag by clicking the "Remove" button next to the product. After removing a product from the bag, users can update the shopping bag.
##### Adjust Quantity
Users can adjust the quantity of products in the shopping bag by entering the desired quantity in the quantity field. After adjusting the quantity, users can update the shopping bag.

#### Checkout
##### Checkout Page
The checkout page displays a summary of the order, including product details, shipping information, and payment information. Users can review the order details, enter shipping information, and proceed to payment.
##### Payment
Users can enter payment information, including credit card details, to complete the order. The payment form includes fields for credit card number, expiration date, and security code.
##### Order Form
Users can enter shipping information, including name, address, and contact number, to complete the order. The order form includes fields for shipping address, city, state, and postal code.
##### Order Confirmation
After completing the order, users receive an order confirmation with the order details. The order confirmation page displays a summary of the order and users can view their orders from thier profile.

#### Contact
##### Contact Page
The contact page displays contact information with a simple contact form. Users can send messages to the business by entering their name, email address, and message in the contact form.
##### Contact Form
Users can send messages to the business by entering their name, email address, and message in the contact form. After submitting the contact form, users receive a confirmation message.

#### Newsletter
##### Newsletter Signup
Users can sign up for the newsletter by providing their email address. After signing up, users receive email updates about new products, promotions, and special offers.

## Future Features
* Product Reviews:
    - Allow users to leave reviews and ratings for products.
    - Display customer reviews and ratings on the product details page.
    - Allow users to edit and delete their reviews.
* Minimum Order Quantity:
    - Set a minimum order quantity for products.
    - Display a message if the order quantity is below the minimum.

## Technologies Used
### Languages
- HTML
- CSS
- JavaScript
- Python

### Libraries & Frameworks
- Django
- Bootstrap

### Tools
- Git
- GitHub
- Visual Studio Code

### Databases
- PostgreSQL

### Hosting
- Heroku

### Version Control
- Git

## Testing
### Manual Testing

### Automated Testing

### User Stories Testing

### Bugs
#### Resolved Bugs
#### Known Bugs

## Web Marketing
### Advantages

### Target Audience

### Marketing Strategy

## SEO
### Meta Tags

### Sitemap

### robots.txt

## Deployment
### Heroku Deployment

## Credits
### Content

### Media

### Acknowledgements