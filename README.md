# Sprint Designs

## Introduction
- Sprint Designs is a fully responsive e-commerce site built using Django. Sprint Designs is a fictional company based in Dublin that offers a B2B service. Sprint Designs provides businesses with robust and easy to customize web templates, as well as graphic designs completely custom to the businesses needs. Users can purchase templates and designs, view recent projects, read testimonials and also create an account. Site admin have certain privileges such as adding,removing or updating products.

- Sprint Designs is my fifth and final project as part of the Code Institute Full Stack Software Development course. Unfortunately, due to time constraints there are are many of the projects where I wish to have developed better.

![Screenshot of responsive site](./docs/am-i-responsive.png)

* [Live Site](https://sprint-designs.herokuapp.com/)

## Table of Contents

* [User Experience](#Introduction)
    * [Site Goals](#Site-Goals)
    * [User Stories](#User-Stories)
    * [Strategy Plane](#Strategy)
    * [Scope Plane](#Scope)
    * [Structure Plane](#Structure)
    * [Skeleton Plane](#Skeleton)
        * [Wireframes](#wireframes)
        * [Seo](#Seo)
    * [Surface Plane](#Surface)
        * [Design](#Design)
    * [Features](#Features)
    * [Marketing](#Marketing)
    * [Testing](#Testing)
    * [Technologies](#Technologies)
    * [Bugs](#Bugs)
    * [Deployment](#Deployment)
    * [Credits](#Credits)
## UX

### User Stories
### **Admin**
- As a Site Owner, I want to be able to add, update and delete products from the store.

- As a Site Owner, I want to be able to add, update and delete recent projects.

- As a Site Owner, I want to be able to add, update and delete blog posts.

- As a Site Owner, I want to be able to view all reviews when viewing a product, so that I can delete reviews if needed.

### **Registered User**
- As a User, I want to be able to view my account profile, so that I can look at my purchase/order history.

- As a User, I want to be able to register for an account, so that I can store my details.

- As a User, I want to be able to add a review to a product that I have purchased, so that I can share my feedback.

- As a User, I want to be able to view a review form when viewing a product, so that I can add feedback about the product.

### **Default User**
- As a User, I want to be able to view a list of products, so that I can add them to my shopping bag.

- As a User, I want to be able to view an individual product on it's own page, so that I can read the information about the product more clearly.

- As a User, I want to view a error page if I visit a page that does not exist on the site, so that I know to head back to an existing page on the site.

- As a User, I want to be able to sign up to a newsletter, so that I can keep up to date with the business.

- As a User, I want to be able to make an order without needing to create an account, so that I can make one off orders.

- As a User, I want to view a projects page, so that I can view the past work completed by the business.

- As a User, I want to be able to view my shopping bag so that I can add or remove any items.

- As a User, I want to view a contact page, so that I can get in touch with the business directly.

- As a User, I want to view testimonials, so that I can add a new testimonial and read about other peoples experience.

- As a User, I want to view blog posts, so that I can read the blogs posted by the company.

- As a User, I want to view a error page if I visit a page that does not exist so that I know to navigate back to the site.

### Site Goals
- To provide users with a site where they can purchase web templates, and designs to help grow their online presence as a business.

- To promote custom built web templates using efficient code that allows business owners to easily add content to their site.

- To promote custom designs that are created using best practices and represent the buyers vision.

### Strategy
- Sprint Designs is a B2B e-commerce site that allows users to purchase web templates (Built using HTML, CSS and Javascript), and designs that are fully custom to the businesses needs. Admin users have extra functionality on the site, including access to adding, removing and updating products.

### Scope
Features to be included:

* Site navigation: Provide users with an easy route of navigation to each page.

* Responsive design: Ensure content and site navigation is presented correctly to the user from mobile devices to desktop screen sizes.

* Purchase products: Users can purchase both web template and design products by adding the item to their shopping bag and filling in their details into the checkout form.

* Testimonials: Users can add their own testimonial to the site.

* Blogs: Users can read blog posts created by the staff at Sprint Designs.

* Review: Users are provided with a form to give feedback and a rating on a store product.

* Projects: Users can read recent projects that Sprint Designs have successfully completed.

* Error page: An error page should be displayed to the user if they try to visit a page that does not exist.

### Structure

### Skeleton

#### Wireframes

* Wireframes were created for each feature such as adding and editing projects, products and blogs as an admin user, and adding a testimonial, adding and removing items from the shopping bag as a regular user.

* Wireframes allowed the development of the project to be smooth a process and acted as a visual aid. Attached below are some of the key features and their wireframes that were needed to ensure the project was planned and developed successfully.

**Navigation**
![Navbar wireframe](./docs/wireframes/navbar.png)

**Footer**
![Footer wireframe](./docs/wireframes/footer.png)

**Products**
![Products wireframe](./docs/wireframes/web-product-desktop.png)

**Homepage**

- The homepage displays to the user exactly what Sprint Designs has to offer - templates and designs. Users are provided with a clear and digestible amount of information about the service through sections such as "What we do". The homepage also provides users a way to form an idea about the quality of service by scrolling down to the testimonial slider.

- [Home Page Wireframe](./docs/wireframes/homepage-desktop.png)

- [Home Page Mobile Wireframe](./docs/wireframes/homepage-mobile.png)

**Products**

- The products page is split into two different templates. Users can view a page with all template products or view a page with all design products. Users can then continue to view an view a product separately by following the link to the single product page.

- [Templates Products Page Wireframe](./docs/wireframes/web-product-desktop.png)

- [Templates Products Page Mobile Wireframe](./docs/wireframes/web-product-mobile.png)

- [Designs Products Page Wireframe](./docs/wireframes/design-product-desktop.png)

- [Designs Products Page Mobile Wireframe](./docs/wireframes/design-product-mobile.png)

- [Single Product Wireframe](./docs/wireframes/product-detail-desktop.png)

- [Single Product Mobile Wireframe](./docs/wireframes/product-detail-mobile.png)


#### Database Schema
![Database schema](./docs/sprint-designs-db.png)

**Testimonials**
* The Testimonials app will allow users to add testimonials to the site by supplying a name and comment into the form field.

**Category**
* The Category model allows the site admin to assign a category to the product they wish to add to the site.

**Product**
* The Product model uses the Category model as a foreign key so that the site admin can assign categories to the product. Products also have a type attribute where the site admin can choose whether the product being added is either a design or web template.

**Review**
* The Review model uses both the User and product models as foreign keys in order to connect a user profile to a product review. Users can provide their review and product rating, which will then be stored as fields inside the review model.

**Project**
* The Project model makes use of the Category model as a foreign key so that site admin can assign categories to the recent projects.

**User & Profile**
* The Profile model is connected to a User instance through a one-to-one field so that a user who registers for an account is connected to a single profile.

**Order & Line item**
* The Order model has a User profile connected as a foreign key along with all the necessary details needed when processing an order. The Line item model also holds a foreign key to an instance of the Order model so that multiple order items can relate to a single order.

**Blogs**
* The Blog model consists of title, name, content, image url and image fields.


### Surface

#### Design
- "Poppins" and "Red Hat Display" were the chosen font families to be used for this project. The Poppins font family is used for the page headings, while the Red Hat Display font family is being used for every other element. The Poppins font family allowed for the headings to stick out from other text elements while the Red Hat Display font provided a professional look for the rest of the elements.

- ![Colour palette](./docs/palette.png) Screenshot of colour palette is provided by [Coolors](https://coolors.co/)


### Features

#### Navigation
- The navigation menu is different depending on what kind of user is logged in. Admin users have access to the testimonials link which gives them access to delete any testimonials written by customers.

- The navigation menu is also split into two sections, page links and shopping/profile links.

- On smaller screen sizes, the navbar collapses into a more mobile friendly layout.

![Navigation](./docs/wireframes/navbar.png)
![Mobile Navigation](./docs/wireframes/navbar-mobile.png)

#### Homepage
- The homepage provides users with a short intro about Sprint Designs. Users can view the multiple services provided by the company and can also read all the reviews written by other customers.

![Homepage](./docs/wireframes/homepage-desktop.png)
![Homepage mobile](./docs/wireframes/home-mobile.png)

#### Testimonials
- Admin users have access to the testimonials archive page where they can view and delete all testimonials.


![Testimonials](./docs/wireframes/testimonials-desktop.png)
![Testimonials Mobile](./docs/wireframes/testimonials-mobile.png)

- Users who would like to add their own testimonial can do so by filling in the form with the required information. Once the user has successfully added their testimonial it will be added to the slider on the homepage.

![Testimonials Form](./docs/wireframes/add-testimonial-desktop.png)
![Testimonials Form Mobile](./docs/wireframes/add-testimonial-mobile.png)

#### Products
- The products page allow users to view all the products sold on the site. Users can visit the templates page which will display all products relating to templates. Or they can visit the designs products page which lists all design products.

![Templates Products](./docs/wireframes/web-product-desktop.png)
![Templates Products Mobile](./docs/wireframes/web-product-mobile.png)
![Design Products](./docs/wireframes/design-product-desktop.png)
![Design Products Mobile](./docs/wireframes/design-product-mobile.png)

#### Product Detail & Product Review
- As users browse through the array of products they can view a single product to get a better look at the product that they might purchase. Users can also choose to whether or not they would like to leave a review for the product.

- Admin users have access to all reviews and can delete reviews if they wish.

![Single Product](./docs/wireframes/product-detail-desktop.png)
![Single Product Mobile](./docs/wireframes/product-detail-mobile.png)

#### Add Product & Edit Product
- Admin users have access to add a new product. Admin users will be presented with a form that they must fill out in order to successfully add a new product.

![Add Product](./docs/wireframes/add-product-desktop.png)
![Add Product Mobile](./docs/wireframes/add-product-mobile.png)

- Admin users also have access to update any existing products by filling in the edit product form.

![Edit Product](./docs/wireframes/edit-product-desktop.png)
![Edit Product Mobile](./docs/wireframes/edit-product-mobile.png)

#### Shopping bag
- The shopping bag feature allows users to view, add, edit, and delete all the products that they have added to their shopping bag.

![Shopping Bag](./docs/wireframes/bag-view-desktop.png)
![Shopping Bag Mobile](./docs/wireframes/shopping-bag-mobile.png)

#### Checkout
- When the user is ready to purchase a product they can visit the checkout page. Users will be required to fill in information such as their email, address and credit card information in order to checkout successfully.

![Checkout](./docs/wireframes/checkout-view-desktop.png)
![Checkout Mobile](./docs/wireframes/checkout-view-mobile.png)

#### Checkout Success
- When a user has successfully purchased a product they will be brought to the checkout success page. Users will be able to view their order information.

![Checkout Success](./docs/wireframes/checkout-success-desktop.png)
![Checkout Success Mobile](./docs/wireframes/checkout-success-mobile.png)

#### Blogs
- The blogs page is an archive for all blog posts created by Sprint Designs.

![Blogs](./docs/wireframes/blogs-desktop.png)
![Blogs Mobile](./docs/wireframes/blogs-mobile.png)

- Admin users have the ability to create, update, and delete blog posts.

![Add Blog](./docs/wireframes/add-blog-desktop.png)
![Add Blog Mobile](./docs/wireframes/add-blog-mobile.png)
![Edit Blog](./docs/wireframes/edit-blog-desktop.png)
![Edit Blog Mobile](./docs/wireframes/edit-blog-mobile.png)

- The single blog view allows users to have a better view of an individual blog post.

![Single Blog](./docs/wireframes/single-blog-desktop.png)
![Single Blog Mobile](./docs/wireframes/single-blog-mobile.png)

#### Projects
- The projects feature was created to allow users to view past work at Sprint Designs.

- The projects archive page allows users to browse through all of the recent projects.

![Projects](./docs/wireframes/projects-desktop.png)
![Projects Mobile](./docs/wireframes/projects-mobile.png)

- The single project view allows users to isolate a single project for a better read.

![Single Project](./docs/wireframes/project-detail-desktop.png)
![Single Project Mobile](./docs/wireframes/project-detail-mobile.png)

- Admin users have access to create, update and delete all projects.

![Add Project](./docs/wireframes/add-product-desktop.png)
![Add Project Mobile](./docs/wireframes/add-project-mobile.png)

![Edit Project](./docs/wireframes/edit-project-desktop.png)


#### Profile
- If a user has created an account they gain access to their own user profile.

- The user profile page allows users to fill in their information and also view any of their past orders.

![User Profile](./docs/wireframes/profile-desktop.png)
![User Profile Mobile](./docs/wireframes/profile-mobile.png)


#### Login and Logout
- Users who have already created an account can log in to and logout of their account when visiting the site.

![User Login](./docs/wireframes/user-login-form-desktop.png)
![User Login](./docs/wireframes/user-login-mobile.png)
![User Logout](./docs/wireframes/user-logout-desktop.png)
![User Logout Mobile](./docs/wireframes/user-logout-mobile.png)

#### Sign up
- Regular users can choose whether or not they would like to register for an account. By registering, users can expect to gain access to new features, such as leaving a review on a product and having their own user profile.

![User Sign Up](./docs/wireframes/user-registration-form-desktop.png)
![User Sign Up Mobile](./docs/wireframes/user-registration-mobile.png)

#### Contact page
-The contact page provides users with all the necessary contact details needed to get in touch with the business.

![Contact Page](./docs/wireframes/contact-desktop.png)
![Contact Page Mobile](./docs/wireframes/contact-mobile.png)

#### 404 Error Page
- The 404 error page notifies the user if they have visited a page on the site that does not exist. This lets the user know that they should follow the link back to an existing page on the site.

![404 Error Page](./docs/wireframes/error-desktop.png)
![404 Error Page Mobile](./docs/wireframes/error-mobile.png)

#### Footer
- The footer provides users with contact details as well as the option to sign-up to the company newsletter.

![Footer](./docs/wireframes/footer.png)

### Marketing
- A [Facebook page](https://www.facebook.com/Sprint-Web-111680221643056/) was created to allow Facebook users to follow the page to find out more information about Sprint Designs. Users can find out more about any upcoming products being added by reading posts on the Sprint Design Facebook page.

- Users can subscribe to the Sprint Designs newsletter to keep up to date with the business.

- A Facebook post was created to let promote news products that will soon be available on the store.

![Facebook Post](./docs/post.png)

- Keyword research:
    - Website
    - Design
    - Professional
    - Business
    - Buy web templates
    - Buy graphic designs

### Testing

#### Manual Testing

#### Superuser / Admin
- **As a Site Owner, I want to be able to add, update and delete products from the store.**
    - Products can be added via the django admin panel or by clicking the "+" icon in the navigation menu and filling in the add product form. When the user has provided the correct data, a new model instance is created and the user is redirected to the new product, followed by a success message that the new product has been created.

    - Products can be deleted by clicking the delete product button below the product description. When the product has been successfully deleted, a message will appear to notify the user that the product was deleted and the model instance is removed from the database and the user is redirected to the products page.

    - Products can be edited/updated by clicking the edit product button below the product description. The user is brought to the edit product form where they can update the product information. Once the product is updated a success message is displayed to the user is redirected to the individual product.

- **As a Site Owner, I want to be able to add, update and delete recent projects.**
    - Projects can be added by following the Add Project link on the projects archive page. When the user has provided the correct data, a new model instance is created and the user is redirected to the projects archive page, followed by a success message that the new project has been created.

    - Projects can be edited/updated by clicking the edit project button below the project description. The user is brought to the edit project form where they can update the project information. Once the project is updated a success message is displayed to the user is redirected to the projects archive page.

    - Projects can be deleted by clicking the delete project button below the project description. When the project has been successfully deleted, a message will appear to notify the user that the project was deleted and the model instance is removed from the database and the user is redirected to the projects archive page.

- **As a Site Owner, I want to be able to add, update and delete blog posts.**

    - Blogs can be added by admin users by clicking the Add Blog button on the blogs archive page. When the user has provided the correct data, a new model instance is created and the user is redirected to the blogs archive page, followed by a success message that the new blog has been created.

    - Blogs can be updated by clicking the delete blog button below the blog content. When the blog has been successfully deleted, a message will appear to notify the user that the blog was deleted and the model instance is removed from the database and the user is redirected to the blog archive page.

    - Blogs can be deleted by clicking the delete blog button below the blog content. When the blog has been successfully deleted, a message will appear to notify the user that the blog was deleted and the model instance is removed from the database and the user is redirected to the blogs archive page.

- **As a Site Owner, I want to be able to view all reviews when viewing a product, so that I can delete reviews if needed.**

    - Admin users have access to the delete review button for all reviews and choose whether or not they would like to remove a review created by another user.

#### Registered User
- **As a User, I want to be able to view my account profile, so that I can look at my purchase/order history.**

    - When the user is signed in and clicks the user icon in the navigation menu they will be brought to their own unique user profile. The user profile page was tested to see if orders would display in the users order history.

- **As a User, I want to be able to register for an account, so that I can store my details.**

    - The user sign up form was tested by entering invalid data into the forms input fields. Incorrect data such as passwords not matching would display an error message to the user.

    - Users who have filled in the sign up form correctly will then be told to verify their email address. Once the user verifies their email address they will be asked to sign in again.

- **As a User, I want to be able to add a review to a product that I have purchased, so that I can share my feedback.**

    - Registered users gain access to the review form for each product on the site. The review form was tested by filling the form with data and clicking the submit button. A new model instance is created when a user has successfully added a review and a success message appears to notify the user that the form submission was successful.

    - Users who have not registered for an account cannot view the review form and will be asked to log in to their account to add a review.

#### Default User
- **As a User, I want to be able to view a list of products, so that I can add them to my shopping bag.**

    - All products are displayed using Bootstrap columns and responsive CSS to ensure that each product is displayed with its description and image side-by-side.

    - The products page was also tested by creating a product without uploading an image. The result is that the product uses the default product image.

- **As a User, I want to be able to view an individual product on it's own page, so that I can read the information about the product more clearly.**

    - The individual product page was tested by clicking the more info button attached to each product on the products page. The result is that the user is then brought to a page that displays the product image, title, category, description, and price.

- **As a User, I want to view a error page if I visit a page that does not exist on the site, so that I know to head back to an existing page on the site.**

    - The error page was tested by visiting a page on the site that does not exist. The result is that a message is displayed to the user notifying them that they have visited a page that does not exist and a button to take them back to the homepage.

- **As a User, I want to be able to sign up to a newsletter, so that I can keep up to date with the business.**

    - The mailchimp newsletter signup form was tested by adding an email to the form and clicking the subscribe button. The result is that a new contact is added to the list of contacts in the mailchimp account.

- **As a User, I want to be able to make an order without needing to create an account, so that I can make one off orders.**

    - The above user story was tested by making a purchase without being logged into an account. The result is that the user is brought to the checkout success page and an email is sent to them with their order details.

- **As a User, I want to view a projects page, so that I can view the past work completed by the business.**

    - The projects page user story was tested by viewing the projects archive page. The result is that eah project is displayed in its own column using the bootstrap responsive grid system.

- **As a User, I want to be able to view my shopping bag so that I can add or remove any items.**

    - The above user story was tested by adding multiple products to the shopping bag and then viewing the shopping bag. The result is that the user is able to view all the items that they have added to their shopping bag, and can choose if they would like to remove items from their shopping bag.

    - The user story was also tested by viewing the shopping bag without having added any items. The result is a message to notify the user that their bag is empty and that they can view store products by clicking either the "Shop our templates", or "Shop our designs" links.

- **As a User, I want to view a contact page, so that I can get in touch with the business directly.**

    - The contact page was tested by clicking the "Contact Us" link in the main site navigation menu. The result is that the user is brought to the contact page where they have access to contact details.

- **As a User, I want to view testimonials, so that I can add a new testimonial and read about other peoples experience.**

    - The testimonials user story was tested by filling in the required information into the add testimonial form. The result is that a new testimonial is added to the testimonial slider on the homepage.

    - If a user does not enter the required information into the add testimonial form, an alert message will display to let the user know that the must enter a value into the required input fields.

- **As a User, I want to view blog posts, so that I can read the blogs posted by the company.**

    - The blog posts user story was tested by visiting the blog posts archive page. The result is that all blog posts are displayed using the bootstrap responsive grid system.

#### W3C Validator

*[W3C Validator](https://validator.w3.org/) was used to ensure that there are no errors in any of the html markup.

#### Pep8 Validator

* All files with the .py file extension were tested using the pycodestyle linter to ensure that the code is clean and follows best practices.

#### Jigsaw Validator

* [Jigsaw Validator](https://jigsaw.w3.org/css-validator/) was used to validate all css style sheets.

#### JS Hint


### Technologies
- **HTML**
    - HTML provided the project with the markup needed to in order to display content to the users.

- **CSS**
    - CSS was used to add custom styles to the project.

- **JavaScript**
    - jQuery
    - [Slick slider](https://kenwheeler.github.io/slick/)

- **Python**
    - Python was used to handle the business logic and backend of the project.
    - asgiref==3.5.2
    - backports.zoneinfo==0.2.1
    - boto3==1.24.74
    - botocore==1.27.74
    - dj-database-url==0.5.0
    - Django==3.2
    - django-allauth==0.41.0
    - django-countries==7.2.1
    - django-crispy-forms==1.14.0
    - django-environ==0.9.0
    - django-storages==1.13.1
    - gunicorn==20.1.0
    - jmespath==1.0.1
    - oauthlib==3.2.0
    - Pillow==9.2.0
    - psycopg2-binary==2.9.3
    - PyJWT==2.4.0
    - python3-openid==3.2.0
    - pytz==2022.2.1
    - requests-oauthlib==1.3.1
    - s3transfer==0.6.0
    - sqlparse==0.4.2
    - stripe==3.5.0

- **Django**
    - [Django](https://www.djangoproject.com/) is a high-level Python web framework that was used for the development of the project.

- **Bootstrap**
    - [Bootstrap](https://getbootstrap.com/) is a front-end web framework which provided the layout and responsiveness of the site.

- **Google Fonts**
    - [Google Fonts](https://fonts.google.com/) provided both the Red Hat Display and Poppins font for the project.

- **Heroku**
    -[Heroku](https://id.heroku.com/login) provided hosting for the project.

- **Font Awesome**
    - [Font Awesome](https://fontawesome.com/) All icons display throughout the project are generated using font awesome.

- **Favicon**
    - [Favicon.io](https://favicon.io/) Provided the favicon used for the project.

- **AWS S3 Bucket**
    - [AWS S3 Bucket](https://aws.amazon.com/) was used to store and serve static and media files for the live project.

- **Balsamiq**
    - Balsamiq was used to create the wireframes for the project.

### Bugs

- For loop counter layout. Originally, the templates and designs products pages were supposed to have a layout where every second product would have a flipped version of the product layout. To try and achieve this layout I used the forloop.counter built-in template tag to check if the for loop counter was an even number. The result was that the for loop indexing was causing the product images to display beside the incorrect product information.

    **Originally intended layout:**
![Original layout](./docs/wireframes/web-product-desktop.png)

#### Fixed Bugs
### Deployment

### Credits
  * [Pexels](https://www.pexels.com/) for the images used throughout the project.

  * [Am I Responsive](http://ami.responsivedesign.is/) to create a display of the project on multiple devices.

  * [Favicon.io](https://favicon.io/) allowed me to generate a favicon for the project.

  * [Slick Slider JS](https://kenwheeler.github.io/slick/) was used to generate the testimonial slider on the homepage.
