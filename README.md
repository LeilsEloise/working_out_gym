# Working Out Gym - Project 4

A Django-powered health and fitness application designed to allow users to make purchases on nutrition and/or fitness plans, business merchandise and products. These plans and other purchases will show up in the user's profile. The app will also promote social interaction amongst it's users on the Discussion Board and encourage feedback through a form on it's About page. 

## Live Site

- **Live Application:** 
  

- **GitHub Repository:** 
  https://github.com/LeilsEloise/working_out_gym

---

# Contents

# 1. UX

- Project Overview
- Project Goals
- User Goals
- Developer and Business Goals
- Design Choices
- Project Value & Purpose
- User Stories
- Wireframes

# 2. Features

- Existing Features
- Features Left to Implement

# 3. Technologies

# 4. Testing

- HTML Validation
- CSS Validation
- Javascript Validation
- Python Validation

# 5. Development & Deployment

- How to run this Project locally

# 6. Credits and Acknowledgements

- Content
- Media
- Code
- Acknowledgements

# 7. Troubleshooting, Debugging & Tidy-up

- Issues with code
- Issues with styling

---

# 1. UX

## Project Overview

Working Out Gym is a full-stack Django web application that allows its users to browse available fitness and nutrition plans and make purchases on these; they can combine one fitness and nutrition plan at a time or choose only a nutrition or fitness plan. The purchased plans will then show up in the user's profile which will be held on a seperate app in the Project. In addition to being able to purchase fitness/nutrition plans, the users will be able to view an individual page of the business' merchandise where they will be able to add multiple items to a shopping cart and checkout to purchase, or be able to buy single items from a single click mechanism from the Products page itself. There will be a seperate app for Checkout. Users will also be encouraged to engage in the wider community of users socially through means of an app within the Project for a Discussion Board; which will allow users to create, edit and delete posts, make comments on their own or others' posts and vote on these individual posts and comments. Users will be able to provide feedback to the site admin through means of a feedback form on the About app within the Project.

---

## Project Goals

To provide the site owner with a Full Stack web application which attracts users who are looking to improve their health and fitness through changing their lifestyles. The Project should produce a multi-page web application that is easy to navigate and is attractive to people already involved in the fitness community or whom are looking to join, in order to gain regular customers of the business and users of the application.

---

## User Goals

The target audience for this site is anyone looking to improve their health and fitness, purchase merchandise and socialise with the wider community of users on the app.

User Goals are:

- Be able to access and view all available fitness and nutrition plans on one page with descriptions about each and the ability to add a fitness and/or nutrition plans to a shopping cart for purchase.
- To be able to access and view a 'Products' page containing a number of merchandise items which can be purchased individually instantly through means of a 'Buy' button or have the option to add multiple items from the page into a cart to then purchase. 
- To be able to provide reviews on previously purchased products.
- Be able to register, login and logout of the page so that purchased plans and past shopping orders can be viewed in a profile.
- When logged into their account, they are able to access the Discussion Board page, where they will be able to see other users' past posts which they can then comment on. They will be able to create, delete and edit posts they make themselves. 

---

## Developer and Business Goals

The business wants to create a web application which showcases their fitness and nutrition plans, with purchase options, to people wanting to improve their fitness. So that they will purchase these plans and other products, such as merchandise. They also want to create a community from these users, by means of a Discussion Board, where they will be able to moderate user posts and comments for safety. 

Site Owner goals are:

- The ability to logon as a superuser and be able to add new nutrition and fitness plans or moderate existing ones.
- While logged in as superuser, they can moderate products listings on the Merchandise page; creating new product listings or removing sold out stock.
- Be able to moderate the Homepage content: leading paragraph and testimonials section.
- Be able to logon to admin panel and see all options, including one for feedback forms where they will be able to review the data inputs to the form on the database.
- Be able to moderate user posts and comments on the discussion board.
- To be able to create posts on the Discussion Board, providing useful tips and updates to their user base.

---

## Design Choices

- Neutral colours and simple layouts to be attractive to everyone.
- Easy to navigate web application, so users can see all services available and make use of these.
- Promotes social interaction through comments and posts on the Discussion Board, having a clear divide between past posts and the options for user to create, edit and delete their own posts.
- Allows users to give feedback through means of reviews on the products and in general on a feedback form located on Homepage.
- Web app functionality is responsive.
- Purchase options are provided where applicable and work seamlessly to give the user the best experience and encourage them to want to use the app.

---

## Project Value & Purpose



---

## User Stories

### User Story 1: Site User can View Homepage and is Clearly Informed of Purpose

- As a **site user**  I want **to be able to access the homepage of the site**  so that **I can find a new fitness community**

### Acceptance Criteria

- Homepage is attractive to target audience and clearly defines its purpose.
- Homepage contains links within its opening paragraph info to the services its detailing.
- Homepage has Navbar which contains links to the other sections of the webpage.

### Tasks

- Create an index.html page which satisfies this.
- Create an app for the Homepage and wire up accordingly.

---

### User Story 2: Site User can Interact with the Discussion Board

- As a **site user**,  I want **to be able to access the Discussion Board from the Navbar on the Homepage**, so that **I can make comments on existing posts from other users and also make posts, edit those posts and delete those posts**

### Acceptance Criteria
- User can access the Discussion Board from the Navbar.
- User can view and open posts from a list of posts on the Discussion Board - both from themselves and other users.
- User can make comments on other user's posts and edit and delete these comments, but not other user's comments.
- Users can make their own posts, edit and delete these posts.

### Tasks
- Create a new app for the Discussion Board and wire this up to my project accordingly.
- Ensure new models are created for 'comment' and 'post'
- Come up with new template for the Discussion Board.

---

### User Story 3: Site Owner can Moderate the Discussion Board

- As a **Site Owner**, I want **to be able to see posts and comments from the Discussion Board in the Admin Panel** so that **I can moderate the comments and posts from the site users**

### Acceptance Criteria
- Site Owner has two options for 'comments' and 'posts' in the Admin Panel
- Site Owner can approve comments and posts
- Site Owner can delete comments and posts.
- Site Owner can make posts.

### Tasks
- Wire up 'comments' and 'posts' to the Admin Panel
- Give Site Owner ability to approve and delete comments and posts.

---

### User Story 4: Site User can View and Buy Fitness and/or Nutrition Plans

- As a **Site User** I want **to be able to view a page with all fitness and nutrition plans** so that **I can purchase a nutrition and/or fitness plan**

### Acceptance Criteria
- Site User can access the Fitness and Nutrition's Plan page from the Homepage and be taken to a page which clearly lays out the different nutrition and fitness plans on offer.
- Site User can click each of the plans to view more information and then has the option to either buy or add to cart.
- Site User has the option of combining a fitness plan and nutrition plan by being able to purchase one from each category.

### Tasks
- Create a new app for the Fitness and Nutrition Plans and wire this up into the Project accordingly.
- Implement pay system into the project to allow users to purchase the plans.

---

### User Story 5: Site Owner can Moderate Fitness and Nutrition Plans

- As a **Site Owner** I want **to see the Fitness and Nutrition Plans in the Admin Panel** so that **I can moderate these as and when required**

## Acceptance Criteria
- Site Owner can login to the Admin Panel and see options for 'Fitness Plans' and 'Nutrition Plans'
- When accessing either option they have the ability to add new plans and edit and delete existing ones.

## Tasks
- Wire up fitness and nutrition plans to the admin panel.

---

### User Story 6: Site User can View and Make Purchases on the Merchandise Page

- As a **Site User** I want **to be able to access a page for Merchandise** so that **I can view products and make purchases and post and view reviews on the products**

### Acceptance Criteria
- Site User can access a page for Merchandise from the Navbar.
- Site User can view a list of products on the Merchandise page which displays a name and price, with option to add to cart or buy.
- User can successfully checkout items in cart or when selected to buy singularly.
- Users can view existing product reviews and make their own.
- Users can view all products added to the 'Shopping Bag'.

### Tasks
- Create a new app for the Merchandise page.
- Add products listings using Fixtures.
- Give users option to buy.
- Give users the option to post and view reviews on the products.
- Give users the option to view and purchase products from a shopping bag through 'Shopping Bag' application.

---

### User Story 7: Site Owner can Moderate Products on the Merchandise Page

- As a **Site Owner** I want **to be able to login to the Admin Panel and view a section for products** so that **I can moderate the products listings when required**

### Acceptance Criteria
- Site Owner can login to the Admin Panel and see option to add and change products for Merchandise Page.
- Site Owner can successfully add, edit and delete a product listing.

### Tasks
- Wire up 'products' for Merchandise into the admin.py file.

---

### User Story 8: Site User can Successfully Login and Has Profile

- As a **Site User** I want **to be able to login to the website** so that **I can view my current fitness and nutrition plans and see past orders.**

### Acceptance Criteria
- User can register an account with email address, username and password.
- User can successfully login to their account using email/username and password.
- User can then access their profile once logged in and view plans or orders.
- User receives an email after registering

### Tasks
- Setup alluth and configure.
- User plans are mapped to profile.
- User orders are mapped to profile.

---

### User Story 9: Site User can Make Queries on Products through their Categories on Merchandise

- As a **site user** I can **view a specific category of product** so that **I can filter results to tailor what I am looking for**

### Acceptance Criteria
- User can quickly find products on the Merchandise page by their category.

---

### User Story 11: Site User can Sort Multiple Categories Simultaneously

As a **site user** I want **to sort multiple categories simultaneously** so that **I can quickly find products based on pricing and name**

### Acceptance Criteria
- User can find best priced products in a specific category
- User can sort the products in a category by name

---

### User Story 12: Site User can Search for a Product by Name

As a **site user** I want **a search facility on products** so that **I can search them by name**

### Acceptance Criteria
- When user searches for a product by name, i.e. womens top, this will return all products with this name.
- Easily see what is selected and the number of results.

---

## Wireframes

(Need to implement static folders for images but not ready to do this just yet)

### Homepage Wireframe

![Wireframe Homepage](/static/images/Wireframes/Homepage%20Wireframe.jpg)

---

### Discussion Board Wireframe

![Wireframe Discussion Board](/static/images/Wireframes/Discussion%20Board%20Wireframe.jpg)

---

### Fitness and Nutrition Plans Wireframe

![Wireframe Fitness and Nutrition Plans](/static/images/Wireframes/Fitness%20Nutrition%20Plan%20Wireframe.jpg)

---

### Merchandise Wireframe

![Wireframe Merchandise](/static/images/Wireframes/Merchandise%20Wireframe.jpg)

---

# 2. Features

## Existing Features

### Model - template to add models into later once created 

#### Fields
- 
- 
- 
- 

#### Admin Enhancements
- 
- 
- 

#### Authentication
- Django Allauth implemented
- 
- 
- 

#### Styling & Static Files

#### Cloudinary Integration

- 

---

# 3. Technologies Used

### Language & Frameworks

- Python 3.12
- Django 4.2
- HTML5
- CSS
- Javascript
- Stripe

### Libraries & Packages

- Django Allauth
- Django Crispy Forms
- Crispy Bootstrap 5
- Django Summernote
- Cloudinary
- WhiteNoise
- Gunicorn
- Pillow
 
### Tools & Platforms

- Git & Github
- Heroku
- PostgreSQL (Code Institute Database)
- Visual Studio Code
- SQLite (local database)
- Cloudinary
- AWS

---

# 4. Testing

- 
- 
- 
- 

## HTML Validation

- 

![HTML Validation]()

---

## CSS Validation

- 

![CSS Validation]()

---

## Javascript Validation

- 

![JS Validation]()

---

## Python Validation

- 

--- 

# 5. Development Process

## Initial Setup and Commit to Github

1. I create a local folder called working_out_gym for the project in my computer and open it in my IDE.

2. In my IDE, I start up a .venv virtual environment with Python v3.12.

3. I then set-up a repo in GitHub with the same name and connect to my workspace using the cmds provided on the repo page of GitHub:

echo "# working_out_gym" >> README.md
git init
git add README.md
git commit -m "first commit"
git branch -M main
git remote add origin https://github.com/LeilsEloise/working_out_gym.git
git push -u origin main


4. Once our workspace and repository are set-up, the next thing we need to is install Django and create a new Django project. So I run the following cmd in my new workspace terminal to set up Django:

pip3 install 'django<4'


5. Once I receive confirmation in the terminal that this is successfully installed, I can then use the following cmd in the terminal to create the project in the current directory:

django-admin start project working_out_gym .

- However, this has errored - Django failed to install in .venv but I have resolved this now using powershell, see file desktop/documents/vs-code-projects/cmds/powershell handy for details


6. After running cmds in powershell I can now see my Django project has been created in my IDE.


7. Now I am create a .gitignore file in the root of my project directory and add the following:

*.sqlite3
*.pyc
__pycache__
env.py
.venv/
.github/


8. Next I run the page on my local server using the below command to ensure all is working which it is:

python3 manage.py runserver

![Django Working Local page](/static/images/Initial%20Setup/Screenshot%20Django%20Install%20successful%20local%20page%20test%201.png)

   
9. I stop running my local server and then run my migrations using:

python3 manage.py migrate

10. Next I create a superuser so that I can log into the admin console, using:

python3 manage.py createsuperuser

- Setting username to: PersonalTrainer
- Setting a fake email address
- Setting a secure password

11. Next I make my initial commit to GitHub using: 

git add .
git commit -m "Initial commit."
git push

---

## Authentication and Homepage Setup

1. I now want to look at how I am going to achieve my user stories for account registration and logging in. I have decided to use Django-allauth as opposed to building my own authentication system. I am going to install it using:

 pip3 install django-allauth==0.50.0

2. I check that my settings.py file has the below at the very top of the file above 'from pathlib import Path':

import os

3. I then head to the allauth documentation @https://docs.allauth.org/en/latest/installation/quickstart.html and copy the code to my settings.py file that I need as per the link.

4. And the code below it for my urls.py file into that:

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts', include('allauth.urls')),
]

5. I also add SITE_ID = 1 to my settings.py file under the AUTHENTICATION_BACKENDS 

6. Once I have updated settings.py and urls.py I then need to run migrations to update the database since I have added some new apps:

python3 manage.py migrate


7. I am now going to run the server with python3 manage.py run server and then navigate to the admin panel and login with the superuser account.

8. Then click 'change' on 'Sites', and update the domain of the default site to workingoutgym.example.com and change the display name to 'Working Out Gym' and then hit 'Save':

![Setting Up Domain Name](/static/images/Initial%20Setup/Screenshot%20setting%20up%20the%20domain%20name.png)

9. By default allauth will send confirmation emails to any new accounts, we need to temporarily log those emails to the console so we can get the confirmation links. To do this, I set the EMAIL_BACKEND setting in settings.py to:

EMAIL_BACKEND = 'Django.core.mail.backends.console.EmailBackend'


10. I am also going to copy in some additional settings from the completed 'Boutique Ado' Project:


ACCOUNT_AUTHENTICATION_METHOD = 'username_email'
ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_EMAIL_VERIFICATION = 'mandatory'
ACCOUNT_SIGNUP_EMAIL_ENTER_TWICE = True
ACCOUNT_USERNAME_MIN_LENGTH = 4
LOGIN_URL = '/accounts/login/'
LOGIN_REDIRECT_URL = '/success'

11. Now all the settings are in place, I need to test that my allauth is working as it should be. I run my pages on my local dev server and then navigate to /accounts/login but this takes me to a 404 not found page.

After asking ChatGPT why we are seeing this error, they have advised that the below line in the error is the giveaway:

accounts signup/
accounts login/

- It says there is no slash between 'accounts' and 'login' so it is actually looking for '/accounts login/' and not '/accounts/login/'. It advised me to update my URL pattern to:

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),
]

12. I have updated my URL patterns as advised and then restarted my server but now I am seeing a different error when I load my app on my local serve:

"Page not found (404) Request Method: GET Request URL: http://127.0.0.1:8000/success Using the URLconf defined in working_out_gym.urls, Django tried these URL patterns, in this order: admin/ accounts/ The current path, success, didn’t match any of these. You’re seeing this error because you have DEBUG = True in your Django settings file. Change that to False, and Django will display a standard 404 page."

13. I ask ChatGPT why this would be and they advised that it is now this line in my settings that is the culprit:

LOGIN_REDIRECT_URL = '/success'

- After a successful login, Django is doing what I told it to do and redirect the user to '/success' but I currently do not have a /success url or view defined so Django is saying 'I don't know what /success is" > 404. Ask ChatGPT recommends updating my settings.py file to:

LOGIN_REDIRECT_URL = '/'

This is the best temporary solution until I have built up my app and the views etc.

14. I have updated my settings.py file but still getting a 404 error on /accounts/login so have asked ChatGPT why this would be and they advised that my urls.py only contains the following patterns:

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),
]

And there is no URL for '/' so Django loads the homepage but cannot find it. The fix for this would be to create a simple homepage.

I do this now using:

python manage.py startapp gymsub

15. I then add this to INSTALLED_APPS in settings.py and create a view for the new homepage in the gymsubs/views.py file:

from django.shortcuts import render

def home(request):
    return render(request, 'index.html')

16. I then create the templates folder in the new app folder and create a new index.html file and use the code ChatGPT has given me for a temporary homepage:

<h1>Working Out Gym</h1>

{% if user.is_authenticated %}
    <p>Welcome, {{ user.username }} 👋</p>
    <a href="/accounts/logout/">Logout</a>
{% else %}
    <a href="/accounts/login/">Login</a>
    <a href="/accounts/signup/">Sign up</a>
{% endif %}

17. I then need to wire up the new view to my urls.py file in my project folder as below:

from django.contrib import admin
from django.urls import path, include
from gymsub.views import home

urlpatterns = [
    path('', home, name='home'),
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),
]

18. I have saved this and restarted my server and tried to run my webpage locally. I can now see the homepage and I am already logged in so have logged out and can now see options for logging in and I am on the accounts/login page. Once I have logged in as the superuser, I can see that allauth is working successfully as I am now prompted with an email verification message upon login:

![email verification msg at login](/static/images/Authentication/Screenshot%20AllAuth%20working%20successfully.png)

19. Because I created this user before AllAuth was installed, I will need to create and confirm an email address for them manually. I log into the admin panel as the super user and click 'Change' on 'Emails':

![email admin panel change](/static/images/Authentication/Screenshot%20AllAuth%20Email%20Admin%20Panel.png)

20. On the next page, I can see the e-mail I set for the superuser but that it is not verified:

![email not verified](//static/images/Authentication/Screenshot%20AllAuth%20not%20verified%20.png)

21. If I click this and go to the next page, I can then tick the verified and primary boxes and then hit 'SAVE':

![verifying email and making primary](/static/images/Authentication/Screenshot%20verifying%20email%20and%20making%20primary.png)

22. Now when I look at this in emails I can see that the email address for my superuser is set to primary and verified:

![email now verified and set to primary](/static/images/Authentication/Screenshot%20super%20user%20email%20now%20verified.png)

23. If I login as my superuser, I am now longer presented with the message about email verification:

![verified email on login](/static/images/Authentication/Screenshot%20verified%20email%20address.png)

24. I am going to freeze the requirements of my project with pip3 freeze > requirements.txt

25. Next, I am going to set up the templates directory in the base of my directory and create a subfolder within that for allauth templates ready for writing my front-end code:

![templates for allauth](/static/images/Authentication/Screenshot%20final%20update%20git%20commit.png)

26. Now I will commit my code and move on to my templates.

---

## Templates

1. I want to create a copy of all the allauth templates from .pip-modules/lib/python 3.12/site-packages /allauth/templates/* into my newly created folder under templates/allauth so I run the below in my terminal:

cp -r ../.pip-modules/lib/python 3.12/site-packages /allauth/templates/* ./templates/allauth/

However, the cmd fails to run. I get the below error:

 cp -r ../.pip-modules/lib/python3.12/site-packages/allauth/templates/* ./templates/allauth/
cp : Cannot find path 
'C:\Users\leila\OneDrive\Desktop\Documents\vscode-projects\.pip-modules\lib\python3.12\site-packages\allauth\templates'      
because it does not exist.
At line:1 char:1
+ cp -r ../.pip-modules/lib/python3.12/site-packages/allauth/templates/ ...
+ ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    + CategoryInfo          : ObjectNotFound: (C:\Users\leila\...lauth\templates:String) [Copy-Item], ItemNotFoundException  
    + FullyQualifiedErrorId : PathNotFound,Microsoft.PowerShell.Commands.CopyItemCommand


2. I ask ChatGPT why this would be and they advise that the path only exists in Code Institute / Heroku-style Linux environments and doesn't exist on Windows locally. It advises that my project uses .venv so the correct path is:

.venv\Lib\site-packages\allauth\templates

The correct powershell command would be: cp -r .\.venv\Lib\site-packages\allauth\templates\* .\templates\allauth\

3. I have ran this now and it has worked so now I can customise the allauth templates at will. I am going to delete the folders within templates/allauth for openid and test as I won't be customising these.

4. I now need a base.html file in my base templates directory so I create this now.

5. I am going to use Bootstrap to style my Project so I will go to Bootstrap.com and get a starter template: https://getbootstrap.com/docs/5.1/getting-started/introduction/

I copy the code into my base.html file I have just created in my base templates folder.

6. I am going to edit the base template slightly so it works for my webpage, I will start with updating the title and removing the h1 element: 

![Base html title and h1 removal](/static/images/Templates/Screenshot%20base%20html%20title%20and%20h1%20removal.png)

7. I am then going to take the scripts from the bottom of the file and place these at these within the head so they load as early as possible and give the user the best possible experience:

![Script moved to head](/static/images/Templates/Screenshot%20script%20move%20to%20head.png)

8. Finally I am going to add {% load static %} at the top of the page for when I need to load in my static files later on. I save the file and commit the changes.

9. Following Code Institute's example, I will organise everything into blocks. I will wrap my meta content in a block, also while I am here I am going to add a line borrowed from Code Institute so that our content works with Edge:

![Base html Code Institute Code and Organisation](/static/images/Templates/Screenshot%20base%20html%20first%20meta%20block.png)

10. I will then add blocks in around  CSS and the JavaScript and add in extra blocks where necessary for the extra Meta, CSS and Javascript we will load in later:

![Blocks in base.html for js css and extra](/static/images/Templates/Screenshot%20blocks%20in%20base%20html%20for%20js%20css%20and%20extra%20.png)

11. I will also add in a block within the title tag which allows me to add an extra chunk of text to my page title if I want to:

![Block for extra title](/static/images/Templates/Screenshot%20block%20extra%20title.png)

12. Within the body, I create a new header with classes of 'fixed-top' and 'container-fluid' to ensure that it sticks to the top of the page also a new div with a class of 'message-container' and wrap it in an if messages template tag. I have borrowed this from Code Institute and acknowledged in my code:

![Base html Code Institute Code and Organisation](/static/images/Templates/Screenshot%20base%20html%20body%20update.png)

13. Again using Code Institute's code, I add a block under the existing code inside the body for a block page header - this acts as an additional header on pages that extend beyond the base template in case I want to add something at the top of the pages but underneath the main header. I also add a block for the main page content as well. And finally a a block JavaScript that will load at the end of the body of the template:

![Base template final blocks](/static/images/Templates/Screenshot%20base%20template%20final%20blocks.png)

---

## Renaming 'gymsub' app to 'home'

1. I am going to rename gymsub to home so I can follow Code Institute's practise that they used for their Boutique Ado Project. I have renamed the gymsub (app) folder to home. I have also added an additional folder to 'templates' in the app directory, called 'home', and then moved index.html into it. I will have to update some code now to reflect this. I first update INSTALLED APPS in settings.py:

![Installed apps update](/static/images/Folder%20Rename/Screenshot%20installed%20apps%20update%20rename%20folder.png)

- I updated the apps.py file so the gymsub references were now 'Home':

from django.apps import AppConfig


class HomeConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'home'

- I have updated the views.py file as below so it goes to the new subfolder in the path:

from django.shortcuts import render

Create your views here.
def home(request):
    return render(request, 'home/index.html')

- Once these changes are done, I can then use Code Institute's practise of extending the base template into my existing index.html template. Now that I have created a base.html template, I can do this. I am going to borrow Code Institute's code for this as below - I will come to edit this later..

{% extends "base.html" %}

{% load static %}

{% block content %}
    <h1 class="display-4 text-success">It works!</h1>
{% endblock %}

- I will also add a docstring to my view for the Homepage so it is more apparent what it is.

2. I have then created a urls.py file in my app directory with the code as below;

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),
    path('', include('home.urls')),
]

3. Finally, I am going to add both the route templates directory and my custom allauth directory to the template directorys setting in settings.py:

            os.path.join(BASE_DIR, 'templates'),
            os.path.join(BASE_DIR, 'templates', 'allauth'),

4. Once I have made and saved the changes, I run my local server and can see page is rendering as expected so can commit changes. 

---

## Static Files directory - CSS

1. I want to add images into my project so create my 'static' folder in the root of my project, creating folders for css, js, images. Within my css folder I create a style.css file and create a test.js file in the js folder. I also drag and drop the folder containing all my development screenshots into the new image folder from File Explorer:

![Static Files directory setup](/static/images/Static%20Directory/Screenshot%20Static%20directories%20initial%20setup.png)

2. Once CSS is in place, I go to my project settings.py file and build the path for my subdirectory static so I can link to files in the static directory from a template: STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static'), ]

3. I need to add some styles to be applied to my Homepage in order to test that CSS is working. I do this quickly - I will ammend once I know it is working and I can then tweak accordingly. I also update my base.html and add a reference to the css stylesheet:

![Base html css link update](/static/images/Static%20Directory/Screenshot%20adding%20css%20stylesheet%20link%20ref%20to%20base.html.png)

4. I will now reload my page on my local server and see if the css is being applied.

5. The page is completely blank on my local server but I can see a 304 error about CSS in my terminal. I cancel running the server and then run:

python manage.py collectstatic

- I am asked if I want to overwrite the files, which I say 'yes' to. However, in the terminal I see an error:

"raise ImproperlyConfigured("You're using the staticfiles app "
django.core.exceptions.ImproperlyConfigured: You're using the staticfiles app without having set the STATIC_ROOT setting to a filesystem path."

- I go into my settings.py file in my project directory, working_out_gym, and set the below for STATIC_ROOT:

STATIC_ROOT = BASE_DIR / "staticfiles"

- I run collectstatic again and this time it runs without any errors. I run my page locally again and check to ensure that css is now being served but it is still blank. I take a closer look in Devtools and can see that it is applying style.css and it is using the index.html template to load Home. The index.html file is basically empty apart from the DTL blocks so I input some code to this so we can then test css properly.

![index.html update](/static/images/Static%20Directory/Screenshot%20index.html%20update.png)

6. Now when I refresh my page, I can see the updated text now showing but it still doesn't look like CSS is applying, I am going to go back to my templates and sort these out first and come back to

![index.html rendering](/static/images/Static%20Directory/Screenshot%20index%20html%20loading%20correctly.png)

7. I am going to add my Navbar into my base.html file:

  <header class="container-fluid fixed-top bg-gray border-bottom">
    <div class="container py-3">
      <a class="navbar-brand brand" href="/">Working Out Gym</a>
    </div>
  </header>

8. If I refresh my page, I can see a navbar now, however, it's not quite how I would like it to be. I want to get my chosen font for my Navbar which will say 'Working Out Gym' and then use that font for any headings on my other pages. To do this, I navigate to https://fonts.google.com/ and then look for 2 x fonts which will work on my page. I have chosen Boldonse - which will be used for the Navbar text and my headers. From the same font family, I will use PT Serif for my smaller texts. I have added the Google Font code to the head of my base.html:

![Google Fonts added to base.html](/static/images/Static%20Directory/Screenshot%20googlefonts%20added%20to%20base.html.png)

9. I now want to make some changes to my current Navbar so that I can start styling this according to my wireframes. I am going to use the same code I used for my Navbar on the Good Newspaper Project and just tweak it accordingly:

![Navbar Code from Good Newspaper](/static/images/Static%20Directory/Screenshot%20Navbar%20code%20Good%20Newspaper.png)

9. I then tweak this code accordingly, updating the brand text and adding further a class blocks under the Nav collapsible bar section for the other pages that I will eventually come to add over the course of the Project:

![Navbar Code Initial Update](/static/images/Static%20Directory/Screenshot%20Navbar%20Code%20initial%20update.png)

10. I also add in the CSS code used for the Navbar classes in the code:

![Navbar CSS Project 3](/static/images/Static%20Directory/Screenshot%20navbar%20css%20from%20project%203.png)

11. Then still in my style.css file, I look at the styles being applied under 'brand' and 'heading' styles. In my .heading class, I update the font-family to 'Boldonse' and the brand class looks okay. However, I take the opportunity to update the font-family being applied to the .body class to the preferred font of: "PT Serif", serif:

![CSS Font Update](/static/images/Static%20Directory/Screenshot%20css%20font%20update.png)

12. I have reloaded my page but I am receiving an error:

NoReverseMatch at /
'working_out_gym' is not a registered namespace

13. I troubleshoot with ChatGPT who advises that this code in my base.html is wrong:

{% url 'working_out_gym:home' %}

- I check my URL patterns in urls.py and can see that I have the following set-up for 'home':

    path('', home, name='home'),

- Therefore, I need to update this in the DTL on my base.html, I update this now to:

{% url 'home' %}

- I also need to update the emptry DTL tags for the other page URL's to just be #, i.e.:

href="#"

- I stop my server and restart and see how the page looks now. The styles and Navbar are now looking as I would like them to be:

![CSS Font Update](/static/images/Static%20Directory/Screenshot%20css%20font%20update.png)

14. I want to make my Navbar and main brand text slightly bigger. I remove the .brand class from the span in my navbar containing the main Navbar text for 'Working Out Gym'. I create a new style class in my css for .navbar-heading and apply the following styles to this:

.navbar-heading {
  font-family: "Boldonse"; system-ui; 
  font-weight: 700;
  font-size: 4rem;
}

15. Now when I refresh the page, the Navbar text is much bigger, as I would like it to be. Now I want the background colour of the navbar to be a slightly dark grey, but not too dark that it stops the text from standing out. In my css file, I update my .dark-bg class to	#3b3b3b and apply this class to the Nav element in my base.html. I hard refresh my page and can see this being applied now. 

16. I want to make the static links for 'Register' and 'Login' in the Navbar be black in font when not being hovered over. So I add the following class in style.css:

.nav-link {
    color: black;
}

- I also want them to use the same font as the main text in the Navbar. In the new .nav-link style container, I add a new style for: font-family: "Boldonse"; system-ui

- Now when I refresh my page I can see the font is updated on my auth links.

- I would like to also tweak my collapsible nav links and menu so it looks more uniform with everything else. I add my .nav-link class to the a elements for my collapsible nav links. This updates the font. 

- I then realise that I would prefer if the collapsible nav links and menu where at the right of the navbar and the authentication links were at the start. in the base.html code, I amend the div classes for each of their containers to be end-0 and start-0 respectively. I also remove the white background class and replace with dark-bg class in the div containing the collapsible nav links. 

- I save and hard refresh the page and this is looking much more like it:

![Navbar styling finished](/static/images/Static%20Directory/Screenshot%20navbar%20styles.png)

17. Finally, to finish with my base.html file for appearances, I need to add a social media footer. To save time, I am going to copy over the code I used in Project 3 and then tweak it accordingly. I will also add the Font Awesome link into my head element so it adds the logos:

![Footer in base html](/static/images/Static%20Directory/Screenshot%20footer%20base.html.png)

18. I add the Bootstrap class 'fixed-bottom' to my footer element so that it will stick to the bottom of the page on base.html:

![Footer fixed to bottom](/static/images/Static%20Directory/Screenshot%20footer%20fixed.png)


19. I want the 'Register' and 'Login' buttons to have more space to the left of them, I am going to make the 'Working Out Gym' text in the Navbar slightly smaller by changing the font-size on the .Navbar-heading class styles I made earlier. I will reduce it from 4rem to 3.5rem: 

![Smaller Navbar Heading text](/static/images/Static%20Directory/Screenshot%20smaller%20navbar%20heading.png)

---

## Homepage Content

1. Now that my base.html file is more or less complete for now, I will add some content to my homepage. To start with, I search Pexels for some free images that I will be using throughout my Project. I download these, acknowledging each as I go along and then add these to my images folder in the Project.

2. Once these are added in, I will look to add the one I have chosen to the main section of my index.html file so its the first thing presented to the user:

% block content %}
<div class="container mt-5 pt-5">
  <img src="/static/images/Homepage/pexels-anete-lusina-4793215.jpg" class="main-image image-fluid" alt="Homepage Main Image - Man Exercising with Weights">
  <p class="leading-p">Homepage is rendering ✅</p>
</div>
{% endblock %}

3. When I check my page, the image is way too large so I add a new class of .main-image and apply styles to this class in css to resize the image:

![Main Homepage Image too Small](/static/images/Homepage%20Content/Screenshot%20image%20too%20small%20homepage.png)

4. I increase the size on my css style as below:

.main-image {
    width: 950px;
    height: auto;
}

- Now the image looks much better and I can look to center it now as well. Before I do, I copy the media queries code from Bootstrap docs into my css so I can update later as I believe the image being so large on the desktop screen won't work for smaller screens so will update these once I am happy with main page. I add the mx-auto and d-block Bootstrap classes to my main image element on my Homepage and this has centered it now:

![Main Homepage Image Centered](/static/images/Homepage%20Content/Screenshot%20Homepage%20Image%20fixed.png)

5. Finally I will update the leading paragraph content and reposition this so it fits in with the main image by adding the mx-auto and d-block classes to the p element in index.html. I also add a class of max-width to the leading-p class in css. Once I have done this it looks much better:

![Main Homepage Image Centered](/static/images/Homepage%20Content/Screenshot%20Homepage%20Image%20fixed.png)

6. I will leave the Homepage as is for now and come back later once I have added a database to the page and add a feedback form at the bottom. For now, I will commit my code to Github, as a few things have been added, and then move onto creating and deploying my Heroku App.

7. I will run a collectstatic, after adding all images to the project, then I will run:

git add .
git commit -m "Updated static folders with images and ran collectstatic"
git push origin main

---

## Heroku Setup

1. I login to Heroku.com and from my personal dashboard, gone to 'New' > 'Create new app':

![Heroku Create New App](/static/images/Homepage%20Content/Screenshot%20Homepage%20Image%20fixed.png)

2. I give my app the name of 'working-out-gym', chosen Europe as my location as it's my closesy region and then selected 'Create App':

![Heroku Naming App and Choosing Region](/static/images/Heroku/Screenshot%20Heroku%20App%20Name%20and%20Region.png)

3. In the newly created app, I have gone to settings and then Config Vars, and hit Reveal Config Vars. Within there I have then added the DISABLECOLLECTSTATIC key

4. Back in VS Code, I have updated my code for deployment. In the terminal I have ran the command to install gunicorn:
   pip3 install gunicorn~=20.1

5. Once this is installed, I have then add the new package to the requirements file:
   pip3 freeze --local > requirements.txt

6. I have created a Procfile in the root of my folder structure and then checked my .wsgi file in my working_out_gym project folder to confirm the correct syntax for my web command which I have then added to my Procfile:
   web: gunicorn working_out_gym.wsgi

7. Then back in my project settings.py file, I have changed debug to FALSE and added '.herokuapp.com', to INSTALLED APPS:

![Heroku settings update](/static/images/Heroku/Screenshot%20settings%20update.png)

8. I have then committed my code to GitHub:

git add .
git commit -m "Readied code for deployment in Heroku."
git push origin main

---

## Heroku App Deployment

1. Back in Heroku on your app, go to the Deploy tab, in the Deployment Method choose 'Connect to Github and then search for your repository to connect to, once you can see the correct repo in the list, click 'Connect':

![Connecting Github Repository](/static/images/Heroku/Screenshot%20Connecting%20Github%20Repo.png)

2. Then make sure that the main brach is selected and do a manual deployment using 'Deploy Branch':

![Deploy Main Branch](/static/images/Heroku/Screenshot%20Heroku%20Deploy%20Main%20Bramch.png)

3. You can check the progress of the build in the window beneath the deploy button and also from the Activity tab, the Activity tab will tell you when the deployment is complete and then we can launch our app. However, I am receiving this error in Heroku and it is failing to deploy the app:

ModuleNotFoundError: No module named 'cgi'

- ChatGPT recommends creating a .python-version file in the root of my project with my Python version inside: 3.12

- I create the file and then commit the code:

git add .python-version
git commit -m "Pin Python version for Heroku"
git push heroku main

- However, it does not allow me to run the 'git push' cmd as it errors:

 git push heroku main
fatal: 'heroku' does not appear to be a git repository
fatal: Could not read from remote repository.

Please make sure you have the correct access rights
and the repository exist

4. I troubleshoot with ChatGPT again who advises me to check what remotes I currently have with:

git remote -v

- I run this and have:

origin  https://github.com/LeilsEloise/working_out_gym.git (fetch)
origin  https://github.com/LeilsEloise/working_out_gym.git (push)

- ChatGPT advises that if there is nothing for Heroku in my list, then I need to add this. To do this I need to run the following cmd:

heroku git:remote -a working-out-gym

- Login to the Heroku app with your credentials and then it will connect to Heroku in the terminal.

- Once you are connected to Heroku, you should then be able to run, however, it is failing now with the error:

"TypeError: the 'package' argument is required to perform a relative import for '.herokuapp.com'"

- I realise that I should have added '.herokuapp.com' to ALLOWED_HOSTS and not INSTALLED APPS in settings.py so I revert this now:

![Heroku settings update](/static/images/Heroku/Screenshot%20settings%20update%20correct%20allowed%20hosts.png)

5. I still receive an error in the terminal when I try to push my code to Heroku again, this time about static files. I run the cmd and say 'yes' to the prompt:

python manage,py collectstatic

6. I commit my code to Github again:

git add .
git commit -m "Updated static files"
Git push origin main

7. I have now been able to successfully run the cmd to push my code to Heroku and deploy the app. If I go into the 'Activity' tab on my Heroku app I can see it has been built successfully:

![Heroku successful build](/static/images/Heroku/Screenshot%20Heroku%20Successful%20Build.png)

8. I can now launch the app using 'Open App' at the top right of the page:

![Heroku open app](/static/images/Heroku/Screenshot%20Heroku%20Open%20App.png)

9. However, the app will not open correctly yet as I haven't added my URL Patterns. To see the page with my code, I will need to add 'home' to the end of the URL in the browser. However the page still is not loading:

![Heroku App Error on /home](/static/images/Heroku/Screenshot%20Heroku%20App%20Error%20on%20Home.png)

- I carry out some checks from what I learnt in Project 3 when I had issues initially deploying my Heroku app:
* I have ran: heroku --version to check that Heroku is installed, which it is showing that it is.
* Add code for APPEND SLASH setting in my settings.py and then commit the code and push back to Heroku again. But app still doesn't load.
* I already have a urls.py file within the 'home' app directory.
* I run 'heroku logs --tail' in my terminal and can see from the log that gunicorn is crashing before Django even starts because it can't import pkg_resources.
* setuptools is showing as installed in my requirements.txt file
* ChatGPT gives me some cmd's to run to ensure setuptools is installed properly, I add setuptools>=70 to requirements.txt and save and then run:

pip install -r requirements.txt

- After running this, I am advised that there is a new version of Pip available: 24.3.1 > 26 so i update.

- I then run the below cmds:

pip freeze > requirements.txt
git add requirements.txt
git commit -m "Ensure setuptools installed for pkg_resources (gunicorn)"
git push heroku main

- Once each of the above has ran successfully, I then run the following to restart the dyno:

heroku restart -a working-out-gym

- However, the app still isn't loading. So I troubleshoot with ChatGPT who advises a common cause is Guinicorn 20.1.0 + modern packaging changes. They advise me to update my requirements.txt line from: gunicorn==20.1.0

To: gunicorn>=21.2

- And then run:

pip install -r requirements.txt
pip freeze > requirements.txt
git add requirements.txt
git commit -m "Upgrade gunicorn for Heroku/Python 3.12 compatibility"
git push heroku main
heroku restart -a working-out-gym

10. Now when I launch my app from Heroku, I can see my content, as the DISABLECOLLECTSTATIC key is currently enabled, there will be no css being applied:

![Heroku App Working](/static/images/Heroku/Screenshot%20Working%20Out%20Gym.png)

---

## Creating the PostreSQL database

1. Now that my app is setup and working on Heroku, I need to create my database to contain all of my site data: user logons, product listings, discussion board posts and comments, fitness and nutrition plan information, etc.

- I will create a PostreSQL instance using the following URL and requesting a new instance from Code Institute (https://dbs.ci-dbs.net/) using my e-mail address:

![Code Institute Database Creation](/static/images/Database/Screenshot%20Code%20Institute%20Database%20email.png)

2. The page should load to step 3 where you will be advised that a new Postgres database has been created for you.

3. Now I need to connect the new database to my code. Back in VS Studio, I have changed DEBUG to TRUE and then created a new file named env.py at the top level of my project, I have also added the env.py to my gitignore file to prevent the secret data I add to it from being pushed to GitHub. In the new env.py file, I can then import Python's OS module and use it to set the value of the DATABASE URL constant with the new database URL I have received in my e-mail from Code Institute:

import os

os.environ.setdefault(
"DATABASE_URL", "DATABASE_URL")


4. Once this is done, I can then pip install the two packages required for connecting to the Postgre SQL database:

pip3 install dj-database-url~=0.5 psycopg2~=2.9
pip3 freeze --local > requirements.txt

5. Once the above cmds have ran successfully and I can see the sw in requirements.txt, in my settings.py file in my project directory, I have then imported the appropriate packages at the top of the file:

import os
import dj_database_url
if os.path.isfile('env.py'):
import env

6. In the same file, I then need to comment out the local SQLite3 database connectio  to use a production ready PostgreSQL cloud database instead.

7. Then under the commented out db code, I need to connect to the environment variable DATABASE_URL in my env.py:

DATABASES = {
'default': dj_database_url.parse(os.environ.get("DATABASE_URL"))
}

8. Once the project is connected to the database, I can now create database tables with Django's migrate command:

python3 manage.py migrate

10. I can now create an admin user for the site owner to use so that they can manage their fitness site. I will choose an appropriate username and password for the user.

python3 manage.py createsuperuser

- However, when I run this cmd, I first get an error regarding the indentation around my if statement in my imports within settings. I resolve this and run the cmd again but this time receive an error to say it cannot find the module for 'dj_database_url'. I install this using:

pip install dj-database-url

- And add it to my requirements.txt file. I try running the cmd again but this time receive an error re. psycopg module not loading so I reinstall this using:

pip install psycopg2-binary

- I add it to my requirements.txt file and try creating the superuser again. This time I receive an error about migrations so I run:

python3 manage.py migrate

- Now I can run the superuser creation cmd and create a superuser successfully.

11. Before committing the code and deploying the app in Heroku, I need to change DEBUG back to FALSE.

12. Once app is built in Heroku, I can connect Heroku to my PostgreSQL database. In Heroku on my app in the settings, under Config Vars I need to add a Key of DATABASE_URL with a Value of the PostgreSQL database URL for my app.

13. Now my deployed app is connected to my database.

14. In order to ensure the security of my app and database, I need to keep my DATABASE_URL variable a secret as this contains sensitive information about my database - including username, password and database name. So I will only store the DATABASE_URL in my env.py file as it is in .gitignore and therefore not being pushed to GitHub. I have used an online Secret Key generator to generate a new secret key at: https://djecrety.ir/

15. Back in env.py, under the code for my database URL I will add a new line and copy the secret key I created into "<your_choice_of_secret_key>":

os.environ.setdefault("SECRET_KEY", "<your_choice_of_secret_key>")

16. In settings.py, I need to add the following so it retrieves the new SECRET_KEY from the environment variables:

SECRET_KEY = os.environ.get("SECRET_KEY")

17. Commit the code and redeploy on Heroku and then add the SECRET_KEY as a new set in Config Var.

18. I have tested my code in both the browser and the Heroku app and it loads okay after adding the Secret Key variable:

![Dev webpages working](/static/images/Database/Screenshot%20dev%20server%20app%20still%20working%20after%20connecting%20db.png)

![Heroku webpages working](/static/images/Database/Screenshot%20production%20working%20with%20db%20connection%20and%20secret%20key.png)

---

## Creating Discussion Board App

 The next thing I want to look at is creating my app for my Discussion Board - it will use a similar model to the news articles in my Project 3 as the functionality will be almost the same, except from creating new posts will be permitted to all users instead of just the site owner. Therefore, I will follow the same process that I did in Project 3 to create this and borrow code where appropriate and tweak to save time. The models for the Discussion Board are pretty much the same as they are for Project 3, there will be a model for 'Posts' and for 'Comments'.

 ---

 ### ERD Model for Posts

![ERD Model for Posts](/static/images/ERD/Screenshot%20ERD%20Model%20for%20Post.png)

---

 ### ERD Model for Comments

![ERD Model for Comments](/static/images/ERD/Screenshot%20ERD%20Model%20for%20Comment.png)

---

## Creating App, Views, Model - Discussion Board

1. To start, I will create my new app for 'Discussion Board' with the below command:

python3 manage.py startapp discussionboard

2. Once new directory is showing for 'discussionboard', I can then add the newly created app to my list of INSTALLED APPS in settings.py in the project directory:

![discussionboard in INSTALLED APPS](/static/images/Discussion%20Board/Screenshot%20creating%20new%20app%20directory%20adding%20to%20settings.png)

3. I then set up some basic code to test the new app, in discussionboard views.py, I add the below code:

from django.shortcuts import render
from django.http import HttpResponse

Create your views here.
def post(request):
return HttpResponse("See posts here!")

4. Then in my project directory urls.py file, I have imported the newly created view using the below code:

from discussionboard.views import post

5. Then in the same file, I define the URL pattern for the new view as below:

(‘discussionboard/’, post, name=’discussionboard’),

6. I will now run my page on the local server, appending the '/discussionboard' to the end of my URL, to ensure the new code is working:

python3 manage.py runserver

7. This is rendering okay:

![First Dev testing of Discussion Board Page](/static/images/Discussion%20Board/Screenshot%20first%20page%20testing.png)

8. I now need to build the model for the posts using the ERD. In my discussionboard models.py file, I copy and paste the model code that I created for 'Article' in Project 3 and tweak accordingly so I can use this for Post; I removed the image field as there won't be images in the post list.

class Post(models.Model):
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="posts")
    content = models.TextField()
    excerpt = models.TextField(blank=True)
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)

    class Meta:
        ordering = ["created_on"]

    def __str__(self):
        return f"{self.title} | written by {self.author}"

9. Now that I have added a new table to the database, I need to run the below so that I can create the set of instructions for the creation of the database table structure using the newly created Python class for Post:

   python3 manage.py makemigrations discussionboard

10. However, when I run the command I am getting an error about the User value that is set against the author key in my new Post model class, saying it is not defined. I realise that I have not added the import below at the top of my app models.py file, so do this now:

from django.contrib.auth.models import User

11. However, when I run makemigrations, it complains again that STATUS is not yet defined, I remove this field from the model for now and will look to add in later. Now that is removed, I can run makemigrations successfully. Once I can see the actions are ready, I then migrate using:

python3 manage.py migrate discussionboard

12. Once that completes successfully, I can then go into the discussionboard/admin.py file and import the new model for 'Posts' so that they can be uploaded, edited and deleted from the admin panel. I will look at adding in the functionality for users later on so that they can upload, edit and delete their own posts:

from .models import Post

13. Then back in my settings.py file in my project directory, below my code for DATABASES, i need to add the CRSF_TRUSTED_ORIGINS details so that the site owner can create, edit and delete posts from the admin dashboard. These are the trusted origins for requests:

CSRF_TRUSTED_ORIGINS = [
"http://127.0.0.1:8000/",
"https://working-out-gym-aaf119c10db9.herokuapp.com/"
]

14. I have tested, I can login to my admin panel when loaded on the dev server but do not appear to be seeing any options for adding new posts and the design isn't appearing as I would expect. In my admin.py file, I have imported the Post model but not registered it, so I do this now:

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ("title", "author", "created_on")

15. Now when I refresh the admin panel, I can see an option for Discussion Board and Posts to Add and Change. I want to fix the styling issues in the admin panel before I go any further so I troubleshoot the issue. I notice that the Homepage has lost css as well. I inspect DevTools and go to the Network tab and can see that there is a red 'x' on the css file.

16. I have reloaded the page and the CSS is now being applied. 

17. I notice that there is only a 'logout' button showing for me - as I am currently logged in as the superuser, but that clicking this does nothing so I would like to have a look at my signin, logout, and login html templates next.

---

## Login Logout Register Templates

1. As there is no styling in place for the registration, login and logout pages, I find the location of my my Django-allauth package files on my computer using the below cmd and copy the location:

pip3 show django-allauth C:\Users\leila\AppData\Roaming\Python\Python312\site-packages

Location: C:\Users\leila\OneDrive\Desktop\Documents\vscode-projects\working_out_gym\.venv\Lib\site-packages

2. I then copy the alllauth templates into the project templates directory using the below terminal command:

cp -r C:\Users\leila\OneDrive\Desktop\Documents\vscode-projects\working_out_gym\.venv\Lib\site-packages\allauth\templates\* .\templates

3. Now I can see a new folder for 'templates' created in my project directory. I am going to use the code I used in Project 3 for my signup.html, logout.html and signup.html templates and tweak accordingly for Project 4:

![Login html](/static/images/Login%20Logout%20Signup/Screenshot%20loginhtml%20edited.png)

![Logout html](/static/images/Login%20Logout%20Signup/Screenshot%20logout%20html%20code.png)

![Signup html](/static/images/Login%20Logout%20Signup/Screenshot%20signup%20html%20code.png)

3. I have added the below constants directly below my INSTALLED APPS, so that when users are logged in or out they are redirected to the Homepage:

LOGIN_REDIRECT_URL = '/'
LOGOUT_REDIRECT_URL = '/'

4. I need to wire up myb alluth to Middleware now, in settings.py, I already have the apps for AllAuth added to my INSTALLED APPS. So in the Middleware section of my settings.pyb I add:

'allauth.account.middleware.AccountMiddleware',

5. However, when I add this in I can see a number of errors being generated in my termninal regarding this. I have troubleshooted with ChatGPT whon advises that there is a number of issues in my code. To start with, I am getting an error when I add my allauth information into the settings file to say:

"ModuleNotFoundError: No module named 'allauth.account.middleware'"

- ChatGPT advises that this means that I am on an older django-allauth that doesn't have AccountMiddleware so to fix this, I need to upgrade to a version that does include it. I have ran the following cmd and found that I am on version 0.5.0 which is too old:

pip show django-allauth

- So I have then ran the following cmd to upgrade this to a current version:

pip install "django-allauth==0.63.6"

- I will run my local dev server now and ensure the errors are removed, I am being warned about migrations so I will run these now:

python3 manage.py migrate

- Now when I run my server, there is no errors in the terminal. I then move on to the other errors that ChatGPT has asked me to address:

- I update my urls.py file in my home directory to:

from django.urls import path
from .views import home

urlpatterns = [
    path('', home, name='home'),
]

- I try running the page on my local dev server and there are no errors with that all in place now and working, I can now look back to the Discussion Board app and making sure this is all wired up correctly.

---

## Discussion Board App

1. My new app directory for the DiscussionBoard needs its own urls.py file. I have created a new file in the directory and filled this with the below so it imports the path and views from my Django URLs py file and views file for Post:

from django.urls import path
from .views import post

urlpatterns = [
    path('', post, name='discussionboard'),
]

2. I will now login to the admin panel of my app as the super user and create some posts for testing. Once I am successfully logged into the admin panel of my app as the superuser, before I create any posts, I will first create a new standard user from the admin panel to tie in with our testing:  

![Creating new standard user from admin panel](/static/images/Discussion%20Board/Screenshot%20create%20new%20user%20admin%20panel.png)


3. The new account is created, so I then revert back to the admin panel and click to 'add' under discussionboard:

![Creating new post for testing](/static/images/Discussion%20Board/Screenshot%20adding%20new%20post%20as%20the%20new%20user.png)


4. Now that I have successfully created a post as a standard user, I will create 2 x more users and posts using the same process so that I have content to test on when it comes to adding my Comments model. If I look under 'change' against the DiscussionBoard now I can see the new posts against the newly created users:

![DiscussionBoard posts](/static/images/Discussion%20Board/Screenshot%20Discussion%20Board%20postsd.png)

---

### Adding Comments to DiscussionBoard app

1. Using the same ERD model for Comments as I did in Project 3, I will now start building my model and views for Comments so that users can comment on posts on the Discussion Board. To start, I will take the code which I used for the Comments in Project 3 and add this to discussionboard/models.py:

class Comment(models.Model):
    Post = models.ForeignKey(
        Post, on_delete=models.CASCADE, related_name="comments"
    )
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="commenter")
    body = models.TextField()
    approved = models.BooleanField(default=False)
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["created_on"]

    def __str__(self):
        return f"Comment {self.body} by {self.author}"

2. I save this new model and apply the migrations to the database which run successfully in the terminal.

3. Then in my admin.py file in the discussionboard directory, I import the new Comments model from the .models file with:

from .models import Post, Comment

4. Then in the same file, I add the below code to register the Comment model:

   admin.site.register(Comment)

5. I now run the app on my local server and go to the Admin panel to ensure that the Comments model is now showing:

![Comments showing in Admin Panel](/static/images/Discussion%20Board/Screenshot%20Comments%20Model%20showing%20in%20Admin%20Panel.png)

6. Then from the Admin Panel, I add 3 x different comments from the 3 x standard users I now have onto the new posts. I will leave one as unapproved:

![Unapproved comment on post](/static/images/Discussion%20Board/Screenshot%20unapproved%20comment.png)

---

### Discussion Board Templates

1. I now need to create a templates directory wtihin the discussionboard app directory so we can see the posts. I create a new folder in discussion board for templates and a subfolder within that called 'discussionboard'. Then within that new folder, I can create a template which will show the full list of posts on the discussion board, I will name this post_list.html. I am going to use the code that I used for my article_detail.html file to save me some time and tweak accordingly:

![Post list html initial](/static/images/Discussion%20Board/)

2. After adding the new temmplate to my discussionboard app, I then delete existing post function-based view and Http import from discussionboard/views.py and create a new class based view. I import generic from Django.views and import my Post model:

from django.shortcuts import render
from django.views import generic
from .models import Post

3. Then, still in the discussionboard views.py file, I create the class-based view named PostList that will inherit from the generic.ListView class to display all of the news articles:

PostList(generic.ListView):
model = Post

4. Then in discussionboard/urls.py I import the new view and path and add a URL pattern do that it uses it as the view() method for the new class-based view:


from . import views
from django.urls import path


urlpatterns = [
    path("", views.PostList.as_view(), name="discussionboard"),
]

5. I run the page on my local dev server but I am seeing a number of errors in my terminal that are preventing me from running the page. I troubleshoot with ChatGPT who has recommended that I fix the following:

* Stop importing post in in working_out_gym/urls.py - in normal Django setup you don't import models into URLS and you usually don't import random lowercase names either. The best practise would be to use the include() method. I am going to update my current discussionboard/urls.py file from: 

from . import views
from django.urls import path


urlpatterns = [
    path("", views.PostList.as_view(), name="discussionboard"),
]


* To:

from django.urls import path
from .views import PostList

urlpatterns = [
    path("", PostList.as_view(), name="post_list"),
]

* Then in working_out_gym/urls.py, I include it:

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', home, name='home'),
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),
    path('discussionboard/', include("discussionboard.urls")),
]

* Finally, I need to update discussionboard/views.py and change model = post to model = Post:

class PostList(generic.ListView):
    model = Post

* Next, I need to update discussionboard/urls.py:

from django.urls import path
from .views import PostList

urlpatterns = [ 
    path("", PostList.as_view(), name="post_list") 
    ]

* Then in my project level urls.py, I need to add the below in place of my current URL pattern for the discussion board:

path("discussion/", include("discussionboard.urls"))

* Once these changes are in place, I need to run: 

python manage.py makemigrations

* However, when I run this I receive an error saying that my URL pattern for home in my project urls file is not defined as the name 'home' is not defined. I need to update the URL pattern in my project URLs file so it uses the include method, so I change this to the below and then add to the bottom of my list:

path("", include("home.urls"),

* Then in my home app urls.py file, I replace  the import for 'home' at the top: 

from .views import home

With: 

from django.urls import path
from . import views

* And add the below to my URL patterns in place of my current URL pattern for home:

path("", views.home, name="home"),

* My view for home is already set up correctly in home/views.py. so I will run my makemigrations again now. However, this time I receive a NameError to say that the name 'path' is not defined against my admin site urls in the home/urls.py file. As we only need the admin site in the project level urls.py file, it is safe to remove this. My home/urls.py file is now:

from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
]

* I can now run makemigrations and migrate successfully.

6. I can see the home page on my dev server now but when I add /discussionboard to the end of my URL, I am taken to an error page which says that it cannot find my path for /discussionboard on the project level urls.py file. I have a look and see I have set the discussionboard page to use /discussion instead of discussionboard so update this as below:

    path("discussionboard/", include("discussionboard.urls")),

* I refresh my page for discussionboard/ and now am presented with a different error, it appears to be erroring on the DTL for crispy form tags, this will be erroring as we haven't installed Django Crispy Forms yet. 

7. To install Django Crispy Forms, I run: 

pip3 install django-crispy-forms~=2.0 crispy-bootstrap5~=0.7

* Once these successfully install in the terminal, I then add them to my requirements.txt file with:

pip3 freeze local > requirements.txt 

* I then need to add the new apps to my INSTALLED APPS list in my settings.py file, as well as adding them both as constants, as below, directly beneath the login and logout redirect URLS:

CRISPY_ALLOWED_TEMPLATE_PACKS = "bootstrap5"
CRISPY_TEMPLATE_PACK = "bootstrap5"

8. Once Crispy Forms is installed properly, I can then create a new forms.py file in the discussionboard directory and add a form for comment swithin the new file and then import the Comment form into discussionboard/views.py:

from .models import Comment
from django import forms

class CommentForm(forms.ModelForm):

class Meta: model = Comment fields = ('body',)

9. I have refreshed my page again to see how it is doing and have received another error now:

Error during template rendering
In template C:\Users\leila\OneDrive\Desktop\Documents\vscode-projects\working_out_gym\discussionboard\templates\discussionboard\post_list.html, error at line 47

'discussionboard' is not a registered namespace

*  I troubleshooted the error with ChatGPT who advises that I need to define the app_name in my discussionboard/urls.py and supplies me with the following code which I use and acknowledge:

from django.urls import path
from . import views

app_name = "discussionboard"

urlpatterns = [
    path("", views.PostList.as_view(), name="post_list"),
    path("vote/<slug:slug>/<int:value>/", views.post_vote, name="post_vote"),
]

* ChatGPT also advises that in my post_list.html file I am looping posts and I render:

{{ post.content }}

However, my vote URL is using:

{% url 'discussionboard:post_vote' article.slug 1 %}

It should be instead:

{% url 'discussionboard:post_vote' post.slug 1 %}

This is the same for the downvote:

{% url 'discussionboard:post_vote' post.slug -1 %}

* I update these pieces of code and acknowledge.

10. I run my page on my local server and it still is not loading but this time with an AttributeError to say that the module 'discussionboard.views' has no attribute for post_vote. I have troubleshooted with ChatGPT who advises that the discussionboard/urls.py references a view function called post_vote which doesn't exist in discussionboard/views.py (or it is named differently or not imported).

* I am going to add the missing post_vote view in now. I first check that within my discussionboard/models.py file that I have the Post model with slug, which I do:

 slug = models.SlugField(max_length=200, unique=True)

* ChatGPT has then advised me to add the following to my discussionboard/views.py file, I add this and acknowledge in my code:

from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect
from django.contrib import messages

from .models import Post

@login_required
def post_vote(request, slug, value):
    post = get_object_or_404(Post, slug=slug)

    if value not in (-1, 1):
        messages.error(request, "Invalid vote.")
        return redirect("discussionboard:post_list")

    # Simple approach: store total on Post (you need vote_total IntegerField on Post)
    post.vote_total = (post.vote_total or 0) + value
    post.save(update_fields=["vote_total"])

    return redirect("discussionboard:post_list")

* It recommends that I also add the following to my discussionboard/models.py to my Post model, so I add this in and acknowledge:

vote_total = models.IntegerField(default=0)

* I then try running makemigrations but I am receiving an AttributeError: module 'discussionboard.views' has no attribute 'PostList'. In my discussionboard.urls.py I have the following code:

views.PostList.as_view()

* ChatGPT has recommended that I update my discussionboard/views.py file so that PostList exists in views.py. It recommends the below code:

from django.views import generic
from .models import Post

class PostList(generic.ListView):
    model = Post
    template_name = "discussionboard/post_list.html"
    context_object_name = "posts"
    ordering = ["-created_on"]  # if you have created_on

* I add this and acknowledge.

11. I can then run makemigrations and migrate successfully. I do this and then try running my local server again. I go to /discussionboard in my URL but it is throwing the below error up when I go to the page:

NoReverseMatch at /discussionboard/
Reverse for 'post_vote' with arguments '('', 1)' not found. 1 pattern(s) tried: ['discussionboard/vote/(?P<slug>[-a-zA-Z0-9_]+)/(?P<value>[0-9]+)/\\Z']

* I troubleshoot with ChatGPT who pinpoints two issues:-
- Some of your posts have an empty slug (post.slug == "") - ChatGPT recommends the best fix to resolve this would be to ensure every Post automatically gets a slug. I need to add to my current Post model in discussionboard /models.py as below:

from django.db import models
from django.utils.text import slugify

class Post(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True, blank=True)
    # ... your other fields ...

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

- I update the current slug field on my Post model from:

    slug = models.SlugField(max_length=200, unique=True)

To:

    slug = models.SlugField(unique=True, blank=True)


- Then under the current function I will add another function for 'save' as below:

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

- Finally I will import slugify to the top of the file:

from django.utils.text import slugify

- Once I have added these in, I will run makemigrations and migrate which both run successfully.

- After adding this code I will need to delete any posts created without a slug. After logging into admin panel as superuser and checking each post, I can see all have a slug.

- ChatGPT also recommends wrapping the vote buttons so they only show if the post has a slug, with the below code:

{% if user.is_authenticated and post.slug %}
   ... vote links ...
{% endif %}

- I update the post_list.html template to include the post.slug statement in the if statement around my voting links.

* The second problem is that my URL pattern doesn't allow for the downvote. My current pattern is:

(?P<value>[0-9]+)

- This means that -1 (the downvote) will never match Django's <int:value> converter.

- To resolve this, I need to make value a string and validate in the view. in my discussionboard/urls.py file, I update: 

path("vote/<slug:slug>/<int:value>/", views.post_vote, name="post_vote"),

To: 

path("vote/<slug:slug>/<str:value>/", views.post_vote, name="post_vote"),

- And then in my discussionboard/views.py file I need to then validate using the below code:

from django.views import generic
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect
from django.contrib import messages

from .models import Post


class PostList(generic.ListView):
    model = Post
    template_name = "discussionboard/post_list.html"
    context_object_name = "posts"
    ordering = ["-id"]  # safe even if you don't have created_on


@login_required
def post_vote(request, slug, value):
    post = get_object_or_404(Post, slug=slug)

    try:
        value = int(value)
    except ValueError:
        messages.error(request, "Invalid vote value.")
        return redirect("discussionboard:post_list")

    if value not in (-1, 1):
        messages.error(request, "Invalid vote.")
        return redirect("discussionboard:post_list")

    post.vote_total = (post.vote_total or 0) + value
    post.save(update_fields=["vote_total"])

    return redirect("discussionboard:post_list")

12. Now I can successfully load the discussionboard app when going to /discussionboard on my local dev server. It still needs work but I first need to resolve the issue with 'logout' not directing the user to the page for logout, I will look at my static Java next:

![DiscussionBoard app working](/static/images/Discussion%20Board/Screenshot%20DiscussionBoard%20almost%20working.png)

13. Before I move onto my Javascript, I wqant to add a fixture into my app folder, so within my discussioboard directory I create a new folder called 'fixtures'. Then within that folder I create a file called post.json. I can then populate this with multiple posts to be added to the discussionboard app:

![Fixtures Directory](/static/images/Discussion%20Board/Screenshot%20fixtures.png)

14. I am then going to run the below in my terminal:

python3 manage.py loaddata post

15. Once this confirms that it has installed the 3 x posts from my Fixtures file, I reload my discussionboard page on my dev server to see the posts have been added, however, the posts have not been added:

![DiscussionBoard before](/static/images/Discussion%20Board/Screenshot%20discussionboard%20before.png)

16. I troubleshoot with ChatGPT why all posts are not showing and also look to see how I would split out the content on my DiscussionBoard app into two columns, the left column containing only posts with no comments on this view and the columnn on the right to be a side panel with options for users to CRUD posts. 

17. To start, I look at why the posts aren't showing. I confirm that the new posts added from fixtures are showing in my admin panel. I then look at the code I have for discussionboard/views.py. I notice that I have 'ordering' in my PostList class defined as ["-id"] but on my model it is set to created_on. I update this now. I also add code to paginate to allow the posts to go over multiple pages when necessary:

    paginate_by = 10

18. I then create a new template for post_detail.html within my discussionboard directory under templates/discussionboard. This will be the view that generates when a user clicks a single post. I use the code provided by ChatGPT and acknowledge.

19. Then in my discussionboard/views.py file, I need to change it so it gives only the list and detail with no comments. I update this to the below on recommendation from ChatGPT:

from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse_lazy
from django.shortcuts import get_object_or_404
from .models import Post

class PostList(generic.ListView):
    model = Post
    template_name = "discussionboard/post_list.html"
    context_object_name = "posts"
    paginate_by = 10
    ordering = ["-created_on"]  # if you have created_on, otherwise use ["-id"]


class PostDetail(generic.DetailView):
    model = Post
    template_name = "discussionboard/post_detail.html"
    context_object_name = "post"


20. Then in my discussionboard/urls.py file, I need to update the views import so it imports PostList and PostDetail from the views.py file in my app:

from .views import PostList, PostDetail

- In the same file, I replace the path I had for Post Vote with a PostDetail slug instead:

    path("<slug:slug>/", PostDetail.as_view(), name="post_detail"),

21. Next I look at my templates, I will first need to change post_list.html, ChatGPT has generated this code for me to save some time:

22. Next I will look at CRUD views for users with permission rules. I update my discussionboard/views.py with the below forms and permission mixin - I add these below my current classes for PostList and PostDetail but above the functions for post vote:

class PostCreate(LoginRequiredMixin, generic.CreateView):
    model = Post
    fields = ["title", "content"]  # add fields you actually have
    template_name = "discussionboard/post_form.html"
    success_url = reverse_lazy("discussionboard:post_list")

    def form_valid(self, form):
        form.instance.author = self.request.user
        if not form.instance.slug:
            form.instance.slug = slugify(form.instance.title)
        return super().form_valid(form)

class PostOwnerOrSuperuserMixin(UserPassesTestMixin):
    def test_func(self):
        post = self.get_object()
        return self.request.user.is_superuser or post.author == self.request.user

class PostUpdate(LoginRequiredMixin, PostOwnerOrSuperuserMixin, generic.UpdateView):
    model = Post
    fields = ["title", "content"]
    template_name = "discussionboard/post_form.html"

    def get_success_url(self):
        return reverse_lazy("discussionboard:post_detail", kwargs={"slug": self.object.slug})

class PostDelete(LoginRequiredMixin, PostOwnerOrSuperuserMixin, generic.DeleteView):
    model = Post
    template_name = "discussionboard/post_confirm_delete.html"
    success_url = reverse_lazy("discussionboard:post_list")

23. Then in my discussionboard/urls.py file, I update the imnprots to include the new classes added to my views.py file. I then add paths for each slug for create, edit and delete:

from .views import PostList, PostDetail, PostCreate, PostUpdate, PostDelete

    path("new/", PostCreate.as_view(), name="post_create"),
    path("<slug:slug>/edit/", PostUpdate.as_view(), name="post_edit"),
    path("<slug:slug>/delete/", PostDelete.as_view(), name="post_delete"),

24. I then create a post_form.html file and post_confirm_delete.html file within the templates directory of my discussionboard app and populate with the code from ChatGPT. 

25. I refresh my local dev server but it will not load and presents an error in the terminal:

  File "C:\Users\leila\OneDrive\Desktop\Documents\vscode-projects\working_out_gym\discussionboard\urls.py", line 3, in <module>
    from .views import PostList, PostDetail, PostCreate, PostUpdate, PostDelete
  File "C:\Users\leila\OneDrive\Desktop\Documents\vscode-projects\working_out_gym\discussionboard\views.py", line 53, in <module>
    @login_required
     ^^^^^^^^^^^^^^
NameError: name 'login_required' is not defined

26. I troubleshoot and find that this is due to the login import being removed from views.py so add this back in now to imports:

from django.contrib.auth.decorators import login_required

- I also notice the messages import and slugify import have been removed so add these both back in and save:

from django.contrib import messages
from django.utils.text import slugify

27. I reload discussionboard on the dev server but now I am receiving a different error:

TemplateSyntaxError at /discussionboard/
Could not parse the remainder: '(user' from '(user'

28. I troubleshoot this with ChatGPT who advises that Django templates don't support parentheses in {% if %} conditions so this line blows up and that's why it can't parse the user:

- {% if user.is_authenticated and (user == post.author or user.is_superuser) %}

- It has recommended replacing this code with the below code as it has clearer logic and avoids precedence issues:

{% if user.is_superuser %}
  <div class="d-flex gap-2">
    <a class="btn btn-sm btn-outline-primary" href="{% url 'discussionboard:post_edit' post.slug %}">Edit</a>
    <a class="btn btn-sm btn-outline-danger" href="{% url 'discussionboard:post_delete' post.slug %}">Delete</a>
  </div>
{% elif user.is_authenticated and user == post.author %}
  <div class="d-flex gap-2">
    <a class="btn btn-sm btn-outline-primary" href="{% url 'discussionboard:post_edit' post.slug %}">Edit</a>
    <a class="btn btn-sm btn-outline-danger" href="{% url 'discussionboard:post_delete' post.slug %}">Delete</a>
  </div>
{% endif %}

- I have updated my post_list.html file to:

<!-- LEFT COLUMN: POSTS LIST -->
<div class="col-12 col-lg-8">
  <h2 class="mb-3">Discussion Board</h2>

  {% if posts %}
    {% for post in posts %}
      <div class="card mb-3">
        <div class="card-body">
          <h5 class="card-title mb-1">
            <a href="{% url 'discussionboard:post_detail' post.slug %}">
              {{ post.title }}
            </a>
          </h5>

          <p class="text-muted mb-2">
            Posted by {{ post.author }} • {{ post.created_on|date:"d M Y" }}
          </p>

          <p class="card-text">
            {{ post.content|truncatewords:30 }}
          </p>

          {% if user.is_superuser %}
            <div class="d-flex gap-2">
              <a class="btn btn-sm btn-outline-primary" href="{% url 'discussionboard:post_edit' post.slug %}">Edit</a>
              <a class="btn btn-sm btn-outline-danger" href="{% url 'discussionboard:post_delete' post.slug %}">Delete</a>
            </div>
          {% elif user.is_authenticated and user == post.author %}
            <div class="d-flex gap-2">
              <a class="btn btn-sm btn-outline-primary" href="{% url 'discussionboard:post_edit' post.slug %}">Edit</a>
              <a class="btn btn-sm btn-outline-danger" href="{% url 'discussionboard:post_delete' post.slug %}">Delete</a>
            </div>
          {% endif %}
        </div>
      </div>
    {% endfor %}

    {% if is_paginated %}
      <nav>
        <ul class="pagination">
          {% if page_obj.has_previous %}
            <li class="page-item">
              <a class="page-link" href="?page={{ page_obj.previous_page_number }}">Previous</a>
            </li>
          {% endif %}

          <li class="page-item disabled">
            <span class="page-link">Page {{ page_obj.number }} of {{ page_obj.paginator.num_pages }}</span>
          </li>

          {% if page_obj.has_next %}
            <li class="page-item">
              <a class="page-link" href="?page={{ page_obj.next_page_number }}">Next</a>
            </li>
          {% endif %}
        </ul>
      </nav>
    {% endif %}

  {% else %}
    <div class="alert alert-info">
      No posts yet. Be the first to start a discussion!
    </div>
  {% endif %}
</div>

- I now need to amend my discussionboard views.py PostList class so that the left column of my page shows paginated posts and the right columns shows all of the logged-in user's posts. Under the current clas based view for PostList, I define a function for get_context_data within the class based view:

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        if self.request.user.is_authenticated:
            context["my_posts"] = Post.objects.filter(
                author=self.request.user
            ).order_by("-created_on")
        else:
            context["my_posts"] = Post.objects.none()

        return context

- Then, back in my post_list.html I need to update the sidebarloop from: {% for post in posts %}

to: {% for post in my_posts %}

- And then in the section beneath it, replace with:

<h6 class="mb-2">Your posts</h6>

{% for post in my_posts %}
  <div class="d-flex justify-content-between align-items-center mb-2">
    <a class="small" href="{% url 'discussionboard:post_detail' post.slug %}">
      {{ post.title|truncatechars:25 }}
    </a>
    <div class="d-flex gap-1">
      <a class="btn btn-sm btn-outline-primary" href="{% url 'discussionboard:post_edit' post.slug %}">Edit</a>
      <a class="btn btn-sm btn-outline-danger" href="{% url 'discussionboard:post_delete' post.slug %}">Del</a>
    </div>
  </div>
{% empty %}
  <p class="text-muted small mb-0">You haven’t posted yet.</p>
{% endfor %}

- I refresh my page to see how this is looking now. But I am getting:

TemplateSyntaxError /discussionboard/
Invalid block tag on line 23: 'endfor', expected 'elif', 'else' or 'endif'. Did you forget to register or load this tag?

- There is an unneccessary {% endfor %} tag in my post_list.html file since making the changes. I remove this and reload the page again. The page is now loading but I can only see the users own posts and I want a left column showing all posts on the page from all users and a right column with this information.

- It is no longer extending my base.html on the discussionboard page, so I have a look at my new templates and ensure the tag for this is applied to them all. It is being applied to all of the templates apart from the post_list.html template so I add this above the template provided by ChatGPT and refresh the page but nothing changes. I also realise there is no block content DTL tags on the post_list.html either so add these to the start and end now and refresh the page and it is looking much better but still not seeing all user posts on the left:

![DiscussionBoard own users posts but not all posts](/static/images/Discussion%20Board/screenshot%20discussionboard%20showing%20only%20own%20posts.png)

- I ask ChatGPT what the issue could be and they provide me with an updated template based on what i asked for earlier:

{% extends "base.html" %}

{% block content %}
<div class="container my-4">
  <div class="row g-4">

    <!-- LEFT COLUMN: ALL POSTS -->
    <div class="col-12 col-lg-8">
      <h2 class="mb-3">Discussion Board</h2>

      {% if posts %}
        {% for post in posts %}
          <div class="card mb-3">
            <div class="card-body">
              <h5 class="card-title mb-1">
                <a href="{% url 'discussionboard:post_detail' post.slug %}">
                  {{ post.title }}
                </a>
              </h5>

              <p class="text-muted mb-2">
                Posted by {{ post.author }} • {{ post.created_on|date:"d M Y" }}
              </p>

              <p class="card-text">
                {{ post.content|truncatewords:30 }}
              </p>

              {% if user.is_authenticated %}
                {% if user.is_superuser or user == post.author %}
                  <div class="d-flex gap-2">
                    <a class="btn btn-sm btn-outline-primary" href="{% url 'discussionboard:post_edit' post.slug %}">Edit</a>
                    <a class="btn btn-sm btn-outline-danger" href="{% url 'discussionboard:post_delete' post.slug %}">Delete</a>
                  </div>
                {% endif %}
              {% endif %}
            </div>
          </div>
        {% endfor %}

        {% if is_paginated %}
          <nav>
            <ul class="pagination">
              {% if page_obj.has_previous %}
                <li class="page-item">
                  <a class="page-link" href="?page={{ page_obj.previous_page_number }}">Previous</a>
                </li>
              {% endif %}

              <li class="page-item disabled">
                <span class="page-link">Page {{ page_obj.number }} of {{ page_obj.paginator.num_pages }}</span>
              </li>

              {% if page_obj.has_next %}
                <li class="page-item">
                  <a class="page-link" href="?page={{ page_obj.next_page_number }}">Next</a>
                </li>
              {% endif %}
            </ul>
          </nav>
        {% endif %}

      {% else %}
        <div class="alert alert-info">
          No posts yet. Be the first to start a discussion!
        </div>
      {% endif %}
    </div>

    <!-- RIGHT COLUMN: SIDEBAR -->
    <div class="col-12 col-lg-4">
      <div class="card">
        <div class="card-body">
          <h5 class="card-title">Actions</h5>

          {% if user.is_authenticated %}
            <a class="btn btn-success w-100 mb-3" href="{% url 'discussionboard:post_create' %}">
              + Create new post
            </a>

            <hr>

            <h6 class="mb-2">Your posts</h6>

            {% for post in my_posts %}
              <div class="d-flex justify-content-between align-items-center mb-2">
                <a class="small" href="{% url 'discussionboard:post_detail' post.slug %}">
                  {{ post.title|truncatechars:25 }}
                </a>
                <div class="d-flex gap-1">
                  <a class="btn btn-sm btn-outline-primary" href="{% url 'discussionboard:post_edit' post.slug %}">Edit</a>
                  <a class="btn btn-sm btn-outline-danger" href="{% url 'discussionboard:post_delete' post.slug %}">Del</a>
                </div>
              </div>
            {% empty %}
              <p class="text-muted small mb-0">You haven’t posted yet.</p>
            {% endfor %}

          {% else %}
            <p class="mb-3">Log in to create and manage posts.</p>
            <a class="btn btn-outline-primary w-100" href="/accounts/login/">Log in</a>
          {% endif %}
        </div>
      </div>
    </div>

  </div>
</div>
{% endblock %}

-  I update the new template as provided by ChatGPT and it looks exactly as I would like it to look:

![DiscussionBoard now showing all posts with an action sidebar for user](/static/images/Discussion%20Board/Screenshot%20dicussionboard%20view%20now%20as%20design.png)

- I am now going to commit my code and work on my static js as this was not working earlier and I will need it if I am going to resolve the issues around the logout button and by proxy the signup and login buttons too so that I can then come back and test and make sure all functionality of my Discussion Board works before I move on to my Merchandise Page.

---

## Additional Installs

1. Before I start looking at the Javascript and login functionality issues, I would first like to install a couple of pieces of software into the Project which I feel will be beneficial.

2. I am going to install Django Summernote first; a robust text editor which will simplify the process of adding and editing article posts for the users. To install I run the below cmd:

pip3 install django-summernote~=0.8.20.0

3. I then add it to my requirements.txt file using:

pip3 freeze local > requirements.txt

4. If I open the requirements.txt file I can see it is now in there. I then add it to my INSTALLED APPS list in my settings.py file and include the Django Summernote as an app in my project/urls.py file:

path("summernote/", include("django_summernote.urls")),

5. I now need to update my app to use Summernote. I do this by importing the class to my discussionboard/admin.py file as below:

from django_summernote.admin import SummernoteModelAdmin

6. In the same file, I then need to update the PostAdmin class which will use the SummernoteModelAdmin import instead, from at the top of the file. I will borrow what I have used from Project 3 for this and acknowledge. I removed any filters for draft and status and replaced with 'title' and 'slug' in the list filter section.

7. I then run the following cmds to migrate the new tables:

python3 manage.py makemigrations

8. In order to make my deployed app look as nicely styled as my local development version, I will deploy the project with static files. In order to do this, I am going to use a Python package called Whitenoise. To install this I run:

pip3 install whitenoise~=5.3.0

9. Once I can see it has successfully installed in my terminal, I add it to my requirements.txt file with:

pip3 freeze --local > requirements.txt

10. Once it is installed and in requirements.txt, I then need to wire it up to Django's Middleware in my project settings.py file:

    "whitenoise.middleware.WhiteNoiseMiddleware",

11. Then, still in settings.py, I update my STATIC_ROOT directory from:

STATIC_ROOT = BASE_DIR / "staticfiles"

To:

STATIC_ROOT = os.path.join(BASE_DIR, "staticfiles")

12. I then run my collectstatic cmd in the terminal to collect all the static files again:

python3 manage.py collectstatic

13. This runs successfully, I then commit my code again and go to the app's dashboard in Heroku and remove the DISABLE_COLLECT_STATIC key, as I no longer need to prevent static files from being collected by the Heroku app. Once this is removed, I run:

git push heroku main

14. I then load up my app in Heroku but the app will not load so I will troubleshoot this now. I have ran:

heroku logs --tail 

- I then copy and paste the traceback to ChatGPT who advises that Whitenoise isn't installed in the Heroku environment so Heroku is crashing because it cannot import it. To fix it I:

* Install Whitenoise locally in my venv using:

pip install whitenoise

* Freeze requirements.txt again:

pip freeze > requirements.txt

* I confirm I can definitely see Whitenoise in the list within requirements.txt and then commit and push the code to Heroku:

git add requirements.txt
git commit -m "Add whitenoise to requirements"
git push heroku main

15. Now when I check the page on Heroku, I can see it loading with my styles on both the Home page and Discussion Board: 

![Heroku Home](/static/images/Heroku/Screenshot%20Heroku%20Home%20page.png)

![Heroku Discussion Board](/static/images/Heroku/Screenshot%20Heroku%20discussion%20board.png)

![Heroku Admin](/static/images/Heroku/Screenshot%20heroku%20admin.png)

---

## Static Javascript

1. I am going to delete the test.js file I created in the static folder earlier and create a new file called script.js which contains the below code:

console.log("I love the gym!");

2. I save this and then set the src to my new js/script.js file in my base.html file:

<script src="{% static 'js/script.js' %}"></script>

3. I refresh my local dev server and check to see if the message is showing in the console now on Devtools. However, it is failing with the following error message:

(index):1 Refused to execute script from 'http://127.0.0.1:8000/static/js/script.js' because its MIME type ('text/html') is not executable, and strict MIME type checking is enabled.

4. I am going to try a fix I used a lot on Project 3 as I have added more static files but not ran a collect static. I will first run:

Remove-Item -Recurse -Force staticfiles  

5. Then I will run collectstatic:

python manage.py collectstatic

6. Now when I run inspect Devtools in the console I see the 'I Love the gym' message from my script.js file. I commit my code to Github and Heroku and then check that I can see the console log on Heroku, which I can.

7. Now that Javascript is working I can look at my code for logins, etc.

---

## User Login, Logout and Register

1. At the moment, the 'Login', 'Logout' and 'Register' buttons are non functional on the site, nothing happens when they are clicked because there is no Javascript in place for this. To start, I check that everything is in place for Django AllAuth which it is. I update the href references for the login urls to use DTL:

![Auth Links Navbar Update](/static/images/Login%20Logout%20Signup/Screenshot%20auth%20links%20navbar%20update.png)

2. I have already got my login, logout and signup.html code in place in the templates/account folder. I am going to run my page on my local server now and see whether they are functional now.

3. The logout button is working now:

![Logout working](/static/images/Login%20Logout%20Signup/Screenshot%20logout%20working%20local%20server.png)

4. However, if I click 'Login' to log back in, I am presented with s Server 500 error message. I turn debug to True in my settings.py and refresh the page. The page refreshes and shows the issue as being a:

TemplateSyntaxError at /accounts/login/
Unclosed tag on line 9: 'block'. Looking for one of: endblock.

5. I go to the file at templates/account/login.html and add the closing endblock tag after line 9 after all the html content. I save and refresh the page and login page now loads. I login as the new superuser I created but their email is not verified yet. However, this highlights that there is no template styling in place for this area of 'confirm-email':

![Confirm email no styling](/static/images/Login%20Logout%20Signup/Screenshot%20confirm%20email%20before.png)

6. Looking in my templates/account folder I can see their is a template here for email_confirm, so I take a look at this. At the top I can see it is loading accounts/base.html instead of the templates/base.html with all styles applied. I update this from:

{% extends "account/base.html" %}

To: {% extends "base.html" %}

7. I refresh the page but nothing happens. I can see there is a verified_email_required.html file in the templates/account folder so try the same update here and refresh but still no change, finally I update verification_sent.html and this does update it so its using the correct styles:

![Login working and styled local dev server](/static/images/Login%20Logout%20Signup/Screenshot%20login%20working%20local%20dev%20server.png)

![Confirm email with styling](/static/images/Login%20Logout%20Signup/Screenshot%20verify%20email%20address%20local%20dev%20server.png)

![Register with styling](/static/images/Login%20Logout%20Signup/Screenshot%20register%20local%20dev%20server.png)

8. I have tested logging in, logging out and registering an account and all are working as should be. I am going to change Debug to False and commit my code and then look at adding a feedback form to my Homepage.

9. I realise I have added more screenshots so run collectstatic and then commit my files to both Github and Heroku.

10. I have tested my app on Heroku and login functionality and styling is now appropriate there too.

---

## Testing Discussion Board app functionality

1. Now that I have resolved the issues around logging in and out, I can test the functionality of the Discussion Board app and make any last changes too. 

2. To start with, I would like to be able to click 'Discussion Board' from the Navbar menu to go to the page. In my base.html, I update the href for my navbar item for Discussion Board to:

{% url 'discussionboard:post_list' %}

3. This now takes you to the Discussion Board from the Navbar item. I login as a standard user to test all functionality before moving on to my feedback form.

4. As the standard user, I can see all the posts I have created in the right hand side panel, with options to moderate these posts:

![Post list is viewable](/static/images/Discussion%20Board/Screenshot%20testing%20as%20standard%20user%20posts%20viewable.png)

5. If I click 'Create a New Post' I am taken to the below page:

![Create new post](/static/images/Discussion%20Board/Screenshot%20create%20new%20post%20standard%20user.png)

6. If i populate this and then click 'save' then my post is saved and I am redirected to the post_list section of DiscussionBoard app:

![Create new post](/static/images/Discussion%20Board/Screenshot%20new%20post%20saved.png)

7. If I click 'Edit' on my own post, then I am taken to a page with the post content where I can edit the 'Title' and 'Content' using Django Crispy-forms and save:

![Editing Current Posts](/static/images/Discussion%20Board/Screenshot%20editing%20posts.png)

8. It then takes you to a page confirming the changes are there:

![Editing Current Posts confirm](/static/images/Discussion%20Board/Screenshot%202confirm%20changes%20edit.png)

9. Finally, if I click delete on my own posts, I am taken to a page asking me to first confirm:

![Deleting Posts confirm](/static/images/Discussion%20Board/Screenshot%20delete%20post%20confirm.png)

10. After click yes to deleting, I am taken back to the post_list section of the DiscussionBoard app where the post is now gone:

![Deleting Posts gone](/static/images/Discussion%20Board/Screenshotdeletd%20post%20gone.png)

11. I go to now test the functionality of posts made by other users, to ensure that I can view them and the comments on them. I can click the individual posts and they load but I cannot see any comments on the posts. Looking at my post_detail.html which loads for the individual posts, I can see that I currently have:

{% extends "base.html" %}
{% block content %}
<div class="container my-4" style="max-width: 900px;">
  <a href="{% url 'discussionboard:post_list' %}">&larr; Back to discussion board</a>

  <div class="card mt-3">
    <div class="card-body">
      <h2 class="mb-1">{{ post.title }}</h2>
      <p class="text-muted">Posted by {{ post.author }} • {{ post.created_on|date:"d M Y" }}</p>
      <div>{{ post.content|safe }}</div>
    </div>
  </div>

  {# comments section goes here (only on detail) #}
</div>
{% endblock %}

- Then in my models.py file in discussionboard I have a Comments model:

class Comment(models.Model):
    Post = models.ForeignKey(
        Post, on_delete=models.CASCADE, related_name="comments"
    )
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="commenter")
    body = models.TextField()
    approved = models.BooleanField(default=False)
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["created_on"]

    def __str__(self):
        return f"Comment {self.body} by {self.author}"

- I am going to remove the   {# comments section goes here (only on detail) #} tag in my post_detail.html file and replace with the below code from my article_detail.html file in my goodnewspaper Project. 

  <!--ACK Code Institute-->
  <!-- Displaying count of comments -->
  <div class="row">
    <div class="col-12">
      <strong class="text-secondary">
        <i class="far fa-comments"></i> {{ comment_count }}
      </strong>
    </div>
    <div class="col-12">
      <hr />
    </div>
  </div>
  <!-- Displaying Comments -->
  <div class="row">
    <div class="col-md-8 card mb-4 mt-3">
      <h3>Comments:</h3>
      <div class="card-body">
        <!-- We want a for loop inside the empty control tags
          to iterate through each comment in comments -->
        {% for comment in comments %}
        <div
          class="p-2 comments {% if not comment.approved and comment.author == user %} faded{% elif not comment.approved %} d-none{% endif %}"
        >
          <p class="font-weight-bold">
            {{ comment.author }}
            <span class="font-weight-normal"> {{ comment.created_on }} </span>
            wrote:
          </p>
          <div id="comment{{ comment.id }}">
            {{ comment.body | linebreaks }}
          </div>
          {% if not comment.approved and comment.author == user %}
          <p class="approval">This comment is awaiting approval</p>
          {% endif %} {% if user.is_authenticated and comment.author == user %}
          <button class="btn btn-edit" comment_id="{{ comment.id }}">
            Edit
          </button>
          <!--ChatGPT Delete Button Code-->
          <a
            href="{% url 'newstories:comment_delete' article.slug comment.id %}"
            class="btn btn-sm btn-danger"
            onclick="
              return confirm('Are you sure you want to delete this comment?');
            "
          >
            Delete
          </a>
          {% endif %}
        </div>
        <!-- Our for loop ends here -->
        {% endfor %}
      </div>
    </div>
    <!-- Creating New Comments -->
    <div class="col-md-4 card mb-4 mt-3">
      <div class="card-body">
        {% if user.is_authenticated %}
        <h3>Leave a comment:</h3>
        <p>Posting as: {{ user.username }}</p>
        <form id="commentForm" method="post" style="margin-top: 1.3em">
          {{ comment_form | crispy }} {% csrf_token %}
          <button id="submitButton" type="submit" class="btn btn-signup btn-lg">
            Submit
          </button>
        </form>
        {% else %}
        <p>Log in to leave a comment</p>
        {% endif %}
      </div>
    </div>
  </div>
</div>

- I will then also need to delete my current script.js file and create a new file called comments.js and use the code from my Project 3 and Code Institute:

- I run collectstatic and then reload my page on my local server. However, I am getting the below error when I click on an individual post from the Discussion Board:

TemplateSyntaxError at /discussionboard/i-love-jogging/
Invalid filter: 'crispy'

It is erroring on line 76 of my post_detail.html.

- I realise I am not loading the cirspy_form_tags in a DTL at the top of my page for post_detail.html so add this in now.

11. Now when I refresh the page, I can see comments on the post. I test leaving a comment but it seems there is still no functionality and if I click the 'Submit' button I am taken to a 405 error page.

12. I troubleshoot this with ChatGPT who advises that if I am getting a HTTP 405 error on Submit then my current view isn't handling POST. They recommend updating my post_detail function view in discussionboard/views.py to the below:

from django.shortcuts import get_object_or_404, redirect, render

def post_detail(request, slug):
    post = get_object_or_404(Post, slug=slug)
    comments = post.comments.all().order_by("-created_on")  # adjust field names

    if request.method == "POST":
        if not request.user.is_authenticated:
            return redirect("account_login")

        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.post = post
            comment.author = request.user  # adjust if your field is "name" etc
            comment.save()
            return redirect("discussionboard:post_detail", slug=post.slug)
    else:
        comment_form = CommentForm()

    return render(
        request,
        "discussionboard/post_detail.html",
        {"post": post, "comments": comments, "comment_form": comment_form},
    )

13. I currently have a class-based view for post_detail so will need to make the changes as follows to views.py:
* I import 'render' and 'redirect' before my get_object_404 import.
* I remove the class based view for post_detail
* I import: from .forms import CommentForm and add Comment to the import I already have for Post.
* I then add the below function-based view in the views.py file:

def post_detail(request, slug):
    post = get_object_or_404(Post, slug=slug)

    # get comments for this post (adjust names to your model)
    comments = post.comments.all().order_by("-created_on")  # or "-id"

    if request.method == "POST":
        if not request.user.is_authenticated:
            return redirect("account_login")

        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.post = post
            comment.author = request.user  # adjust field name if yours is "user" etc
            comment.save()
            return redirect("discussionboard:post_detail", slug=post.slug)
    else:
        comment_form = CommentForm()

    return render(
        request,
        "discussionboard/post_detail.html",
        {
            "post": post,
            "comments": comments,
            "comment_form": comment_form,
        },
    )
* I then update discussionboard/urls.py to point at the function view with:

path("<slug:slug>/", views.post_detail, name="post_detail")

14. However, I can see a number of errors in my terminal when I run my server again. There is an indentation issue in my forms.py file which I resolve.

15. It is also showing that my urls.py file is still importing the PostDetail class based view that I deleted from views.py, I update this now to post_detail. I also add the below to import the new views into urls.py:

from . import views

16. After updating this, I can then run my page on the local server and see comments:

![Comments now working](/static/images/Discussion%20Board/Screenshot%20comments%20working.png)

17. However, if I enter text in the new comment window and click the 'submit' button I am taken to an error page which says:

IntegrityError at /discussionboard/i-love-jogging/
null value in column "Post_id" of relation "discussionboard_comment" violates not-null constraint
DETAIL:  Failing row contains (4, yes i agree, f, 2026-03-04 09:34:46.262351+00, null, 2).

18. I have troubleshooted with ChatGPT who advises that the new comment is saving but not being linked to the post:

null value in column "Post_id" … violates not-null constraint

- Django is trying to insert a Comment row where post_id is NULL. In my view I am using:

comment.post = post

- But because my Comment model's foreign key field is not called post or there is a mismatch like Post, the database column shown is "Post_id" suggesting the comment model is likely something like:

Post = models.ForeignKey(Post, ...)

- So I need to fix the Foreign Key using the actual field name. I find my Comment model in models.py and found the code I need:

 Post = models.ForeignKey(
        Post, on_delete=models.CASCADE, related_name="comments"
    )

- Then I go back into my views.py file and update my post_detail view and capitalise the 'P' in post as below:

comment.Post = post

- I save and refresh the page and try to submit a new comment but now I am receiving an error from my template now to say that Django is trying to build a URL for comment_delete but there is no URL pattern with that name. This is because my discussionboard/urls.py only has post_delete and not comment_delete. ChatGPT provides me with a class based function for CommentDelete which I can add into my views.py code as below:

class CommentOwnerOrSuperuserMixin(UserPassesTestMixin):
    def test_func(self):
        comment = self.get_object()
        return self.request.user.is_superuser or comment.author == self.request.user


class CommentDelete(LoginRequiredMixin, CommentOwnerOrSuperuserMixin, generic.DeleteView):
    model = Comment
    template_name = "discussionboard/comment_confirm_delete.html"

    def get_success_url(self):
        # send user back to the post detail page after deleting the comment
        return reverse_lazy("discussionboard:post_detail", kwargs={"slug": self.object.Post.slug})

- I then need to add the URL path to my urls.py file:

path("comment/<int:pk>/delete/", views.CommentDelete.as_view(), name="comment_delete"),

- Then I need to fix the template link to ensure that post_detail.html uses:

{% url 'discussionboard:comment_delete' comment.pk %}

- Finally, I create a comment_confirm_delete.html using the code from ChatGPT. Now when I save and refresh my browser I can see the comment I submitted earlier:

![Comments now can be created](/static/images/Discussion%20Board/Screenshot%20create%20new%20comments%20working.png)

- I can also delete the comments:

![Comments deleted](/static/images/Discussion%20Board/Screenshot%20comment%20successfully%20removed.png)

- I can now commit my code and move onto the feedback form on the Homepage.

- I have just realised when testing on the Heroku app that the 'edit' button on my comments is not doing anything. I believe this is because I need to create a similar function for CommentEdit so will do this quickly now. I have asked ChatGPT to create the class based view for CommentEdit, I add this under my 

class CommentOwnerOrSuperuserMixin(UserPassesTestMixin):
    def test_func(self):
        comment = self.get_object()
        return self.request.user.is_superuser or comment.author == self.request.user


class CommentUpdate(LoginRequiredMixin, CommentOwnerOrSuperuserMixin, generic.UpdateView):
    model = Comment
    fields = ["body"]
    template_name = "discussionboard/comment_form.html"

    def get_success_url(self):
        return reverse_lazy("discussionboard:post_detail", kwargs={"slug": self.object.Post.slug})

- I then add the following URL path into my urls.py patterns:

path("comment/<int:pk>/edit/", views.CommentUpdate.as_view(), name="comment_edit"),

- I then create the comment_form.html template within discussionboard/templates/discussionboard.

- Finally I add the 'Edit' button to my html code in post_detail.html:

{% if user == comment.author or user.is_superuser %}
  <a class="btn btn-sm btn-outline-primary"
     href="{% url 'discussionboard:comment_edit' comment.pk %}">
     Edit
  </a>

- After saving these changes, I can now edit comments now too:

![Comments editing](/static/images/Discussion%20Board/Screenshot%202edit%20comments%20working.png)

- I commit my code to Github and Heroku and move on.

---

## Feedback Form

1. On my Home app, under all my current content, I would like there to be a feedback form which users can use to provide feedback on services and the app if they wish. To start, I need to create a Feedback model in home/models.py, I am going to use some code from ChatGPT to save some time as there is still a lot to do and want to get through these bits quickly:

from django.db import models
from django.contrib.auth.models import User

class Feedback(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    name = models.CharField(max_length=80, blank=True)
    email = models.EmailField(blank=True)
    message = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    handled = models.BooleanField(default=False)

    class Meta:
        ordering = ["-created_on"]

    def __str__(self):
        return f"Feedback #{self.pk} ({self.email or self.name or 'anonymous'})"

2. I then need to create a FeedbackForm within home/forms.py - I do not have a forms.py file in the home app directory so create this now and then populate with the below:

from django import forms
from .models import Feedback

class FeedbackForm(forms.ModelForm):
    class Meta:
        model = Feedback
        fields = ("name", "email", "message")
        widgets = {
            "message": forms.Textarea(attrs={"rows": 4}),
        }

3. Finally, ChatGPT recommends updating the homepage view to handle POST in home/views.py, I update the imports accordingly and then update my function based view for home to the below:

from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import FeedbackForm

def home(request):
    if request.method == "POST":
        form = FeedbackForm(request.POST)
        if form.is_valid():
            feedback = form.save(commit=False)
            if request.user.is_authenticated:
                feedback.user = request.user
                # optionally prefill name/email if you want
            feedback.save()
            messages.success(request, "Thanks! Your feedback has been sent.")
            return redirect("home")  # your homepage url name
    else:
        form = FeedbackForm()

    return render(request, "home/index.html", {"feedback_form": form})

4. I then add the below code for the form to appear in my index.html template at the the bottom of my page:

{% load crispy_forms_tags %}

<div class="container mt-5">
  <div class="card p-4">
    <h3 class="mb-3 text-center">Send feedback</h3>

    <form method="post">
      {% csrf_token %}
      {{ feedback_form|crispy }}
      <button type="submit" class="btn btn-primary w-100">Send</button>
    </form>
  </div>
</div>

5. I makemigrations and migrate the new database tables and then register the new class in my admin.py file in home:

from .models import Feedback

@admin.register(Feedback)
class FeedbackAdmin(admin.ModelAdmin):
    list_display = ("created_on", "email", "user", "handled")
    list_filter = ("handled", "created_on")
    search_fields = ("email", "name", "message")

6. I refresh my page but can only see so much of the feedback form and cannot scroll to see the rest:

![Feedback form not fully showing](/static/images/Feedback%20form/Screenshot%20feedbackform%20not%20displaying%20whole%20content.png)

7. I inspect this in Devtools and create a temporary css class to change the fixed height of the text-area box for messages, this makes the messages box taller but still not fully viewable meaning the page has been clipped off somewhere. ChatGPT recommends updating my code to the below in my feedback form in forms.py:

class FeedbackForm(forms.ModelForm):
    class Meta:
        model = Feedback
        fields = ("name", "email", "message")
        widgets = {
            "message": forms.Textarea(attrs={
                "rows": 8,
                "class": "form-control",
                "placeholder": "Your feedback..."
            }),
        }

8. I can now see the bottom of the feedback message window but no buttons to then submit the feedback with. I then update my html to add another div beneath the feedback form div. I refresh my page and can now see the 'Sebd' button for my feedback form. I am going to test that I can submit a Feedback form and if successful will commit my code and move on to my authentication message:

![Feedback form fully showing](/static/images/Feedback%20form/Screenshot%20feedback%20form%20working.png)

9. I enter some information in the feedback form and click 'Send', I can then see the feedback message in the Admin panel under Home > Feedback:

![Feedback form fully showing](/static/images/Feedback%20form/Screenshot%20admin%20home%20feedback.png)

10. It would be good if the user got a message to confirm it had been sent so I will add this in now. 

11. I confirm that messages is enabled in my settings.py file in the below areas, which it is:

INSTALLED_APPS = [
    ...
    "django.contrib.messages",
    ...
]

MIDDLEWARE = [
    ...
    "django.contrib.messages.middleware.MessageMiddleware",
    ...
]

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            os.path.join(BASE_DIR, 'templates'),
            os.path.join(BASE_DIR, 'templates', 'allauth'),
        ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

12. I then add a messages display block in base.html:

{% if messages %}
  <div class="container mt-3">
    {% for message in messages %}
      <div class="alert alert-{{ message.tags }} alert-dismissible fade show" role="alert">
        {{ message }}
        <button type="button" class="btn-close" data-bs-dismiss="alert" aria-label="Close"></button>
      </div>
    {% endfor %}
  </div>
{% endif %}

13. Then at the bottom of my base.html above my static JS, I add the script src for Bootstrap so I can get the close 'x' to work on clicking off messages:

<script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/js/bootstrap.bundle.min.js"></script>

14. Then I will add messages in my views for all the different elements where a message would be appropriate:

- Feedback Form - in home/views.py I add the below into my current home view:

inside POST success:
messages.success(request, "Thanks! Your feedback has been sent.")
on invalid form:
messages.error(request, "Please correct the errors in the form and try again.")

15. A quick test of the feedback form on the Homepage shows this is working so I move onto the other elements now. I next look at my Comment submit view and update by adding the below code into the post_detail function I have in discussionboard/views.py:

            messages.success(request, "Your comment has been posted.")
            return redirect("discussionboard:post_detail", slug=post.slug)
        else:
            messages.error(request, "Couldn’t post comment — please check the form.")

    else:
        comment_form = CommentForm()

16. I refresh my page and go to my Discussion Board and open a post and get message prompts upon creating and trying to submit comments without information. I now need to update the class based views for PostUpdate, PostDelete and PostCreate with the appropriate message code:

class PostCreate(LoginRequiredMixin, generic.CreateView):

        messages.success(self.request, "Post created successfully.")

class PostUpdate(LoginRequiredMixin, PostOwnerOrSuperuserMixin, generic.UpdateView):
    ...
    def form_valid(self, form):
        messages.success(self.request, "Post updated successfully.")
        return super().form_valid(form)

class PostDelete(LoginRequiredMixin, PostOwnerOrSuperuserMixin, generic.DeleteView):

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, "Post deleted.")
        return super().delete(request, *args, **kwargs)

17. I update the code in views.py and refresh my page, I test whether I am then prompted on post creation/updates etc. and the new code is working. When I try to edit a post, I am taken to a new page to make changes but then when clicking 'Save' I am taken to an error page:

ImproperlyConfigured at /discussionboard/i-love-jogging/edit/
No URL to redirect to.  Either provide a url or define a get_absolute_url method on the Model.

18. I troubleshoot with ChatGPT who advises to add get_success_url back to PostUpdate, I add the below back in to the bottom of PostUpdate function:

    def get_success_url(self):
        return reverse_lazy("discussionboard:post_detail", kwargs={"slug": self.object.slug})

19. I refresh my page again and now I have a message to say 'Post updated successfully. 

20. I am happy that the message prompts are working as should be so run collectstatic and then commit my code to Github and Heroku.

---

## Authentication Message in Footer

1. I am going to add an authentication message into my footer on the left hand side, to avoid clashing with social media links, that tells the user they are logged in and what account this is logged in as. I go to my base.html file and replace the footer code with the below from ChatGPT:

<footer class="bg-dark text-light mt-5">
  <div class="container py-3">
    <div class="row">

      <div class="col-md-6">
        {% if user.is_authenticated %}
          <p class="mb-0 small">
            Logged in as <strong>{{ user.username }}</strong>
          </p>
        {% else %}
          <p class="mb-0 small">
            You are not logged in
          </p>
        {% endif %}
      </div>

      <div class="col-md-6 text-end">
        <p class="mb-0 small">© Working Out Gym</p>
      </div>

    </div>
  </div>
</footer>

2. Now when I refresh my page, I can see it is showing me the message in the footer:

![Feedback form fully showing](/static/images/Feedback%20form/Screenshot%20admin%20home%20feedback.png)

---

## Merchandise App

1. Now the functionality of my homepage, dicussionboard and login is all working acceptedly well, I am going to start building my Merchandise app which is going to contain a list of the business' products that the users can purchase and see under their profile. To start with, I go to kaggle.com to find a sample dataset that I can use for my new app. I find one at: https://www.kaggle.com/datasets/ahrnishpdahal/gymshark-products-dataset

2. Next, I create the app using:

python3 manage.py startapp merchandise

3. Once the app is created, I add it to my INSTALLED APPS list in settings:

    'merchandise',

4. I am then going to look at adding all of the data from the dataset i found on the kaggle website. To do this I have consulted ChatGPT, I have downloaded the dataset zip file from the URL above and then extracted it into my folder in the below location:

working_out_gym > merchandise > data

5. I next need to create my models in my new app's models.py file for 'Product':

from django.db import models
from django.utils.text import slugify


class Product(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(unique=True, blank=True)

    category = models.CharField(max_length=100, blank=True)
    description = models.TextField(blank=True)

    price = models.DecimalField(max_digits=8, decimal_places=2)

    image_url = models.URLField(blank=True)

    brand = models.CharField(max_length=100, default="Gymshark")

    is_active = models.BooleanField(default=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name

6. I then run makemigrations and migrate:

python manage.py makemigrations
python manage.py migrate

7. I then create a management cmd:

merchandise/
    management/
        commands/
            import_products.py

8. I then run the import with the below cmd so the database will be filled with the products from the Kaggle dataset, I will be able to view these in my admin panel:

python manage.py import_products

9. However, this has errored with:

KeyError: 'product_name'

10. I have troubleshooted with ChatGPT who advises its a mismatch between columns in the dataset to what I have set in the model code for Products. I change my import_products.py code to the below temporarily so I can then run the import_products cmd again to see all the CSV columns from the dataset in the terminal:

import csv
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = "Import Gymshark dataset"

    def handle(self, *args, **kwargs):
        with open("merchandise/data/gymshark_products.csv", encoding="utf-8") as f:
            reader = csv.DictReader(f)
            self.stdout.write(self.style.WARNING(f"CSV columns: {reader.fieldnames}"))
            return

python manage.py import_products

CSV columns: ['title', 'product_type', 'vendor', 'tags', 'handle', 'variant_title', 'sku', 'price', 'inventory_quantity', 'image_src']


11. Once I update what the columns are in the dataset, I can then update my Product model accordingly:

class Product(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(unique=True, blank=True)

    product_type = models.CharField(max_length=120, blank=True)
    vendor = models.CharField(max_length=120, blank=True)

    tags = models.TextField(blank=True)

    variant_title = models.CharField(max_length=255, blank=True)
    sku = models.CharField(max_length=80, blank=True)

    price = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    inventory_quantity = models.IntegerField(default=0)

    image_src = models.URLField(blank=True)

    is_active = models.BooleanField(default=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            base = slugify(self.title)[:45]  # keep it short-ish
            slug = base
            i = 1
            while Product.objects.filter(slug=slug).exclude(pk=self.pk).exists():
                i += 1
                slug = f"{base}-{i}"
            self.slug = slug
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title

12. I then run makemigrations and select yes to all prompts in the terminal. I then migrate. 

13. I then update my import cmd with a new one from ChatGPT. 

14. Finally I run the below, to try to import my dataset again:

python manage.py import_products --clear

15. However, the import fails to run and gives the below error:

DataError: value too long for type character varying(200)

16. This is likely due to max_length settings on my character fields within my Product model. I go to models.py and add a max length of 1000 characters to my image_src field within my Product model:

    image_src = models.URLField(blank=True, max_length=1000)

17. I run makemigrations and then migrate, as I have made changes to the Product database table.

18. I then try to run the below cmd again:

python manage.py import_products --clear

19. However, this time it fails to run with a different error:

django.db.utils.DataError: value too long for type character varying(1000)

20. I query this with ChatGPT who advised that the longer fields in the datasets are causing issues and to resolve this I need to update the below fields in my merchandise/models.py file for Products:

image_src = models.TextField(blank=True)

- This was the TextField is safer than trying to guess a max length.

- I update this and then run my migrations again.

- I then need to stop massive values being saved by mistake. Some rows in the dataset may have image_src like "url2, url2,url3" but for my business we will just want to use the first image.

- Therefore, I need to update the import command i have in import_products.py so that it only keeps the first URL, replacing my current 'defaults' section with the below:

    Clean image URL
    image_src = (row.get("image_src") or "").strip()

    If multiple URLs exist, keep the first
    if "," in image_src:
        image_src = image_src.split(",")[0].strip()

    if " " in image_src and image_src.startswith("http"):
        image_src = image_src.split()[0].strip()

    defaults = {
        "product_type": (row.get("product_type") or "").strip(),
        "vendor": (row.get("vendor") or "").strip(),
        "tags": (row.get("tags") or "").strip(),
        "variant_title": (row.get("variant_title") or "").strip(),
        "sku": (row.get("sku") or "").strip(),
        "price": to_decimal(row.get("price")),
        "inventory_quantity": to_int(row.get("inventory_quantity")),
        "image_src": image_src,
        "is_active": True,
    }

- This permits the code to read the image, clean the image and then store the cleaned image value in a dictionary.

21. ChatGPT then mentions that mu current code for Products and the import could be cleaner and 30% shorter than what I currently have and can provide me with something that is easier for me to build my Stripe checkout on top of; the cleanest setup for Stripe Checkout is Product + Variant because Stripe items map to a specific purchasable thing which is usually a variant like small/black. I first update my models.py code in Merchandise to the below:
- adding the 'handle' field to group rows by handle into one Product
- cleans long tags + image_src
- adds a new model for ProductVariant under our current expanded Product class based view

class Product(models.Model):
    title = models.CharField(max_length=255)
    handle = models.SlugField(max_length=255, unique=True)  # from dataset
    slug = models.SlugField(max_length=255, unique=True, blank=True)

    product_type = models.CharField(max_length=120, blank=True)
    vendor = models.CharField(max_length=120, blank=True)

    tags = models.TextField(blank=True)
    image_src = models.TextField(blank=True)  # scraped URLs can be long

    is_active = models.BooleanField(default=True)

    # Stripe (optional now, useful later)
    stripe_product_id = models.CharField(max_length=255, blank=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            # use handle if possible (stable, already URL-friendly)
            base = self.handle or slugify(self.title)
            slug = base[:240]
            i = 1
            while Product.objects.filter(slug=slug).exclude(pk=self.pk).exists():
                i += 1
                slug = f"{base[:235]}-{i}"
            self.slug = slug
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title


class ProductVariant(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="variants")

    variant_title = models.CharField(max_length=255, blank=True)  # e.g. "Small / Black"
    sku = models.CharField(max_length=80, blank=True, db_index=True)

    price = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    inventory_quantity = models.IntegerField(default=0)

    image_src = models.TextField(blank=True)  # variant-specific image if present

    is_active = models.BooleanField(default=True)

    # Stripe (this is the important one later)
    stripe_price_id = models.CharField(max_length=255, blank=True)

    class Meta:
        constraints = [
            # SKU is the best unique key when present
            models.UniqueConstraint(fields=["sku"], name="uniq_variant_sku"),
            # fallback uniqueness (when SKU missing)
            models.UniqueConstraint(fields=["product", "variant_title"], name="uniq_variant_per_product_title"),
        ]

    def __str__(self):
        return f"{self.product.title} — {self.variant_title or self.sku or 'Variant'}"

22. After adding in the new model and changing the Products model, I run makemigrations and migrate consecutively. This runs successfully and now I can move on and update my import_products.py management cmd so that it is cleaner, grouped and Stripe friendly:

import csv
import re
from decimal import Decimal, InvalidOperation
from pathlib import Path

from django.core.management.base import BaseCommand
from django.db import transaction

from merchandise.models import Product, ProductVariant


def to_decimal(value) -> Decimal:
    if value is None:
        return Decimal("0.00")
    s = str(value).strip()
    if not s:
        return Decimal("0.00")
    s = re.sub(r"[^\d\.,-]", "", s).replace(",", "")
    try:
        return Decimal(s)
    except (InvalidOperation, ValueError):
        return Decimal("0.00")


def to_int(value) -> int:
    try:
        return int(float(str(value).strip()))
    except Exception:
        return 0


def clean_image_src(raw: str) -> str:
    s = (raw or "").strip()
    if not s:
        return ""
    # sometimes scraped data contains multiple URLs
    if "," in s:
        s = s.split(",")[0].strip()
    # sometimes contains extra whitespace after URL
    if " " in s and s.startswith("http"):
        s = s.split()[0].strip()
    return s


class Command(BaseCommand):
    help = "Import Gymshark CSV into Product + ProductVariant (grouped by handle)"

    def add_arguments(self, parser):
        parser.add_argument(
            "--path",
            type=str,
            default="merchandise/data/gymshark_products.csv",
            help="Path to the CSV file",
        )
        parser.add_argument(
            "--clear",
            action="store_true",
            help="Delete existing products & variants before import",
        )

    @transaction.atomic
    def handle(self, *args, **options):
        csv_path = Path(options["path"])

        if not csv_path.exists():
            self.stderr.write(self.style.ERROR(f"CSV not found: {csv_path}"))
            return

        if options["clear"]:
            ProductVariant.objects.all().delete()
            Product.objects.all().delete()
            self.stdout.write(self.style.WARNING("Cleared existing products & variants."))

        created_products = 0
        updated_products = 0
        created_variants = 0
        updated_variants = 0
        skipped_rows = 0

        with csv_path.open(encoding="utf-8-sig", newline="") as f:
            reader = csv.DictReader(f)
            self.stdout.write(self.style.WARNING(f"Detected columns: {reader.fieldnames}"))

            for row in reader:
                title = (row.get("title") or "").strip()
                handle = (row.get("handle") or "").strip()

                if not title or not handle:
                    skipped_rows += 1
                    continue

                product_defaults = {
                    "title": title,
                    "product_type": (row.get("product_type") or "").strip(),
                    "vendor": (row.get("vendor") or "").strip(),
                    "tags": (row.get("tags") or "").strip(),
                    "image_src": clean_image_src(row.get("image_src") or ""),
                    "is_active": True,
                }

                product, p_created = Product.objects.update_or_create(
                    handle=handle,
                    defaults=product_defaults,
                )
                if p_created:
                    created_products += 1
                else:
                    updated_products += 1

                variant_title = (row.get("variant_title") or "").strip()
                sku = (row.get("sku") or "").strip()

                variant_defaults = {
                    "product": product,
                    "variant_title": variant_title,
                    "price": to_decimal(row.get("price")),
                    "inventory_quantity": to_int(row.get("inventory_quantity")),
                    "image_src": clean_image_src(row.get("image_src") or ""),
                    "is_active": True,
                }

                # Use SKU as primary key if present (best for Stripe mapping)
                if sku:
                    variant, v_created = ProductVariant.objects.update_or_create(
                        sku=sku,
                        defaults=variant_defaults,
                    )
                else:
                    # Fallback (some datasets miss SKU)
                    variant, v_created = ProductVariant.objects.update_or_create(
                        product=product,
                        variant_title=variant_title,
                        defaults=variant_defaults,
                    )

                if v_created:
                    created_variants += 1
                else:
                    updated_variants += 1

        self.stdout.write(
            self.style.SUCCESS(
                "Import complete.\n"
                f"Products  - created: {created_products}, updated: {updated_products}\n"
                f"Variants  - created: {created_variants}, updated: {updated_variants}\n"
                f"Rows skipped (missing title/handle): {skipped_rows}"
            )
        )

23. I then run: 

python manage.py import_products --clear

24. It is clearing down the products but then staying stuck in the terminal and doing nothing. I cancel and then run:

python manage.py shell

And then: 

>>> from merchandise.models import Product
>>> Product.objects.count()

This returns 0, so the import hasn't been working.

25. I run Python shell again and then paste in the below to confirm the CSV file is actually readable, which it is as it returns values from within the file:

import csv
with open("merchandise/data/gymshark_products.csv", encoding="utf-8-sig", newline="") as f:
    r = csv.DictReader(f)
    first = next(r)
    print(first)
    print("title:", first.get("title"))
    print("handle:", first.get("handle"))

26. I advise the results back to ChatGPT who recommends that I now update my Product and ProductsVariant models as below:

Product
image_src = models.TextField(blank=True)

ProductVariant
sku = models.CharField(max_length=80, blank=True, null=True, db_index=True)
image_src = models.TextField(blank=True)

This is so:
- image_src on Product can be TextField(blank=True)
- image_src on ProductVariant can be TextField(blank=True)
- sku should allow null=True so blank SKUs don’t conflict


27. I update as advised and fix the importer so it only keeps the first image URL, I place this above my defaults dictionary in my import_products.py command:

for row in reader:
    title = (row.get("title") or "").strip()
    handle = (row.get("handle") or "").strip()

    if not title or not handle:
        skipped_rows += 1
        continue

    # ✅ clean image list into a single URL
    image_src = clean_image_src(row.get("image_src") or "")

    product_defaults = {
        "title": title,
        "product_type": (row.get("product_type") or "").strip(),
        "vendor": (row.get("vendor") or "").strip(),
        "tags": (row.get("tags") or "").strip(),
        "image_src": image_src,
        "is_active": True,
    }

    product, p_created = Product.objects.update_or_create(
        handle=handle,
        defaults=product_defaults,
    )
    if p_created:
        created_products += 1
    else:
        updated_products += 1

    variant_title = (row.get("variant_title") or "").strip()
    sku = (row.get("sku") or "").strip() or None  # ✅ empty -> None

    variant_defaults = {
        "product": product,
        "variant_title": variant_title,
        "price": to_decimal(row.get("price")),
        "inventory_quantity": to_int(row.get("inventory_quantity")),
        "image_src": image_src,
        "is_active": True,
    }

27. I run the import cmd again but it is returning an error so I consult ChatGPT about this who advises that I have two separate problems mixed together in the output:

28. NameError: reader is not defined at line 85 in class Command
That only happens when you accidentally have a for row in reader: outside the handle() method (i.e., at class/module level). Python tries to run it while importing the command, before reader exists.

29. After I fixed that and ran again, it got slow (nested savepoints from update_or_create) → I hit KeyboardInterrupt, and then Postgres eventually threw:
server closed the connection unexpectedly (often because Postgres restarted/crashed or the connection got killed while it was under heavy load).

The clean fix is: since I'm using --clear, don’t use update_or_create at all. Just create products/variants once, fast, with a cache. This avoids the savepoint spam that’s slowing you down and stressing Postgres.

ChatGPT recommends using the following code in place of my current import_products.py:

import csv
import re
from decimal import Decimal, InvalidOperation
from pathlib import Path

from django.core.management.base import BaseCommand

from merchandise.models import Product, ProductVariant


def to_decimal(value) -> Decimal:
    if value is None:
        return Decimal("0.00")
    s = str(value).strip()
    if not s:
        return Decimal("0.00")
    s = re.sub(r"[^\d\.,-]", "", s).replace(",", "")
    try:
        return Decimal(s)
    except (InvalidOperation, ValueError):
        return Decimal("0.00")


def to_int(value) -> int:
    try:
        return int(float(str(value).strip()))
    except Exception:
        return 0


def clean_image_src(raw: str) -> str:
    s = (raw or "").strip()
    if not s:
        return ""
    # dataset has multiple URLs separated by commas; keep first
    if "," in s:
        s = s.split(",")[0].strip()
    # remove any trailing junk after url
    if " " in s and s.startswith("http"):
        s = s.split()[0].strip()
    return s


class Command(BaseCommand):
    help = "Import Gymshark CSV into Product + ProductVariant (FAST create mode for --clear)"

    def add_arguments(self, parser):
        parser.add_argument(
            "--path",
            type=str,
            default="merchandise/data/gymshark_products.csv",
            help="Path to the CSV file",
        )
        parser.add_argument(
            "--clear",
            action="store_true",
            help="Delete existing products & variants before import",
        )

    def handle(self, *args, **options):
        csv_path = Path(options["path"])

        if not csv_path.exists():
            self.stderr.write(self.style.ERROR(f"CSV not found: {csv_path}"))
            return

        if options["clear"]:
            ProductVariant.objects.all().delete()
            Product.objects.all().delete()
            self.stdout.write(self.style.WARNING("Cleared existing products & variants."))

        # Cache products by handle so we only create once per handle
        product_cache = {}

        # Dedupe variants in-memory to avoid IntegrityErrors
        seen_skus = set()
        seen_variant_keys = set()  # (handle, variant_title) fallback

        created_products = 0
        created_variants = 0
        skipped_rows = 0
        row_num = 0

        with csv_path.open(encoding="utf-8-sig", newline="") as f:
            reader = csv.DictReader(f)
            self.stdout.write(self.style.WARNING(f"Detected columns: {reader.fieldnames}"))

            for row in reader:
                row_num += 1

                title = (row.get("title") or "").strip()
                handle = (row.get("handle") or "").strip()

                if not title or not handle:
                    skipped_rows += 1
                    continue

                image_src = clean_image_src(row.get("image_src") or "")
                product_type = (row.get("product_type") or "").strip()
                vendor = (row.get("vendor") or "").strip()
                tags = (row.get("tags") or "").strip()

                product = product_cache.get(handle)
                if product is None:
                    product = Product.objects.create(
                        title=title,
                        handle=handle,
                        product_type=product_type,
                        vendor=vendor,
                        tags=tags,
                        image_src=image_src,
                        is_active=True,
                    )
                    product_cache[handle] = product
                    created_products += 1

                variant_title = (row.get("variant_title") or "").strip()
                sku = (row.get("sku") or "").strip() or None

                # dedupe variants
                if sku:
                    if sku in seen_skus:
                        continue
                    seen_skus.add(sku)
                else:
                    key = (handle, variant_title)
                    if key in seen_variant_keys:
                        continue
                    seen_variant_keys.add(key)

                ProductVariant.objects.create(
                    product=product,
                    variant_title=variant_title,
                    sku=sku,
                    price=to_decimal(row.get("price")),
                    inventory_quantity=to_int(row.get("inventory_quantity")),
                    image_src=image_src,
                    is_active=True,
                )
                created_variants += 1

                if row_num % 250 == 0:
                    self.stdout.write(
                        f"Processed {row_num} rows... products: {created_products}, variants: {created_variants}"
                    )

        self.stdout.write(
            self.style.SUCCESS(
                "Import complete.\n"
                f"Products created: {created_products}\n"
                f"Variants created: {created_variants}\n"
                f"Rows skipped: {skipped_rows}"
            )
        )

It advises that this is better as:
- No chance of reader NameError (everything is inside handle()).
- No update_or_create() → massively fewer DB savepoints/locks → much faster.
- Designed for --clear (seed import) which is exactly your use case.

30. I try to run the import cmd again with the new code:

python manage.py import_products --clear

---

## Setting Local Database to Local SQLite and Resetting/Rebuilding PostgreSQL Database

1. This has failed again with an error message but my password for my database has been compromised so I must deal with that first. I am unable to reset the database password of my Postgre SQL database as it is owned by Code Institute and I need to protect my database security. 

To start with, I change my database to SQLite locally by going to settings.py abd updating the database content to the below:

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}

2. I save the file and then create the new local database using:

python manage.py migrate

3. This creates the db.sqlite3 file in the root of my Project folder.

4. This has now allowed me to run the below cmd and import all the products from the CSV file:

python manage.py import_products --clear

4. I verify the import with the following cmd:

python manage.py shell

from merchandise.models import Product, ProductVariant
print(Product.objects.count())
print(ProductVariant.objects.count())

- Which returns a number of products and variants.

5. I realise that I haven't added db.sqlite3 to my .gitignore file before committing to Github. I make sure that it is now added in there. 

6. I then run the following cmd from my project root to stop it tracking the file (keeping it only locally and removing from Git):

git rm --cached db.sqlite3

- This returns:

fatal: pathspec 'db.sqlite3' did not match any files

- Meaning the file was never committed. I then run the following cmd to ensure that it was definitely not committed:

git ls-files | findstr sqlite

- This doesn't return anything, meaning that I am safe. I am now going to create a new PostgreSQL Database and replace the one I have currently in my Project with the new one.

7. I request a new database from Code Institute at https://dbs.ci-dbs.net/ and then replace the URL in my env.py with my current database URL with the new one. 

8. I then run:

python manage.py migrate

- And I receive the following message:

  Your models in app(s): 'merchandise' have changes that are not yet reflected in a migration, and so won't be applied.
  Run 'manage.py makemigrations' to make new migrations, and then re-run 'manage.py migrate' to apply them.

- I run makemigrations which then allows me to run migrate.

9. I update my Heroku app settings for my DATABASE URL key with the new database URL.

---

## Merchandise Importing Products

1. I run the import cmd again since changing the database:

python manage.py import_products --clear

2. This completes successfully which I confirm by receiving a count after running the below cmds in powershell:

python manage.py shell

from merchandise.models import Product, ProductVariant
print(Product.objects.count())
print(ProductVariant.objects.count())

3. I check that my pages are still running on my local server. Everything looks to be okay on the Homepage, the feedback form produces a message to say it is sent after I populate all fields. All of the posts are gone from the Discussion Board but these can easily be added back in. I seem to be unable to access accounts using the password I set so I run the below on my superuser account:

python manage.py changepassword <username>

- I get the following result back:

CommandError: user 'fitnessguru' does not exist

- So it looks as though when I changed the database I lost my accounts and posts and previous content. I create a new superuser using:

python3 manage.py createsuperuser

- I recreate the superuser and verify the email address once logged into the admin panel as the superuser, I then create the standard users x 3 and verify their email addresses too. I then post 3 x posts as the superuser. 

4. I notice on the Discussion Board that the footer is not sticking to the bottom of the page. I query this with ChatGPT who recommends changing the body class in base.html from:

<body class="d-flex flex-column h-100 main-bg">

To:

<body class="d-flex flex-column min-vh-100 main-bg">

- And also to wrap the block content and endblock content blocks in a div with flex-grow-1 class applied.

- It recommends adding the below code to CSS to add bottom padding content so it never hides behind the footer:

body {
  padding-bottom: 1rem;
}

- It also points out there are three links for Bootstrap in my head and then a single one in the bottom of my base.html and it recommends removing the three in my head element, I update this now.

5. After making these changes and refreshing the page, the footer is now sticking to the page. I quickly test the other functionalities such as creating post as standard user and leaving comment on another post.

6. I realise that I never updated settings.py to go back to using the PostgreSQL database environment variable now the new URL was set in env.py. Therefore, I update the DATABASES element of settings.py with:

DATABASE_URL = os.environ.get("DATABASE_URL")

if DATABASE_URL:
    DATABASES = {"default": dj_database_url.parse(DATABASE_URL)}
else:
    DATABASES = {
        "default": {
            "ENGINE": "django.db.backends.sqlite3",
            "NAME": os.path.join(BASE_DIR, "db.sqlite3"),
        }
    }

7. Once I update this in settings.py I then need to run:

python manage.py migrate

8. Once this runs successfully, I can then run the products import cmd again ready for building my Merchandise app:

python manage.py import_products --clear

- This is going to take a while to run as there are so many products and it is essentially rebuilding the database again. I have added the below code to dj_database_url.parse() call so Postgres connections stay alive longer:

conn_max_age=600

10. This completes successfully so I commit my code to Github and Heroku.

11. Now that my CSV with my dataset is successfully imported, I want to look at creating soem fixture json files from the data for Categories and Products. I consult ChatGPT how to best do this and they recommend creating a new Category model and link it to the Product model in merchandise/models.py:

class Category(models.Model):
    name = models.CharField(max_length=120, unique=True)
    slug = models.SlugField(max_length=140, unique=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)[:140]
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name

12. I then run:

python manage.py makemigrations
python manage.py migrate

13. I now need to update my import to populate Category from product_type, inside my import loop I replace where it creates the product so it assigns a category:

from merchandise.models import Category, Product, ProductVariant

category_name = (row.get("product_type") or "").strip()
category = None
if category_name:
    category, _ = Category.objects.get_or_create(name=category_name)
product = Product.objects.create(
    title=title,
    handle=handle,
    category=category,
    vendor=vendor,
    tags=tags,
    image_src=image_src,
    is_active=True,
)

14. I update the code as advised and then create the two new fixture files using:

python manage.py dumpdata merchandise.Category --indent 2 > merchandise/fixtures/categories.json

python manage.py dumpdata merchandise.Product merchandise.ProductVariant --indent 2 > merchandise/fixtures/products.json

15. I can now see the two new fixture files in the fixtures folder in Merchandise app. 

16. I am going to install Pillow using the following cmd:

pip install pillow==10.3.0

17. Once successfully installed I can then add to my requirements file:

pip3 freeze local > requirements.txt 

18. I am now going to register the Products and Category models into my merchandise/admin.py file using the below:

from .models import Product

admin.site.register(Product)
admin.site.register(Category)


19. I am then going to run the following cmds to use my new fixtures:

python manage.py migrate
python manage.py loaddata categories

- When I run my loaddata cmd for categories it is erroring with 

UnicodeDecodeError: 'utf-8' codec can't decode byte 0xff in position 0: invalid start byte

- I check my encoding on my categories fixture file but then find it is blank apart from [], I run the below cmd to see if I have categories in my database:

python manage.py shell -c "from merchandise.models import Category; print(Category.objects.count())"

- I then confirm that my Product model has category field but it does not so I add the below in place of the current product_type field:

category = models.ForeignKey(Category, null=True, blank=True, on_delete=models.SET_NULL, related_name="products")

- I then run makemigrations and migrate successfully.

- Once I have done that, I then need to update my import_products.py loop from:

product_type = (row.get("product_type") or "").strip()

To:

category_name = (row.get("product_type") or "").strip()
category = None
if category_name:
    category, _ = Category.objects.get_or_create(name=category_name)

And instead of in my Product.objects.create() block in my importer loop:

product_type=product_type,

To:

category=category,

- I then run my imports cmd again:

python manage.py import_products --clear

- I make sure that this is running again before leaving it to run and getting lunch.

- When I come back and check it it has errored:

django.db.utils.IntegrityError: duplicate key value violates unique constraint "merchandise_category_slug_key" DETAIL: Key (slug)=(womens-socks) already exists.

- I query this with ChatGPT who advises the failure I am hitting is a Category slug uniqueness collision, meaning I have two different category names that both slugify to the same slug:

duplicate key value violates unique constraint "merchandise_category_slug_key"
Key (slug)=(womens-socks) already exists.

- To fix this, I will need to make Category slug unique automatically, therefore, I need to update the Category.save() in merchandise/models.py. I update this to:

class Category(models.Model):
    name = models.CharField(max_length=120, unique=True)
    slug = models.SlugField(max_length=140, unique=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            base = slugify(self.name)[:130] or "category"
            slug = base
            i = 1
            while Category.objects.filter(slug=slug).exclude(pk=self.pk).exists():
                i += 1
                slug = f"{base[:130 - (len(str(i)) + 1)]}-{i}"
            self.slug = slug
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name

20. Once this is updated I run again:

python manage.py import_products --clear

- While this is running, I delete my current fixtures folder in the Merchandise app directory.

- Once the import cmd finishes running successfully, I can then create a new 'fixtures' folder in my merchandise app directory and then run:

python manage.py dumpdata merchandise.Category --indent 2 --output merchandise/fixtures/categories.json

- I check the newly created categories.json file and it is now populated with data. I then run the following cmd to create the new json file for products:

python manage.py dumpdata merchandise.Product merchandise.ProductVariant --indent 2 --output merchandise/fixtures/products.json

21. Once both json files are created and my products imported I can then use my fixtures, I am going to load the categories first as the products need to know which category to go in:

python manage.py loaddata merchandise/fixtures/categories.json

- This installs 91 objects from 1 fixture.

22. The next thing I do is then create the products from the fixture file using:

python manage.py loaddata merchandise/fixtures/products.json

- However, this has returned an error which ChatGPT believes means the fixture file wasn't run correctly. I run the below in my terminal:

python manage.py dumpdata merchandise.Product merchandise.ProductVariant --indent 2 --output merchandise/fixtures/products.json

23. I then run my loaddata cmd again against the new json file:

python manage.py loaddata merchandise/fixtures/products.json

24. I leave this to run and it eventually finishes installing the products from the fixture file into my project:

Installing json fixture 'products' from 'C:\Users\leila\OneDrive\Desktop\Documents\vscode-projects\working_out_gym\merchandise/fixtures'.
Resetting sequences
Installed 52258 object(s) from 1 fixture(s)

25. To confirm that my fixtures have installed correctly, I will run my page locally and go to my Admin panel to ensure they are now showing:

![Admin Panel showing Categorys and Products](/static/images//Merchandise/Screenshot%20admin%20panel%20showing%20products%20and%20vategorys.png)

24. If I click 'Change' on Products then I can see a list of all the products we have imported:

![Admin Panel Products List in Change](/static/images/Merchandise/Screenshot%20admin%20panel%20products%20change.png)

25. If I then click into one of the products then I can see everything as I would expect, the title, handle, slug, category, tags, image src, active status and stripe product ID.

26. I will now commit my changes to Github and Heroku.

---

## Merchandise App Admin

1. To start with, I will rectify the incorrect plural spelling of 'categorys' that currently shows in the admin panel. This is an easy fix, I just need to add the below Meta class into my Category model:

    class Meta:
        verbose_name_plural = 'Categories'

2. Then in my admin.py file, I am going to create to create 2 x new classes for product admin and category admin that will both extend the built in model admin class. I am going to use Code Institute's code for these from their Boutique Ado Project and tweak to match my models; ChatGPT also provided some guidance around the models:

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("name", "slug")
    prepopulated_fields = {"slug": ("name",)}
    search_fields = ("name",)

#ChatGPT Code
class ProductVariantInline(admin.TabularInline):
    model = ProductVariant
    extra = 0
    fields = ("variant_title", "sku", "price", "inventory_quantity", "is_active")
    readonly_fields = ()
    show_change_link = True


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ("title", "handle", "category", "vendor", "is_active")
    list_filter = ("is_active", "category", "vendor")
    search_fields = ("title", "handle", "vendor", "tags")
    ordering = ("title",)
    inlines = [ProductVariantInline]


@admin.register(ProductVariant)
class ProductVariantAdmin(admin.ModelAdmin):
    list_display = ("product", "variant_title", "sku", "price", "inventory_quantity", "is_active")
    list_filter = ("is_active",)
    search_fields = ("sku", "product__title", "variant_title")
    ordering = ("product__title", "variant_title")
    )

3. If I go back into my admin panel now, I can see that 'Categories' is spelt correctly:

![Admin Panel Correct Spelling of Categories](/static/images/Merchandise/Screenshot%20admin%20categories%20correct%20spelling.png)

- The Products and Categories fields are looking good as well:

![Admin Categories Fields](/static/images/Merchandise/Screenshot%20admin%20categories%20fields.png)

![Admin Products Fields](/static/images/Merchandise/Screenshotadmin%20products%20fields.png)

4. This looks good so I will commit my code to Github and then get the first of my products views set up in views.py.

---

## Merchandise App Products List Views

1. To start, I add in the below to my Merchandise/views.py as the view will be simplistic to start with. This will return the template products.html, which I will build next. It will import the model I have for Product and use context as I need to send things back to the template:

from django.shortcuts import render
from .models import Product

def all_products(request)
    """ A view to show list of all Products"""

    products = Product.objects.all()

    context = {
        'products': products
    }
    
    return render(request, 'merchandise/products.html', context)

2. The next thing that I want to do is create my urls in my merchandise/urls.py file, I populate this as below, importing path so we can use it in our URL pattern and then setting the views to use the new function based view we created for all_products and finally setting the name to 'merchandise':

from django.urls import path
from . import views

urlpatterns = [
    path("", views.all_products, name="merchandise"),
]

3. I save this and then include the new URL in my project level urls.py file with the below pattern, as I did for the discussionboard app:

    path("merchandise/", include("merchandise.urls")),

4. I am now going to update the navbar href with the new link for my Merchandise app in my base.html:

  <a class="d-block nav-link" href="{% url 'merchandise:products' %}">Merchandise</a>

5. Next I create a templates/merchandise folder and within that create a products.html file as I put in my view earlier. I am going to use my homepage index.html template and then tweak as appropriate:

{% extends "base.html" %}

{% load static %}

{% block content %}
<div class="container mt-5 pt-5">
<h2>Merchandise</h2>
  <p class="leading-p mx-auto d-block">Welcome to the <strong>Working Out Gym's</strong> merchandise page,
    where you will find all products being sold by our business!</p>
</div>

<div class="container mt-5 mb-5">
</div>
{% endblock %}

6. However, after applying this I am no longer able to run my dev server. I try closing the session and creating a new but I am still getting a server 500 error. I turn debug to True and then reload the page to see what it is telling me and it is giving me the below error message:

NoReverseMatch at /
'merchandise' is not a registered namespace

- I check and I have not created the app_name for merchandise in my merchandise/urls.py file so add this in now and then refresh my page. The page is now loading. I further expand my new products.html and add a new block content tag with a div for container, a div for row and then a div for column within one another. Then within the column div I set the template variable that I created for products:

{% block content %}
<div class="container">
    <div class="row">
        <div class="col">
            {{ products }}
        </div>
    </div>
</div>
{% endblock %}

7. I refresh my page and can see the query set is showing under my header and paragraph content:

![Merchandise Page Products Queryset](/static/images/Merchandise/Screenshot%20products%20lisitng%20query%20set.png)

8. I commit my changes to Github and Heroku and then move onto the next.

9. I am now going to fill in the template blocks that I left empty in my new products.html. First I will apply the container-fluid class to my outer div in my second block. This is going to be the container for my products:

{% block content %}
    <div class="container-fluid">
        <div class="row">
            <div class="col">
            {{ products }}
            </div>
        </div>
    </div>
{% endblock %}

10. I remove the {{ products }} tag and then add a div with a class of "product-container col10 offset-1" below the div for my container. I then update my classes on the row div to include mt-1 and mb-2 classes:

{% block content %}
    <div class="container-fluid">
        <div class="product-container col-10 offset-1">
        <div class="row mt-1 mb-2"></div>
            <div class="row">
            </div>
        </div>
    </div>
{% endblock %}

11. I am then going to steal Code Institute's Django for loop to iterate through the product variable within my second div row in the container. For each product, it generates a column inside which will be a bootstrap card. Products stack on mobile, be side-by-side on small and medium screens, three columns on large screens and four columns on extra-large. The code they have used comes from the Bootstrap documentation; the card is divided into a top which contains the product image and then the body contains the product name, and the footer contains the price and rating. The image portion of the card uses an if statement that renders the product image using the image fields URL attribute if an image exists or the default image from the media folder otherwise. The card body is just a paragraph with the products name and the card footer contains a row and a column which will envelop the product price and rating if one exists:

{% block content %}
    <div class="container-fluid">
        <div class="product-container col-10 offset-1">
        <div class="row mt-1 mb-2"></div>
            <div class="row">
                {% for product in products %}
                <div class="col-sm-6 col-md-6 col-lg-4 col-xl-3">
                    <div class="card h-100 border-0">
                        {% if product.image %}
                        <a href="">
                            <img class="card-img-top img-fluid" src="{{ product.image.url }}" alt="{{ product.name }}">
                        </a>
                        {% else %}
                        <a href="">
                            <img class="card-img-top img-fluid" src="{{ MEDIA_URL }}noimage.png" alt="{{ product.name }}">
                        </a>
                        {% endif %}
                        <div class="card-body pb-0">
                            <p class="mb-0">{{ product.name }}</p>
                        </div>
                        <div class="card-footer bg-white pt-0 border-0 text-left">
                            <div class="row">
                                <div class="col">
                                    <p class="lead mb-0 text-left font-weight-bold">${{ product.price }}</p>
                                    {% if product.rating %}
                                        <small class="text-muted"><i class="fas fa-star mr-1"></i>{{ product.rating }} / 5</small>
                                    {% else %}
                                        <small class="text-muted">No Rating</small>
                                    {% endif %}
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
{% endblock %}

12. I have added in the above content and was expecting to then see the products listed but it appears something in the code hasn't agreed with mine as I'm being presented with a server 500 error. I turn Debug to true and investigate. The page is saying that my last endblock is incorrect. I decide to add in the rest of the code from Code Institute:

{% if forloop.counter|divisibleby:1 %}
                            <div class="col-12 d-sm-none mb-5">
                                <hr>
                            </div>
                        {% endif %}                        
                        {% if forloop.counter|divisibleby:2 %}
                            <div class="col-12 d-none d-sm-block d-md-block d-lg-none mb-5">
                                <hr>
                            </div>
                        {% endif %}
                        {% if forloop.counter|divisibleby:3 %}
                            <div class="col-12 d-none d-lg-block d-xl-none mb-5">
                                <hr>
                            </div>
                        {% endif %}
                        {% if forloop.counter|divisibleby:4 %}
                            <div class="col-12 d-none d-xl-block mb-5">
                                <hr>
                            </div>
                        {% endif %}
                    {% endfor %}
                </div>
            </div>
        </div>
    </div>

13. After adding in the last part and saving, I can now see the change on my Merchandise page, but there is no product name or images:

![Merchandise Page Products no images or names](/static/images/Merchandise/Screenshot%20product%20listings%20no%20image%20or%20name.png)

14. I have not ran a collectstatic since adding images so I will run this now and see if this makes any difference. It does not.

15. I troubleshoot the error with ChatGPT who advises that the template from Code Institute is using the fields: name, price, rating and image but the dataset I have used has title instead of name, image_src and not image, price is on ProductVariant.price and not Product.price, and it does not have a rating. I need to fix my template to match my models.

- To resolve the issue with images not showing, I replace my current image block with:

{% if product.image_src %}
  <img class="card-img-top img-fluid" src="{{ product.image_src }}" alt="{{ product.title }}">
{% else %}
  <img class="card-img-top img-fluid" src="{% static 'images/noimage.png' %}" alt="{{ product.title }}">
{% endif %}


- To resolve the code so that the product name displays, I replace the product.name tag with the product.title tag as below:

<p class="mb-0">{{ product.title }}</p>

- As my dataset uses product variant pricing, I need to update my view to show the cheapest variant price. First, I need to update my view to annotate a "from price", in merchandise/views.py in my all_products function, I update the current products variable, within the function, with the below code:

    products = (
        Product.objects.filter(is_active=True)
        .annotate(from_price=Min("variants__price"))  # assumes related_name="variants"
    )

- Next I need to update the template so it doesn't use the Django tag product.price but instead uses the if statement provided by ChatGPT below:

{% if product.from_price %}
  <p class="lead mb-0 font-weight-bold">£{{ product.from_price }}</p>
{% else %}
  <small class="text-muted">Price unavailable</small>
{% endif %}

- I also need to replace the fields I have for 'rating' with 'product category' which is a field in my dataset. I replace the code for rating with the below:

{% if product.category %}
  <small class="text-muted">{{ product.category.name }}</small>
{% endif %}

16. I refresh my page but I am seeing a NameError at /merchandise to say name 'Min' is not defined, this relates to the below line in my code in views.py:

        .annotate(from_price=Min("variants__price"))  # assumes related_name="variants"

17. I troubleshoot this with ChatGPT who advises that I need to import Min from django.db.models and update my function for all_products to the below:

products = (
        Product.objects.filter(is_active=True)
        .select_related("category")
        .annotate(from_price=Min("variants__price"))
    )

    context = {"products": products}
    return render(request, "merchandise/products.html", context)

18. I then need to update my products.html template with the below:

{% for product in products %}
  <div class="col-sm-6 col-md-6 col-lg-4 col-xl-3">
    <div class="card h-100 border-0">

      <a href="#">
        {% if product.image_src %}
          <img class="card-img-top img-fluid" src="{{ product.image_src }}" alt="{{ product.title }}">
        {% else %}
          <img class="card-img-top img-fluid" src="{% static 'images/noimage.png' %}" alt="{{ product.title }}">
        {% endif %}
      </a>

      <div class="card-body pb-0">
        <p class="mb-0">{{ product.title }}</p>

        {% if product.category %}
          <small class="text-muted">{{ product.category.name }}</small>
        {% endif %}
      </div>

      <div class="card-footer bg-white pt-0 border-0 text-left">
        {% if product.from_price %}
          <p class="lead mb-0 text-left fw-bold">£{{ product.from_price }}</p>
        {% else %}
          <small class="text-muted">Price unavailable</small>
        {% endif %}
      </div>

    </div>
  </div>
{% endfor %}

19. Now when I reload the Merchandise page, I am seeing the product listings:

![Merchandise Page Products now showing](/static/images/Merchandise/Screenshot%20products%20now%20displaying.png)

20. However, this isn't ideal as I would like to be showing the products in three columns on the page. I look at the bootstrap classes being applied to my div for the products tag and can see I am using col-xl-3 which forces 4 columns on xl screens. ChatGPT comes up with some better code for my block content area, this removes the <hr> elements as they are no longer needed in the new code with the addition of the g-4 class which is Bootstrap gutter spacing. I am instead also using the following instead of the previous Bootstrap grid classes:
- row-cols-1 → stacked on mobile
- row-cols-sm-2 → 2 across on small + medium
- row-cols-lg-3 → 3 across on large and up

{% block content %}
<div class="container-fluid">
  <div class="product-container col-10 offset-1">
    <div class="row mt-1 mb-2"></div>

    <div class="row row-cols-1 row-cols-sm-2 row-cols-lg-3 g-4">
      {% for product in products %}
        <div class="col">
          <div class="card h-100 border-0">

            <a href="#">
              {% if product.image_src %}
                <img class="card-img-top img-fluid" src="{{ product.image_src }}" alt="{{ product.title }}">
              {% else %}
                <img class="card-img-top img-fluid" src="{% static 'images/noimage.png' %}" alt="{{ product.title }}">
              {% endif %}
            </a>

            <div class="card-body pb-0">
              <p class="mb-0">{{ product.title }}</p>

              {% if product.category %}
                <small class="text-muted">{{ product.category.name }}</small>
              {% endif %}
            </div>

            <div class="card-footer bg-white pt-0 border-0 text-left">
              {% if product.from_price %}
                <p class="lead mb-0 fw-bold">£{{ product.from_price }}</p>
              {% else %}
                <small class="text-muted">Price unavailable</small>
              {% endif %}
            </div>

          </div>
        </div>
      {% endfor %}
    </div>

  </div>
</div>
{% endblock %}

21. I save this and refresh my page and now can see the 3 products per row as I wanted:

![Merchandise Page Products 3 products per row](/static/images/Merchandise/Screenshot%203%20products%20per%20row.png)

---

## Merchandise App - Products Details Views

1. Now that the all_products view is working successfully on the Merchandise app, I want to add a view so that when the user clicks a product they are taken to a new page where they can view and review the products. To start with, I copy and paste the function view I created for all_products and paste this directly beneath the function. I update the name of the view to product_detail and change the name of the template to product_detail.html, I add in product ID to the parameters. I only want to return one product so update products to use get_object_or_404 taking in the product id. I then remove the 's' from 'products' in context and then import the get_object_or_404 function:

def product_detail(request, product_id):
    """ A view to show individual Products"""

    product = get_object_or_404(Product, pk=product_id)

    context = {
        'product': product
    }
    
    return render(request, 'merchandise/product_detail.html', context)

2. Once my view is created, I then need to create a new URL for my view in merchandise/urls.py:

path("<product_id>", views.product_detail, name="product_detail")

3. I am going to duplicate the products.html file and call this product_detail.html as per my view, then take out and rearrange the grid according to what we will want displayed for the indidividual products.

- I remove the content from my header container at the top of the template as will not be needing this on the individual products.

- I delete all the content from the second block apart from the div container-fluid. I then  add my div code that I used for the grid layout of my products.html code and add the offset-2 class to this to push it into the middle of the screen:

        <div class="row row-cols-1 row-cols-sm-2 row-cols-lg-3 g-4 offset-lg-2">

- I then borrow the code from Code Institute's Boutique Ado for the image container and tweak according to my own Project:

            <div class="image-container my-5">
                {% if product.image_src %}
                    <a href="{{ product.image_src }}" target="_blank">
                        <img class="card-img-top img-fluid" src="{{ product.image_src }}" alt="{{ product.title }}">
                    </a>
                {% else %}
                    <a href="">
                        <img class="card-img-top img-fluid" src="{% static 'images/noimage.png' %}" alt="{{ product.title }}">
                    </a>
                {% endif %}
            </div>
        </div>

- In the second column for product description, I borrow the code from Code Institute's Boutique Ado Project and tweak accordingly for my own Project:

        <!-- Code Institute ACK-->
        <div class="row row-cols-1 row-cols-sm-2 row-cols-lg-3 g-4">
            <div class="product-details-container mb-5 mt-md-5">
                <p class="mb-0">{{ product.title }}</p>
                <p class="lead mb-0 text-left font-weight-bold">${{ product.from_price }}</p>
                {% endif %}
                <p class="mt-3">{{ product.description }}</p>
            </div>
        </div>
    </div>
</div>
{% endblock %}

4. I reload my Merchandise page and then try to load an individual product by clicking on it, however, nothing happens apart from a # is added to the end of the URL browser bar. I troubleshoot with ChatGPT who advises that my product cards to link to 'href="#" so I need to update a couple of things:

- In my products.html template I need to change the card link from:

<a href="#">

To: <a href="{% url 'merchandise:product_detail' product.id %}">

- I update this and then I need to fix the app level urls.py, my path is missing the type converter and slash so I update this as below:

path("<int:product_id>/", views.product_detail, name="product_detail"),

- There are a few issues in my product_detail template as well, I have product.image.url which need to change to image_src, I need to remove the stray {% endif %} in the middle and I do not have product.description in my model. ChatGPT provides me with the below corrected version so I use this for now:

{% extends "base.html" %}
{% load static %}

{% block page_header %}
<div class="container mt-5 pt-5"></div>
{% endblock %}

{% block content %}
<div class="container my-5">
  <div class="row g-4">

    <div class="col-12 col-md-6">
      {% if product.image_src %}
        <a href="{{ product.image_src }}" target="_blank" rel="noopener">
          <img class="img-fluid" src="{{ product.image_src }}" alt="{{ product.title }}">
        </a>
      {% else %}
        <img class="img-fluid" src="{% static 'images/noimage.png' %}" alt="{{ product.title }}">
      {% endif %}
    </div>

    <div class="col-12 col-md-6">
      <h3 class="mb-2">{{ product.title }}</h3>

      {% if product.category %}
        <p class="text-muted mb-2">{{ product.category.name }}</p>
      {% endif %}

      {% if product.variants.exists %}
        <p class="lead fw-bold mb-3">
          From £{{ product.variants.all|first.price }}
        </p>
      {% endif %}

      <p class="text-muted">{{ product.vendor }}</p>
    </div>

  </div>
</div>
{% endblock %}

- I also need to update my view so product.from_price will also exist in the product_detail view, to do this I update my detail view to this:

def product_detail(request, product_id):
    """ A view to show individual Products"""

    product = get_object_or_404(
        Product.objects.annotate(from_price=Min("variants__price")),
        pk=product_id
    )
    
    return render(request, 'merchandise/product_detail.html', {"product": product})

- Once that is in place, I can then update the price section of the product_details template:

{% if product.from_price %}
  <p class="lead fw-bold">From £{{ product.from_price }}</p>
{% endif %}

5. I reload my server again, doing a shift ctrl + R to hard refresh, and then try acessing a product from the page and find this is loading okay now:

![Merchandise Product Detail Working](/static/images/Merchandise/Screenshot%20product%20detail%20working.png)

5. I commit my code and move onto increasing the Merchandise page functionality.

---

## Navbar Styling on Different Screen Sizes

1. I have decided to quickly sort my Navbar sizing issue on my small screens, as it currently doesn't look right with the text for 'Working Out Gym' so I want to replace this with a Favicon and then also make the text smaller for 'Register' and 'Login'. To achieve this, I start by creating a new folder in my base templates folder called 'includes' that contains two htmls: mobile-top-header.html and main-nav.html:

![Navbar styling on different screen sizes](/static/images/Navbar/Screenshot%20includes%20templates%20directory%20and%20html%20templates%20for%20nav.png)

2. Then once I have done this, I replace my current nav elements in my base.html with:

<!-- Navigation -->
{% include "includes/mobile-top-header.html" %}
{% include "includes/main-nav.html" %}

3. I then populate the mobile-top-header.html with the below code:

<div class="d-lg-none dark-bg shadow-sm">
  <div class="container-fluid py-2">
    <div class="d-flex justify-content-between align-items-center">

      <!-- Left: auth links -->
      <div class="small-auth-links">
        {% if user.is_authenticated %}
          <a class="nav-link d-inline p-0 me-2 small" href="{% url 'account_logout' %}">Logout</a>
        {% else %}
          <a class="nav-link d-inline p-0 me-2 small" href="{% url 'account_signup' %}">Register</a>
          <a class="nav-link d-inline p-0 small" href="{% url 'account_login' %}">Login</a>
        {% endif %}
      </div>

      <!-- Centre: favicon/logo -->
      <a href="{% url 'home' %}" class="mobile-brand text-center">
        <img src="{% static 'images/favicon.png' %}" alt="Working Out Gym logo" class="mobile-logo">
      </a>

      <!-- Right: navbar toggler -->
      <button
        class="navbar-toggler border-0"
        type="button"
        data-bs-toggle="collapse"
        data-bs-target="#main-nav"
        aria-controls="main-nav"
        aria-expanded="false"
        aria-label="Toggle navigation"
      >
        <span class="navbar-toggler-icon"></span>
      </button>

    </div>
  </div>
</div>

4. I then populate the main-nav.html with the below code from ChatGPT:

<nav class="navbar navbar-expand-lg navbar-light dark-bg shadow-sm">
  <div class="container-fluid">

    <!-- Desktop brand only -->
    <a class="navbar-brand mx-auto d-none d-lg-block text-center" href="{% url 'home' %}">
      <span class="navbar-heading">Working Out Gym</span>
    </a>

    <!-- Desktop auth links only -->
    <div class="position-absolute start-0 ms-3 d-none d-lg-block">
      {% if user.is_authenticated %}
        <a class="nav-link d-inline" href="{% url 'account_logout' %}">Logout</a>
      {% else %}
        <a class="nav-link d-inline me-2" href="{% url 'account_signup' %}">Register</a>
        <a class="nav-link d-inline" href="{% url 'account_login' %}">Login</a>
      {% endif %}
    </div>

    <!-- Desktop toggler hidden, mobile handled above -->
    <button
      class="navbar-toggler d-none d-lg-block position-absolute end-0 me-3"
      type="button"
      data-bs-toggle="collapse"
      data-bs-target="#main-nav"
      aria-controls="main-nav"
      aria-expanded="false"
      aria-label="Toggle navigation"
    >
      <span class="navbar-toggler-icon"></span>
    </button>

    <div class="collapse navbar-collapse justify-content-center" id="main-nav">
      <div class="navbar-nav text-center p-3">
        <a class="nav-link mb-2" href="{% url 'home' %}">Home</a>
        <a class="nav-link mb-2" href="#">Fitness and Nutrition Plans</a>
        <a class="nav-link mb-2" href="{% url 'merchandise:products' %}">Merchandise</a>
        <a class="nav-link" href="{% url 'discussionboard:post_list' %}">Discussion Board</a>
      </div>
    </div>

5. I then add the following styles to my styles.css:

.small-auth-links .nav-link {
  font-size: 0.85rem;
}

.mobile-logo {
  height: 40px;
  width: auto;
  display: block;
}

.mobile-brand {
  text-decoration: none;
}

.navbar-toggler {
  padding: 0.25rem 0.5rem;
}

@media (max-width: 991.98px) {
  .nav-link {
    font-size: 0.95rem;
  }
}

@media (max-width: 575.98px) {
  .small-auth-links .nav-link {
    font-size: 0.75rem;
  }

  .mobile-logo {
    height: 32px;
  }
}

6. I decide to use the beating heart emoji from Favicon as my logo for my site so download this to static/images and save as favicon. I save and then try loading my page on my dev server but receive a server 500 error on the Homepage. I turn debug to True and reload to see what is happening:

TemplateSyntaxError at /
Invalid block tag on line 18: 'static'. Did you forget to register or load this tag?

The error is regarding the following code:

<img src="{% static 'images/favicon.png' %}" alt="Working Out Gym logo" class="mobile-logo">

7. In the top of my mobile-top-header.html, i add the missing {% loadstatic %} tag to the top of the file. I can load the page now but it looks totally wrong now on the large screen:

![Navbar styling wrong large screen](/static/images/Navbar/Screenshot%20navbar%20large%20screen%20weird.png)

8. I relay this to ChatGPT who recommends replacing the current nav templates as below:

templates/includes/mobile-top-header.html:

{% load static %}

<div class="d-lg-none dark-bg shadow-sm">
  <div class="container-fluid py-2">
    <div class="d-flex justify-content-between align-items-center">

      <div class="small-auth-links">
        {% if user.is_authenticated %}
          <a class="nav-link d-inline p-0 me-2 small" href="{% url 'account_logout' %}">Logout</a>
        {% else %}
          <a class="nav-link d-inline p-0 me-2 small" href="{% url 'account_signup' %}">Register</a>
          <a class="nav-link d-inline p-0 small" href="{% url 'account_login' %}">Login</a>
        {% endif %}
      </div>

      <a href="{% url 'home' %}" class="mobile-brand">
        <img src="{% static 'images/favicon.png' %}" alt="Working Out Gym logo" class="mobile-logo">
      </a>

      <button
        class="navbar-toggler"
        type="button"
        data-bs-toggle="collapse"
        data-bs-target="#main-nav"
        aria-controls="main-nav"
        aria-expanded="false"
        aria-label="Toggle navigation">
        <span class="navbar-toggler-icon"></span>
      </button>

    </div>
  </div>
</div>

templates/includes/main-nav.html:

<nav class="navbar navbar-expand-lg dark-bg shadow-sm">
  <div class="container-fluid">

    <div class="w-100 d-none d-lg-flex justify-content-between align-items-center">

      <div class="small-auth-links">
        {% if user.is_authenticated %}
          <a class="nav-link d-inline me-2" href="{% url 'account_logout' %}">Logout</a>
        {% else %}
          <a class="nav-link d-inline me-2" href="{% url 'account_signup' %}">Register</a>
          <a class="nav-link d-inline" href="{% url 'account_login' %}">Login</a>
        {% endif %}
      </div>

      <a class="navbar-brand m-0 text-center" href="{% url 'home' %}">
        <span class="navbar-heading">Working Out Gym</span>
      </a>

      <div class="desktop-nav-links text-end">
        <a class="nav-link d-inline me-3" href="{% url 'home' %}">Home</a>
        <a class="nav-link d-inline me-3" href="#">Fitness and Nutrition Plans</a>
        <a class="nav-link d-inline me-3" href="{% url 'merchandise:products' %}">Merchandise</a>
        <a class="nav-link d-inline" href="{% url 'discussionboard:post_list' %}">Discussion Board</a>
      </div>

    </div>

    <div class="collapse navbar-collapse d-lg-none" id="main-nav">
      <div class="navbar-nav text-center w-100 py-3">
        <a class="nav-link mb-2" href="{% url 'home' %}">Home</a>
        <a class="nav-link mb-2" href="#">Fitness and Nutrition Plans</a>
        <a class="nav-link mb-2" href="{% url 'merchandise:products' %}">Merchandise</a>
        <a class="nav-link" href="{% url 'discussionboard:post_list' %}">Discussion Board</a>
      </div>
    </div>

  </div>
</nav>

- It then asks me to update css with the following:

.navbar-heading {
  font-family: "Boldonse", system-ui;
  font-weight: 700;
  font-size: 2.2rem;
  color: black;
  margin: 0;
}

.desktop-nav-links .nav-link,
.small-auth-links .nav-link,
.navbar-nav .nav-link {
  color: black;
  font-family: "Boldonse", system-ui;
  text-decoration: none;
}

.desktop-nav-links .nav-link {
  font-size: 0.95rem;
}

.small-auth-links .nav-link {
  font-size: 0.8rem;
}

.mobile-logo {
  height: 36px;
  width: auto;
  display: block;
}

.mobile-brand {
  text-decoration: none;
}

.navbar-toggler {
  padding: 0.25rem 0.5rem;
  border: none;
}

.navbar-toggler:focus {
  box-shadow: none;
}

@media (max-width: 991.98px) {
  .navbar-nav .nav-link {
    font-size: 0.95rem;
  }
}

@media (max-width: 575.98px) {
  .small-auth-links .nav-link {
    font-size: 0.7rem;
  }

  .mobile-logo {
    height: 30px;
  }
}

9. I do this and reload but it still doesn't look right so go back to ChatGPT who says my desktop nav html is incomplete, Bootstrap collapse was bleeding into the rest of the page and the desktop toggler should have been removed:

- I finally update my main-nav.html t:

<nav class="navbar navbar-expand-lg dark-bg shadow-sm">
  <div class="container-fluid">

    <!-- Desktop navbar -->
    <div class="w-100 d-none d-lg-flex justify-content-between align-items-center">

      <div class="small-auth-links">
        {% if user.is_authenticated %}
          <a class="nav-link d-inline me-2" href="{% url 'account_logout' %}">Logout</a>
        {% else %}
          <a class="nav-link d-inline me-2" href="{% url 'account_signup' %}">Register</a>
          <a class="nav-link d-inline" href="{% url 'account_login' %}">Login</a>
        {% endif %}
      </div>

      <a class="navbar-brand m-0 text-center" href="{% url 'home' %}">
        <span class="navbar-heading">Working Out Gym</span>
      </a>

      <div class="desktop-nav-links text-end">
        <a class="nav-link d-inline me-3" href="{% url 'home' %}">Home</a>
        <a class="nav-link d-inline me-3" href="#">Fitness and Nutrition Plans</a>
        <a class="nav-link d-inline me-3" href="{% url 'merchandise:products' %}">Merchandise</a>
        <a class="nav-link d-inline" href="{% url 'discussionboard:post_list' %}">Discussion Board</a>
      </div>

    </div>

    <!-- Mobile collapsed menu -->
    <div class="collapse navbar-collapse d-lg-none" id="main-nav">
      <div class="navbar-nav text-center w-100 py-3">
        <a class="nav-link mb-2" href="{% url 'home' %}">Home</a>
        <a class="nav-link mb-2" href="#">Fitness and Nutrition Plans</a>
        <a class="nav-link mb-2" href="{% url 'merchandise:products' %}">Merchandise</a>
        <a class="nav-link" href="{% url 'discussionboard:post_list' %}">Discussion Board</a>
      </div>
    </div>

  </div>
</nav>

- Then I update my current css rules for the below to:

.desktop-nav-links .nav-link,
.small-auth-links .nav-link,
.navbar-nav .nav-link {
  color: black;
  font-family: "Boldonse", system-ui;
  text-decoration: none;
}

- And also add a new rule to css for the navbar links hover:

.nav-link:hover {
  color: #d9d9d9;
}

10. Now when I reload my page, it looks much better:

![Navbar styling looking better](/static/images/Navbar/Screenshot%20new%20navbar.png)

11. I want the Navbar to be styled more like previously so consult with ChatGPT how I would add a menu toggler back in so the app names are hidden again, the white text does look better on the dark grey background though so will keep that. Also it appears as though the navbar itself is duplicated in above screenshot. ChatGPT advises that there are currently 2 x navsystems at play:
- the desktop inline links in desktop-nav-links
- the collapsed menu in #main-nav

So on large screens it looks duplicated and if i keep both the include files, mobile can also feel like two stacked navbars. I remove the below code from base.html:

{% include "includes/mobile-top-header.html" %}
{% include "includes/main-nav.html" %}

- And replace with 

{% include "includes/main-nav.html" %}

- To replace main-nav.html with:

{% load static %}

<nav class="navbar dark-bg shadow-sm">
  <div class="container-fluid d-flex justify-content-between align-items-center">

    <!-- Left: auth links -->
    <div class="small-auth-links">
      {% if user.is_authenticated %}
        <a class="nav-link d-inline me-2" href="{% url 'account_logout' %}">Logout</a>
      {% else %}
        <a class="nav-link d-inline me-2" href="{% url 'account_signup' %}">Register</a>
        <a class="nav-link d-inline" href="{% url 'account_login' %}">Login</a>
      {% endif %}
    </div>

    <!-- Centre: desktop brand / mobile logo -->
    <a class="navbar-brand m-0 text-center" href="{% url 'home' %}">
      <span class="navbar-heading d-none d-lg-inline">Working Out Gym</span>
      <img src="{% static 'images/favicon.png' %}" alt="Working Out Gym logo" class="mobile-logo d-inline d-lg-none">
    </a>

    <!-- Right: toggler -->
    <button
      class="navbar-toggler"
      type="button"
      data-bs-toggle="collapse"
      data-bs-target="#main-nav"
      aria-controls="main-nav"
      aria-expanded="false"
      aria-label="Toggle navigation">
      <span class="navbar-toggler-icon"></span>
    </button>

  </div>

  <!-- Collapsed nav menu -->
  <div class="collapse dark-bg text-center" id="main-nav">
    <div class="p-3">
      <a class="d-block mb-2 nav-link" href="{% url 'home' %}">Home</a>
      <a class="d-block mb-2 nav-link" href="#">Fitness and Nutrition Plans</a>
      <a class="d-block mb-2 nav-link" href="{% url 'merchandise:products' %}">Merchandise</a>
      <a class="d-block nav-link" href="{% url 'discussionboard:post_list' %}">Discussion Board</a>
    </div>
  </div>
</nav>

- Then finally update my css to match a simpler setup:

.navbar-heading {
  font-family: "Boldonse", system-ui;
  font-weight: 700;
  font-size: 2.4rem;
  color: white;
  margin: 0;
}

.nav-link,
.small-auth-links .nav-link {
  color: white;
  font-family: "Boldonse", system-ui;
  text-decoration: none;
}

.nav-link:hover,
.small-auth-links .nav-link:hover {
  color: #d9d9d9;
}

.small-auth-links .nav-link {
  font-size: 0.8rem;
}

.mobile-logo {
  height: 34px;
  width: auto;
  display: block;
}

.navbar-toggler {
  border: none;
  padding: 0.25rem 0.5rem;
}

.navbar-toggler:focus {
  box-shadow: none;
}

.navbar-toggler-icon {
  filter: invert(1);
}

@media (max-width: 575.98px) {
  .small-auth-links .nav-link {
    font-size: 0.7rem;
  }

  .mobile-logo {
    height: 28px;
  }
}

12. I refresh my page with the new code applied and it looks much better. I notice that the navbar items are not centralised so run devtools to see whats being applied to these elements.

![Navbar styling almost fixed app items not central](/static/images/Navbar/Screenshot%20centralise%20navbar%20menu%20items.png)

- While I am in Devtools, it is set to mobile and I can see that looks much better too but could also do with the items being centralised - I will also take a look at what settings are being applied to the main image on Home to make this fit each screen size better:

![Navbar styling almost fixed app items not centra - mobile](/static/images/Navbar/Screenshot%20mobile%20navbar%20menu.png)

- I can see that these are all a links within a div element with class p-3 currently applied, so apply text-center to this div as it is the one containing all links.

- However, this makes no difference so i consult ChatGPT who advises me to update my css as Bootstrap's .nav-link padding/text alignment is overriding what I expect so asks to add the below to css:

#main-nav .navbar-nav {
  align-items: center;
}

#main-nav .nav-item {
  width: 100%;
}

#main-nav .nav-link {
  display: block;
  text-align: center;
  margin: 0 auto;
}

- It then advises me to change the below code in main-nav.html:

<!-- Collapsed nav menu -->
<div class="collapse dark-bg" id="main-nav">
  <div class="p-3 nav-menu-links">
    <a class="nav-link py-2" href="{% url 'home' %}">Home</a>
    <a class="nav-link py-2" href="#">Fitness and Nutrition Plans</a>
    <a class="nav-link py-2" href="{% url 'merchandise:products' %}">Merchandise</a>
    <a class="nav-link py-2" href="{% url 'discussionboard:post_list' %}">Discussion Board</a>
  </div>
</div>

<div class="desktop-nav-links text-end">

- To:

<!-- Collapsed nav menu -->
<div class="collapse dark-bg" id="main-nav">
  <ul class="navbar-nav mx-auto text-center py-3">
    <li class="nav-item">
      <a class="nav-link py-2" href="{% url 'home' %}">Home</a>
    </li>
    <li class="nav-item">
      <a class="nav-link py-2" href="#">Fitness and Nutrition Plans</a>
    </li>
    <li class="nav-item">
      <a class="nav-link py-2" href="{% url 'merchandise:products' %}">Merchandise</a>
    </li>
    <li class="nav-item">
      <a class="nav-link py-2" href="{% url 'discussionboard:post_list' %}">Discussion Board</a>
    </li>
  </ul>
</div>

13. However, this still makes no difference. After a bit of back and forth with ChatGPT it identifies that the issue is with the top navbar layout, because I am using:

<div class="container-fluid d-flex justify-content-between align-items-center">

The three sections are spaced by content width, not by equal columns, so:
- left auth links take one width
- centre brand takes another
- right toggler takes a tiny width

- They have provided me the below template to use for my main-nav which will make the navbar header 3 equal columns:

{% load static %}

<nav class="navbar dark-bg shadow-sm">
  <div class="container-fluid">

    <div class="row w-100 align-items-center m-0">

      <!-- Left: auth links -->
      <div class="col-4 text-start small-auth-links">
        {% if user.is_authenticated %}
          <a class="nav-link d-inline me-2" href="{% url 'account_logout' %}">Logout</a>
        {% else %}
          <a class="nav-link d-inline me-2" href="{% url 'account_signup' %}">Register</a>
          <a class="nav-link d-inline" href="{% url 'account_login' %}">Login</a>
        {% endif %}
      </div>

      <!-- Centre: desktop brand / mobile logo -->
      <div class="col-4 text-center">
        <a class="navbar-brand m-0" href="{% url 'home' %}">
          <span class="navbar-heading d-none d-lg-inline">Working Out Gym</span>
          <img src="{% static 'images/favicon.png' %}" alt="Working Out Gym logo" class="mobile-logo d-inline d-lg-none">
        </a>
      </div>

      <!-- Right: toggler -->
      <div class="col-4 text-end">
        <button
          class="navbar-toggler"
          type="button"
          data-bs-toggle="collapse"
          data-bs-target="#main-nav"
          aria-controls="main-nav"
          aria-expanded="false"
          aria-label="Toggle navigation">
          <span class="navbar-toggler-icon"></span>
        </button>
      </div>

    </div>

    <!-- Collapsed nav menu -->
    <div class="collapse dark-bg w-100" id="main-nav">
      <div class="nav-collapse-links py-3">
        <a class="nav-link py-2" href="{% url 'home' %}">Home</a>
        <a class="nav-link py-2" href="#">Fitness and Nutrition Plans</a>
        <a class="nav-link py-2" href="{% url 'merchandise:products' %}">Merchandise</a>
        <a class="nav-link py-2" href="{% url 'discussionboard:post_list' %}">Discussion Board</a>
      </div>
    </div>

  </div>
</nav>

- They also advise me to add the below to my css:

.nav-collapse-links {
  display: flex;
  flex-direction: column;
  align-items: center;
  text-align: center;
}

.nav-collapse-links .nav-link {
  display: block;
  text-align: center;
}

- The big change is the below as it forces the divs into equal widths:

<div class="row w-100">
  <div class="col-4">...</div>
  <div class="col-4">...</div>
  <div class="col-4">...</div>
</div>

- I apply the changes and then refresh the code and it looks much better on both desktop and mobile:

![Navbar styling fixed on desktop](/static/images/Navbar/Screenshot%20desktop%20navbar%20fixed.png)

![Navbar styling fixed on mobile](/static/images/Navbar/Screenshot%20mobile%20navbar%20fixed.png)

- However, on tablets it doesn't look great right now - i want the same view on mobile to apply to tablets:

![Navbar styling fixed on tablet](/static/images/Navbar/Screenshot%20mobile%20navbar%20fixed.png)

13. I ask ChatGPT for the code to resolve this and the issue with the sizing of the main image, on both phones and tablets, and they advise in main-nav.html to change:

<span class="navbar-heading d-none d-lg-inline">Working Out Gym</span>

to:

<span class="navbar-heading d-none d-xl-inline">Working Out Gym</span>

- And to change this line for the image:

<img src="{% static 'images/favicon.png' %}" alt="Working Out Gym logo" class="mobile-logo d-inline d-lg-none">

To: 

<img src="{% static 'images/favicon.png' %}" alt="Working Out Gym logo" class="mobile-logo d-inline d-xl-none">

- I then make auth links smaller on tablet with the below css:

@media (max-width: 1199.98px) {
  .small-auth-links .nav-link {
    font-size: 0.7rem;
  }

  .mobile-logo {
    height: 30px;
  }
}

- I add the following css to reduce navbar height a bit on tablet/mobile:

@media (max-width: 1199.98px) {
  .navbar {
    padding-top: 0.5rem;
    padding-bottom: 0.5rem;
  }
}

- Fix the collapsed menu width with the following css:

.nav-collapse-links .nav-link {
  display: block;
  text-align: center;
  white-space: normal;
  word-break: break-word;
  max-width: 260px;
}

- Update my current css for the main-image class to:

.main-image {
  width: 100%;
  max-width: 950px;
  height: auto;
  display: block;
  margin: 0 auto;
}

- Then i add the following media queries to my css:

@media (max-width: 1199.98px) {
  .main-image {
    max-width: 700px;
  }

  .leading-p {
    max-width: 90%;
    font-size: 1.2rem;
  }
}

@media (max-width: 767.98px) {
  .main-image {
    max-width: 100%;
  }

  .leading-p {
    max-width: 95%;
    font-size: 1rem;
  }
}

- And finally some css rules to make the navbar collapse look better on tablet:

.nav-collapse-links {
  display: flex;
  flex-direction: column;
  align-items: center;
  text-align: center;
  padding-left: 1rem;
  padding-right: 1rem;
}

- After adding in this code, I refresh and it looks much better on mobiles and tablets now:

![Homepage on mobile](/static/images/Navbar/Screenshot%20mobile%20homepage%20fully%20styled%20and%20functional.png)

![Homepage on tablet](/static/images/Navbar/Screenshot%20tablet%20homepage%20fully%20styled%20and%20functional.png)

- I am finally going to update the navbar toggler, my navbar uses dark-bg and the Boostrap icon is dark by default so i cannot see it. I update my toggler button in main-nav.html to:

<button
  class="navbar-toggler text-white"
  type="button"
  data-bs-toggle="collapse"
  data-bs-target="#main-nav"
  aria-controls="main-nav"
  aria-expanded="false"
  aria-label="Toggle navigation">

  <i class="fas fa-bars"></i>

</button>

14. I can see the menu toggle now across all screens, I commit my code to Github and Heroku and move on.

15. I test the app on Heroku but it's not reflecting my changes on mobile and tablet properly. So I consult with ChatGPT and identify there is a spelling mistake on my image-fluid Boostrap class on the main image, it should be img-fluid. I update this now.

- I also replace my current Homepage css code with the below:

.main-image {
  width: 100%;
  max-width: 950px;
  height: auto;
  display: block;
  margin: 0 auto;
}

.leading-p {
  font-size: 1.4rem;
  max-width: 75%;
}

@media (max-width: 1199.98px) {
  .main-image {
    max-width: 700px;
  }

  .leading-p {
    max-width: 90%;
    font-size: 1.2rem;
  }
}

@media (max-width: 767.98px) {
  .main-image {
    max-width: 90%;
  }

  .leading-p {
    max-width: 95%;
    font-size: 1rem;
  }
}

- I change the below for my div container at the top of my homepage from:

<div class="container mt-5 pt-5">

to: 

<div class="container home-content">

- And then add the below css:

.home-content {
  margin-top: 3rem;
  padding-top: 2rem;
}

@media (max-width: 767.98px) {
  .home-content {
    margin-top: 1.5rem;
    padding-top: 1rem;
  }
}

- And then I use Django static properly for the image path, instead of hardcoding:

<img src="/static/images/Homepage/pexels-anete-lusina-4793215.jpg"

I use:

<img src="{% static 'images/Homepage/pexels-anete-lusina-4793215.jpg' %}"

16. Now when I update, the image and navbar are sized correctly across all screen sizes. I just want to revert back to white text and centralise the navbar items again and this will be all good to recommit and test on Heroku. Bootstrap's nav-link styling is stronger than mine so layout changed and it took priority again.

- ChatGPT recommends updating main-nav.html to something cleaner as below:

{% load static %}

<nav class="navbar custom-navbar dark-bg shadow-sm">
  <div class="container-fluid">

    <div class="row w-100 align-items-center m-0">

      <div class="col-4 text-start small-auth-links">
        {% if user.is_authenticated %}
          <a class="auth-link" href="{% url 'account_logout' %}">Logout</a>
        {% else %}
          <a class="auth-link me-2" href="{% url 'account_signup' %}">Register</a>
          <a class="auth-link" href="{% url 'account_login' %}">Login</a>
        {% endif %}
      </div>

      <div class="col-4 text-center">
        <a class="navbar-brand m-0" href="{% url 'home' %}">
          <span class="navbar-heading d-none d-xl-inline">Working Out Gym</span>
          <img
            src="{% static 'images/favicon.png' %}"
            alt="Working Out Gym logo"
            class="mobile-logo d-inline d-xl-none"
          >
        </a>
      </div>

      <div class="col-4 text-end">
        <button
          class="navbar-toggler custom-toggler"
          type="button"
          data-bs-toggle="collapse"
          data-bs-target="#main-nav"
          aria-controls="main-nav"
          aria-expanded="false"
          aria-label="Toggle navigation">
          <i class="fas fa-bars"></i>
        </button>
      </div>

    </div>

    <div class="collapse w-100" id="main-nav">
      <div class="nav-collapse-links py-3">
        <a class="menu-link" href="{% url 'home' %}">Home</a>
        <a class="menu-link" href="#">Fitness &amp; Nutrition Plans</a>
        <a class="menu-link" href="{% url 'merchandise:products' %}">Merchandise</a>
        <a class="menu-link" href="{% url 'discussionboard:post_list' %}">Discussion Board</a>
      </div>
    </div>

  </div>
</nav>

- And to replace my Navbar css with this block:

.custom-navbar {
  background-color: #3b3b3b;
}

.navbar-heading {
  font-family: "Boldonse", system-ui;
  font-weight: 700;
  font-size: 2.2rem;
  color: #ffffff;
  margin: 0;
}

.navbar-brand {
  color: #ffffff !important;
  text-decoration: none;
}

.auth-link {
  color: #ffffff;
  font-family: "Boldonse", system-ui;
  text-decoration: none;
  font-size: 0.8rem;
}

.auth-link:hover {
  color: #d9d9d9;
}

.mobile-logo {
  height: 30px;
  width: auto;
  display: block;
  margin: 0 auto;
}

.custom-toggler {
  border: none;
  color: #ffffff;
  font-size: 1.2rem;
  padding: 0.25rem 0.5rem;
}

.custom-toggler:focus {
  box-shadow: none;
}

.nav-collapse-links {
  display: flex;
  flex-direction: column;
  align-items: center;
  text-align: center;
  padding-left: 1rem;
  padding-right: 1rem;
}

.menu-link {
  display: block;
  color: #ffffff;
  font-family: "Boldonse", system-ui;
  text-decoration: none;
  text-align: center;
  padding: 0.6rem 0;
  max-width: 280px;
  width: 100%;
}

.menu-link:hover {
  color: #d9d9d9;
}

@media (max-width: 1199.98px) {
  .auth-link {
    font-size: 0.7rem;
  }

  .mobile-logo {
    height: 28px;
  }

  .custom-navbar {
    padding-top: 0.5rem;
    padding-bottom: 0.5rem;
  }
}

17. Now when I refresh my page and check across all screen sizes, it is showing the navbar as was. I am going to recommit the code and make sure the same is true in the production app.

---

## Merchandise App - Product Queries by Name

1. Now that my Merchandise page is showing all products correctly on the initial Merchandise app page, and clicking is taking us to the product detail on the next page, I can now look at giving the user the functionality to view specific categories of products. 


2. I am going to start with the search queries. Code Institure are using a search form in their main site header on base.html. I am going to borrow their code and add to mine and tweak accordingly:

<!-- Search bar -->
<div class="navbar-search py-3">
  <div class="container">
    <form method="GET" action="{% url 'merchandise:products' %}">
      <div class="input-group w-100">
        <input
          class="form-control rounded-0"
          type="text"
          name="q"
          placeholder="Search our site">

        <button class="btn btn-dark rounded-0" type="submit">
          <i class="fas fa-search"></i>
        </button>
      </div>
    </form>
  </div>
</div>

- I also add the following styles:

.navbar-search {
  background-color: #3b3b3b;
  border-top: 1px solid rgba(255,255,255,0.1);
}

.navbar-search .form-control {
  border: none;
}

.navbar-search .btn {
  border: none;
}

.navbar-search .form-control:focus {
  box-shadow: none;
}

.navbar-search {
  margin-bottom: 1rem;
}

3. When I reload my page I can see a search bar now and it looks good on all screen sizes:

![Searchbar on Navbar](/static/images/Product%20Query/Screenshot%20searchform.png)

4. Then in my views.py file in merchandise, I create an if statement, using Code Institute's code, and add to my all_products view as below:

    products = (
        Product.objects.filter(is_active=True)
        .select_related("category")
        .annotate(from_price=Min("variants__price"))
    )
    query = None

    if request.GET:
        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                message.error(request, "You didn't enter any search criteria!")
                return redirect(reverse('products'))
            
            queries = Q(name__icontains=query) | Q(description__icontains=query)
            products = products.filter(queries)

    context = {
        'products': products,
        'search_term': query,
    }
    

- I also import the following to allow for the error message to display and for Q to work:

from django.db.models import Q
from django.contrib import messages

- After adding this code, my page will no longer run so I set Debug to True and reload to troubleshoot the issue:

FieldError at /merchandise/
Cannot resolve keyword 'name' into field. Choices are: category, category_id, from_price, handle, id, image_src, is_active, slug, stripe_product_id, tags, title, variants, vendor

- I update this in my new query updates to the all_products view to use title instead of name in the offending line. Now when I search it doesn't take me to an error page but also doesn't return anything when I search:


![Searchbar on Navbar results empty](/static/images/Product%20Query/Screenshot%20product%20query%20empty.png)

- I query this with ChatGPT who advises that I need to update message.error to mnessages.error and my rever('products') statement should instead be namespaced as: reverse('merchandise:products')

- It also recommends adding the below if statement to give a message in my template when no products match the search query:

{% else %}
  <p class="text-center mt-4">No products matched your search.</p>
{% endif %}

- This fails to run as Django only allows the {% else %} statement inside an if, else or endif statement and not a for. Therefore it recommends wrapping my for products statement in an if products statement. However, this failed as well, so ChatGPT finally recommended replacing my whole products loop section with the below which uses the for products statement:

<div class="row row-cols-1 row-cols-sm-2 row-cols-lg-3 g-4">
  {% for product in products %}
    <div class="col">
      <div class="card h-100 border-0">
        <a href="{% url 'merchandise:product_detail' product.id %}">
          {% if product.image_src %}
            <img
              class="card-img-top img-fluid"
              src="{{ product.image_src }}"
              alt="{{ product.title }}"
            >
          {% else %}
            <img
              class="card-img-top img-fluid"
              src="{% static 'images/noimage.png' %}"
              alt="{{ product.title }}"
            >
          {% endif %}
        </a>

        <div class="card-body pb-0">
          <p class="mb-0">{{ product.title }}</p>

          {% if product.category %}
            <small class="text-muted">{{ product.category.name }}</small>
          {% endif %}
        </div>

        <div class="card-footer bg-white pt-0 border-0 text-left">
          {% if product.from_price %}
            <p class="lead mb-0 fw-bold">£{{ product.from_price }}</p>
          {% else %}
            <small class="text-muted">Price unavailable</small>
          {% endif %}
        </div>
      </div>
    </div>
  {% empty %}
    <div class="col-12">
      <p class="text-center mt-4">No products matched your search.</p>
    </div>
  {% endfor %}
</div>

5. Now when I reload the search it is returning all 'womens crop tops':

![Searchbar returning correct results](/static/images/Product%20Query/Screenshot%20search%20function%20working.png)

6. I can now commit my changes and deploy to Heroku as well.

---


## Merchandise App - Product Queries by Category

1. Next I want to set it up so that the users the ability to show specific categories of products. I will do this by creating some subfolder Nav menu links beneath Merchandise for the different categories of products. To start with, I will identify all the possible categories by running the following:

python manage.py shell

from merchandise.models import Product

Product.objects.values_list("category__name", flat=True).distinct()

- This returns the following result:

<QuerySet [None, 'Womens Crop Top', 'Mens Pullovers', 'Mens Drop Armhole Tank', 'Womens T-Shirt', 'Womens Bottoms', 'Mens Leggings', 'Mens Shorts', 'Gift Card', 'Misc.', 'Mens Ss Tops', 'Mens Long Sleeve Top', 'Bag', 'Womens Swimwear', 'Womens Shorts', 'Womens', 'Pullovers', 'Mens Stringer', 'womens Shorts', 'Womens Jackets', '...(remaining elements truncated)...']>

So ideally I want to have 3 subfolder beneath my 'Merchandise' Nav item:

- Womens
- Mens
- Unisex

Then within the womens folder I will create the following subfolders:
- Tops > 'Womens Crop Top', 'Womens T-Shirt'
- Bottoms > 'Womens Bottoms', 'Womens Shorts'
- Swimwear > 'Womens Swimwear'
- Outerwear > 'Womens Jackets', 'Womens Pullovers',

Then within the mens folder, I will create the following subfolders:
- Tops > 'Mens Drop Armhole Tank', 'Mens Ss Tops', 'Mens Long Sleeve Top', 
- Bottoms > 'Mens Leggings', 'Mens Shorts', 'Mens Stringer',

Then within the unisex folder, I will create the following subfolders:
- Accessories > 'Bag',
- Gift Cards > 'Gift Card',

2. Now that I have identified the different categories and Nav menu subfolders, I update my all_products view to add category filtering:

- I first update the docstring so it reflects the latest functionality.
- Under the query = None statement I add: current_category = None
- I add a new if category request.GET statement under my current if request.GET statement:

        if "category" in request.GET:
            current_category = request.GET["category"]
            products = products.filter(category__name=current_category)

- I add "current_category": current_category, to my context parameters.

3. I then need to update my main-nav.html so that my main Merchandise link has one drop down menu with section headings for: 

- Womens
- Mens
- Unisex

- I update my collapsed nav menu with the below code, ChatGPT has created this to save time using the output from the below cmd to generate the categories for all the products to save time: 

python manage.py shell -c "from merchandise.models import Category; print(list(Category.objects.values_list('name', flat=True)))"

<div class="collapse w-100" id="main-nav">
  <div class="nav-collapse-links py-3">
    <a class="menu-link" href="{% url 'home' %}">Home</a>
    <a class="menu-link" href="#">Fitness &amp; Nutrition Plans</a>

    <a class="menu-link" href="{% url 'merchandise:products' %}">Merchandise</a>

    <details class="menu-folder">
      <summary class="menu-link">Womens</summary>

      <details class="menu-subfolder">
        <summary class="menu-sublink">Tops</summary>
        <a class="submenu-link" href="{% url 'merchandise:products' %}?category=Womens%20Crop%20Tops">Womens Crop Tops</a>
        <a class="submenu-link" href="{% url 'merchandise:products' %}?category=Womens%20Crop%20Top">Womens Crop Top</a>
        <a class="submenu-link" href="{% url 'merchandise:products' %}?category=Womens%20Ss%20Tops">Womens Ss Tops</a>
        <a class="submenu-link" href="{% url 'merchandise:products' %}?category=Womens%20T-Shirt">Womens T-Shirt</a>
        <a class="submenu-link" href="{% url 'merchandise:products' %}?category=Womens%20Sleeveless%20Tops">Womens Sleeveless Tops</a>
        <a class="submenu-link" href="{% url 'merchandise:products' %}?category=Womens%20Sleeveless%20Top">Womens Sleeveless Top</a>
        <a class="submenu-link" href="{% url 'merchandise:products' %}?category=Womens%20Ls%20Tops">Womens Ls Tops</a>
        <a class="submenu-link" href="{% url 'merchandise:products' %}?category=Womens%20Long%20Sleeve%20Top">Womens Long Sleeve Top</a>
        <a class="submenu-link" href="{% url 'merchandise:products' %}?category=Womens%20Tank">Womens Tank</a>
        <a class="submenu-link" href="{% url 'merchandise:products' %}?category=Womens%20Tanks">Womens Tanks</a>
        <a class="submenu-link" href="{% url 'merchandise:products' %}?category=Womens%20tank">Womens tank</a>
        <a class="submenu-link" href="{% url 'merchandise:products' %}?category=Womens%20Vest">Womens Vest</a>
      </details>

      <details class="menu-subfolder">
        <summary class="menu-sublink">Sports Bras</summary>
        <a class="submenu-link" href="{% url 'merchandise:products' %}?category=Womens%20Sports%20Bras">Womens Sports Bras</a>
        <a class="submenu-link" href="{% url 'merchandise:products' %}?category=Womens%20Sports%20Bra">Womens Sports Bra</a>
      </details>

      <details class="menu-subfolder">
        <summary class="menu-sublink">Bottoms</summary>
        <a class="submenu-link" href="{% url 'merchandise:products' %}?category=Womens%20Leggings">Womens Leggings</a>
        <a class="submenu-link" href="{% url 'merchandise:products' %}?category=Womens%20Shorts">Womens Shorts</a>
        <a class="submenu-link" href="{% url 'merchandise:products' %}?category=womens%20Shorts">womens Shorts</a>
        <a class="submenu-link" href="{% url 'merchandise:products' %}?category=Womens%20Pants">Womens Pants</a>
        <a class="submenu-link" href="{% url 'merchandise:products' %}?category=Womens%20Bottoms">Womens Bottoms</a>
        <a class="submenu-link" href="{% url 'merchandise:products' %}?category=Womens%20Skort">Womens Skort</a>
      </details>

      <details class="menu-subfolder">
        <summary class="menu-sublink">Swimwear</summary>
        <a class="submenu-link" href="{% url 'merchandise:products' %}?category=Womens%20Swimwear">Womens Swimwear</a>
        <a class="submenu-link" href="{% url 'merchandise:products' %}?category=Womens%20One%20Pieces">Womens One Pieces</a>
        <a class="submenu-link" href="{% url 'merchandise:products' %}?category=Womens%20One%20Piece">Womens One Piece</a>
      </details>

      <details class="menu-subfolder">
        <summary class="menu-sublink">Outerwear</summary>
        <a class="submenu-link" href="{% url 'merchandise:products' %}?category=Womens%20Pullovers">Womens Pullovers</a>
        <a class="submenu-link" href="{% url 'merchandise:products' %}?category=Womens%20Pullover">Womens Pullover</a>
        <a class="submenu-link" href="{% url 'merchandise:products' %}?category=Womens%20Jackets%20%2F%20Outerwear">Womens Jackets / Outerwear</a>
        <a class="submenu-link" href="{% url 'merchandise:products' %}?category=Womens%20Jackets">Womens Jackets</a>
        <a class="submenu-link" href="{% url 'merchandise:products' %}?category=Womens%20Jacket">Womens Jacket</a>
        <a class="submenu-link" href="{% url 'merchandise:products' %}?category=Womens%20Hoodies">Womens Hoodies</a>
        <a class="submenu-link" href="{% url 'merchandise:products' %}?category=Womens%20Hoodie">Womens Hoodie</a>
        <a class="submenu-link" href="{% url 'merchandise:products' %}?category=Womens%20Hoodies%20and%20Jackets">Womens Hoodies and Jackets</a>
        <a class="submenu-link" href="{% url 'merchandise:products' %}?category=Womens%20Sweater">Womens Sweater</a>
        <a class="submenu-link" href="{% url 'merchandise:products' %}?category=Womens%20swe">Womens swe</a>
      </details>

      <details class="menu-subfolder">
        <summary class="menu-sublink">Accessories &amp; Other</summary>
        <a class="submenu-link" href="{% url 'merchandise:products' %}?category=Womens%20Underwear">Womens Underwear</a>
        <a class="submenu-link" href="{% url 'merchandise:products' %}?category=womens%20Socks">womens Socks</a>
        <a class="submenu-link" href="{% url 'merchandise:products' %}?category=Womens%20Socks">Womens Socks</a>
        <a class="submenu-link" href="{% url 'merchandise:products' %}?category=womens%20Bags">womens Bags</a>
        <a class="submenu-link" href="{% url 'merchandise:products' %}?category=womens%20Headwear">womens Headwear</a>
        <a class="submenu-link" href="{% url 'merchandise:products' %}?category=womens%20Accessories">womens Accessories</a>
        <a class="submenu-link" href="{% url 'merchandise:products' %}?category=Womens">Womens</a>
        <a class="submenu-link" href="{% url 'merchandise:products' %}?category=Womens%20Dress">Womens Dress</a>
        <a class="submenu-link" href="{% url 'merchandise:products' %}?category=Womens%20Bodysuit">Womens Bodysuit</a>
      </details>
    </details>

    <details class="menu-folder">
      <summary class="menu-link">Mens</summary>

      <details class="menu-subfolder">
        <summary class="menu-sublink">Tops</summary>
        <a class="submenu-link" href="{% url 'merchandise:products' %}?category=Mens%20Drop%20Armhole%20Tank">Mens Drop Armhole Tank</a>
        <a class="submenu-link" href="{% url 'merchandise:products' %}?category=Mens%20Ss%20Tops">Mens Ss Tops</a>
        <a class="submenu-link" href="{% url 'merchandise:products' %}?category=mens%20Ss%20Tops">mens Ss Tops</a>
        <a class="submenu-link" href="{% url 'merchandise:products' %}?category=Mens%20T-Shirt">Mens T-Shirt</a>
        <a class="submenu-link" href="{% url 'merchandise:products' %}?category=mens%20T-Shirt">mens T-Shirt</a>
        <a class="submenu-link" href="{% url 'merchandise:products' %}?category=Mens%20Long%20Sleeve%20Top">Mens Long Sleeve Top</a>
        <a class="submenu-link" href="{% url 'merchandise:products' %}?category=Mens%20Ls%20Tops">Mens Ls Tops</a>
        <a class="submenu-link" href="{% url 'merchandise:products' %}?category=Mens%20Shirt">Mens Shirt</a>
        <a class="submenu-link" href="{% url 'merchandise:products' %}?category=Mens%20Tank">Mens Tank</a>
        <a class="submenu-link" href="{% url 'merchandise:products' %}?category=Mens%20Sleeveless%20Tops">Mens Sleeveless Tops</a>
        <a class="submenu-link" href="{% url 'merchandise:products' %}?category=Mens%20Sleeveless%20T-Shirt">Mens Sleeveless T-Shirt</a>
        <a class="submenu-link" href="{% url 'merchandise:products' %}?category=Mens%20Stringer">Mens Stringer</a>
        <a class="submenu-link" href="{% url 'merchandise:products' %}?category=Mens%20Tops">Mens Tops</a>
        <a class="submenu-link" href="{% url 'merchandise:products' %}?category=Mens%20t">Mens t</a>
        <a class="submenu-link" href="{% url 'merchandise:products' %}?category=Mens%20Baselayer">Mens Baselayer</a>
      </details>

      <details class="menu-subfolder">
        <summary class="menu-sublink">Bottoms</summary>
        <a class="submenu-link" href="{% url 'merchandise:products' %}?category=Mens%20Leggings">Mens Leggings</a>
        <a class="submenu-link" href="{% url 'merchandise:products' %}?category=Mens%20Shorts">Mens Shorts</a>
        <a class="submenu-link" href="{% url 'merchandise:products' %}?category=Mens%20Pants">Mens Pants</a>
        <a class="submenu-link" href="{% url 'merchandise:products' %}?category=Mens%20Joggers">Mens Joggers</a>
        <a class="submenu-link" href="{% url 'merchandise:products' %}?category=Mens%20Bottoms">Mens Bottoms</a>
      </details>

      <details class="menu-subfolder">
        <summary class="menu-sublink">Outerwear</summary>
        <a class="submenu-link" href="{% url 'merchandise:products' %}?category=Mens%20Pullovers">Mens Pullovers</a>
        <a class="submenu-link" href="{% url 'merchandise:products' %}?category=Mens%20Pullover">Mens Pullover</a>
        <a class="submenu-link" href="{% url 'merchandise:products' %}?category=Mens%20Hoodie">Mens Hoodie</a>
        <a class="submenu-link" href="{% url 'merchandise:products' %}?category=Mens%20Sweater">Mens Sweater</a>
        <a class="submenu-link" href="{% url 'merchandise:products' %}?category=Mens%20Jackets%20%2F%20Outerwear">Mens Jackets / Outerwear</a>
        <a class="submenu-link" href="{% url 'merchandise:products' %}?category=Mens%20Jackets">Mens Jackets</a>
        <a class="submenu-link" href="{% url 'merchandise:products' %}?category=Mens%20Jacket">Mens Jacket</a>
        <a class="submenu-link" href="{% url 'merchandise:products' %}?category=Mens%20Outerwear">Mens Outerwear</a>
      </details>

      <details class="menu-subfolder">
        <summary class="menu-sublink">Swimwear &amp; Other</summary>
        <a class="submenu-link" href="{% url 'merchandise:products' %}?category=Mens%20Swimwear">Mens Swimwear</a>
        <a class="submenu-link" href="{% url 'merchandise:products' %}?category=Mens%20Underwear">Mens Underwear</a>
      </details>
    </details>

    <details class="menu-folder">
      <summary class="menu-link">Unisex</summary>

      <details class="menu-subfolder">
        <summary class="menu-sublink">Accessories</summary>
        <a class="submenu-link" href="{% url 'merchandise:products' %}?category=Accessories">Accessories</a>
        <a class="submenu-link" href="{% url 'merchandise:products' %}?category=Headwear">Headwear</a>
        <a class="submenu-link" href="{% url 'merchandise:products' %}?category=Socks">Socks</a>
        <a class="submenu-link" href="{% url 'merchandise:products' %}?category=Bags">Bags</a>
        <a class="submenu-link" href="{% url 'merchandise:products' %}?category=Bag">Bag</a>
        <a class="submenu-link" href="{% url 'merchandise:products' %}?category=Thirft%20Bag">Thirft Bag</a>
        <a class="submenu-link" href="{% url 'merchandise:products' %}?category=Bottles">Bottles</a>
        <a class="submenu-link" href="{% url 'merchandise:products' %}?category=Equipment">Equipment</a>
        <a class="submenu-link" href="{% url 'merchandise:products' %}?category=Footwear">Footwear</a>
        <a class="submenu-link" href="{% url 'merchandise:products' %}?category=footwear">footwear</a>
      </details>

      <details class="menu-subfolder">
        <summary class="menu-sublink">Bottoms</summary>
        <a class="submenu-link" href="{% url 'merchandise:products' %}?category=unisex%20Pants">unisex Pants</a>
        <a class="submenu-link" href="{% url 'merchandise:products' %}?category=Pants">Pants</a>
        <a class="submenu-link" href="{% url 'merchandise:products' %}?category=mens%20unisex%20Bottoms">mens unisex Bottoms</a>
      </details>

      <details class="menu-subfolder">
        <summary class="menu-sublink">Pullovers &amp; Tops</summary>
        <a class="submenu-link" href="{% url 'merchandise:products' %}?category=Pullovers">Pullovers</a>
        <a class="submenu-link" href="{% url 'merchandise:products' %}?category=mens%20unisex%20Pullovers">mens unisex Pullovers</a>
        <a class="submenu-link" href="{% url 'merchandise:products' %}?category=Ss%20Tops">Ss Tops</a>
        <a class="submenu-link" href="{% url 'merchandise:products' %}?category=Underwear">Underwear</a>
      </details>

      <details class="menu-subfolder">
        <summary class="menu-sublink">Gift Cards &amp; Misc</summary>
        <a class="submenu-link" href="{% url 'merchandise:products' %}?category=Gift%20Card">Gift Card</a>
        <a class="submenu-link" href="{% url 'merchandise:products' %}?category=Misc.">Misc.</a>
      </details>
    </details>

    <a class="menu-link" href="{% url 'discussionboard:post_list' %}">Discussion Board</a>
  </div>
</div>

4. I reload my page on my dev server with the new changes, I can see the new dropdown menu under the 'Merchandise' nav bar menu item, then within that can see the different categories:

![Merchandise Navbar Dropdown](/static/images/Product%20Query/Screenshot%20search%20function%20working.png)


- However, if i click on Womens Crop Tops in the Womens category this doesn't return any results:

![No results womens crop top category](/static/images/Product%20Query/Screenshot%20womens%20crop%20top%20no%20results.png)

- I query this with ChatGPT who advises that a better approach would be to fix my view to update the category filter part of all_products so that it is more forgiving. As my menu is grouped, the below code will be more flexible - i update my all_products view with this - this means that I can pass either one category or multiple:

if "category" in request.GET:
    current_category = request.GET["category"].strip()

    category_list = [c.strip() for c in current_category.split(",") if c.strip()]
    products = products.filter(category__name__in=category_list)

- ChatGPT advises that my current links fails as it contains duplicates/variants such as:
- Womens Crop Tops
- Womens Crop Top

- ChatGPT provides me with updated group links for all my a elements in my drop down menu, such as the below for Womens Tops; which groups all the alike product categories into the one href:

<a class="submenu-link" href="{% url 'merchandise:products' %}?category=Womens%20Crop%20Tops,Womens%20Crop%20Top,Womens%20Ss%20Tops,Womens%20T-Shirt,Womens%20Sleeveless%20Tops,Womens%20Sleeveless%20Top,Womens%20Ls%20Tops,Womens%20Long%20Sleeve%20Top,Womens%20Tank,Womens%20Tanks,Womens%20tank,Womens%20Vest">
  Tops
</a>

- Now when I load up the womens tops page from Merchandise, it is showing all of the womens tops from products and categories. However, the menu is not styled right:

![Bad navbar styling - category resturns results now](/static/images/Product%20Query/Screenshot%20merchandise%20not%20a%20drop%20down%20item%20anymore.png)

- I consult ChatGPT about this who provides me with some cleaner code to use for my Merchandise and css stylings of my navbar:

<div class="menu-dropdown">
  <div class="menu-dropdown-header">
    <a class="menu-link menu-link-main" href="{% url 'merchandise:products' %}">
      Merchandise
    </a>

    <button
      class="menu-toggle-btn"
      type="button"
      data-bs-toggle="collapse"
      data-bs-target="#merchandise-submenu"
      aria-expanded="false"
      aria-controls="merchandise-submenu"
      aria-label="Toggle merchandise menu">
      <i class="fas fa-chevron-down"></i>
    </button>
  </div>

  <div class="collapse" id="merchandise-submenu">
    <div class="submenu-panel">

      <div class="submenu-section">
        <h6 class="submenu-heading">Womens</h6>

        <p class="submenu-group-title">Tops</p>
        <a class="submenu-link" href="{% url 'merchandise:products' %}?category=Womens%20Crop%20Tops,Womens%20Crop%20Top,Womens%20Ss%20Tops,Womens%20T-Shirt,Womens%20Sleeveless%20Tops,Womens%20Sleeveless%20Top,Womens%20Ls%20Tops,Womens%20Long%20Sleeve%20Top,Womens%20Tank,Womens%20Tanks,Womens%20tank,Womens%20Vest">
          View Womens Tops
        </a>

        <p class="submenu-group-title">Sports Bras</p>
        <a class="submenu-link" href="{% url 'merchandise:products' %}?category=Womens%20Sports%20Bras,Womens%20Sports%20Bra">
          View Womens Sports Bras
        </a>

        <p class="submenu-group-title">Bottoms</p>
        <a class="submenu-link" href="{% url 'merchandise:products' %}?category=Womens%20Leggings,Womens%20Shorts,womens%20Shorts,Womens%20Pants,Womens%20Bottoms,Womens%20Skort">
          View Womens Bottoms
        </a>

        <p class="submenu-group-title">Swimwear</p>
        <a class="submenu-link" href="{% url 'merchandise:products' %}?category=Womens%20Swimwear,Womens%20One%20Pieces,Womens%20One%20Piece">
          View Womens Swimwear
        </a>

        <p class="submenu-group-title">Outerwear</p>
        <a class="submenu-link" href="{% url 'merchandise:products' %}?category=Womens%20Pullovers,Womens%20Pullover,Womens%20Jackets%20%2F%20Outerwear,Womens%20Jackets,Womens%20Jacket,Womens%20Hoodies,Womens%20Hoodie,Womens%20Hoodies%20and%20Jackets,Womens%20Sweater,Womens%20swe">
          View Womens Outerwear
        </a>

        <p class="submenu-group-title">Accessories &amp; Other</p>
        <a class="submenu-link" href="{% url 'merchandise:products' %}?category=Womens%20Underwear,womens%20Socks,Womens%20Socks,womens%20Bags,womens%20Headwear,womens%20Accessories,Womens,Womens%20Dress,Womens%20Bodysuit">
          View Womens Accessories &amp; Other
        </a>
      </div>

      <div class="submenu-section">
        <h6 class="submenu-heading">Mens</h6>

        <p class="submenu-group-title">Tops</p>
        <a class="submenu-link" href="{% url 'merchandise:products' %}?category=Mens%20Drop%20Armhole%20Tank,Mens%20Ss%20Tops,mens%20Ss%20Tops,Mens%20T-Shirt,mens%20T-Shirt,Mens%20Long%20Sleeve%20Top,Mens%20Ls%20Tops,Mens%20Shirt,Mens%20Tank,Mens%20Sleeveless%20Tops,Mens%20Sleeveless%20T-Shirt,Mens%20Stringer,Mens%20Tops,Mens%20t,Mens%20Baselayer">
          View Mens Tops
        </a>

        <p class="submenu-group-title">Bottoms</p>
        <a class="submenu-link" href="{% url 'merchandise:products' %}?category=Mens%20Leggings,Mens%20Shorts,Mens%20Pants,Mens%20Joggers,Mens%20Bottoms">
          View Mens Bottoms
        </a>

        <p class="submenu-group-title">Outerwear</p>
        <a class="submenu-link" href="{% url 'merchandise:products' %}?category=Mens%20Pullovers,Mens%20Pullover,Mens%20Hoodie,Mens%20Sweater,Mens%20Jackets%20%2F%20Outerwear,Mens%20Jackets,Mens%20Jacket,Mens%20Outerwear">
          View Mens Outerwear
        </a>

        <p class="submenu-group-title">Swimwear &amp; Other</p>
        <a class="submenu-link" href="{% url 'merchandise:products' %}?category=Mens%20Swimwear,Mens%20Underwear">
          View Mens Swimwear &amp; Other
        </a>
      </div>

      <div class="submenu-section">
        <h6 class="submenu-heading">Unisex</h6>

        <p class="submenu-group-title">Accessories</p>
        <a class="submenu-link" href="{% url 'merchandise:products' %}?category=Accessories,Headwear,Socks,Bags,Bag,Thirft%20Bag,Bottles,Equipment,Footwear,footwear">
          View Unisex Accessories
        </a>

        <p class="submenu-group-title">Bottoms</p>
        <a class="submenu-link" href="{% url 'merchandise:products' %}?category=unisex%20Pants,Pants,mens%20unisex%20Bottoms">
          View Unisex Bottoms
        </a>

        <p class="submenu-group-title">Pullovers &amp; Tops</p>
        <a class="submenu-link" href="{% url 'merchandise:products' %}?category=Pullovers,mens%20unisex%20Pullovers,Ss%20Tops,Underwear">
          View Unisex Pullovers &amp; Tops
        </a>

        <p class="submenu-group-title">Gift Cards &amp; Misc</p>
        <a class="submenu-link" href="{% url 'merchandise:products' %}?category=Gift%20Card,Misc.">
          View Gift Cards &amp; Misc
        </a>
      </div>

    </div>
  </div>
</div>

.menu-dropdown {
  width: 100%;
  max-width: 320px;
  text-align: center;
}

.menu-dropdown-header {
  display: flex;
  justify-content: center;
  align-items: center;
  gap: 0.5rem;
}

.menu-link-main {
  width: auto;
  margin: 0;
}

.menu-toggle-btn {
  background: transparent;
  border: none;
  color: #ffffff;
  font-size: 0.95rem;
  padding: 0;
}

.menu-toggle-btn:focus {
  box-shadow: none;
}

.submenu-panel {
  margin-top: 0.75rem;
  padding: 0.5rem 0;
}

.submenu-section {
  margin-bottom: 1.25rem;
}

.submenu-heading {
  color: #ffffff;
  font-family: "Boldonse", system-ui;
  font-size: 1.1rem;
  margin-bottom: 0.5rem;
}

.submenu-group-title {
  color: #d9d9d9;
  font-weight: 700;
  margin: 0.5rem 0 0.2rem;
}

.submenu-link {
  display: block;
  color: #ffffff;
  text-decoration: none;
  padding: 0.25rem 0;
}

.submenu-link:hover {
  color: #d9d9d9;
}

- I apply these to my code and refresh and the menu looks much much better:

![Fixed merchandise drop down](/static/images/Product%20Query/Screenshot%20merchandise%20drop%20down%20fixed.png)

- If I click the 'view womens tops' link it takes me to the page with all the womens tops.

- I run a collectstatic and then commit the changes to Git and deploy to Heroku.

---

## Merchandise App - Products Sorting on Price and Category

1. I now want to further improve sorting for users on products by providing them with the functionality to sort products by price and category in the navbar. I am going to expand upon my current all_products view and add the code to handle the 2 x new get parameters I am going to create for 'sort' and 'direction'. For price, I am going to add a parameter of 'sort' and will set it equal to the price and a direction of ascending. I am first going to make the all products link within my main-nav.html into a drop down menu which will contain the 2 x menu items for 'By Price' and 'By Category'. I will use the same code as I used for the drop down menu for Merchandise and then tweak accordingly.

  <div class="collapse" id="merchandise-submenu">
    <div class="submenu-panel">

      <div class="submenu-section">
        <h6 class="submenu-heading">All Products</h6>

        <p class="submenu-group-title">By Price</p>
        <a class="submenu-link" href="{% url 'merchandise:products' %}sort=price&direction=asc">
          View All Products by Price
        </a>

        <p class="submenu-group-title">By Categories</p>
        <a class="submenu-link" href="{% url 'merchandise:products' %}?sort=category&direction=asc">
          View All Products by Category
        </a>
      </div>


- I save the template and then refresh my code in my dev server to see how this looks and it looks good, I can now see the sorting menu under my Merchandise menu in the navbar:

![Navbar updated with sorting for price and category](/static/images/Product%20Query/Screenshot%20nav%20bar%20updated%20with%20price%20and%20category%20sorting%20menu%20items.png)

2. Once this looks good, I can then move on to my all_products view in views.py and add the code to handle my new GET parameters. The code below checks whether 'sort' is in request.GET and if it is, then it checks whether the direction is there. I also add 'sort = None' and 'direction = none' at the top to make sure they are both defined in order to return the template properly when not using sorting:

   sort = None
    direction = None

    if request.GET:
        if 'sort' in request.GET:
            if 'direction' in request.GET:

3. I then want to create a variable called sortkey = to rqeuest.GET['sort'] and then set sort directly below it to the new sortkey variable. In order to allow case insensitive sorting of the name field, I also annotate all the products with a new field. Annotation allows us to add a temporary field on a model. I then check whether the sortkey is equal to name and if it is, I set to lower_name; which is the field created with the annotation next. To create the annotation, I add products = products.annotate(lower_name=Lower("name")) - this is just using the 'lower' function on the original name field and preserving the original field for sorting by name by copying the sort parameter into a new variable called sortkey:

    if request.GET:
        if 'sort' in request.GET:
            sortkey = request.GET['sort']
            sort = sortkey
            if sortkey === 'name':
                sortkey = 'lower_name'
                products = products.annotate(lower_name=Lower("name"))

4. I then move on to creating the direction parameter. I add the below code, borrowing Code Insitute's code for this and acknowledging. This code checks whether the direction is descending. There is a minus in front of the sort key using string formatting which reverses the order. 

            if 'direction' in request.GET:
                direction = request.GET['direction']
                if direction == 'desc':
                    sortkey = f'-{sortkey}'
            products = products.order_by(sortkey)

5. I now want to return the current sorting methodology, using the string formatting with the sort and direction variables that are now stored. I will borrow Code Institute's code from Boutique Ado's Products page again, using the below, storing it direcly below the if 'q' request.GET statement:

    current_sorting = f'{sort}_{direction}'

6. Then in my contexts in views.py I add the below:

        'current_sorting': current_sorting,

7. I then start my server up to make sure that everything works but unfortunately, when I try to load the page with the products sorted by price I am seeing the below error screen:

![Merchandise sort by price not working](/static/images/Product%20Query/Screenshot%20merchandise%20sort%20by%20price%20not%20working.png)

However, the sort by all category is working okay:

![Merchandise sort by categories is working](/static/images/Product%20Query/Screenshot%20merchandise%20sort%20by%20categories%20is%20working%20okay.png) 

8. I turn debug mode to true in settings and reload the error page to see if i can pinpoint the issue:

Page not found (404)
Request Method:	GET
Request URL:	http://127.0.0.1:8000/merchandise/sort%3Dprice&direction%3Dasc
Using the URLconf defined in working_out_gym.urls, Django tried these URL patterns, in this order:

admin/
accounts/
discussionboard/
[name='home']
merchandise/ [name='products']
merchandise/ <int:product_id>/ [name='product_detail']
summernote/
The current path, merchandise/sort=price&direction=asc, didn’t match any of these.

9. I go back to my views.py file and notice that I haven't added current_sorting to contexts correctly and its removed the code. I add back in with double quotes as the rest of the code is. I reload the page again but see a different error this time:

![Fielderror merchandise price sorting](/static/images/Product%20Query/Screenshot%20fielderror%20price%20sorting%20on%20merchandise3.png) 

10. I go back to my views.py file and update the code so that in my sorting logic, if the sortkey is 'price' then it has been changed to 'from_price' instead as this is the correct ID for the price in my code. I have done this by adding an elif statement for price which sets the sortkey as from_price:

def all_products(request):
    """A view to show all products, including search and category filtering"""

    products = (
        Product.objects.filter(is_active=True)
        .select_related("category")
        .annotate(from_price=Min("variants__price"))
    )

    query = None
    current_category = None
    sort = None
    direction = None

    if request.GET:
        if 'sort' in request.GET:
            sortkey = request.GET['sort']
            sort = sortkey
            if sortkey == 'name':
                sortkey = 'lower_name'
                products = products.annotate(lower_name=Lower("name"))
            elif sortkey == 'price':
                sortkey = 'from_price'
            if 'direction' in request.GET:
                direction = request.GET['direction']
                if direction == 'desc':
                    sortkey = f'-{sortkey}'
            products = products.order_by(sortkey)

    if request.GET:
        if "category" in request.GET:
            current_category = request.GET["category"].strip()

            category_list = [c.strip() for c in current_category.split(",") if c.strip()]
            products = products.filter(category__name__in=category_list)

        if "q" in request.GET:
            query = request.GET["q"].strip()

            if not query:
                messages.error(request, "You didn't enter any search criteria!")
                return redirect(reverse("merchandise:products"))

            queries = (
                Q(title__icontains=query) |
                Q(vendor__icontains=query) |
                Q(tags__icontains=query) |
                Q(category__name__icontains=query)
            )

            products = products.filter(queries).distinct()

    current_sorting = f'{sort}_{direction}'

    context = {
        "products": products,
        "search_term": query,
        "current_category": current_category,
    }

    return render(request, "merchandise/products.html", context)

11. Now when I reload the page, I can see that it is sorting all products by lowest price first so I will commit my code here:

![Merchandise Price Sorting Working](/static/images/Product%20Query/Screenshot%20merchandise%20price%20sorting%20working%20now.png) 

12. I now want to further improve the sorting functionality on my site, such as:

- User can see the number of search results as well as what was searched for when executing a search query.
- User can search individual categories from the All Products page rather than having to use the Navbar menu all the time.

13. To start with, I add the category to each individual product card which makes it a link to the actual category. In my products.html file, I am going to update my current if product.category statement from:

{% if product.category %}
<small class="text-muted">{{ product.category.name }}</small>
{% endif %}

To:

{% if product.category %}
<small class="text-muted">
<a class="text-muted" href="{% url 'products' %}?category={{ product.category.name }}">
<i class="fas fa-tag mr-1"></i>{{ product.category.name }}
</a>
</small>
{% endif %}

- This says that if the product has a category, then we want to render it out using the product category name as the text and as the href.

14. I now need to also update this on my product_detail.html file too, under my 'Merchandise' header, I update my if product.category statement on there to the below:

      {% if product.category %}
        <p class="text-muted mb-2">
          <a class="text-muted" href="{% url 'products' %}?category={{ product.category.name }}">
            <i class="fas fa-tag mr-1"></i>{{ product.category.name }}
          </a>
        </p>
      {% endif %}

15. I save the updates to my code and refresh my Merchandise page to see if the sorting has come into effect. However, I am receiving an error when I load the Merchandise page as the code I used from Code Institute hasn't been updated with my url of Merchandise instead of products:

![Merchandise url not set in new code](/static/images/Product%20Query/Screenshot%20new%20code%20not%20updated%20with%20merchandise%20url.png)

16. I update my href class as below and reload the page and can now see the sorting by category on the individual products:

 <a class="text-muted" href="{% url 'merchandise:products' %}?category={{ product.category.name }}">

![Products items have individual sorting set](/static/images/Product%20Query/Screenshot%20indiviual%20products%20have%20category%20sorting.png) 

17. If I click the category on the products then this takes me to the product page for all Womens Crop Tops:

![Products sorting takes to all womens crop tops](/static/images/Product%20Query/Screenshot%20all%20womens%20crop%20tops.png) 

18. I now need to look at what happens if the user selects multiple categories, if they go to the All Products page then there are a number of categories being selected. Back in my products.html file and under the header for 'Merchandise', I am going to iterate through that and render some category links using the code from Code Institute's Boutique Ado. This code hreh uses the same linking mechanism as the links in the individual product cards:

                {% for c in current_categories %}
                    <a class="category-badge text-decoration-none" href="{% url 'merchandise:products' %}?category={{ c.name }}">
                        <span class="p-2 mt-2 badge badge-white text-black rounded-0 border border-dark">{{ c.friendly_name }}</span>
                    </a>
                {% endfor %}

19. I am also going to use Code Institute's CSS for the badge hover effect too:

a.category-badge > span.badge:hover {
    background: #212529 !important;
    color: #fff !important;
}

20. I will now refresh my page on my local dev server and see how that looks, However, I am not seeing the different categories under my header:

![Categories not showing under header](/static/images/Product%20Query/Screenshot%20categories%20not%20showing%20under%20header.png) 

21. I have queried this with Claude AI who advises that the current_categories variable is not being passed from the all_products view to the products.html template, I need to update my all_products view to populate the current_categories variable and pass it to the template:

- In my views.py file, I update the imports to include Category
- Under my current category statement (current_category = None) I add a new statement for: current_categories = Category.objects.all()
- I have also added "current_categories": current_categories to the context dicitionary

22. Then in my products.html template, I have updated my for category statement to the below:

              {% if product.category %}
                <small class="text-muted">
                  <a class="text-muted" href="{% url 'merchandise:products' %}?category={{ product.category.name }}">
                    <i class="fas fa-tag mr-1"></i>{{ product.category.name }}
                  </a>
                </small>
                {% endif %}

23. I refresh my page but I am still not seeing the category buttons, so I consult again with Claude AI who advises that the issue is that I am not passing the current_categories variable to the context in my product_detail view which means that the category badges will not be displayed on the product detail page, I update my view to the below, adding the current_categories to my context dictionary and setting the variable as I did in all_products:

def product_detail(request, product_id):
    """A view to show individual products"""

    product = get_object_or_404(
        Product.objects.annotate(from_price=Min("variants__price")),
        pk=product_id
    )

    current_categories = Category.objects.all()

    context = {
        "product": product,
        "current_categories": current_categories,
    }

    return render(request, "merchandise/product_detail.html", context)

24. I also add the below to my product_detail.html template in my first div:

      {% if product.category %}
        <p class="text-muted mb-2">
          <a class="text-muted" href="{% url 'merchandise:products' %}?category={{ product.category.name }}">
            <i class="fas fa-tag mr-1"></i>{{ product.category.name }}
          </a>
        </p>
      {% endif %}

25. I reload the page but this still isn't showing me the badges for the categories in my 'all products' page. I consult Claude AI about this. They advise that the code looks correct but that to complete the functionality I should try the following:

- Displaying the number of search results: to do this I will need to add a line of text above the product grid that displays the number of search results and what was searched for, e.g: "Showing 12 results for 'Womens Crop Tops". To do this, I must first add the below to my context dictionary in my all_products view in views.py and also update the current_categories context to the below, I update this now:

    "current_categories": current_categories,
    "product_count": products.count(),

- Then in my products.html template, I add the below code above the product grid:

{% if search_term or current_category %}
<div class="row mb-4">
  <div class="col">
    {% if search_term %}
    <p>Showing {{ product_count }} results for '{{ search_term }}'</p>
    {% elif current_category %}
    <p>Showing {{ product_count }} results in the '{{ current_category }}' category</p>
    {% endif %}
  </div>
</div>
{% endif %}

- I then want to allow searching within categories so that users can search within a specific category, so I need to update the search form in my main-nav.html template to include a hidden input field for the category. When the form is submitted, the category parameter will be included in the URL. I update the search form as follows:

<form method="GET" action="{% url 'merchandise:products' %}">
  <div class="input-group w-100">
    <input class="form-control rounded-0" type="text" name="q" placeholder="Search our site" />
    {% if current_category %}
    <input type="hidden" name="category" value="{{ current_category }}">
    {% endif %}
    <button class="btn btn-dark rounded-0" type="submit">
      <i class="fas fa-search"></i>
    </button>
  </div>
</form>

26. I refresh the page and can search on products but this doesn't resolve the issue with badge sorting on the all products page so I go back to Claude AI again. They advise that the current_categproes variable may not be being populated correctly and to try the following steps to verify this:

- I first verify the data in the Category model by ensuring it has the correct data and that the friendly_name is being populated correctly. I start by going to the admin panel on my dev server and logging in as the superuser. Then I locate the Category model and click on the 'Categories' link to view the Category model. I then see a list of all categories that have been created in my application, I need to verify that the 'name' and 'friendly_name' fields are populated correctly which they are:

![Categories in admin panel](/static/images/Product%20Query/Screenshot%20admin%20categories.png) 

- I then debug the all_products view by adding the below print statements into prooducts.html to ensure that the current_categories variable is being correctly populated in the all_products view:

{% for category in current_categories %}
  <a class="category-badge text-decoration-none" href="{% url 'merchandise:products' %}?category={{ category.name }}">
    <span class="p-2 mt-2 badge badge-white text-black rounded-0 border border-dark">{{ category.friendly_name }}</span>
  </a>
{% empty %}
  <p>No categories found.</p>
{% endfor %}

- After adding this and refreshing the page I can now see the below:

![Current categories statement all products](/static/images/Product%20Query/Screenshot%20current%20categories%20on%20all%20products.png) 

- I consulted Claude AI about this who advises that it looks like there is a lot of categories being displayed, it seems as though the current_categories variable is being populated with a large number of categories which is causing the lengthy output. To further investigate the issue, I can add some further debugging code to the all_products view in the views.py file to help me understand how the current_categories variable is being set. It advises me to update all_products view to:

def all_products(request):
    """A view to show all products, including search and category filtering"""

    products = (
        Product.objects.filter(is_active=True)
        .select_related("category")
        .annotate(from_price=Min("variants__price"))
    )

    query = None
    current_category = None
    current_categories = Category.objects.all()
    sort = None
    direction = None

    print("Current categories:")
    for category in current_categories:
        print(f"- {category.friendly_name}")

    if request.GET:
        if 'sort' in request.GET:
            sortkey = request.GET['sort']
            sort = sortkey
            if sortkey == 'name':
                sortkey = 'lower_name'
                products = products.annotate(lower_name=Lower("name"))
            elif sortkey == 'price':
                sortkey = 'from_price'
            if 'direction' in request.GET:
                direction = request.GET['direction']
                if direction == 'desc':
                    sortkey = f'-{sortkey}'
            products = products.order_by(sortkey)

    if request.GET:
        if "category" in request.GET:
            current_category = request.GET["category"].strip()
            category_list = [c.strip() for c in current_category.split(",") if c.strip()]
            products = products.filter(category__name__in=category_list)

        if "q" in request.GET:
            query = request.GET["q"].strip()

            if not query:
                messages.error(request, "You didn't enter any search criteria!")
                return redirect(reverse("merchandise:products"))

            queries = (
                Q(title__icontains=query) |
                Q(vendor__icontains=query) |
                Q(tags__icontains=query) |
                Q(category__name__icontains=query)
            )

            products = products.filter(queries).distinct()

    current_sorting = f'{sort}_{direction}'

    context = {
        "products": products,
        "search_term": query,
        "current_category": current_category,
        "current_categories": current_categories,
        "product_count": products.count(),
    }

    return render(request, "merchandise/products.html", context)

- This adds a print statement to the current_categories variable to help us understand what is being passed to the template. Now when I refresh the page I am seeing the following error:

![Attribute error no friendly name](/static/images/Product%20Query/Screenshot%20attribute%20error.png) 

- I have decided not to add the friendly_name field to my category model and instead will use the name field instead in my products.html template. I update the code in products.html to the below:

{% if current_categories %}
  <p>Current categories: {% for category in current_categories %}{{ category.name }}, {% endfor %}</p>
{% else %}
  <p>No current categories found.</p>
{% endif %}

{% for category in current_categories %}
  <a class="category-badge text-decoration-none" href="{% url 'merchandise:products' %}?category={{ category.name }}">
    <span class="p-2 mt-2 badge badge-white text-black rounded-0 border border-dark">{{ category.name }}</span>
  </a>
{% empty %}
  <p>No categories found.</p>
{% endfor %}#

- Then in my views.py I update all_products view to use the name field instead of friendly_name as below:

def all_products(request):
    """A view to show all products, including search and category filtering"""

    products = (
        Product.objects.filter(is_active=True)
        .select_related("category")
        .annotate(from_price=Min("variants__price"))
    )

    query = None
    current_category = None
    current_categories = Category.objects.all()
    sort = None
    direction = None

    print("Current categories:")
    for category in current_categories:
        print(f"- {category.name}")

    if request.GET:
        if 'sort' in request.GET:
            sortkey = request.GET['sort']
            sort = sortkey
            if sortkey == 'name':
                sortkey = 'lower_name'
                products = products.annotate(lower_name=Lower("name"))
            elif sortkey == 'price':
                sortkey = 'from_price'
            if 'direction' in request.GET:
                direction = request.GET['direction']
                if direction == 'desc':
                    sortkey = f'-{sortkey}'
            products = products.order_by(sortkey)

    if request.GET:
        if "category" in request.GET:
            current_category = request.GET["category"].strip()
            category_list = [c.strip() for c in current_category.split(",") if c.strip()]
            products = products.filter(category__name__in=category_list)

        if "q" in request.GET:
            query = request.GET["q"].strip()

            if not query:
                messages.error(request, "You didn't enter any search criteria!")
                return redirect(reverse("merchandise:products"))

            queries = (
                Q(title__icontains=query) |
                Q(vendor__icontains=query) |
                Q(tags__icontains=query) |
                Q(category__name__icontains=query)
            )

            products = products.filter(queries).distinct()

    current_sorting = f'{sort}_{direction}'

    context = {
        "products": products,
        "search_term": query,
        "current_category": current_category,
        "current_categories": current_categories,
        "product_count": products.count(),
    }

    return render(request, "merchandise/products.html", context)

- I refresh my page to see if the badges are now displaying and they are! The issue here was that I was trying to access the friendly_name field in my products.html template but the Category model did not have this field. By adding the debugging code I could print out the current_categories variable, helping me pinpoint the issue. Updating the products.html template to use the name field instead of friendly_name field:

![Categories now showing in all_products view](/static/images/Product%20Query/Screenshot%20categories%20now%20showing%20in%20all%20products%20page.png) 

- I test the categories themselves to ensure that clicking then redirects to the relevant page, however, this is not working, so I go back to Claude AI who advises that the category filtering is not working as expected, even though the badges are now being displayed correctly. The output in my terminal shows that the category=Womens%20Crop%20Tops parameter is being passed correctly in the URL, but it's not filtering the products as expected.

- I first check the URL pattern which appears to be set up correctly. I consult Claude AI on what I need to do next and they advise that I need to ensure that Category model has the correct name field and that the database is consistent. To do this, I open Dajngo shell using:

python manage.py shell

- Then in the shell, I import the Category model and inspect the fields using the below; which will show me my fields defined in the Category model and I can verify that the name field is present:

from merchandise.models import Category
print(Category._meta.fields)

- This returns the following:

(<django.db.models.fields.BigAutoField: id>, <django.db.models.fields.CharField: name>, <django.db.models.fields.SlugField: slug>)

- I query this with Claude who advises there are no issues with this output because:

id: A BigAutoField that serves as the primary key for the Category model.
name: A CharField that stores the name of the category.
slug: A SlugField that stores a URL-friendly version of the category name.

- This is standard set up for a Category model in a Django application. Next I inspect the data in the Category table by querying the model using:

categories = Category.objects.all()
for category in categories:
    print(category.name)

- I have ran some database related querys in shell and these are returning results so database connection is fine. 

- Claude AI recommends checking the badge model and view logic next, they advise that the Badge model needs to be correctly defined in my Django application and verify that the views responsible for handling the badge-related functionality. I consult AI about this who provides me with some code so I can define the Badge model as below, I add this to my models.py code and then acknowledge:

from django.db import models

class Badge(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='badges', null=True, blank=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name

- Now that I have defined the badge model, I need to integrate it into my app views, templates and URL's. In my views file, I need to import the new Badge model at the top and add it to the context dictionary in all_products views, create the variable for it and also add to the context dictionary for my product_detail views, Claude AI has provided the code:

def all_products(request):
    # Your existing all_products view code...
    context = {
        "products": products,
        "search_term": query,
        "current_category": current_category,
        "current_categories": current_categories,
        "product_count": products.count(),
        "badges": Badge.objects.filter(is_active=True),  # Add this line to fetch active badges
    }

def product_detail(request, product_id):
    # Your existing product_detail view code...
    product = get_object_or_404(
        Product.objects.annotate(from_price=Min("variants__price")),
        pk=product_id
    )

    current_categories = Category.objects.all()
    active_badges = Badge.objects.filter(is_active=True)  # Add this line to fetch active badges

    context = {
        "product": product,
        "current_categories": current_categories,
        "active_badges": active_badges,  # Add this line to pass active badges to the template
    }

- I then need to update my merchandise urls.py file so include two new patterns to allow for badge functionality:

    path("badges/", views.all_badges, name="all_badges"),
    path("badge/<int:badge_id>/", views.badge_detail, name="badge_detail"),

- Then I implement the all_badges and badge_detail views within the merchandise views file:

def all_badges(request):
    badges = Badge.objects.filter(is_active=True)
    context = {
        "badges": badges,
    }
    return render(request, "merchandise/all_badges.html", context)

def badge_detail(request, badge_id):
    badge = get_object_or_404(Badge, pk=badge_id)
    context = {
        "badge": badge,
    }
    return render(request, "merchandise/badge_detail.html", context)

- I then need to create two new templates in the merchandise templates directory: all_badges.html - which displays a list of all active badges and badge_detail.html - which displays the details of a specific badge. AI has provided the code for this which I acknowledge and add to the two new templates.

- In my products.html, I add the if statement for badges provided by Clude AI, under my container for products:

  {% if badges %}
    <div class="badges-container">
      <h2>Badges</h2>
      <ul>
        {% for badge in badges %}
          <li>
            {% if badge.image %}
              <img src="{{ badge.image.url }}" alt="{{ badge.name }}">
            {% endif %}
            <h3>{{ badge.name }}</h3>
            <p>{{ badge.description }}</p>
          </li>
        {% endfor %}
      </ul>
    </div>
  {% endif %}
{% endblock %}

- I also update my product_detail.html file with the below code for active badges:

 {% if active_badges %}
        <div class="badges-container mt-4">
          <h2>Badges</h2>
          <ul>
            {% for badge in active_badges %}
              <li>
                {% if badge.image %}
                  <img src="{{ badge.image.url }}" alt="{{ badge.name }}">
                {% endif %}
                <h3>{{ badge.name }}</h3>
                <p>{{ badge.description }}</p>
              </li>
            {% endfor %}
          </ul>
        </div>
      {% endif %}
    </div>

- I save the code and then stop and start my dev server to see if the new changes are working. However, I am presented with the following screen:

![Badge model not migrated](/static/images/Product%20Query/Screenshot%20make%20migrations%20not%20ran%20for%20new%20badge%20model.png) 

- I realise I have added a new model to the database and not ran migrations so run these now:

python3 manage.py makemigrations

python3 manage.py migrate

- Both cmds run successfully and migrate the new badge model into the database. I test if clicking the badges now takes the user to the relevant page which it does, so I turn Debug to false and then commit my code:

![Badges now working](/static/images/Product%20Query/Screenshot%20badges%20now%20redirecting.png) 

- Before I move on, I want to remove the list of current categories that is appearing above the badges, to do this, I remove the following code from products.html:

  {% if current_categories %}
  <p>Current categories: {% for category in current_categories %}{{ category.name }}, {% endfor %}</p>
  {% else %}
  <p>No current categories found.</p>
  {% endif %}

- I now want to add a bar in the top right, as Code Institute have in their Boutique Ado Project, which allows user to sort: price high to low, price low to high, name A-Z, name Z-A, category A-Z and category z-a. To do this I am going to borrow Code Institute's code for their sort-selector div in products.html and remove the two options for rating as my dataset doesn't use these:

       <div class="row">
            <div class="product-container col-10 offset-1">
                <div class="row mt-1 mb-2">
                    <div class="col-12 col-md-6 my-auto order-md-last d-flex justify-content-center justify-content-md-end">
                        <div class="sort-select-wrapper w-50">
                            <select id="sort-selector" class="custom-select custom-select-sm rounded-0 border border-{% if current_sorting != 'None_None' %}info{% else %}black{% endif %}">
                                <option value="reset" {% if current_sorting == 'None_None' %}selected{% endif %}>Sort by...</option>
                                <option value="price_asc" {% if current_sorting == 'price_asc' %}selected{% endif %}>Price (low to high)</option>
                                <option value="price_desc" {% if current_sorting == 'price_desc' %}selected{% endif %}>Price (high to low)</option>
                                <option value="name_asc" {% if current_sorting == 'name_asc' %}selected{% endif %}>Name (A-Z)</option>
                                <option value="name_desc" {% if current_sorting == 'name_desc' %}selected{% endif %}>Name (Z-A)</option>
                                <option value="category_asc" {% if current_sorting == 'category_asc' %}selected{% endif %}>Category (A-Z)</option>
                                <option value="category_desc" {% if current_sorting == 'category_desc' %}selected{% endif %}>Category (Z-A)</option>
                            </select>
                        </div>
                    </div>
                    <div class="col-12 col-md-6 order-md-first">
                        <p class="text-muted mt-3 text-center text-md-left">
                            {% if search_term or current_categories or current_sorting != 'None_None' %}
                                <span class="small"><a href="{% url 'products' %}">Products Home</a> | </span>
                            {% endif %}
                            {{ products|length }} Products{% if search_term %} found for <strong>"{{ search_term }}"</strong>{% endif %}
                        </p>
                    </div>
                </div>

- I add this code after the code for badges but before the for products statement in my products.html file. I will refresh the page and see how this looks. I am getting server 500 error when I refresh the page, so turn debug on and see what is going on and find that there is an {% endif %} tag mismatch so resolve this. When I refresh the page again I now receive an error to say that 'products' is not defined, and this is due to the fact I didn't update the code from Code Institute with the Merchandise urls so I update the code with this now. Now when I refresh my page I can see the new sort feature and a link to the Products Home page - I need to update this so it reflects the correct page name for my application, so I do this now.

![New sort options and return to merchandise home option](/static/images/Product%20Query/Screenshot%20sorting%20options%20and%20return%20to%20home.png) 

- However, the options when selected are not sorting our page out so we need to add some Javascript to the products.html file so that the new sorting options will work. I am going to borrow Code Institute's code for this again:

{% block postloadjs %}
    {{ block.super }}
    <script type="text/javascript">
		$('.btt-link').click(function(e) {
			window.scrollTo(0,0)
		})
	</script>
    
    <script type="text/javascript">
        $('#sort-selector').change(function() {
            var selector = $(this);
            var currentUrl = new URL(window.location);
            var selectedVal = selector.val();
            if(selectedVal != "reset"){
                var sort = selectedVal.split("_")[0];
                var direction = selectedVal.split("_")[1];
                currentUrl.searchParams.set("sort", sort);
                currentUrl.searchParams.set("direction", direction);
                window.location.replace(currentUrl);
            } else {
                currentUrl.searchParams.delete("sort");
                currentUrl.searchParams.delete("direction");
                window.location.replace(currentUrl);
            }
        })
    </script>
{% endblock %}

- I refresh my page again to see if the Javascript is coming into play but nothing happens when I select one of the sort options. I consult AI on this, who advises that there is nothing set for sort or direction parameters in views.py so it won't handle the request. I update views.py with the parameters below:

    if 'sort' in request.GET:
        sort = request.GET['sort']
        direction = request.GET['direction']
        if direction == 'desc':
            sort = f'-{sort}'
        products = products.order_by(sort)

- I now refresh my page but it is still not actioning the different sort functionalities. I notice that I am receiving the below error in my terminal:

  File "C:\Users\leila\OneDrive\Desktop\Documents\vscode-projects\working_out_gym\merchandise\views.py", line 28
    sort = request.GET['sort']
    ^
IndentationError: expected an indented block after 'if' statement on line 27

- I update my views.py so indentations are correct, I refresh but now receive an error to say the import for Lower is not defined so remove this from imports and refresh again. However, this is still doing nothing. I consult AI who asks me to check what happens to the url when I am selecting the options, which is nothing. They recommend updating my Javascript block to not use the window.location.replace(currentUrl) method as its not updating the URL correctly and instead use the history.pushState() to update the URL without reloading the page:

{% block postloadjs %}
    {{ block.super }}
    <script type="text/javascript">
		$('.btt-link').click(function(e) {
			window.scrollTo(0,0)
		})
	</script>
    
    <script type="text/javascript">
        $('#sort-selector').change(function() {
            var selector = $(this);
            var currentUrl = new URL(window.location);
            var selectedVal = selector.val();
            if(selectedVal != "reset"){
                var sort = selectedVal.split("_")[0];
                var direction = selectedVal.split("_")[1];
                currentUrl.searchParams.set("sort", sort);
                currentUrl.searchParams.set("direction", direction);
                var newUrl = currentUrl.toString();
                history.pushState({}, null, newUrl);
                // Trigger a page reload or update the products list
                location.reload();
            } else {
                currentUrl.searchParams.delete("sort");
                currentUrl.searchParams.delete("direction");
                var newUrl = currentUrl.toString();
                history.pushState({}, null, newUrl);
                // Trigger a page reload or update the products list
                location.reload();
            }
        })
    </script>
{% endblock %}

- I add this to my products.html, replacing the current Javascript code, and refresh the page, however, there is still nothing happening. I inspect the sort selector and look at the console in dev tools and can see the following errors:

Failed to load resource: the server responded with a status of 404 (Not Found)Understand this error
merchandise/:238307 Uncaught ReferenceError: $ is not defined
    at merchandise/:238307:3Understand this error
merchandise/:238313 Uncaught ReferenceError: $ is not defined
    at merchandise/:238313:9Understand this error
noimage.png:1  Failed to load resource: the server responded with a status of 404 (Not Found)Understand this error
script.js:1  Failed to load resource: the server responded with a status of 404 (Not Found)Understand this error

- I consult AI about this, who advises that it appears there are a couple of issues here:

404 Errors for Static Files: The error messages indicate that the static files (images and JavaScript files) are not being served correctly. This could be due to an issue with your Django project's configuration or the way you're serving the static files.

Uncaught ReferenceError: $ is not defined: This error suggests that the jQuery library is not being loaded correctly. The JavaScript code in your products.html template is using the $ function, which is part of the jQuery library.

- AI recommends checking my Static Files configuration, I check my settings.py file and this looks okay to me, as does the Static folder, its located in the root of my project structure. I run the following cmds:

Remove-Item -Recurse -Force staticfiles  

python manage.py collectstatic 

- I restart my dev server but sorting still isn't working. AI suggests adding the below code to the bottom of my base.html file, to ensure that I am loading the jQuery Library in the template correctly:

{% block postloadjs %}
    {{ block.super }}
    <script src="https://code.jquery.com/jquery-3.6.0.min.js"></script>
    {# Your other JavaScript code #}
{% endblock %}

- After I reload the page with the new code and try the different sorting options, I can see category sorting is working, however, price is not. The error I receive is below:

![Price variable sorting on error](/static/images/Product%20Query/Screenshot%20sorting%20options%20and%20return%20to%20home.png) 

- I know from past issues that this is because we are using 'from_price' due to the dataset size and different options available in that data, so I need to update price to from_price in the new code. I add the below statement to the request.GET if statement for sorting so it looks at from_price when price is selected:

    if 'sort' in request.GET:
        sort = request.GET['sort']
        direction = request.GET['direction']
        if direction == 'desc':
            sort = f'-{sort}'
        if sort == 'price':
            sort = 'from_price'
        products = products.order_by(sort)

- When I refresh the page now, it loads with the products sorted in lowest to highest order:

![Price low to high sorting ](/static/images/Product%20Query/Screenshot%20price%20low%20to%20high%20sorting%20working.png) 

- However, if I sort this from high to low on price it is giving the following error:

![Price high to low sorting error](/static/images/Product%20Query/Screenshot%20price%20high%20to%20low%20broken.png) 

- I consult AI who advises that I need to modify the sorting logic in all_products view to handle the descending sort for the from_price field. They recommend adding the below code to the if statement for price:

    if 'sort' in request.GET:
        sort = request.GET['sort']
        direction = request.GET['direction']
        if sort == 'price':
            if direction == 'desc':
                sort = '-from_price'
            else:
                sort = 'from_price'
        elif direction == 'desc':
            sort = f'-{sort}'
        products = products.order_by(sort)

- I update the code and refresh and test again and can see high to low sorting on price now works too:

![Price high to low working](/static/images/Product%20Query/Screenshot%20price%20high%20to%20low%20working.png) 

- I next test the 'Name A-Z' sorting but I am presented with an error:

![Sorting Name A-Z broken](/static/images/Product%20Query/Screenshot%20name%20a-z%20sorting%20broken.png) 

- I am seeing this error as 'name' is not a field in my data, I instead need to use 'title' so using the same logic as was used on price, I add a new elif statement as below:

    if 'sort' in request.GET:
        sort = request.GET['sort']
        direction = request.GET['direction']
        if sort == 'price':
            if direction == 'desc':
                sort = '-from_price'
            else:
                sort = 'from_price'
        elif sort == 'name':
            if direction == 'desc':
                sort = '-title'
            else:
                sort = 'title'
        elif direction == 'desc':
            sort = f'-{sort}'
        products = products.order_by(sort)

- Refreshing the page shows this is working for both name A-Z and name Z-A:

![Sorting Name working](/static/images/Product%20Query/Screenshot%20name%20sorting%20working.png) 

- Finally, I test the category sorting and this is also working okay:

![Category sorting selector working](/static/images/Product%20Query/Screenshot%20category%20sorting%20working%20okay.png) 

- I finally test the link I created at the top of the Merchandise page that redirects user to all products and this works too, so set Debug back to false and commit my code. 

- Before moving on to the shopping bag, as I am using a large dataset of products, it would be useful if there was a back to top button users could use that isn't the 'Merchandise Home' link at the top of the page that they would have to scroll back up to to use. I borrow Code Institute's code from Boutique Ado, and add this to the bottom of my products.html file:

    <div class="btt-button shadow-sm rounded-0 border border-black">
        <a class="btt-link d-flex h-100">
            <i class="fas fa-arrow-up text-black mx-auto my-auto"></i>
        </a>	
    </div>
{% endblock %}

{% block postloadjs %}
    {{ block.super }}
    <script type="text/javascript">
		$('.btt-link').click(function(e) {
			window.scrollTo(0,0)
		})
	</script>

- I also need to add the css styles that Code Institute have used for back to top link, so will borrow their code and add to style.css:

.text-black {
    color: #000 !important;
}

.btt-button {
    height: 42px;
    width: 42px;
    position: fixed;
    bottom: 10px;
    right: 10px;
}
.btt-link {
    cursor: pointer;
}#

- I add this in and reload the page and can now see the back to top link rendering on the page, however, clicking this does nothing:

![Back to Top Link Showing but Doing Nothing](/static/images/Product%20Query/Screenshot%20back%20to%20top%20button%20showing%20but%20not%20doing%20anything.png) 

- I consult AI who recommends I update my products.html code to: 

{% block postloadjs %}
{{ block.super }}
<script type="text/javascript" src="{% static 'js/script.js' %}"></script>

- It also advises that I need a static/script.js file creating with the below code, so I create and populate this and then acknowledge:

// Back to Top functionality
$('.btt-link').click(function(e) {
  window.scrollTo(0,0)
});

// Sorting functionality
$('#sort-selector').change(function() {
  var selector = $(this);
  var currentUrl = new URL(window.location);
  var selectedVal = selector.val();
  if (selectedVal != "reset") {
    var sort = selectedVal.split("_")[0];
    var direction = selectedVal.split("_")[1];
    currentUrl.searchParams.set("sort", sort);
    currentUrl.searchParams.set("direction", direction);
    var newUrl = currentUrl.toString();
    history.pushState({}, null, newUrl);
    // Trigger a page reload or update the products list
    location.reload();
  } else {
    currentUrl.searchParams.delete("sort");
    currentUrl.searchParams.delete("direction");
    var newUrl = currentUrl.toString();
    history.pushState({}, null, newUrl);
    // Trigger a page reload or update the products list
    location.reload();
  }
});

- I run collectstatic:

python manage.py collectstatic

- I then restart my dev server and see if the button now works, which it does so I commit my code and get ready to start creating my shopping bag next.


## Shopping Bag Application Creation and Wiring

1.  To start, I create a new app for 'Shopping Bag' using the following cmd:

python3 manage.py startapp shoppingbag

2. Once I can see the new app directory is successfully created, I update INSTALLED APPS in project settings.py to include the new application as below:

'shoppingbag',

3. Next, I will create a simple view in my views.py file which will render the shopping bag page:

from django.shortcuts import render

def view_shoppingbag(request):
    """ A view to show the shopping bag contents """

    return render(request, 'shoppingbag/shoppingbag.html')

4. Next, I need to create the templates directory and the shoppingbag.html template that I have just set in our view for the shopping bag:

![Shopping Bag Template Directory](/static/images/shoppingbag/Screenshot%20template%20directory%20creation.png)

5. Next I will populate my shoppingbag.html, I will copy the contents of my index.html file from my home app as the structure is going to be similar. I remove the content block ready to populate with the shopping bag content:

![Shopping Bag html intial](/static/images/shoppingbag/Screenshot%20shoppingbag%20html%20initial.png)

6. Next I copy my 'home' urls.py file and create a new urls.py file in the shoppingbag directory. I paste the content from the home urls py file into the new file and update with the appropriate views and name:

from django.urls import path
from . import views

urlpatterns = [
    path("", views.view_shoppingbag, name="view_shoppingbag"),
]

7. Next, I include the shoppingbag urls in the project level urls.py file:

    path("shoppingbag/", include("shoppingbag.urls")),

8. Next I go to my main-nav.html and update it so that it will show an inline menu item for both 'Account' and the 'Shopping Bag' with an appropriate icon. I want this to appear at the right hand side of my navbar and always be visible to the end user. I ask Claude AI for some help with this and they give me the following code - I add this just before my closing nav element tag:

<!-- Account and Shopping Bag Icons -->
    <div class="col-12 col-lg-4 my-auto py-1 py-lg-0">
      <ul class="list-inline list-unstyled text-center text-lg-right my-0">
        <li class="list-inline-item dropdown">
          <a class="text-black nav-link" href="#" id="user-options" data-toggle="dropdown" aria-haspopup="true"
            aria-expanded="false">
            <div class="text-center">
              <div><i class="fas fa-user fa-lg"></i></div>
              <p class="my-0">My Account</p>
            </div>
          </a>
          <div class="dropdown-menu border-0" aria-labelledby="user-options">
            {% if request.user.is_authenticated %}
            {% if request.user.is_superuser %}
            <a href="" class="dropdown-item">Product Management</a>
            {% endif %}
            <a href="" class="dropdown-item">My Profile</a>
            <a href="{% url 'account_logout' %}" class="dropdown-item">Logout</a>
            {% else %}
            <a href="{% url 'account_signup' %}" class="dropdown-item">Register</a>
            <a href="{% url 'account_login' %}" class="dropdown-item">Login</a>
            {% endif %}
          </div>
        </li>
        <li class="list-inline-item">
          <a class="{% if grand_total %}text-info font-weight-bold{% else %}text-black{% endif %} nav-link" href="{% url 'view_bag' %}">
            <div class="text-center">
              <div><i class="fas fa-shopping-bag fa-lg"></i></div>
              <p class="my-0">
                {% if grand_total %}
                ${{ grand_total|floatformat:2 }}
                {% else %}
                $0.00
                {% endif %}
              </p>
            </div>
          </a>
        </li>
      </ul>
    </div>
  </div>

  - Claude AI also provides the following css styles:

  /* Shopping Bag Icon Styles */
.nav-link {
  color: #ffffff;
  text-decoration: none;
}

.nav-link:hover {
  color: #d9d9d9;
}

.text-info {
  color: #17a2b8 !important;
}

.font-weight-bold {
  font-weight: 700 !important;
}

9. I refresh my page but the shopping bag and account are not showing within the navbar as expected. I consult Claude AI about this who advises that it may be that I am not passing the grand_total varaible into the template correctly through my views. I check and I do not have a grand_total variable created so need to update the view for shopping_bag as below and also import ShoppingBagItem at the top of the file:

    bag_items = ShoppingBagItem.objects.filter(user=request.user)
    grand_total = sum(item.product.from_price for item in bag_items)

    context = {
        'bag_items': bag_items,
        'grand_total': grand_total,
    }

- I also add the following content to my shoppingbag.html template file: 

<p class="my-0">
  {% if grand_total %}
  ${{ grand_total|floatformat:2 }}
  {% else %}
  $0.00
  {% endif %}
</p>

- And finally in the shoppingbag.models file add the below content:

from django.db import models
from django.contrib.auth.models import User
from merchandise.models import Product


class ShoppingBagItem(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.quantity} x {self.product.name}"

- I then run makemigrations and migrate to create the migration file and then migrate.

- However, it is still not showing the shopping bag and account in the navbar. I have consulted Claude AI about this who says I need to update shoppingbag/views to return the context dicitonary so I update it to do this:

    return render(request, 'shoppingbag/shoppingbag.html', context)

- However, still not seeing the shopping bag and account. I decide to test the Favicons in my index.html in a new div above the feedback form as below:

<div>
  <i class="fas fa-user"></i>
  <i class="fas fa-shopping-bag"></i>
</div>

- This is rendering fine so it is clearly an issue with the html code. Claude AI has rewritten the code as below:

{% load static %}

<nav class="navbar custom-navbar dark-bg shadow-sm">
  <div class="container-fluid">
    <div class="row w-100 align-items-center m-0">
      <div class="col-4 text-start small-auth-links">
        {% if user.is_authenticated %}
        <a class="auth-link" href="{% url 'account_logout' %}">Logout</a>
        {% else %}
        <a class="auth-link me-2" href="{% url 'account_signup' %}">Register</a>
        <a class="auth-link" href="{% url 'account_login' %}">Login</a>
        {% endif %}
      </div>

      <div class="col-4 text-center">
        <a class="navbar-brand m-0" href="{% url 'home' %}">
          <span class="navbar-heading d-none d-xl-inline">Working Out Gym</span>
          <img
            src="{% static 'images/favicon.png' %}"
            alt="Working Out Gym logo"
            class="mobile-logo d-inline d-xl-none"
          />
        </a>
      </div>

      <div class="col-4 text-end">
        <div class="d-flex justify-content-end align-items-center">
          <a class="{% if grand_total %}text-info font-weight-bold{% else %}text-black{% endif %} nav-link me-3" href="{% url 'view_shoppingbag' %}">
            <i class="fas fa-shopping-bag fa-lg"></i>
            {% if grand_total %}
            <span class="ms-2">${{ grand_total|floatformat:2 }}</span>
            {% else %}
            <span class="ms-2">£0.00</span>
            {% endif %}
          </a>

          <div class="dropdown">
            <a class="text-black nav-link" href="#" id="user-options" data-bs-toggle="dropdown" aria-haspopup="true"
              aria-expanded="false">
              <i class="fas fa-user fa-lg"></i>
              <span class="ms-2">My Account</span>
            </a>
            <div class="dropdown-menu dropdown-menu-end border-0" aria-labelledby="user-options">
              {% if request.user.is_authenticated %}
              {% if request.user.is_superuser %}
              <a href="" class="dropdown-item">Product Management</a>
              {% endif %}
              <a href="" class="dropdown-item">My Profile</a>
              <a href="{% url 'account_logout' %}" class="dropdown-item">Logout</a>
              {% else %}
              <a href="{% url 'account_signup' %}" class="dropdown-item">Register</a>
              <a href="{% url 'account_login' %}" class="dropdown-item">Login</a>
              {% endif %}
            </div>
          </div>

          <button
            class="navbar-toggler custom-toggler ms-3"
            type="button"
            data-bs-toggle="collapse"
            data-bs-target="#main-nav"
            aria-controls="main-nav"
            aria-expanded="false"
            aria-label="Toggle navigation">
            <i class="fas fa-bars"></i>
          </button>
        </div>
      </div>
    </div>

    <!-- Search bar -->
    <div class="navbar-search py-3">
      <div class="container">
        <form method="GET" action="{% url 'merchandise:products' %}">
          <div class="input-group w-100">
            <input class="form-control rounded-0" type="text" name="q" placeholder="Search our site" />
            {% if current_category %}
            <input type="hidden" name="category" value="{{ current_category }}">
            {% endif %}
            <button class="btn btn-dark rounded-0" type="submit">
              <i class="fas fa-search"></i>
            </button>
          </div>
        </form>
      </div>
    </div>

    <!-- Navbar Collapse -->
    <div class="collapse w-100" id="main-nav">
      <div class="nav-collapse-links py-3">
        <a class="menu-link" href="{% url 'home' %}">Home</a>
        <a class="menu-link" href="#">Fitness &amp; Nutrition Plans</a>
        <a class="menu-link" href="{% url 'discussionboard:post_list' %}">
          Discussion Board
        </a>

        <div class="menu-dropdown">
          <div class="menu-dropdown-header">
            <a class="menu-link menu-link-main" href="{% url 'merchandise:products' %}">
              Merchandise
            </a>

            <button
              class="menu-toggle-btn"
              type="button"
              data-bs-toggle="collapse"
              data-bs-target="#merchandise-submenu"
              aria-expanded="false"
              aria-controls="merchandise-submenu"
              aria-label="Toggle merchandise menu">
              <i class="fas fa-chevron-down"></i>
            </button>
          </div>

          <div class="collapse" id="merchandise-submenu">
            <!-- Merchandise Submenu Content -->
          </div>
        </div>
      </div>
    </div>
  </div>
</nav>

- This looks good now, however, I notice in mobile view it looks off:

![Shopping Bag and account mobile view skewiff](/static/images/shoppingbag/Screenshot%20mobile%20shopping%20bag%20and%20account.png)

- Claude AI recommends some css for mobile screen sizes I can use:

@media (max-width: 991.98px) {
  .navbar-collapse {
    padding-top: 1rem;
    padding-bottom: 1rem;
  }

  .nav-link i {
    font-size: 1.2rem;
  }

  .nav-link span {
    font-size: 0.9rem;
    padding-left: 0.5rem;
  }
}

- I update my styles so that they have !important in order to override any Bootstrap styles:

.navbar .nav-link,
.navbar .nav-link i,
.navbar .nav-link span {
  color: #ffffff !important;
  text-decoration: none !important;
}

- However, this hasn't changed anything. Claude AI suggests simplifying my style.css code so it is less messy which it does for me as below:

/* Variables */
:root {
  --font-heading: "Boldonse", system-ui;
  --font-body: "PT Serif", serif;
  --color-primary: #ffffff;
  --color-secondary: #d9d9d9;
  --color-dark: #3b3b3b;
  --color-info: #17a2b8;
}

/* Base Styles */
body {
  font-family: var(--font-body);
}

.heading {
  font-family: var(--font-heading);
  font-weight: 700;
  font-size: 3rem;
}

.brand {
  font-weight: 700;
  font-size: 1.4rem;
}

.thin {
  font-weight: 300;
}

.main-bg {
  background-color: var(--color-primary);
}

.dark-bg {
  background-color: var(--color-dark);
}

/* Navbar Styles */
.custom-navbar {
  background-color: var(--color-dark);
}

.navbar-heading {
  font-family: var(--font-heading);
  font-weight: 700;
  font-size: 2.2rem;
  color: var(--color-primary);
  margin: 0;
}

.navbar-brand {
  color: var(--color-primary) !important;
  text-decoration: none;
}

.auth-link {
  color: var(--color-primary);
  font-family: var(--font-heading);
  text-decoration: none;
  font-size: 0.8rem;
}

.auth-link:hover {
  color: var(--color-secondary);
}

.mobile-logo {
  height: 30px;
  width: auto;
  display: block;
  margin: 0 auto;
}

.custom-toggler {
  border: none;
  color: var(--color-primary);
  font-size: 1.2rem;
  padding: 0.25rem 0.5rem;
  background: transparent;
}

.custom-toggler:focus {
  box-shadow: none;
}

.nav-collapse-links {
  display: flex;
  flex-direction: column;
  align-items: center;
  text-align: center;
  padding-left: 1rem;
  padding-right: 1rem;
}

.menu-link {
  display: block;
  color: var(--color-primary);
  font-family: var(--font-heading);
  text-decoration: none;
  text-align: center;
  padding: 0.6rem 0;
  max-width: 280px;
  width: 100%;
}

.menu-link:hover {
  color: var(--color-secondary);
}

/* Navbar Search Styles */
.navbar-search {
  background-color: var(--color-dark);
  border-top: 1px solid rgba(255, 255, 255, 0.1);
}

.navbar-search .form-control {
  border: none;
}

.navbar-search .btn {
  border: none;
}

.navbar-search .form-control:focus {
  box-shadow: none;
}

/* Menu Dropdown Styles */
.menu-dropdown {
  width: 100%;
  max-width: 320px;
  text-align: center;
}

.menu-dropdown-header {
  display: flex;
  justify-content: center;
  align-items: center;
  gap: 0.5rem;
}

.menu-link-main {
  width: auto;
  margin: 0;
}

.menu-toggle-btn {
  background: transparent;
  border: none;
  color: var(--color-primary);
  font-size: 0.95rem;
  padding: 0;
}

.menu-toggle-btn:focus {
  box-shadow: none;
}

.submenu-panel {
  margin-top: 0.75rem;
  padding: 0.5rem 0;
}

.submenu-section {
  margin-bottom: 1.25rem;
}

.submenu-heading {
  color: var(--color-primary);
  font-family: var(--font-heading);
  font-size: 1.1rem;
  margin-bottom: 0.5rem;
}

.submenu-group-title {
  color: var(--color-secondary);
  font-weight: 700;
  margin: 0.5rem 0 0.2rem;
}

.submenu-link {
  display: block;
  color: var(--color-primary);
  text-decoration: none;
  padding: 0.25rem 0;
}

.submenu-link:hover {
  color: var(--color-secondary);
}

/* Homepage Styles */
.main-image {
  width: 100%;
  max-width: 950px;
  height: auto;
  display: block;
  margin: 0 auto;
}

.leading-p {
  font-size: 1.4rem;
  max-width: 75%;
}

/* Merchandise Styles */
a.category-badge > span.badge:hover {
  background: #212529 !important;
  color: #fff !important;
}

.text-black {
  color: #000 !important;
}

.btt-button {
  height: 42px;
  width: 42px;
  position: fixed;
  bottom: 10px;
  right: 10px;
}

.btt-link {
  cursor: pointer;
}

/* Shopping Bag Icon Styles */
.nav-link {
  color: var(--color-primary);
  text-decoration: none;
}

.nav-link:hover {
  color: var(--color-secondary);
}

.text-info {
  color: var(--color-info) !important;
}

.font-weight-bold {
  font-weight: 700 !important;
}

@media (max-width: 991.98px) {
  .navbar-collapse {
    padding-top: 1rem;
    padding-bottom: 1rem;
  }

  .nav-link i {
    font-size: 1.2rem;
  }

  .nav-link span {
    font-size: 0.9rem;
    padding-left: 0.5rem;
  }
}

- I update style.css with the tidied up version of my style.css and then run the below to remove the staticfiles so i can rerun the collection of them as I have had issues with this in the past:

Remove-Item -Recurse -Force staticfiles

- I then run:

python manage.py collectstatic 

- I then refresh my page to see if this has made any difference and it hasn't made the icons and text white but has moved the content over on mobile. I decide that I want the mobile and tablet views to show only the icons for the shopping bag and account:

![Shopping Bag and account mobile view](/static/images/shoppingbag/Screenshot%20mobile%20shopping%20bag%20and%20account.png)

- I consult Claude AI about the icons not being white and it suggests I use:

@media (max-width: 1199.98px) {
  .nav-link,
  .nav-link i {
    color: var(--color-primary) !important;
  }
}

- However, this code is already in style.css and not applying, Claude AI then suggests the following code to replace the above code with:

@media (max-width: 1199.98px) {
  .navbar .nav-link i.fa,
  .navbar .nav-link i.fas {
    color: var(--color-primary) !important;
  }
}

-  I update the css code and now the links are displaying white on both tablets and mobile, however, I still need to update the desktop view so add the below code in style.css in my navbar styles section:

.nav-link {
  color: var(--color-primary);
  text-decoration: none;
}

.nav-link i {
  color: var(--color-primary);
}

- The icons on the desktop page are now white, but the text is still black so I need to update this, Claude AI suggests using the following code:

@media (max-width: 1199.98px) {
  .navbar .nav-link,
  .navbar .nav-link i {
    color: var(--color-primary) !important;
  }
}

- However, this isn't working so i decide instead to apply the following class to my span where the 'Shopping Bag' and 'Account':

nav-link-text

- I then add the below code to css:

.nav-link-text {
  color: var(--color-primary);
}

- I refresh the page and now this is looking much better on desktop, tablet and mobile - i just want to move the icons to across from the search bar on mobile view.

- I notice that the text is too large on mobile view on the home page so ask Claude AI to create a new media query to set the text to a smaller size on the small screen, it provides the below:

@media (max-width: 767.98px) {
  .leading-p {
    font-size: 1.2rem;
  }
}

- This looks much better, I am just going to leave mobile view for now and address later.

- The link for the shopping bag works when clicked, so now I want to look at my shoppingbag.html template to make this more functional. I borrow Code Institute's code from Boutique Ado for this and tweak accordingly as per below:

{% block page_header %}
    <div class="container header-container">
        <div class="row">
            <div class="col"></div>
        </div>
    </div>
{% endblock %}

{% block content %}
    <div class="container mb-2">
        <div class="row">
            <div class="col">
                <hr>
                <h2 class="logo-font mb-4">Shopping Bag</h2>
                <hr>
            </div>
        </div>

        <div class="row">
            <div class="col">
                {% if bag_items %}
                    <div class="table-responsive rounded"></div>
                {% else %}
                    <p class="lead mb-5">Your bag is empty.</p>
                    <a href="{% url 'merchandise:products' %}" class="btn btn-outline-black rounded-0 btn-lg">
                        <span class="icon">
                            <i class="fas fa-chevron-left"></i>
                        </span>
                        <span class="text-uppercase">Keep Shopping</span>
                    </a>
                {% endif %}
            </div>
        </div>
{% endblock %}

- I update my page and can see this has given us a header for the page, a message to say the bag is empty and then a back to Merchandise button too:

![Shopping Bag Template created](/static/images/shoppingbag/Screenshot%20shoppingbag%20html%20new.png)

- I then commit my code before moving on to looking at adding functionality to the app so it tracks what items are held in the bag.


## Shopping Bag - Contexts

1. Next I am going to add some functionality to my Shopping Bag app so that it tracks the items in the bag. To start, I need to create a new file called contexts.py in the root of my shoppingbag app directory. Within the new file, I create a new function called bag_contents which takes the request as a parameter. This function will return a dictionary called context instead of a template; this is a context processor and its purpose is to make the dicitonary available to all templates across the entire application:

def bag_contents(request):

    context = {}

    return context

2. In order to make the context processor that I just set up available to the whole application, I then need to add it to the list of context processors in the templates variable in settings.py. In the TEMPLATES section within context_processors, I add:

                'bag.contexts.bag_contents',

- This means that anytime I need to access the bag contents in any templates within the app that they will be available without having to return them from multiple views across different apps.

3. Also in settings.py, I need to add two new variables that will calculate delivery costs. I add these at the very bottom of my settings file as below:

FREE_DELIVERY_THRESHOLD = 50
STANDARD_DELIVERY_PERCENTAGE = 10

4. Now I can update my contexts with the below code, borrowing and acknowledging this from Code Institute to save some time:
- bag_items is an empty list [] for the products to live in.
- total and product_count to allow for adding things to the bag - this is set to 0
- then there is an if statement which says if the total price spent is more than what FREE_DELIVERY_THRESHOLD variable is set to in settings.py which will entice customers more. If it less then it will be calculated by the total multipled by the STANDARD_DELIVERY_PERCENTAGE variable in settings.py
- the calculation is wrapped in the decimal function which is also imported at the top of the file with the settings file so it can see the delivery variables. This is because it is a financial transaction and using float is susceptible to rounding errors; this is the preferred option for money as its most accurate.
- then there is a statement which lets user know how much more they need to spend to get free delivery by created a variable called free_delivery_delta
- then there is an else statement which says if the total is equal to or greater than the threshold then it sets the delivery and free_delivery_delat to 0.
- then finally there is statement which calculates the grand_total from this by adding the delivery and total together. 
- then all these items are added into the context library


from decimal import Decimal
from django.conf import settings


    bag_items = []
    total = 0
    product_count = 0

    if total < settings.FREE_DELIVERY_THRESHOLD:
        delivery = total * Decimal(settings.STANDARD_DELIVERY_PERCENTAGE / 100)
        free_delivery_delta = settings.FREE_DELIVERY_THRESHOLD - total
    else:
        delivery = 0
        free_delivery_delta = 0
    
    grand_total = delivery + total
    
    context = {
        'bag_items': bag_items,
        'total': total,
        'product_count': product_count,
        'delivery': delivery,
        'free_delivery_delta': free_delivery_delta,
        'free_delivery_threshold': settings.FREE_DELIVERY_THRESHOLD,
        'grand_total': grand_total,
    }

- Now everything in the context will be available across every app on the website.

5. I refresh my dev server but I am getting a server 500 error so set debug to on and refresh and I am receiving the following error page:

![Shopping Bag no module bag error](/static/images/shoppingbag/Screenshot%20no%20module%20bag.png)

6. Going back to the code, I update the below in settings.py from:

                'bag.contexts.bag_contents',

To:

                'shoppingbag.contexts.bag_contents',

7. I refresh the dev server but I am now receiving an error about an indentation problem on line 6 in the contexts.py file, I look at contexts.py and realise the function has been removed when I have copied code over from Code Institute so add this back in and refresh:

def bag_contents(request):

8. My page is loading again after this last change and I am not seeing any errors in the terminal so I commit my changes and then I can start looking at the code for allowing users to add to their shopping bags.

---

## Shopping Bag - Adding Items to Bag

1. Next I want to give the user the functionality to add to the shopping bag so i start in my product_detail.html file in the merchandise app. Underneathe my '{{ product.vendor }} tag, I add the below form, borrowing the code from Code Institute's Boutique Ado. The first column uses the POST method to send information to the server about the product being added to the bag, therefore, we need to have the csrf token at the very top so that it uses Django's cross-site request forgery protection; as a security precaution, without this token Django won't allow you to submit the form. Then the form is split into a single form row with two columns. The first column contains an input group for quality input; allowing users to select how much of the product they want. Then the second column contains the submit button for the form and  a keep shopping button which takes the user back to merchandise pages. It also has a hidden input which uses request.path attribute to submit a field named redirect_URL which contains the current URL: 

        <form class="form" action="{% url 'add_to_bag' product.id %}" method="POST">
          {% csrf_token %}
          <div class="form-row">
            <div class="col-12">
              <p class="mt-3"><strong>Quantity:</strong></p>
                <div class="form-group w-50">
                  <div class="input-group">
                    <input class="form-control qty_input" type="number" name="quantity" value="1" min="1" max="99" data-item_id="{{ product.id }}" id="id_qty_{{ product.id }}">
                  </div>
                </div>
              </div>
              <div class="col-12">
                <a href="{% url 'products' %}" class="btn btn-outline-black rounded-0 mt-5">
                  <span class="icon">
                    <i class="fas fa-chevron-left"></i>
                  </span>
                  <span class="text-uppercase">Keep Shopping</span>
                </a>
                <input type="submit" class="btn btn-black rounded-0 text-uppercase mt-5" value="Add to Bag">
                </div>
                <input type="hidden" name="redirect_url" value="{{ request.path }}">
              </div>
         </form>

2. As part of this code, I have introduced a new class to the code 'btn-outline-black', borrowing the code from Code Institute again:

.btn-outline-black {
  background: white;
  color: black !important;
  border: 1px solid black;
}

.btn-outline-black:hover,
.btn-outline-black:active,
.btn-outline-black:focus {
  background: black;
  color: white !important;
}

3. I then run my dev server to see how this looks but I am receiving an error message when I try and access a product page:

![Product Detail add to bag error](/static/images/shoppingbag/Screenshot%20product%20detail%20add%20to%20bag%20not%20found.png)

4. I believe this is due to me having no views yet for the add_to_bag function so I move on to create this next to see if this then allows me to view the product detail pages again. In my shoppingbag.views file: 
- I create a new view called add_to_bag which takes in both parameter for request and product_id for whichever product user is adding to their bag. 
- It then gets the quantity from the form we created earlier using the request.POST.get method and is converted into an integer as it will come from the template as a string. 
- It then gets the redirect URL from the form so its knows where to redirect to once it is done. This uses a session allowing information to be stored until the Django server side and client side are done communicating; this is good practise for e-commerce stores as it allows the user to store contents of a bag while user browses the site and adds more items to be purchased.
- To allow the method to work, I then create a bag varaible which accesses the requests session and gets the variable if it already exists and initialises it to an empty dictionary if it doesn't. This checks if there's a bag variable in the session and if there isn't then it creates one.
- I then create a python dictionary which just has a key of the product_id and set it to equal to the quantity if the item is already in the bag and increment the quality accordingly. 
- Then it adds the bag variable into the session.
- At the top of the file, I import redirect so it can redirect the user back to the redirect URL.

def add_to_bag(request, product_id):
    """ A view to allow users to add products to shopping bag """

    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    bag = request.session.get('bag', {})

    if product_id in list(bag.keys()):
        bag[product_id] += quantity
    else:
        bag[product_id] = quantity

    request.session['bag'] = bag
    return redirect(redirect_url)

5. Now that my views are set up I can now create the URL. in shoppingbag.urls, I add the below path:

    path('add/<product_id>/', views.add_to_bag, name='add_to_bag'),

6. Then back in my product_detail template, I need to update the form action with the URL tag:

{% url 'add_to_bag' product.id %}

7. I then add code to print the shopping bag from the session in the add_to_bag view under the request.session to allow me to see the quantity and product_id in the console when products are being added.

print(request.session['bag'])

8. Now when I run my dev server, I can see product detail pages again and there is an 'Add to Bag' button on the page now, however, it is not serving the css styles on the button - I have seen this issue also on my deployed Heroku pages so I will take a look at this now before committing my code:

![Product Detail add to bag option now shows](/static/images/shoppingbag/Screenshot%20product%20details%20add%20to%20bag%20option%20now%20there.png)

9. I am going to try collectstatic and see if this resolves things first but it doesn't. I then try increasing the specificity on my css styles as below:

.btn.btn-black.rounded-0.text-uppercase.mt-5 {
    background-color: black;
    color: white !important;
    border-color: black;
}

.btn.btn-black.rounded-0.text-uppercase.mt-5:hover,
.btn.btn-black.rounded-0.text-uppercase.mt-5:active,
.btn.btn-black.rounded-0.text-uppercase.mt-5:focus {
    background-color: white;
    color: black !important;
    border-color: black;
}

- I reload the page and this works. I then change Debug to false, run a collectstatic and then commit my code to both Github and Heroku. 

10. I check my pages on Heroku and these are serving the styles now, I hadn't run collectstatic before last deployment to Heroku and now this is okay:

![Heroku styles working - add to bag showing](/static/images/shoppingbag/Screenshot%20add%20to%20bag%20showing%20on%20heroku%20with%20other%20styles.png)

11. If i run the console on my local dev server and try adding products then this shows in the console, proving the code is correct so far:

[19/Mar/2026 10:55:48] "GET /merchandise/13446/ HTTP/1.1" 200 32620
{'13446': 1}

---

## Shopping Bag - Making Contents Available to the Entire App

1. I now want to make the content of the Shopping Bag show across the whole platform, i.e. show total cost of the shopping bag in the navbar and render the products added in the shoppingbag.html template. To start, I go to my contexts.py and add the below code, following the same method as the add_to_bag view; getting it if it already exists or initialising it to an empty dictionary if it doesn't:

bag = request.session.get('bag'), {})

- Then, still in contexts below the new code just created, I create a for statement which says for each item and quantity in bag_items from the bag session I created earlier:
- First get the product
- Then add its quantity times the price to the total
- Then increment the product count by the quantity
- I then add a dictionary to the list of bag items containing the id, the quantity and the product object itself; to give access to all the other fields such as the product image and so on when iterating through the bag items in the templates.
- I import the product model and the get_object_404 shortcut at the top of the file.

from django.shortcuts import get_object_or_404
from merchandise.models import Product

    for product_id, quantity in bag.items():
        product = get_object_or_404(Product, pk=product_id)
        total += quantity = product.from_price
        product_count += quantity
        bag_items.append({
            'product_id': product_id,
            'quantity': quantity,
            'product': product,
        })

2. Now that the context processor is saved, I go to the shoppingbag.html template to render the bag item. To prove it is working I add the below code into the if bag_items div:

                    <div class="table-responsive rounded">
                        {{ bag_items }}
                    </div>

3. I restart my dev server and add some items to the shopping bag and then check the shopping bag to see how this looks but I am getting a server 500 error as soon as I try to access the home page. I turn debug on to see what is happening. I can see in my terminal the below error message:

  File "C:\Users\leila\OneDrive\Desktop\Documents\vscode-projects\working_out_gym\shoppingbag\contexts.py", line 16
    total += quantity = product.from_price
                      ^
SyntaxError: invalid syntax

- I update this line to: 
total += (quantity * product.from_price)

- I stop and start my server but I am now seeing the same error but for product.from_price. I look at my models.py file and believe I know what the issue is now, I need to be using the product_variants model to obtain the price so update the code so that the for loop now retrieves ProductVariant and the total then uses the product_variant.price instead of product.price, I import the ProductVariant model as well as the Product model from Merchandise app now:

    for product_id, quantity in bag.items():
        product = get_object_or_404(Product, pk=product_id)
        product_variant = get_object_or_404(ProductVariant, product=product)
        total += (quantity * product_variant.price)
        product_count += quantity
        bag_items.append({
            'product_id': product_id,
            'quantity': quantity,
            'product': product,
            'product_variant': product_variant,
        })

4. Now when I restart the server and access the page, I am seeing the following error message:

![MultipleObjectsReturned error ProductVariant](/static/images/shoppingbag/Screenshot%20multipleobjectsreturned%20error.png)

5. I consult Claude AI about the error who advises that the get_object_or_404 method must be returning multiple ProductVariant objects for a single Product object and to resolve this so change my code from:

product_variant = get_object_or_404(ProductVariant, product=product)

To:

product_variant = get_object_or_404(ProductVariant, product=product, sku=bag[product_id])

- This will utilise the sku field from the bag dicitionary to identify the correct ProductVariant object for the product in the shopping bag.

6. I refresh my page again and I am presented with yet another error:

![Page not Found](/static/images/shoppingbag/Screenshot%202page%20not%20found.png)

7. I consult Claude AI again who advises that the issue is that my add_to_bag function view is not using the ProductVariant model to add the product to the shopping bag. Instead it is using the custom ShoppingBagItem model. I need to update my ShoppingBagItem model to reference the Product and ProductVariant models like below and import ProductVariant at the top after Product:

from django.db import models
from django.contrib.auth.models import User
from merchandise.models import Product, ProductVariant

class ShoppingBagItem(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    product_variant = models.ForeignKey(ProductVariant, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f"{self.quantity} x {self.product.title} - {self.product_variant.variant_title}"

- I then need to update my add_to_bag view so that it works with my updated model:

from django.shortcuts import render, redirect, get_object_or_404
from merchandise.models import Product, ProductVariant
from .models import ShoppingBagItem

def add_to_bag(request, product_id):
    """ A view to allow users to add products to shopping bag """
    product = get_object_or_404(Product, pk=product_id)
    product_variant_sku = request.POST.get('product_variant_sku')
    product_variant = get_object_or_404(ProductVariant, product=product, sku=product_variant_sku)
    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')

    bag_item, created = ShoppingBagItem.objects.get_or_create(
        user=request.user,
        product=product,
        product_variant=product_variant,
        defaults={'quantity': quantity}
    )

    if not created:
        bag_item.quantity += quantity
        bag_item.save()

    return redirect(redirect_url)

- I refresh the page to see if this has worked but I am still seeing the same error message. I consult Claude AI again who advises it is an issue with the way I am trying to access the shopping bag contents in my view_shoppingbag function and recommends updating my view to the below:

from django.shortcuts import render
from .models import ShoppingBagItem

def view_shoppingbag(request):
    """ A view to show the shopping bag contents """
    bag_items = ShoppingBagItem.objects.filter(user=request.user)
    grand_total = sum(item.product_variant.price * item.quantity for item in bag_items)

    context = {
        'bag_items': bag_items,
        'grand_total': grand_total,
    }

    return render(request, 'shoppingbag/shoppingbag.html', context)

- I update this but I am still receiving the same error message. If I add /shoppingbag to my URL: then I get the below error message:

![ShoppingBag programming error](/static/images/shoppingbag/Screenshot%20prograamingerror.png)

- I consult Claude AI again and they advise that I have updated the ShoppingBagItems model to include the ProductVariant model but then not migrated the database to a new field. I stop my dev server and then run the following code:

python manage.py makemigrations shoppingbag

- This returns the following because the { product_variant } is a non-nullable field and I am trying to add it to the existing ShoppingBagItem model but there are already existing rows in the database that don't have a value for this field:

It is impossible to add a non-nullable field 'product_variant' to shoppingbagitem without specifying a default. This is because the database needs something to populate existing rows.
Please select a fix:
 1) Provide a one-off default now (will be set on all existing rows with a null value for this column)
 2) Quit and manually define a default value in models.py.

 - I cancel this as Claude AI says I will need to update my code to create a suitable default value first. I am going to use a calculated default value for the product_variant field. I update my ShoppingBagItem model as below:

 from django.db import models
from django.contrib.auth.models import User
from merchandise.models import Product, ProductVariant

def get_default_product_variant(product):
    return product.productvariant_set.first()

class ShoppingBagItem(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    product_variant = models.ForeignKey(ProductVariant, on_delete=models.CASCADE, default=get_default_product_variant)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f"{self.quantity} x {self.product.title} - {self.product_variant.variant_title}"

- I save and then run the makemigrations cmd again which runs successfully. I then run migrate but notice this message at the bottom of my terminal:

TypeError: get_default_product_variant() missing 1 required positional argument: 'product'

- I ask Claude AI about it and it saus that the get_default_product_variant has been defined incorrectly in my ShoppingBagItem model. The default value for a ForeignKey field needs to be a callable that takes no arguments but my function expects a 'product' argument. In order to fix this, I need to use a lambda function or partial function to wrap the function in and make compatible with the default value requirement. I can do this by importing the below at the top of the file:

from functools import partial

- I run makemigrations again and I am seeing a number of errors so I take my code in models.py back to: 

from django.db import models
from django.contrib.auth.models import User
from merchandise.models import Product, ProductVariant

class ShoppingBagItem(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    product_variant = models.ForeignKey(ProductVariant, on_delete=models.CASCADE, default=1)  # Replace 1 with a valid ID
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f"{self.quantity} x {self.product.title} - {self.product_variant.variant_title}"

- I then delete the migrations files in shoppingbag/migrations and then run makemigrations again which has now ran successfully. I then run migrate which also runs successfully.

- I decide to consulkt ChatGPT as I am struggling to resolve the issues now and Calude AI has made too many changes to what I wanted to originally do. ChatGPT recommends deleting the ShoppingBagItems completely from shoppingbag/models and the import for it in shoppingbag/views. I do this and then run makemigrations and migrate which complete successfully.

- ChatGPT advises that I update my shoppingbag/contexts.py file to:

from decimal import Decimal
from django.conf import settings
from django.shortcuts import get_object_or_404
from merchandise.models import Product

def bag_contents(request):
    bag_items = []
    total = 0
    product_count = 0
    bag = request.session.get('bag', {})

    for product_id, quantity in bag.items():
        product = get_object_or_404(Product, pk=product_id)

        total += quantity * (product.variants.first().price if product.variants.exists() else 0)
        product_count += quantity

        bag_items.append({
            'product_id': product_id,
            'quantity': quantity,
            'product': product,
        })

    if total < settings.FREE_DELIVERY_THRESHOLD:
        delivery = total * Decimal(settings.STANDARD_DELIVERY_PERCENTAGE / 100)
        free_delivery_delta = settings.FREE_DELIVERY_THRESHOLD - total
    else:
        delivery = 0
        free_delivery_delta = 0

    grand_total = total + delivery

    return {
        'bag_items': bag_items,
        'total': total,
        'product_count': product_count,
        'delivery': delivery,
        'free_delivery_delta': free_delivery_delta,
        'free_delivery_threshold': settings.FREE_DELIVERY_THRESHOLD,
        'grand_total': grand_total,
    }

- It then recommends that I update my shoppingbag/views to:

from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from merchandise.models import Product

def view_bag(request):
    return render(request, 'shoppingbag/shoppingbag.html')


def add_to_bag(request, product_id):
    product = get_object_or_404(Product, pk=product_id)

    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')

    bag = request.session.get('bag', {})

    if product_id in bag:
        bag[product_id] += quantity
        messages.success(request, f'Updated {product.title} quantity')
    else:
        bag[product_id] = quantity
        messages.success(request, f'Added {product.title} to your bag')

    request.session['bag'] = bag

    return redirect(redirect_url)


def adjust_bag(request, product_id):
    quantity = int(request.POST.get('quantity'))
    bag = request.session.get('bag', {})

    if quantity > 0:
        bag[product_id] = quantity
    else:
        bag.pop(product_id)

    request.session['bag'] = bag
    return redirect(reverse('view_shoppingbag'))


def remove_from_bag(request, product_id):
    bag = request.session.get('bag', {})

    bag.pop(product_id, None)

    request.session['bag'] = bag
    return redirect(reverse('view_shoppingbag'))

- Then I update my shoppingbag/urls.py file to:

from django.urls import path
from . import views

urlpatterns = [
    path('', views.view_bag, name='view_shoppingbag'),
    path('add/<int:product_id>/', views.add_to_bag, name='add_to_bag'),
    path('adjust/<int:product_id>/', views.adjust_bag, name='adjust_bag'),
    path('remove/<int:product_id>/', views.remove_from_bag, name='remove_from_bag'),
]

- Then in my product_detail.html file, I remove this line:

name="product_variant_sku" and update the form to:

      <form action="{% url 'add_to_bag' product.id %}" method="POST">
        {% csrf_token %}
        <input type="number" name="quantity" value="1" min="1" max="99">
        <input type="hidden" name="redirect_url" value="{{ request.path }}">
        <input type="submit" value="Add to Bag">
      </form>

- Then finally, I update my shoppingbag.html if bag_items statement with:

      {% if bag_items %} {% for item in bag_items %}
      <p>{{ item.product.title }} - {{ item.quantity }}</p>
      {% endfor %}

      <p>Total: £{{ total }}</p>
      <p>Delivery: £{{ delivery }}</p>
      <p><strong>Grand Total: £{{ grand_total }}</strong></p>

      {% else %}
      <p>Your bag is empty.</p>
      {% endif %}
    </div>
  </div>
  {% endblock %}

- I have refreshed the page and can now see my page again and it looks like it has added the item to the shopping bag too:

![Page loading again](/static/images/shoppingbag/Screenshot%20webpage%20loading%20again.png)

- If I look in the bag, I can see the name of the product that I added:

![Contents in shopping bag](/static/images/shoppingbag/Screenshot%20contents%20showing%20in%20shopping%20%20bag.png)

8. I now want to update my shopping bag so that it now renders out the list of items in the bag using five columns, containing the product image, some info about it, the per-item price, the quantity and subtotal for that item and each row will be a new item. I have made a table with a header row and the second header is blank as product info will span two columns. The other three will contain the price, the quantity and the subtotal. Then in the table body I will iterate through each item in the shopping and create a row for each one. Then finally in the last two rows i am using the variables I created for the total of the delivery charges, the grand total and the delivery_delta:

 <div class="table-responsive rounded">
            <table class="table table-sm table-borderless">
                <thead class="text-black">
                    <tr>
                        <th scope="col">Product Info</th>
                        <th scope="col"></th>
                        <th scope="col">Price</th>
                        <th scope="col">Qty</th>
                        <th scope="col">Subtotal</th>
                    </tr>
                </thead>     
                {% for item in bag_items %}
                    <tr>
                        <td class="p-3 w-25">
                            <img class="img-fluid rounded" src="{{ item.product.image.url }}">
                        </td>
                        <td class="py-3">
                            <p class="my-0"><strong>{{ item.product.name }}</strong></p>
                            <p class="my-0 small text-muted">SKU: {{ item.product.sku|upper }}</p>
                        </td>
                        <td class="py-3">
                            <p class="my-0">${{ item.product.price }}</p>
                        </td>
                        <td class="py-3 w-25">
                            <p class="my-0">{{ item.quantity }}</p>
                        </td>
                        <td class="py-3">
                            <p class="my-0">${{ item.product.price }}</p>
                        </td>
                    </tr>
                {% endfor %}
                <tr>
                    <td colspan="5" class="pt-5 text-right">
                        <h6><strong>Bag Total: ${{ total|floatformat:2 }}</strong></h6>
                        <h6>Delivery: ${{ delivery|floatformat:2 }}</h6>
                        <h4 class="mt-4"><strong>Grand Total: ${{ grand_total|floatformat:2 }}</strong></h4>
                        {% if free_delivery_delta > 0 %}
                            <p class="mb-1 text-danger">
                                You could get free delivery by spending just <strong>${{ free_delivery_delta }}</strong> more!
                            </p>
                            {% endif %}
                        </td>
                    </tr>
                    <tr>
                        <td colspan="5" class="text-right">
                            <a href="{% url 'merchandise:products' %}" class="btn btn-outline-black rounded-0 btn-lg">
                                <span class="icon">
                                    <i class="fas fa-chevron-left"></i>
                                </span>
                                <span class="text-uppercase">Keep Shopping</span>
                            </a>
                            <a href="" class="btn btn-black rounded-0 btn-lg">
                                <span class="text-uppercase">Secure Checkout</span>
                                <span class="icon">
                                    <i class="fas fa-lock"></i>
                                </span>
                            </a>
                        </td>
                    </tr>
            </table>

- However, when I run this it looks like this, not in a table and not showing product image, name or info:

![Product name, image and info not showing in shoppingbag.html](/static/images/shoppingbag/Screenshot%20contents%20showing%20in%20shopping%20%20bag.png)

- I ask ChatGPT why the table is not rendering and it advises that Django is rendering the page but not passing any context at all because bag_items doesn't exist so the {% for item in bag_items %} never runs correctly. To resolve, I need to update my view_bag function view as below:

def view_bag(request):
    bag = request.session.get('bag', {})
    bag_items = []
    total = 0

    for product_id, quantity in bag.items():
        product = get_object_or_404(Product, pk=product_id)
        subtotal = quantity * product.price
        total += subtotal

        bag_items.append({
            'product': product,
            'quantity': quantity,
            'subtotal': subtotal,
        })

    delivery = 3 if total > 0 else 0
    grand_total = total + delivery

    context = {
        'bag_items': bag_items,
        'total': total,
        'delivery': delivery,
        'grand_total': grand_total,
    }

    return render(request, 'shoppingbag/shoppingbag.html', context)

- It also recommends that I update some of the code in shoppingbag.html so it renders correctly. I need to change the below to fix my template subtotal from:

${{ item.product.price }}

To:

${{ item.subtotal|floatformat:2 }}

- I also need to fix my currency formatting from:

${{ item.product.price }}

To:

£{{ item.product.price|floatformat:2 }}

- And apply image safety:

{% if item.product.image %}
    <img class="img-fluid rounded" src="{{ item.product.image.url }}">
{% endif %}

- I save the code and rerun the server but I am receiving the following error:

AttributeError at /shoppingbag/
'Product' object has no attribute 'price'

- This is because my Products model doesn't have a price field, ProductVariant does. ChatGPT advises me to update the following code in my view_bag view from:

subtotal = quantity * product.price

To:

variant = product.variants.first()

if not variant:
    continue  # skip if no price available

subtotal = quantity * variant.price
total += subtotal

- I also need to update my template to use the correct field names so update this now to change any dollar signs to pound signs before tags where they have been missed. I update my image tag to that of the one being used in the Product model. I update product.name to product.title, fix the price column so it uses the correct item.price:

        <table class="table table-sm table-borderless">
          <thead class="text-black">
            <tr>
              <th scope="col">Product Info</th>
              <th scope="col"></th>
              <th scope="col">Price</th>
              <th scope="col">Qty</th>
              <th scope="col">Subtotal</th>
            </tr>
          </thead>
          {% for item in bag_items %}
          <tr>
            <td class="p-3 w-25">
              {% if item.product.image_src %}
              <img
                class="img-fluid rounded"
                src="{{ item.product.image_src }}"
              />
              {% endif %}
            </td>
            <td class="py-3">
              <p class="my-0"><strong>{{ item.product.title }}</strong></p>
              <p class="my-0 small text-muted">
                SKU: {{ item.sku }}
              </p>
            </td>
            <td class="py-3">
              <p class="my-0">£{{ item.price|floatformat:2 }}</p>
            </td>
            <td class="py-3 w-25">
              <p class="my-0">{{ item.quantity }}</p>
            </td>
            <td class="py-3">
              <p class="my-0">£{{ item.subtotal|floatformat:2 }}</p>
            </td>
          </tr>
          {% endfor %}
          <tr>
            <td colspan="5" class="pt-5 text-right">
              <h6><strong>Bag Total: £{{ total|floatformat:2 }}</strong></h6>
              <h6>Delivery: £{{ delivery|floatformat:2 }}</h6>
              <h4 class="mt-4">
                <strong>Grand Total: £{{ grand_total|floatformat:2 }}</strong>
              </h4>
              {% if free_delivery_delta > 0 %}
              <p class="mb-1 text-danger">
                You could get free delivery by spending just
                <strong>${{ free_delivery_delta }}</strong> more!
              </p>
              {% endif %}
            </td>
          </tr>
          <tr>
            <td colspan="5" class="text-right">
              <a
                href="{% url 'merchandise:products' %}"
                class="btn btn-outline-black rounded-0 btn-lg"
              >
                <span class="icon">
                  <i class="fas fa-chevron-left"></i>
                </span>
                <span class="text-uppercase">Keep Shopping</span>
              </a>
              <a href="" class="btn btn-black rounded-0 btn-lg">
                <span class="text-uppercase">Secure Checkout</span>
                <span class="icon">
                  <i class="fas fa-lock"></i>
                </span>
              </a>
            </td>
          </tr>
        </table>

9. The shopping bag looks much better and as I expected it to look with the new updates

![Shopping bag contents displaying correctly](/static/images/shoppingbag/Screenshot%20shoppingbag%20looking%20as%20it%20should.png)

10. I commit my changes and push them to Github and Heroku after running a collectstatic. 

---

## Shopping Bag - Size Options for Clothing

1. I now want to give users the option to select different sizes if they are purchasing clothing from the site. I go to my merchandise.models file and add a new field to the Product model as below, this is a BooleanField which will be false by default and allowed to be blank both in the database and in forms rather than having to implement different sizes for every product in the database. As this is not an official commercial e-commerce site, I am just going to mimic the functionality, the same as Code Institute, by simply describing if the object has different sizes available and then give user the choice of some generic sizes to be added to their item details in the bag

has_sizes = models.BooleanField(default=False, null=True, blank=True)

2. After updating the Product model, I then need to run makemigrations and migrate which run successfully.

3. Next I want to set the has_size field to true on all clothing products using the manage.py shell cmd:

python manage.py shell

4. I then run the below to import the Product model from the Merchandise app:

from merchandise.models import Product

5. Next I create a variable which holds all of the non-clothing categories:

kdbb = ['bags', 'accessories', 'bottles', 'womens bags', 'headwear', 'womens headwear', 'misc', 'womens accessories', 'bag', 'thirft bag', 'equipment', 'gift card']

6. Then I can use the built in exclude method to get all products whose category name is not in that list which will effectively give all of the clothing categories:

clothes = Product.objects.exclude(category__name__in=kdbb)

7. Then if I run the below it will show me how many products I am setting the size on, which is 7427:

clothes.count()

8. Now all I need to do is write a simple for loop that will iterate through the query set and set the has_size field to true and then save the product, hitting enter twice to execute:

for item in clothes:
item.has_sizes = True
item.save()

9. To confirm it has worked, I run the below cmd in the terminal which will filter on only those which have sizes available:

Product.objects.filter(has_sizes=True)

10. This has worked as I can see in my terminal only products from clothing categories being returned. I can run the below code to see a count of this, which is 6985. This looks like this has correctly only ran on clothing categories as only a small amount of products are not clothing so numbers look right:

Product.objects.filter(has_sizes=True).count()

11. I exit the shell with exit function:

exit()

12. Now I want to add a size selector box to my product_detail template. I am going to borrow Cide Institute's Boutique Ado code, creating a with statement under my quantity selector with the product.has_sizes variable assigned to it that only appears if the product has_sizes assigned to its category. It also uses their options as string values keeping code clean and straight forward:

        <div class="form-row">
            {% with product.has_sizes as s %}
            {% if s %}
                <div class="col-12">
                    <p><strong>Size:</strong></p>
                    <select class="form-control rounded-0 w-50" name="product_size" id='id_product_size'>
                        <option value="xs">XS</option>
                        <option value="s">S</option>
                        <option value="m" selected>M</option>
                        <option value="l">L</option>
                        <option value="xl">XL</option>
                    </select>
                </div>
            {% endif %}
            {% endwith %}

13. I save this and when I refresh the product detail page of an item, I can now see size being shown:

![Product Details clothing size](/static/images/shoppingbag/Screenshot%20clothing%20size.png)

14. This won't let us actually select a size yet, I now want to add the size to the product info on the shoppingbag template. I am going to borrow Code Institute's code for this and add between the name and SKU ID:

<p class="my-0"><strong>Size: </strong>{% if item.product.has_sizes %}{{ item.size|upper }}{% else %}N/A{% endif %}</p>

15. I go to the shoppingbag to see how this looks and can see the 'size' field is there waiting to be populated:

![Shopping Bag Size Field](/static/images/shoppingbag/Screenshot%20size%20in%20shopping%20bag.png)

16. I run collectstatic and then commit my code to Github and Heroku.

---

## Shopping Bag - Size Update for Context Processor and Add_To_Bag View

1. I now need to update my add_to_bag view so that it can handle the new code for size. I add the below code under the redirect_url in add_to_bag view:

    size = None
    if 'product_size' in request.POST:
        size = request.POST['size']

2. Then still in the add_to_bag view, I add the below code under the bag variable. This code allows the bags to have a single item ID for each item but track multiple sizes of the same item:

   if size:
        if item_id in list(bag.keys()):
            if size in bag[item_id]['items_by_size'].keys():
                bag[item_id]['items_by_size'][size] += quantity
            else:
                bag[item_id]['items_by_size'][size] = quantity
        else:
            bag[item_id] = {'items_by_size': {size: quantity}}

3. I then wrap the original code in an else block so if there is no size then this logic is applied:

else:
        if product_id in bag:
            bag[product_id] += quantity
            messages.success(request, f'Updated {product.title} quantity')
        else:
            bag[product_id] = quantity
            messages.success(request, f'Added {product.title} to your bag')

4. Next I need to update the context.py file and update all of the references of 'quantity', barring the one for the key in my dictionary, to item_data as there is now the possibility of there being two different types of data in our bag items and in the case of an item with no size, it will just be the quantity.

- I update this from:

def bag_contents(request):
    bag_items = []
    total = 0
    product_count = 0
    bag = request.session.get('bag', {})

    for product_id, quantity in bag.items():
        product = get_object_or_404(Product, pk=product_id)

        total += quantity * (product.variants.first().price if product.variants.exists() else 0)
        product_count += quantity

        bag_items.append({
            'product_id': product_id,
            'quantity': quantity,
            'product': product,
        })

    if total < settings.FREE_DELIVERY_THRESHOLD:
        delivery = total * Decimal(settings.STANDARD_DELIVERY_PERCENTAGE / 100)
        free_delivery_delta = settings.FREE_DELIVERY_THRESHOLD - total
    else:
        delivery = 0
        free_delivery_delta = 0

    grand_total = total + delivery

    return {
        'bag_items': bag_items,
        'total': total,
        'product_count': product_count,
        'delivery': delivery,
        'free_delivery_delta': free_delivery_delta,
        'free_delivery_threshold': settings.FREE_DELIVERY_THRESHOLD,
        'grand_total': grand_total,
    }

To:

def bag_contents(request):
    bag_items = []
    total = 0
    product_count = 0
    bag = request.session.get('bag', {})

    for product_id, item_data in bag.items():
        product = get_object_or_404(Product, pk=product_id)

        total += item_data * (product.variants.first().price if product.variants.exists() else 0)
        product_count += item_data

        bag_items.append({
            'product_id': product_id,
            'quantity': item_data,
            'product': product,
        })

    if total < settings.FREE_DELIVERY_THRESHOLD:
        delivery = total * Decimal(settings.STANDARD_DELIVERY_PERCENTAGE / 100)
        free_delivery_delta = settings.FREE_DELIVERY_THRESHOLD - total
    else:
        delivery = 0
        free_delivery_delta = 0

    grand_total = total + delivery

    return {
        'bag_items': bag_items,
        'total': total,
        'product_count': product_count,
        'delivery': delivery,
        'free_delivery_delta': free_delivery_delta,
        'free_delivery_threshold': settings.FREE_DELIVERY_THRESHOLD,
        'grand_total': grand_total,
    }

5. I only want to execute this code if the item has no sizes, which can be done by checking whether or not the item data is an integer and if it is an integer then we know the item data is just the quantity. Otherwise we will know its a dictionary and needs handling differently. To do this I will iterate through the inner dictionary of items_by_size incrementing the product count and total accordingly. Then for each of the items, it will add the size to the bag items returned to the template as well. I update the def bag_contents in contexts.py as below:

    for product_id, item_data in bag.items():
        if isinstance(item_data, int):
            product = get_object_or_404(Product, pk=product_id)

            total += item_data * (product.variants.first().price if product.variants.exists() else 0)
            product_count += item_data

            bag_items.append({
                'product_id': product_id,
                'quantity': item_data,
                'product': product,
            })
        else:
            product = get_object_or_404(Product, pk=product_id)
            for size, quantity in item_data['items_by_size'].items()
                total += quantity * product.price
                product_count += quantity
                bag_items.append({
                    'product_id': product_id,
                    'quantity': item_data,
                    'product': product,
                    'size' : size,
                })

6. Then in the shoppingbag.html I want to render this out temporarily just to see how the code looks and is structured before implementing something more permanent. To do this, I udpate the code with the below, adding above my table for the product info:

      {% if bag_items %}
        {{ bag_items }}
        <br>
        <br>
        {{ request.session.bag }}

7. I restart my server to see how the new code is looking:

![Shopping Bag showing new html after context update](/static/images/shoppingbag/Screenshot%20new%20html%20shopping%20bag%20contexts.png)

8. I am going to now delete the session data to empty the shopping bag without having to close the browser. To do this, I inspect the page, go to the 'Application Tab', open up the 'Cookies' folder under that and then delete the 'sessionid':

![Delete sessionid](/static/images/shoppingbag/Screenshot%20delete%20sessionid.png)

9. Now when I refresh, I can see the bag is now empty:

![Empty Bag Contents](/static/images/shoppingbag/Screenshot%20emptied%20bag%20contents%20after%20deleted%20sessionid.png)

10. I am going to now try an add an item of clothing with the size of medium to the bag but when I do so I receive the following error:

![MultiValue DictKeyError](/static/images/shoppingbag/Screenshot%20MultiValueDictLeyError.png)

11. In my shopping bag views, I update the code below from:

size = request.POST['size']

To:

size = request.POST['product_size']

12. I refresh the page but encounter another error:

NameError at /shoppingbag/add/7954/
name 'item_id' is not defined

13. I update my code in views so that it uses product_id rather than item_id as this is the field which my dataset uses:

    if size:
        if product_id in list(bag.keys()):
            if size in bag[product_id]['items_by_size'].keys():
                bag[product_id]['items_by_size'][size] += quantity
            else:
                bag[product_id]['items_by_size'][size] = quantity
        else:
            bag[product_id] = {'items_by_size': {size: quantity}}    
    else:
        if product_id in bag:
            bag[product_id] += quantity
            messages.success(request, f'Updated {product.title} quantity')
        else:
            bag[product_id] = quantity
            messages.success(request, f'Added {product.title} to your bag')

14. I refresh the page again but this time receive yet another error:

AttributeError at /merchandise/7954/
'Product' object has no attribute 'price'

15. I go to my contexts.py file and update the offending line of code to use ProductVariant.price as this is where price is set on my models, I also import ProductVariant at the top of the file:

total += quantity * ProductVariant.price

16. However, this then gives the following error:

TypeError at /merchandise/7954/
unsupported operand type(s) for *: 'int' and 'DeferredAttribute'
Request Method:	GET
Request URL:	http://127.0.0.1:8000/merchandise/7954/
Django Version:	6.0.2
Exception Type:	TypeError
Exception Value:	
unsupported operand type(s) for *: 'int' and 'DeferredAttribute'
Exception Location:	C:\Users\leila\OneDrive\Desktop\Documents\vscode-projects\working_out_gym\shoppingbag\contexts.py, line 28, in bag_contents

17. I consult ChatGPT about this, who advises that ProductVariant.price is not a value, its a model field definition so I need to get a real variant instance and then access its price using the below code:

            for size, quantity in item_data['items_by_size'].items():
                    variant = product.variants.first()
                    price = variant.price if variant else 0
                    total += quantity * price
                    product_count += quantity
                    bag_items.append({
                        'product_id': product_id,
                        'quantity': item_data,
                        'product': product,
                        'size' : size,
                        'price' : price,
                    })

- It also recommends updating this code in shoppingbag/views:

size = request.POST['product_size']

to:

size = request.POST.get('product_size')

- This stops the code crashing if no size is selected.

18. I refresh the server and can see the product again so try to add to bag again but this time receive the following error message:

TypeError at /shoppingbag/add/7954/
'method' object is not subscriptable
Request Method:	POST
Request URL:	http://127.0.0.1:8000/shoppingbag/add/7954/
Django Version:	6.0.2
Exception Type:	TypeError
Exception Value:	
'method' object is not subscriptable
Exception Location:	C:\Users\leila\OneDrive\Desktop\Documents\vscode-projects\working_out_gym\shoppingbag\views.py, line 49, in add_to_bag

19. ChatGPT advises that I have the wrong parantheses around my product_size and to update to:

request.POST.get('product_size')

20. I update and refresh the server and can finally add the item to my bag. Going to add the same item in 2 x different sizes to the bag and some items with no sizes. However, when I click on an item which shouldn't have a size, it has a size so I consult ChatGPT about this who advises that the category names in the database don't exactly match the strings in kdbb, Django is doing an exact match with:

category__name__in=kdbb

- It recommends I do a reset and redo of setting my variable against the categories. But first it recommends running the below cmd in shell to determine what the actual category names are:

Product.objects.values_list('category__name', flat=True).distinct()

- I run this and it returns the below:

<QuerySet [None, 'Womens Crop Top', 'Mens Pullovers', 'Mens Drop Armhole Tank', 'Womens T-Shirt', 'Womens Bottoms', 'Mens Leggings', 'Mens Shorts', 'Gift Card', 'Misc.', 'Mens Ss Tops', 'Mens Long Sleeve Top', 'Bag', 'Womens Swimwear', 'Womens Shorts', 'Womens', 'Pullovers', 'Mens Stringer', 'womens Shorts', 'Womens Jackets', '...(remaining elements truncated)...']>

- ChatGPT advises that as my categories are not clean or consistent that I will have issues with the mixed casing and different naming styles.

- I then run this cmd in the shell to get the full correct list of categories:

categories = list(Product.objects.values_list('category__name', flat=True).distinct())
print(len(categories))

Womens Crop Top
Mens Pullovers
Mens Drop Armhole Tank
Womens T-Shirt
Womens Bottoms
Mens Leggings
Mens Shorts
Gift Card
Misc.
Mens Ss Tops
Mens Long Sleeve Top
Bag
Womens Swimwear
Womens Shorts
Womens
Pullovers
Mens Stringer
womens Shorts
Womens Jackets
Womens Socks
Womens Tank
Womens Vest
Mens Bottoms
Womens Tanks
Womens One Pieces
Womens swe
Mens Sleeveless Tops
Womens Ls Tops
Womens Leggings
Mens Swimwear
mens Ss Tops
Mens Pullover
Mens Jackets / Outerwear
Bags
Mens Sweater
Ss Tops
Mens Ls Tops
footwear
Mens Sleeveless T-Shirt
Mens Hoodie
Mens Jackets
womens Bags
Womens Ss Tops
Bottles
Thirft Bag
womens Accessories
Underwear
womens Headwear
Womens Crop Tops
Womens tank
Mens Baselayer
Pants
mens unisex Pullovers
Mens Pants
Womens Hoodie
Accessories
Footwear
Mens Tank
Mens t
mens unisex Bottoms
Mens Shirt
Mens Underwear
Womens Pullovers
Womens Sports Bras
Womens Skort
Mens T-Shirt
Womens Sweater
Headwear
Mens Tops
Womens Jacket
Womens Jackets / Outerwear
Womens Long Sleeve Top
mens T-Shirt
Womens Sports Bra
Womens Pullover
Womens Hoodies and Jackets
Womens Dress
Womens Hoodies
Womens Bodysuit
Womens Sleeveless Top
Mens Outerwear
Equipment
Womens Sleeveless Tops
Mens Jacket
unisex Pants
womens Socks
Socks
Womens One Piece
Womens Underwear
Mens Joggers
Womens Pants

- ChatGOT recommends that I run the following in shell, using exclusions on non_clothing instead:

from django.db.models import Q
from merchandise.models import Product

non_clothing = [
    'gift card', 'misc.', 'bag', 'bags', 'bottles',
    'thirft bag', 'accessories', 'headwear',
    'equipment', 'footwear', 'socks'
]

reset
Product.objects.update(has_sizes=False)

build filter (case insensitive)
non_clothing_filter = Q()
for item in non_clothing:
    non_clothing_filter |= Q(category__name__icontains=item)

apply
Product.objects.exclude(non_clothing_filter).update(has_sizes=True)

21. I restart my server now and can see it has removed sizes off of the non-clothing items:

![Non clothing items size removed](/static/images/shoppingbag/Screenshot%20non%20clothing%20size%20removed.png)

22. I then consult ChatGPT about the issue of me not being able to add two items of the same product but in different sizes to the bag. It advises that the bag is sometimes stored like:

{ "123": 2 }   ❌ (no sizes)

or:

{ "123": { "items_by_size": { "m": 1 } } }   ✅

23. It recommends enforcing one structure for sized products by replacing my add_to_bag view logic:

- I replace the 'size = None' with > size = request.POST.get('product_size')

- Replace the current if size statement with the below code:

    if size:
        # Ensure product exists as dict
        if product_id in bag:
            if isinstance(bag[product_id], dict):
                # already has sizes
                if size in bag[product_id]['items_by_size']:
                    bag[product_id]['items_by_size'][size] += quantity
                else:
                    bag[product_id]['items_by_size'][size] = quantity
            else:
                # was previously added WITHOUT size → convert it
                bag[product_id] = {
                    'items_by_size': {
                        size: quantity
                    }
                }
        else:
            bag[product_id] = {
                'items_by_size': {
                    size: quantity
                }
            }

        messages.success(request, f'Added {product.title} (size {size.upper()}) to your bag')

    else:
        # No sizes
        if product_id in bag:
            if isinstance(bag[product_id], int):
                bag[product_id] += quantity
            else:
                # edge case: product previously had sizes
                bag[product_id] = quantity
        else:
            bag[product_id] = quantity

        messages.success(request, f'Added {product.title} to your bag')

    request.session['bag'] = bag
    return redirect(redirect_url)

- ChatGPT advises that this will work better as it handles all cases: add same size again, add different size, previously added without size and no size product.

- I delete my sessionid in Devtools and restart the dev server to test that the code is working okay. I add an item in two different sizes and see the message appear to say it has added this but the shopping cart price doesn't increase after adding the second item so i click the shopping cart and it is giving me this error:

TypeError at /shoppingbag/
unsupported operand type(s) for *: 'dict' and 'decimal.Decimal'
Request Method:	GET
Request URL:	http://127.0.0.1:8000/shoppingbag/
Django Version:	6.0.2
Exception Type:	TypeError
Exception Value:	
unsupported operand type(s) for *: 'dict' and 'decimal.Decimal'
Exception Location:	C:\Users\leila\OneDrive\Desktop\Documents\vscode-projects\working_out_gym\shoppingbag\views.py, line 20, in view_bag
Raised during:	shoppingbag.views.view_bag

- I consult ChatGPT about why this would be as it has been introduced with the latest code we have added together. ChatGPT recommends updating the bag_contents in shoppingbag/contexts.py to a pattern which handles both sized and non-sized items as below:

from decimal import Decimal
from django.conf import settings
from django.shortcuts import get_object_or_404
from merchandise.models import Product

def bag_contents(request):
    bag_items = []
    total = 0
    product_count = 0
    bag = request.session.get('bag', {})

    for product_id, item_data in bag.items():
        product = get_object_or_404(Product, pk=product_id)

        if isinstance(item_data, int):
            # Non-sized product
            quantity = item_data
            total += quantity * (product.variants.first().price if product.variants.exists() else 0)
            product_count += quantity

            bag_items.append({
                'product_id': product_id,
                'quantity': quantity,
                'product': product,
            })

        else:
            # Product with sizes
            for size, quantity in item_data['items_by_size'].items():
                price = product.variants.first().price if product.variants.exists() else 0
                total += quantity * price
                product_count += quantity

                bag_items.append({
                    'product_id': product_id,
                    'quantity': quantity,
                    'product': product,
                    'size': size,
                })

    # Delivery calculations
    if total < settings.FREE_DELIVERY_THRESHOLD:
        delivery = total * Decimal(settings.STANDARD_DELIVERY_PERCENTAGE / 100)
        free_delivery_delta = settings.FREE_DELIVERY_THRESHOLD - total
    else:
        delivery = 0
        free_delivery_delta = 0

    grand_total = total + delivery

    return {
        'bag_items': bag_items,
        'total': total,
        'product_count': product_count,
        'delivery': delivery,
        'free_delivery_delta': free_delivery_delta,
        'free_delivery_threshold': settings.FREE_DELIVERY_THRESHOLD,
        'grand_total': grand_total,
    }

- I delete my sessionid from devtools and restart the server but the issue is the same. ChatGOT advsies I need to update my views.py file to get the totals from the context function using:

from django.shortcuts import render
from .contexts import bag_contents

def view_bag(request):
    """
    A view that renders the shopping bag page
    """
    context = bag_contents(request)  # get all totals, items, etc.
    return render(request, 'shoppingbag/shoppingbag.html', context)

- I can now get back into the shopping bag, but it seems that the second item i add override the first and I can only see the item in the large size. I consult ChatGPT again who advises that there is likely an issue in the add_to_bag view so takes a look and advises that the product_id is being stored as a string and not an integer whereas Django sessions keys are always strings. So my if product_id in bag: check can fail if product_id is an int (from get_object_or_404) but keys in bag are strings. This means each new addition creates a new entry instead of updating the existing one, and your dict overwrites prior sizes incorrectly. It advises that I should update my add_to_bag view as below:

def add_to_bag(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    quantity = int(request.POST.get('quantity', 1))
    redirect_url = request.POST.get('redirect_url', '/')
    size = request.POST.get('product_size')

    # session keys must be string
    product_id = str(product_id)

    bag = request.session.get('bag', {})

    if size:
        # Ensure the product exists as a dict for sizes
        if product_id in bag:
            if isinstance(bag[product_id], dict):
                # Already has sizes
                bag[product_id]['items_by_size'][size] = bag[product_id]['items_by_size'].get(size, 0) + quantity
            else:
                # Previously added without size → convert it
                bag[product_id] = {'items_by_size': {size: quantity}}
        else:
            # First time adding this product
            bag[product_id] = {'items_by_size': {size: quantity}}

        messages.success(request, f'Added {product.title} (size {size.upper()}) to your bag')

    else:
        # Non-sized products
        if product_id in bag and isinstance(bag[product_id], int):
            bag[product_id] += quantity
        else:
            bag[product_id] = quantity

        messages.success(request, f'Added {product.title} to your bag')

    request.session['bag'] = bag
    return redirect(redirect_url)

- I delete my sessionid and then restart the dev server and test and can see this is now working:

![Adding items in mutliple sizes](/static/images/shoppingbag/Screenshot%20add%20items%20in%20multiple%20sizes%20working.png)

24. I copy the session variable which is displayed above the items in my shopping bag into jsonformatter.org so I can better see the data structure.

{'7954': {'items_by_size': {'m': 1, 'l': 1}}}

25. As my code is working now, I remove the ugly rendered items above from my code and then set Debug to false, collectstatic and then commit to Github and Heroku.

26. Before moving on, I notice that the price of each item is not showing in the shopping bag or the subtotals on the prices (if there is the same item in same size added twice, etc.) ChatGOT recommends updating bag_contents to include price and subtotal as it doesn't currently:
- I update the total to use Decimal('0.00') instead of 0
- I add the subtotal and total calculations into the if isinstance statement:

        if isinstance(item_data, int):
            # Non-sized product
            quantity = item_data
            price = product.variants.first().price if product.variants.exists() else Decimal('0.00')
            subtotal = quantity * price
            total += subtotal
            product_count += quantity

- I update the for size statement to include the subtotal and total calculations

            for size, quantity in item_data['items_by_size'].items():
                price = product.variants.first().price if product.variants.exists() else Decimal('0.00')
                subtotal = quantity * price
                total += subtotal
                product_count += quantity

- I include them in the bag_items lists.

27. I delete the sessionid in devtools and restart the server and test and can now see the subtotals and price of each item in the shopping bag:

![Price and subtotal showing in shopping bag](/static/images/shoppingbag/Screenshot%20price%20and%20subtotals%20now%20calculated%20and%20showing%20in%20shopping%20bag.png)

28. I commit my code again and move on.

---

## Shopping Bag - Quantity Selector Javascript

1. I am now going to add some buttons to the quantity selector on the product details. In the product_details template, I am going to use the built-in input group append and input group prepend classes from Bootstrap with some buttons that use the appropriate Font Awesome icons. I consult ChatGPT on how best to do this and ask for some guidance on restyling the Size and Quantity layout on Product Details, it provides me the below code which I update:

<form action="{% url 'add_to_bag' product.id %}" method="POST">
    {% csrf_token %}

    <!-- Size + Quantity row -->
    <div class="d-flex align-items-end flex-wrap mb-3">
        <!-- Size selector -->
        {% with product.has_sizes as s %}
        {% if s %}
            <div class="me-2 mb-2" style="min-width: 100px;">
                <label for="id_product_size" class="form-label"><strong>Size:</strong></label>
                <select class="form-control form-control-sm rounded-0" name="product_size" id="id_product_size">
                    <option value="xs">XS</option>
                    <option value="s">S</option>
                    <option value="m" selected>M</option>
                    <option value="l">L</option>
                    <option value="xl">XL</option>
                </select>
            </div>
        {% endif %}
        {% endwith %}

        <!-- Quantity selector -->
        <div class="me-2 mb-2">
            <label for="id_qty_{{ product.id }}" class="form-label d-block"><strong>Quantity:</strong></label>
            <div class="input-group input-group-sm" style="width: 120px;">
                <button type="button" class="decrement-qty btn btn-black rounded-0"
                    data-item_id="{{ product.id }}" id="decrement-qty_{{ product.id }}">
                    <span class="icon"><i class="fas fa-minus"></i></span>
                </button>
                <input class="form-control text-center qty_input" type="number" name="quantity" value="1"
                    min="1" max="99" data-item_id="{{ product.id }}" id="id_qty_{{ product.id }}">
                <button type="button" class="increment-qty btn btn-black rounded-0"
                    data-item_id="{{ product.id }}" id="increment-qty_{{ product.id }}">
                    <span class="icon"><i class="fas fa-plus"></i></span>
                </button>
            </div>
        </div>
    </div>

    <!-- Add to Bag row -->
    <div class="mb-3">
        <input type="submit" value="Add to Bag" class="btn btn-black rounded-0">
    </div>

    <input type="hidden" name="redirect_url" value="{{ request.path }}">
</form>

2. This looks good but the button styles don't appear to be applying to the buttons on quantity and Add to Bag:

![Button styles not applying in details](/static/images/shoppingbag/Screenshot%20buttons%20styles%20not%20applying%20details.png)

3. I run a collectstatic and hard reload the page and add the following styles to css:

.btn-black {
    background-color: #000;
    color: #fff;
    border: none;
}

.btn-black:hover {
    background-color: #222;
    color: #fff;
}

4. It looks much better now:

![Button styles applied product details](/static/images/shoppingbag/Screenshot%20product%20details%20button%20classes%20working.png)

5. Next I can look at adding my Javascript so that my quantity selector buttons will work. First I am going to create an 'includes' directory in my merchandise/templates directory and then create a file in there called quantity_input_script.html. I am then going to borrow Code Institute's html to populate the new html file with, as below. This says that on the click event of the increment quantity button, that first we'll want to prevent the default button action and then find the closest input box. The closest method here searches up to the Dom and the find method searches down.
This tells code that from the button element go up the tree to the closest input group class. Then it drills down to find the first element with the class quantity input. Then it just caches the value that's currently in it in a variable called currentValue. And then uses that variable to set the input boxes new value to the current value plus one:

<script type="text/javascript">
    // Disable +/- buttons outside 1-99 range
    function handleEnableDisable(itemId) {
        var currentValue = parseInt($(`#id_qty_${itemId}`).val());
        var minusDisabled = currentValue < 2;
        var plusDisabled = currentValue > 98;
        $(`#decrement-qty_${itemId}`).prop('disabled', minusDisabled);
        $(`#increment-qty_${itemId}`).prop('disabled', plusDisabled);
    }

    // Ensure proper enabling/disabling of all inputs on page load
    var allQtyInputs = $('.qty_input');
    for(var i = 0; i < allQtyInputs.length; i++){
        var itemId = $(allQtyInputs[i]).data('item_id');
        handleEnableDisable(itemId);
    }

    // Check enable/disable every time the input is changed
    $('.qty_input').change(function() {
        var itemId = $(this).data('item_id');
        handleEnableDisable(itemId);
    });

    // Increment quantity
    $('.increment-qty').click(function(e) {
       e.preventDefault();
       var closestInput = $(this).closest('.input-group').find('.qty_input')[0];
       var currentValue = parseInt($(closestInput).val());
       $(closestInput).val(currentValue + 1);
       var itemId = $(this).data('item_id');
       handleEnableDisable(itemId);
    });
    
    // Decrement quantity
    $('.decrement-qty').click(function(e) {
       e.preventDefault();
       var closestInput = $(this).closest('.input-group').find('.qty_input')[0];
       var currentValue = parseInt($(closestInput).val());
       $(closestInput).val(currentValue - 1);
       var itemId = $(this).data('item_id');
       handleEnableDisable(itemId);
    });
</script>

6. I then include this in the product_details template:

{% block postloadjs %}
{{ block.super }}
{% include 'merchandise/includes/quantity_input_script.html' %}
{% endblock %}

7. I run collectstatic and hard reload the page and can now see that the quantity selector buttons are working. I commit my code and move on.

8. I have the quantity selector buttons showing on my shoppingbag.html but the buttons will not work until the javascript is applied, I paste the below code into the bottom of my shoppingbag.html file and then reload to confirm this has worked, which it has:

{% block postloadjs %}
{{ block.super }}
{% include 'merchandise/includes/quantity_input_script.html' %}
{% endblock %}

9. Now when I reload the page, I can see this is working:

![Button styles applied product details](/static/images/shoppingbag/Screenshot%20shoppingbag%20quantity%20selector%20buttons%20working.png)

10. I now need to make it possible for the user to update the form when they have updated the quantity. To do this I will borrow Code Institute's code from Boutique Ado, creating two anchor elements under the form in my shoppingbag.html: one for updating the quantity which submits the form and the other for removing it from my bag entirely. They will use a data attribute similar to the data item id on the buttons so it can discern which specific item the customer is removing:

<a class="update-link text-info"><small>Update</small></a>
<a class="remove-item text-danger float-right" id="remove_{{ item.product_id }}" data-size="{{ item.size }}"><small>Remove</small></a>

11. I then copy and paste the Javascript from Boutique Ado which will handle the clcik events of the two elements within the html. I paste this into the post loadjs block in the bottom of the file:

- On the click event of the update link, it uses the previous method to find the most recently seen update form in the Dom then stores the form in a variable and then calls the forms submit method.

- The remove link is more complex but still uses the click event to be handled - the intention will be to post some data to a URL which I will create later. Once the response comes back from the server then it reloads the page to reflect the changes in the bag. The csrf token is used as post method is in use and provides security we need. It is stored as a string and uses the actual template variable as opposed to the template tag; this is because the former renders the token while the latter renders a hidden input field in a form. Then itemid and size of item to be used. The item id can be obtained by splitting the id of the update link being clicked on at the underscore and taking the second half of it. The entire first part of the string remove_ has been used to be explicit about what is being split. To get the size, again using the data method to pull it from the data size attribute. Finally, two more variables: A URL which will be bag/remove/ the itemId - this is a template literal; the url will be created later.Then I need dataw which is the object I'll use to send this data to the server. The data variable will contain a special key called CSRF middleware token which will have our variable as its value and it'll contain the size. The CSRF middleware token key will match the field Django is expecting to see in request.post when I post it to the server. To do that it's as simple as using the post method from jQuery giving it both the URL and the data. And finally a function will execute to reload the page.

    // Update quantity on click
    $('.update-link').click(function(e) {
        var form = $(this).prev('.update-form');
        form.submit();
    })

    // Remove item and reload on click
    $('.remove-item').click(function(e) {
        var csrfToken = "{{ csrf_token }}";
        var itemId = $(this).attr('id').split('remove_')[1];
        var size = $(this).data('size');
        var url = `/bag/remove/${itemId}`;
        var data = {'csrfmiddlewaretoken': csrfToken, 'size': size};
        $.post(url, data)
         .done(function() {
             location.reload();
         });
    })
</script>

12. I refresh my page to see how this is looking. I can see a number of issues. The size is showing as the template literal rather than the size it is on products in the bag, the update and remove buttons are not clickable and there is a django tagline for the script showing outside of where it should be so it is displaying as text on the page:

![Button styles applied product details](/static/images/shoppingbag/Screenshot%20shoppingbag%20quantity%20selector%20buttons%20working.png)

- I start with the {% include 'merchandise/includes/quantity_input_script.html' %} showing in the rendered template and have a look at my code and realise I have stripped out the javascript. I update the file again as below:

{% block postloadjs %} 
{{ block.super }} 
{% include 'merchandise/includes/quantity_input_script.html' %}
<script type="text/javascript">

    // Update quantity on click
    $('.update-link').click(function(e) {
        var form = $(this).prev('.update-form');
        form.submit();
    })

    // Remove item and reload on click
    $('.remove-item').click(function(e) {
        var csrfToken = "{{ csrf_token }}";
        var itemId = $(this).attr('id').split('remove_')[1];
        var size = $(this).data('size');
        var url = `/bag/remove/${itemId}`;
        var data = {'csrfmiddlewaretoken': csrfToken, 'size': size};
        $.post(url, data)
         .done(function() {
             location.reload();
         });
    })
</script>
{% endblock %}

13. Now when I refresh I can click the quantity button and then click update, although this fails to change the quantity so I need to look at why this isn't working. It has removed the random Django tag from the bottom now though. I look next to make my mouse into a pointer when hovered over 'update' or 'delete'. I add the below styles into style.css to do thisand refreshing the page shows this has worked.

.update-link,
.remove-item {
    cursor: pointer;
}

14. I consult ChatGPT about the other two issues, as to why quantity updates don't stay intact and why the size isn't displaying and showing {{ item.size|upper }} on all clothing items. It advises that there is no product variable in scope in the shoppingbag.html file and I am using the following code:

{% with product.has_sizes as s %}

- I need to update this to the below as I am using the item.product variable in this loop:

{% with item.product.has_sizes as s %}

- I also fix the spacing of my display line for size too and refresh the shoppingbag to see if this has resolved the issue with size being incorrectly shown:

![Shopping Bag Clothing Size showing](/static/images/shoppingbag/Screenshot%20size%20showing%20again%20clothing.png)

15. I then work with ChatGPT on why the update click isn't working and it recommends creating a view for update_bag in shoppingbag/views. I add this now:

from django.shortcuts import redirect
from django.contrib import messages

def update_bag(request, item_id):
    quantity = int(request.POST.get('quantity'))
    size = request.POST.get('product_size')
    bag = request.session.get('bag', {})

    if size:
        if item_id in bag and 'items_by_size' in bag[item_id]:
            if quantity > 0:
                bag[item_id]['items_by_size'][size] = quantity
            else:
                del bag[item_id]['items_by_size'][size]

                if not bag[item_id]['items_by_size']:
                    del bag[item_id]
    else:
        if quantity > 0:
            bag[item_id] = quantity
        else:
            del bag[item_id]

    request.session['bag'] = bag
    messages.success(request, "Bag updated")

    return redirect('view_bag')

- I then add the below url path for the new view to my shoppingbag/urls file:

path('update/<item_id>/', views.update_bag, name='update_bag'),

- Next, I fix my form by providing it the url for the new update_bag view:

              <form class="form update-form" method="POST" action="{% url 'update_bag' item.product_id %}">

- Next, I fix the input values on my html for value="1", as this is always "1" this is why it resets so I need to set it to:

value="{{ item.quantity }}"

- It also recommends updating thbe size selection code so that you have to pre-select the current size, I update this now to:

<select name="product_size" class="form-control form-control-sm rounded-0">
    <option value="xs" {% if item.size == 'xs' %}selected{% endif %}>XS</option>
    <option value="s" {% if item.size == 's' %}selected{% endif %}>S</option>
    <option value="m" {% if item.size == 'm' %}selected{% endif %}>M</option>
    <option value="l" {% if item.size == 'l' %}selected{% endif %}>L</option>
    <option value="xl" {% if item.size == 'xl' %}selected{% endif %}>XL</option>
</select>

16. The shopping bag looks much better upon a refresh now, however, when I try to update the quantity I am taken to an error page:

NoReverseMatch at /shoppingbag/update/9984/
Reverse for 'view_bag' not found. 'view_bag' is not a valid view function or pattern name.
Request Method:	POST
Request URL:	http://127.0.0.1:8000/shoppingbag/update/9984/
Django Version:	6.0.2
Exception Type:	NoReverseMatch

- Looking at the new update_bag view it uses the below code, whereas the convention I have followed is to have (appname:view) so I update the code below from:

    return redirect('view_bag')

To: 

return redirect('shoppingbag:view_bag')

- However, when I reload the page it still isn't rendering and gives me this error:

NoReverseMatch at /shoppingbag/update/9984/
'shoppingbag' is not a registered namespace

- I check shoppingbag/urls and realise I haven't set shoppingbag as the app name so do this now:

app_name = "shoppingbag"

- I also update my url for the new path:

path('', views.view_bag, name='view_bag'),

- I refresh the page but I am receiving another error now:

NoReverseMatch at /shoppingbag/
Reverse for 'view_shoppingbag' not found. 'view_shoppingbag' is not a valid view function or pattern name.

- I find the offending line:

<a class="{% if grand_total %}text-info font-weight-bold{% else %}text-black{% endif %} nav-link me-3" href="{% url 'view_shoppingbag' %}">

- And update the url to:

{% url 'shoppingbag:view_bag' %}

- This error is removed and replaced by another error:

NoReverseMatch at /shoppingbag/
Reverse for 'update_bag' not found. 'update_bag' is not a valid view function or pattern name.

- I go to the offending line in shoppingbag.html and change from:

<form class="form update-form" method="POST" action="{% url 'update_bag' item.product_id %}">

To:

<form class="form update-form" method="POST" action="{% url 'shoppingbag:update_bag' item.product_id %}">

17. Now finally when I refresh my page, I can see that the quantity has updated and is retained in the code as should be so I will turn Debug off, collectstatic and deploy to Git and Heroku:

![Shopping Bag Clothing Size showing](/static/images/shoppingbag/Screenshot%20product%20updating%20in%20shopping%20bag%20working.png)

18. I have noticed that the remove button is not working, when clicked it is not removing the products from the shopping bag, so i turn debug mode on and inspect it in devtools console to see what is happening. I have the following error message:

Failed to load resource: the server responded with a status of 404 (Not Found)   bag/remove/9984:1

- I first check my views in the shoppingbag app and see that i have the below set for removing items from the shopping bag:

def remove_from_bag(request, product_id):
    bag = request.session.get('bag', {})

    bag.pop(product_id, None)

    request.session['bag'] = bag
    return redirect(reverse('view_shoppingbag'))

- I then check what I have set up for the app urls:

    path('remove/<int:product_id>/', views.remove_from_bag, name='remove_from_bag'),

- I cannot see any obvious issues so consult ChatGPT who advises that at the moment, my remove_from_bag view is only doing the below function:

bag.pop(product_id, None)

- This removes the whole product while my frontend is sending a size too using:

var size = $(this).data('size');
var data = {'csrfmiddlewaretoken': csrfToken, 'size': size};

- So on my sized products, I am never removing the specific size which breaks things. So I need to update my remove_from_bag view to handle the sizes:

def remove_from_bag(request, product_id):
    try:
        bag = request.session.get('bag', {})
        size = request.POST.get('size')

        if size:
            # Remove specific size
            if product_id in bag and 'items_by_size' in bag[product_id]:
                del bag[product_id]['items_by_size'][size]

                # If no sizes left, remove product entirely
                if not bag[product_id]['items_by_size']:
                    bag.pop(product_id)
        else:
            # Remove whole product
            bag.pop(product_id, None)

        request.session['bag'] = bag
        return redirect(reverse('shoppingbag:view_bag'))

    except Exception as e:
        messages.error(request, 'Error removing item')
        return redirect(reverse('shoppingbag:view_bag'))

19. ChatGPT also notices a bug in my javascript code - it was missing the trailing slash as was used in my url path for the remove_bag function but is also fragile because it is using hardcoded urls so ChatGPT recommends updating this so it uses the more robust Django tag instead so it won't matter if the url changes now:

var url = "{% url 'shoppingbag:remove_from_bag' 0 %}".replace('0', itemId);

20. I refresh my dev server and empty cache and hard reload the page but the remove button is still not doing anything. I can see a number of errors in my terminal as below but no errors in the devtool console anymore:

[21/Mar/2026 14:00:32] "POST /shoppingbag/remove/9984/ HTTP/1.1" 302 0
[21/Mar/2026 14:00:33] "GET /shoppingbag/ HTTP/1.1" 200 30179
[21/Mar/2026 14:00:33] "POST /shoppingbag/remove/9984/ HTTP/1.1" 302 0
[21/Mar/2026 14:00:33] "GET /shoppingbag/ HTTP/1.1" 200 30179
[21/Mar/2026 14:00:34,556] - Broken pipe from ('127.0.0.1', 62398)
Not Found: /.well-known/appspecific/com.chrome.devtools.json

21. I consult ChatGPT about this who advises that this statement shows that the request is now hitting the view correctly, so the routing and javascript are now correct:

POST /shoppingbag/remove/9984/ 302

- The issue is that my remove_from_bag view is using:

if product_id in bag:

- But in my add_to_bag view I am using:

product_id = str(product_id)

- So the session keys look like this:

bag = {
    "9984": {...}   # STRING
}

- Whereas my Django URL passes:

product_id = 9984  # INT

- So this statement fails silently as it will always be false:

if product_id in bag:

- To resolve this, I need to convert the product_id to a string in the remove_from_bag view and also in the adjust_bag view. I start with the remove_from_bag view and update this to:

def remove_from_bag(request, product_id):
    try:
        bag = request.session.get('bag', {})
        product_id = str(product_id) 
        size = request.POST.get('size')

        if size:
            if product_id in bag and 'items_by_size' in bag[product_id]:
                del bag[product_id]['items_by_size'][size]

                if not bag[product_id]['items_by_size']:
                    bag.pop(product_id)
        else:
            bag.pop(product_id, None)

        request.session['bag'] = bag
        return redirect(reverse('shoppingbag:view_bag'))

    except Exception as e:
        messages.error(request, 'Error removing item')
        return redirect(reverse('shoppingbag:view_bag'))

- Then in adjust_bag I update the code from: bag[product_id] = quantity
To: product_id = str(product_id)

- And finally in update_bag from: if item_id in bag:
To:

- This now converts the product_id to a string in each of my views so it can be used in the session.

22. Now when I test, the code for both updating and removing items from the shopping bag is working as expected so I commit my code and move on.

---

##  Toasts

1. I now want to add messages to my webapp so that users have an informative and ineractive experience. I am going to do this using the Toasts feature from Bootstrap. To start with, I add a subfolder to the main templates folder under the 'includes' subfolder called 'toasts':

![Toasts Template Folder Creation](/static/images/toasts/Screenshot%20toasts%20template%20folder%20creation.png)

2. Then I create four html files within this called toast_sucess.html, toast_warning.html, toast_error.html and toast_info.html. I then populate these with the code from Code Institute's same files. These are straight from Bootstrap apart from the custom-toast class. e.g. the toast_success.html file:

<div class="toast custom-toast rounded-0 border-top 0" data-autohide="false">
    <div class="arrow-up arrow-success"></div>
    <div class="w-100 toast-capper bg-success"></div>
    <div class="toast-header bg-white text-dark">
        <strong class="mr-auto">Success!</strong>
        <button type="button" class="ml-2 mb-1 close text-dark" data-dismiss="toast" aria-label="Close">
            <span aria-hidden="true">&times;</span>
        </button>
    </div>
    <div class="toast-body bg-white">
        {{ message }}
    </div>
</div>

3. Once I have my Toasts templates created, I then need to add these to the messages container in base.html. I find the container in my template and remove the below:

      <div class="container mt-3">
        {% for message in messages %}
      <div class="alert alert-{{ message.tags }} alert-dismissible fade show" role="alert">
        {{ message }}
        <button type="button" class="btn-close" data-bs-dismiss="alert" aria-label="Close"></button>
      </div>
      {% endfor %}
      </div>

- And then I replace it with the code for my new Toasts method:

      <div class="message-container mt-3">
      {% for message in message %}
          {% include 'includes/toasts/toast_success.html' %}
      {% endfor %}
      </div>

4. Next I need to update my base.html to use the Bootstrap Javascript to show the toast, this is done in the postload js script block in the base.html, I replace the current content with the below so that it calls the toast method from Bootstrap with an option to show on any elements with the toast class. By putting this in the base.html, it ensures that every page that loads will immediately call the show option on all toasts that have been rendered in the messages container:

  <script type="text/javascript">
    $('.toast').toast('show');
  </script>

5. I then update my settings file with the below so it will store messages in the session.

MESSAGE_STORAGE = 'django.contrib.messages.storage.session.SessionStorage'

6. Finally before testing the new messages using the Toasts method on my website, I update css - borrowing from Code Institute:

/* ------------------------------- bootstrap toasts */

.message-container {
    position: fixed;
    top: 72px;
    right: 15px;
    z-index: 99999999999;
}

.custom-toast {
    overflow: visible;
}

.toast-capper {
    height: 2px;
}

7. I hard refresh the page but it fails to show me the toasts message when I try adding an item with no size to the cart. I consult ChatGPT about this who advises that the error I am seeing in the devtools console below:

Uncaught ReferenceError: $ is not defined

- Means that jQuery is not loaded but my code is using: $('.toast').toast('show');
And: $('.remove-item').click(...)
So my Javascript is failing silently, Bootstrap Toast never runs and the clcik handlers also break.

- It advises that I update base.html as below so it uses jQuery then Bootstrap and then executes the scripts for Toast:

<!-- jQuery FIRST -->
<script src="https://code.jquery.com/jquery-3.6.0.min.js"></script>

<!-- Then Bootstrap JS -->
<script src="https://cdn.jsdelivr.net/npm/bootstrap@4.6.2/dist/js/bootstrap.min.js"></script>

<!-- Then your scripts -->
<script>
    $('.toast').toast('show');
</script>

- It also spots a typo in my template loop, I am using '{% for message in message %}' but it should be {% for message in messages %} - without this the messages won't render at all, so I update this now in base.html

- It also advises that I am always loading success toast which ignores message types and to updatye my includes tag to the below so it looks at all the new templates I have created. I update the for loop in base.html now:

{% for message in messages %}
    {% if message.level == DEFAULT_MESSAGE_LEVELS.SUCCESS %}
        {% include 'includes/toasts/toast_success.html' %}
    {% elif message.level == DEFAULT_MESSAGE_LEVELS.ERROR %}
        {% include 'includes/toasts/toast_error.html' %}
    {% elif message.level == DEFAULT_MESSAGE_LEVELS.WARNING %}
        {% include 'includes/toasts/toast_warning.html' %}
    {% else %}
        {% include 'includes/toasts/toast_info.html' %}
    {% endif %}
{% endfor %}

8. Now when I refresh the page I can see the success message:

![Success Toast message](/static/images/toasts/Screenshot%20success%20message%20showing.png)

9. I commit my code ready for adding further functionality to Toast success.

10. The next thing I want to do is improve the Toasts function further. To start, I am going to update my add_to_bag view so that when quantity or sizes is changed then the user receives a Toast message advising them. To do this I add to the two below statements to the appropriate fields in my if statement in add_to_bag view:

    if size:
        # Ensure the product exists as a dict for sizes
        if product_id in bag:
            if isinstance(bag[product_id], dict):
                # Already has sizes
                bag[product_id]['items_by_size'][size] = bag[product_id]['items_by_size'].get(size, 0) + quantity
                messages.success(request, f'Updated size {size.upper()} {product.title} quantity to {bag[product_id]["items_by_size"][size]}')
            else:
                # Previously added without size → convert it
                bag[product_id] = {'items_by_size': {size: quantity}}
                messages.success(request, f'Added size {size.upper()} {product.title} to your bag')
        else:
            # First time adding this product
            bag[product_id] = {'items_by_size': {size: quantity}}

        messages.success(request, f'Added {product.title} (size {size.upper()}) to your bag')

    else:
        # Non-sized products
        if product_id in bag and isinstance(bag[product_id], int):
            bag[product_id] += quantity
            messages.success(request, f'Updated {product.name} quantity to {bag[item_id]}')
        else:
            bag[product_id] = quantity
            messages.success(request, f'Added {product.name} to your bag')

11. Next I look at my adjust_bag view in the same file and look to update the code I have here so it will now use Toast messages, ChatGPT helps me create this. I update the adjust_bag view from:

def adjust_bag(request, product_id):
    quantity = int(request.POST.get('quantity'))
    bag = request.session.get('bag', {})

    if quantity > 0:
        product_id = str(product_id)
    else:
        bag.pop(product_id)

    request.session['bag'] = bag
    return redirect(reverse('view_shoppingbag'))

To:

def adjust_bag(request, product_id):
    """Adjust the quantity of the specified product"""

    product = get_object_or_404(Product, pk=product_id)
    product_id = str(product_id)

    quantity = int(request.POST.get('quantity'))
    size = request.POST.get('product_size')

    bag = request.session.get('bag', {})

    if size:
        if quantity > 0:
            bag[product_id]['items_by_size'][size] = quantity
            messages.success(
                request,
                f'Updated size {size.upper()} {product.title} quantity to {quantity}'
            )
        else:
            del bag[product_id]['items_by_size'][size]

            if not bag[product_id]['items_by_size']:
                bag.pop(product_id)

            messages.success(
                request,
                f'Removed size {size.upper()} {product.title} from your bag'
            )
    else:
        if quantity > 0:
            bag[product_id] = quantity
            messages.success(
                request,
                f'Updated {product.title} quantity to {quantity}'
            )
        else:
            bag.pop(product_id)
            messages.success(
                request,
                f'Removed {product.title} from your bag'
            )

    request.session['bag'] = bag
    return redirect(reverse('shoppingbag:view_bag'))

13. Finally, I update remove_from_bag from:

def remove_from_bag(request, product_id):
    try:
        bag = request.session.get('bag', {})
        product_id = str(product_id)
        size = request.POST.get('size')

        if size:
            if product_id in bag and 'items_by_size' in bag[product_id]:
                del bag[product_id]['items_by_size'][size]

                if not bag[product_id]['items_by_size']:
                    bag.pop(product_id)
        else:
            bag.pop(product_id, None)

        request.session['bag'] = bag
        return redirect(reverse('shoppingbag:view_bag'))

    except Exception as e:
        messages.error(request, 'Error removing item')
        return redirect(reverse('shoppingbag:view_bag'))

To:

def remove_from_bag(request, product_id):
    """Remove item from shopping bag"""

    try:
        product = get_object_or_404(Product, pk=product_id)
        product_id = str(product_id)

        bag = request.session.get('bag', {})
        size = request.POST.get('product_size')

        if size:
            del bag[product_id]['items_by_size'][size]

            if not bag[product_id]['items_by_size']:
                bag.pop(product_id)

            messages.success(
                request,
                f'Removed size {size.upper()} {product.title} from your bag'
            )
        else:
            bag.pop(product_id)
            messages.success(
                request,
                f'Removed {product.title} from your bag'
            )

        request.session['bag'] = bag
        return HttpResponse(status=200)

    except Exception as e:
        messages.error(request, f'Error removing item: {e}')
        return HttpResponse(status=500)

- And also imported HttpResponse at the top of the file.

14. I run my page on my dev server and do some tests to see the Toasts messages coming into play. However, now the quantity selector buttons, update and remove buttons do not work at all so I consult ChatGPT who advises that my template is currently using the wrong variable - its using product.id when it should be using item.product as thats the variable I have available in my scope so this is breaking my quantity buttons. My update form is now pointing to the wrong view, its pointing to adjust_bag but I have updated the update_bag - I should probably look to remove one of these view but had tried previously and it broke something. The Javascript for my remove function is sending the wrong POST key, it sends: var data = {'csrfmiddlewaretoken': csrfToken, 'size': size};

But my view expects: size = request.POST.get('product_size')

So Javascript is failing silently.

- In my shoppingbag.html I go through and update any iterations of product.id with item.product.id

- I updated my action form url to use adjust_bag instead of update_bag view: action="{% url 'shoppingbag:adjust_bag' item.product_id %}"

- Then finally updated my Javascript in the bottom of the html to use the correct field:

var data = {'csrfmiddlewaretoken': csrfToken, 'product_size': size};

- I also remove the view for update_bag and its associated url path: path('update/<item_id>/', views.update_bag, name='update_bag'),

- Now when I refresh the page, I still cannot do anything - I can see a lot of Javascript related errors in the terminal and on the console too:

Uncaught ReferenceError: $ is not defined
    at shoppingbag/:787:7Understand this error
shoppingbag/:802 Uncaught ReferenceError: $ is not defined
    at shoppingbag/:802:24Understand this error
shoppingbag/:837 Uncaught ReferenceError: $ is not defined
    at shoppingbag/:837:5

- I consult ChatGPT about this who advises that the way I am loading Javascript is wrong, it advises me to remove the empty corejs brackets as it is being loaded at the bottom of base.html, I remove this and the duplication of Toasts scripts in the middle of the file and replace with this at the bottom:

{% block corejs %}
<script src="https://code.jquery.com/jquery-3.6.0.min.js"></script>
<script src="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/js/bootstrap.bundle.min.js"></script>
{% endblock %}

15. Now when I run the server, I can see that I have my functionality back in the shopping bag and it is giving me Toast notifications. I commit my code and move on to creating checkout app.

16. Before I move on to creating my checkout app, I am going to update my style.css with the content from Code Institute's Boutique Ado from CSS Tricks and the convenient classes. This will make the colours match the built-in Bootstrap colors for warning, info and so on, pulling directly from Bootstrap CSS itself.

/* from CSS-tricks.com: https://css-tricks.com/snippets/css/css-triangle/ */

.arrow-up {
    width: 0; 
    height: 0; 
    border-left: 4px solid transparent;
    border-right: 4px solid transparent; 
    border-bottom: 10px solid black;
    position: absolute;
    top: -10px;
    right: 36px;
}

/* Code Institute - Convenience classes - colors copied from Bootstrap */
.arrow-primary {
    border-bottom-color: #007bff !important;
}

.arrow-secondary {
    border-bottom-color: #6c757d !important;
}

.arrow-success {
    border-bottom-color: #28a745 !important;
}

.arrow-danger {
    border-bottom-color: #dc3545 !important;
}

.arrow-warning {
    border-bottom-color: #ffc107 !important;
}

.arrow-info {
    border-bottom-color: #17a2b8 !important;
}

.arrow-light {
    border-bottom-color: #f8f9fa !important;
}

.arrow-dark {
    border-bottom-color: #343a40 !important;
}

.bag-notification-wrapper {
    height: 100px;
    overflow-x: hidden;
    overflow-y: auto;
}

- Then I need to update the success notification in toast_success.html so that it includes a preview of the bag in the notification itself, so I wrap the original message in success.html in a row and a column with a horizontal rule below it as below:

    <div class="toast-body bg-white">
        <div class="row">
            <div class="col">
        {{ message }}
        <hr class="mt-1 mb-3"
    </div>
</div>

- Then beneath that I render the original shopping bag items with the grand total using the below Django tag to do this, borrrowing code from Code Institute to do this. It renders the shoppping bag if there is a grand total which shows the number of items in the bag in parentheses,

<div class="toast custom-toast rounded-0 border-top 0" data-autohide="false">
    <div class="arrow-up arrow-success"></div>
    <div class="w-100 toast-capper bg-success"></div>
    <div class="toast-header bg-white text-dark">
        <strong class="mr-auto">Success!</strong>
        <button type="button" class="ml-2 mb-1 close text-dark" data-dismiss="toast" aria-label="Close">
            <span aria-hidden="true">&times;</span>
        </button>
    </div>
    <div class="toast-body bg-white">
        <div class="row">
            <div class="col">
                {{ message }}
                <hr class="mt-1 mb-3">
            </div>
        </div>
        {% if grand_total %}
            <p class="logo-font bg-white text-black py-1">Your Bag ({{ product_count }})</p>
            <div class="bag-notification-wrapper">
                {% for item in bag_items %}
                    <div class="row">
                        <div class="col-3 my-1">
                            <img class="w-100" src="{{ item.product.image.url }}">
                        </div>
                        <div class="col-9">
                            <p class="my-0"><strong>{{ item.product.name }}</strong></p>
                            <p class="my-0 small">Size: {% if item.product.has_sizes %}{{ item.size|upper }}{% else %}N/A{% endif %}</p>
                            <p class="my-0 small text-muted">Qty: {{ item.quantity }}</p>
                        </div>
                    </div>
                {% endfor %}
            </div>
            <div class="row">
                <div class="col">
                    <strong><p class="mt-3 mb-1 text-black">
                        Total{% if free_delivery_delta > 0 %} (Exc. delivery){% endif %}: 
                        <span class="float-right">${{ total|floatformat:2 }}</span>
                    </p></strong>
                    {% if free_delivery_delta > 0 %}
                        <p class="mb-0 p-2 bg-warning shadow-sm text-black text-center">
                            Spend <strong>${{ free_delivery_delta }}</strong> more to get free next day delivery!
                        </p>
                    {% endif %}
                    <a href="{% url 'view_bag' %}" class="btn btn-black btn-block rounded-0">
                        <span class="text-uppercase">Go To Secure Checkout</span>
                        <span class="icon">
                            <i class="fas fa-lock"></i>
                        </span>
                    </a>
                </div>
            </div>
        {% endif %}
    </div>

17. I refresh my dev server to see this coming into play, I add a random item to the bag but ge the following error message:

![Server 500 error](/static/images/toasts/Screenshot%20Toasts%20error%20page%20after%20adding%20to%20cart.png)

18. I switch debug back on and can now see the issue:

![Server 500 error](/static/images/toasts/Screenshot%20template%20rendering%20issue.png)

19. I update my code in the toast_successs.html to:

   <a href="{% url 'shoppingbag:view_bag' %}"

11. I save the code and refresh the dev server and I am no longer presented with the 500 server error and I do see a preview when adding an item to the shopping bag. However, this isn't exactly what I expected to see:

![Addding items to the bag with Toast](/static/images/toasts/Screenshot%20preview%20of%20items%20in%20cart.png)

12. I query this with ChatGPT who advises that there is no fallback if the product doesn;t have an image so I can improve my code by adding a fallback as below, using an else statement if there is no image as below, I update this in my toast_success.html code:

{% if item.product.image %}
    <img class="w-100" src="{{ item.product.image.url }}" alt="{{ item.product.name }}">
{% else %}
    <img class="w-100" src="{{ MEDIA_URL }}noimage.png" alt="{{ item.product.name }}">
{% endif %}

13. ChatGPT has highlighted that MEDIA is not set correctly in settings.py, in my new toast HTML code I have the below for example, but this will not work as my Project has no MEDIA_URL and MEDIA_ROOT variables set:

{{ item.product.image.url }}

14. In my settings,py file I add the below under my static settings:

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

15. Then in my project level urls file I update to include the below at the bottom of the file:

+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

- I also import these at the top of the file:

from django.conf import settings
from django.conf.urls.static import static

- I save the code and test but it doesn't seem like anything has changed. Im the terminal I can see the below errors:

[26/Mar/2026 14:05:13] "GET /static/css/style.css HTTP/1.1" 200 6771
[26/Mar/2026 14:05:13] "GET /static/images/favicon.png HTTP/1.1" 200 1246
[26/Mar/2026 14:05:16] "GET /merchandise/7955/ HTTP/1.1" 200 35046
[26/Mar/2026 14:05:18] "POST /shoppingbag/add/7955/ HTTP/1.1" 302 0
[26/Mar/2026 14:05:19] "GET /merchandise/7955/ HTTP/1.1" 200 44046
Not Found: /merchandise/7955/noimage.png
[26/Mar/2026 14:05:19] "GET /merchandise/7

- I am going to find an image on Pexels that I can use when there is no image on the product to resolve these errors. I have found an appropriate image on Pexels and uploaded to my project static images folder with the name noimage.jpg. 

- I then update my toast_success.html file so that it loads static at the top of the file and replace my image code in the file with the below so it looks at the new file:

{% if item.product.image %}
    <img class="w-100" src="{{ item.product.image.url }}" alt="{{ item.product.name }}">
{% else %}
    <img class="w-100" src="{% static 'images/noimage.png' %}" alt="{{ item.product.name }}">
{% endif %}

- I test this again and I do now see an image in the preview but its not the correct one so I consult ChatGPT about this who advises that the tag I am using for image in the Toast_success.htmnl is wrong:

{{ item.product.image.url }}

- My Product model doesn't have an image field it instead has:

image_src = models.TextField(blank=True)

- To resolve the issue, I replace the below (in toast_succcesss)from:

{% if item.product.image %}
    <img class="w-100" src="{{ item.product.image.url }}" alt="{{ item.product.name }}">
{% else %}


To: 

{% if item.product.image_src %}
    <img class="w-100" src="{{ item.product.image_src }}" alt="{{ item.product.title }}">
{% else %}
    <img class="w-100" src="{% static 'images/noimage.jpg' %}" alt="{{ item.product.title }}">
{% endif %}

- I also need to fix the item.product.name tag to use 'title' instead of 'name' as the field I use on the model for Product is: title = models.CharField(...)

{{ item.product.name }} Should be {{ item.product.title }}

- I update this and test again and now I am not seeing the issue with the wrong image. However, I do not want to see the category badges in my add to bag preview as I am currently. I start by removing the code for badges from my product_detail.html, as I also do not want these showing on the individual product pages anymore either. I remove the below code from my product_detail.html:

{% block page_header %}
<div class="container mt-5 pt-5">
  {% for category in current_categories %}
    <a class="category-badge text-decoration-none" href="{% url 'merchandise:products' %}?category={{ category.name }}">
      <span class="p-2 mt-2 badge badge-white text-black rounded-0 border border-dark">{{ category.name }}</span>
    </a>
  {% endfor %}
</div>
{% endblock %}

- I refresh my page on the dev server to see if this has had the desired effect which it does, I am going to fill out the bottom section of the page with a reviews section but will do this later:

![Product Detail Categorys removed](/static/images/toasts/Screenshot%20badge%20categorys%20removed%20from%20individual%20product%20page.png)

- I also add the item to the cart to see how the bag preview looks and it looks much better as it has stopped showing all the product categorys when the product is added. However, it appears as though it produces 2 x success messages when a product is added to the cart:

![Two Success Messages on Cart](/static/images/toasts/Screenshot%20bag%20preview%20badge%20categorys%20removed.png)

- I have a look at the messages and can see one is updating the quantity of the product in the bag as it is already in there and the other is saying it is successful in being added to the bag. The confusion is that the wrong image is being used in the toast success message to what is actually being added to the bag. I consult this with ChatGPT who advises that it looks as though I have two image sources. on my Product model I defined:

image_src = models.TextField(blank=True)

Then on ProductVariant I defined:

image_src = models.TextField(blank=True)

- This creates ambiguity so my bag uses Product.image_src but my real image may be stored on Variant.image_src. ChatGPT recommends that I use the variant image in my toast mnessage, I replace the DEBUG code in toast_success.html with the below:

{% if item.product.variants.first.image_src %}
    <img class="w-100" src="{{ item.product.variants.first.image_src }}">
{% else %}
    <img class="w-100" src="{% static 'images/noimage.jpg' %}">
{% endif %}

- I also resolve the issue around the duplicate success messages double-triggering messages in the add_to_bag view. I add the below code to my add_to_bag view replacing my current 'if size' block:

    if size:
        if product_id in bag:
            if isinstance(bag[product_id], dict):
                # Already has sizes → update quantity
                bag[product_id]['items_by_size'][size] = (
                    bag[product_id]['items_by_size'].get(size, 0) + quantity
                )
                messages.success(
                    request,
                    f'Updated {product.title} (size {size.upper()}) quantity to {bag[product_id]["items_by_size"][size]}'
                )
            else:
                # Convert non-sized item into sized structure
                bag[product_id] = {'items_by_size': {size: quantity}}
                messages.success(
                    request,
                    f'Added {product.title} (size {size.upper()}) to your bag'
                )
    else:
        # First time adding this product
        bag[product_id] = {'items_by_size': {size: quantity}}
        messages.success(
            request,
            f'Added {product.title} (size {size.upper()}) to your bag'
        )

- However, this results in an error page so ChatGPT advises me to update my toast_success template again, replacing this section:

{% for item in bag_items %}
    <div class="row">
        <div class="col-3 my-1">
            {% if item.product.image_src %}
            <img class="w-100" src="{{ item.product.image_src }}" alt="{{ item.product.title }}">
            {% else %}
            <img class="w-100" src="{% static 'images/noimage.jpg' %}" alt="{{ item.product.title }}">
            {% endif %}
        </div>
        <div class="col-9">
            <p class="my-0"><strong>{{ item.product.title }}</strong></p>

            {% if item.product.variants.first.image_src %}
                <img class="w-100" src="{{ item.product.variants.first.image_src }}">
            {% else %}
                <img class="w-100" src="{% static 'images/noimage.jpg' %}"> 
            {% endif %}

With the below, as I currently rendering two images, it also asks me to remove the product vairant image source block slightly below this code too:

{% for item in bag_items %}
    <div class="row">
        <div class="col-3 my-1">
            {% if item.product.variants.first.image_src %}
                <img class="w-100" src="{{ item.product.variants.first.image_src }}" alt="{{ item.product.title }}">
            {% elif item.product.image_src %}
                <img class="w-100" src="{{ item.product.image_src }}" alt="{{ item.product.title }}">
            {% else %}
                <img class="w-100" src="{% static 'images/noimage.jpg' %}" alt="{{ item.product.title }}">
            {% endif %}
        </div>
        <div class="col-9">
            <p class="my-0"><strong>{{ item.product.title }}</strong></p>

- I have updated the code and ran the dev server again and tried to add an item to cart but I am getting the following error: 

AttributeError at /shoppingbag/add/12729/
'NoneType' object has no attribute 'upper'
Request Method:	POST
Request URL:	http://127.0.0.1:8000/shoppingbag/add/12729/
Django Version:	6.0.2
Exception Type:	AttributeError
Exception Value:	
'NoneType' object has no attribute 'upper'
Exception Location:	C:\Users\leila\OneDrive\Desktop\Documents\vscode-projects\working_out_gym\shoppingbag\views.py, line 52, in add_to_bag

- I have consulted ChatGPT about this who advises that when I have tried to add an item with no size that it has crahsed because I have added an item with no size and in my code it has crashed because None.upper doesn't exist as product_size is not in the POST data and size = None but my code tries to treat it the same as size.upper. It also points out that the structure of my add_tobag view is now broken and my else statement that says if there is no size on a product to treat it differently but my current logic is still treating it like a size. ChatGPT recommends updating the whole add_to_bag view to resolve this:

def add_to_bag(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    quantity = int(request.POST.get('quantity', 1))
    redirect_url = request.POST.get('redirect_url', '/')
    size = request.POST.get('product_size')

    product_id = str(product_id)
    bag = request.session.get('bag', {})

    # ✅ PRODUCTS WITH SIZE
    if size:
        if product_id in bag:
            if isinstance(bag[product_id], dict):
                bag[product_id]['items_by_size'][size] = (
                    bag[product_id]['items_by_size'].get(size, 0) + quantity
                )
                messages.success(
                    request,
                    f'Updated {product.title} (size {size.upper()}) quantity to {bag[product_id]["items_by_size"][size]}'
                )
            else:
                bag[product_id] = {'items_by_size': {size: quantity}}
                messages.success(
                    request,
                    f'Added {product.title} (size {size.upper()}) to your bag'
                )
        else:
            bag[product_id] = {'items_by_size': {size: quantity}}
            messages.success(
                request,
                f'Added {product.title} (size {size.upper()}) to your bag'
            )

    # ✅ PRODUCTS WITHOUT SIZE
    else:
        if product_id in bag and isinstance(bag[product_id], int):
            bag[product_id] += quantity
            messages.success(
                request,
                f'Updated {product.title} quantity to {bag[product_id]}'
            )
        else:
            bag[product_id] = quantity
            messages.success(
                request,
                f'Added {product.title} to your bag'
            )

    request.session['bag'] = bag
    return redirect(redirect_url)

- I refresh the page on my local dev server and test it out. I try adding a pair of socks with no size and the bag preview is looking much better:

![Shopping Cart Preview now showing correct images](/static/images/toasts/Screenshot%20bag%20preview%20non%20sized%20items%20working%20well.png)

- However, I go to open the Merchandise menu so I can go to the clothing section and choose an item with a size to add to the cart but the image is staying stuck to the page and not flowing with the rest of the app and the footer doesn't look right either so I will need to resolve this quickly before moving on:

![Individual Products not flowing](/static/images/toasts/Screenshot%20bag%20preview%20non%20sized%20items%20working%20well.png)

- I have done a hard refresh and notice this issue only occurs after adding the product to the bag. I consult ChatGPT who advises that I am using the below in my toast_success.html template which can break if any closing div is missing and break the entire page:

<div class="row">
    <div class="col-3">...</div>
<div class="col-9">...</div>
</div>

- It recommends that I replace my for loop of item in bag_items with the below as it is a cleaner structure from:

                {% for item in bag_items %}
                <div class="row">
                    <div class="col-3 my-1">
                        {% if item.product.variants.first.image_src %}
                        <img class="w-100" src="{{ item.product.variants.first.image_src }}" alt="{{ item.product.title }}">
                        {% elif item.product.image_src %}
                        <img class="w-100" src="{{ item.product.image_src }}" alt="{{ item.product.title }}">
                        {% else %}
                        <img class="w-100" src="{% static 'images/noimage.jpg' %}" alt="{{ item.product.title }}">
                        {% endif %}
                    </div>
                <div class="col-9">
                <p class="my-0"><strong>{{ item.product.title }}</strong></p>
                <p class="my-0 small">Size: {% if item.product.has_sizes %}{{ item.size|upper }}{% else %}N/A{% endif %}</p>
                <p class="my-0 small text-muted">Qty: {{ item.quantity }}</p>
            </div>
        </div>
            {% endfor %}

- To:

{% for item in bag_items %}
    <div class="row">
        <div class="col-3 my-1">
            {% if item.product.variants.first.image_src %}
                <img class="w-100" src="{{ item.product.variants.first.image_src }}" alt="{{ item.product.title }}">
            {% elif item.product.image_src %}
                <img class="w-100" src="{{ item.product.image_src }}" alt="{{ item.product.title }}">
            {% else %}
                <img class="w-100" src="{% static 'images/noimage.jpg' %}" alt="{{ item.product.title }}">
            {% endif %}
        </div>

        <div class="col-9">
            <p class="my-0"><strong>{{ item.product.title }}</strong></p>
            <p class="my-0 small">
                Size:
                {% if item.product.has_sizes %}
                    {{ item.size|upper }}
                {% else %}
                    N/A
                {% endif %}
            </p>
            <p class="my-0 small text-muted">Qty: {{ item.quantity }}</p>
        </div>
    </div>
{% endfor %}

- It also recommends updating my .custom-toast css styles to:

.custom-toast {
    position: fixed;
    top: 80px;
    right: 20px;
    z-index: 9999;
}

- I apply these updates and then restart my dev server to test. It looks much better now, I can add a product to the bag and then still see the correct view on my individual products view afterwards:

![Individual Products view okay after bag adding](/static/images/toasts/Screenshot%20individual%20products%20view%20now%20resolved.png)

16. I am going to switch debug back to False, run a collectstatic and then commit my code to Github and Heroku.

---

## Checkout App - Creating the App and Models

1. The next thing that I am going to do is create my Checkout app so that my users can actually make purchases. I start by running the below cmd in my terminal to create the new app for checkout:

python manage.py startapp checkout

2. Once I can see that the new directory is created in the root of the project, I'll then add the new app to my INSTALLED APPS section of my settings.py in project folder as below:

'checkout',

3. I am going to start on the models for my checkout app, as Code Institute did for their Boutique Ado. I am going to borrow Code Institute's code for their Order model as below, to save time, as there is a lof of fields that we will need for the order, i.e.e full address details, name, phone number, etc. It already has the correct settings for the fields which may not be used everywhere so are set to false (postcode and county):

class Order(models.Model):
    order_number = models.CharField(max_length=32, null=False, editable=False)
    full_name = models.CharField(max_length=50, null=False, blank=False)
    email = models.EmailField(max_length=254, null=False, blank=False)
    phone_number = models.CharField(max_length=20, null=False, blank=False)
    country = models.CharField(max_length=40, null=False, blank=False)
    postcode = models.CharField(max_length=20, null=True, blank=True)
    town_or_city = models.CharField(max_length=40, null=False, blank=False)
    street_address1 = models.CharField(max_length=80, null=False, blank=False)
    street_address2 = models.CharField(max_length=80, null=True, blank=True)
    county = models.CharField(max_length=80, null=True, blank=True)
    date = models.DateTimeField(auto_now_add=True)
    delivery_cost = models.DecimalField(max_digits=6, decimal_places=2, null=False, default=0)
    order_total = models.DecimalField(max_digits=10, decimal_places=2, null=False, default=0)
    grand_total = models.DecimalField(max_digits=10, decimal_places=2, null=False, default=0)

4. I am then going to paste Code Institute's OrderLineItem model code directly below this, this model relates to the Order model and creates the OrderLineItem for each order:

class OrderLineItem(models.Model):
    order = models.ForeignKey(Order, null=False, blank=False, on_delete=models.CASCADE, related_name='lineitems')
    product = models.ForeignKey(Product, null=False, blank=False, on_delete=models.CASCADE)
    product_size = models.CharField(max_length=2, null=True, blank=True) # XS, S, M, L, XL
    quantity = models.IntegerField(null=False, blank=False, default=0)
    lineitem_total = models.DecimalField(max_digits=6, decimal_places=2, null=False, blank=False, editable=False)

5. I am then going to import the UUID at the top of the file so that it generates the order number:

import uuid

6. Then I will import the sum function from django.db.models and the settings module from django.conf so it can generate the delivery cost and calculate this:

from django.db.models import Sum
from django.conf import settings

7. Then finally I need to import the products.model as the OrderLineItem model has a foreign key to this:

from merchandise.models import Product

8. Next, I am going to add the model methods that Code Institute used in Boutique Ado to generate my order number and to also save this. The first method for _generate_order_number will generate a random string of 32 characters and the save method overrides the default save method in case the order being saved doesn't have an order number at that time. It will call the generate order method and then execite the original save method. There is also a function to update_total. It uses the aggregate function by using the sum function across all line-item total fields for all line items on the order and then add a new field to the query set called line-item total sum, which we grab and then set the order total to this. I also add the standard string method to return the order number for the model:

 def _generate_order_number(self):
        """
        Generate a random, unique order number using UUID
        """
        return uuid.uuid4().hex.upper()
    
    def update_total(self):
        """
        Update grand total each time a line item is added,
        accounting for delivery costs.
        """
        self.order_total = self.lineitems.aggregate(Sum('lineitem_total'))['lineitem_total__sum']
        if self.order_total < settings.FREE_DELIVERY_THRESHOLD:
            self.delivery_cost = self.order_total * settings.STANDARD_DELIVERY_PERCENTAGE / 100
        else:
            self.delivery_cost = 0
        self.grand_total = self.order_total + self.delivery_cost
        self.save()
    
    def save(self, *args, **kwargs):
        """
        Override the original save method to set the order number
        if it hasn't been set already.
        """
        if not self.order_number:
            self.order_number = self._generate_order_number()
        super().save(*args, **kwargs)

    def __str__(self):
        return self.order_number

9. I now need to set the line-item total field on the order line-item model by overriding its save method using the below code. This logic is simple, it just multiplies the product price by the quanitty for each line item and then adds the standard string method, returning just the order number for the order model. The SKU of the product with its order number is also part of each order line item.

    def save(self, *args, **kwargs):
        """
        Override the original save method to set the lineitem total
        and update the order total.
        """
        self.lineitem_total = self.product.price * self.quantity
        super().save(*args, **kwargs)

    def __str__(self):
        return f'SKU {self.product.sku} on order {self.order.order_number}'

10. Once the models file is saved, I can then run the dry migrations to be created using:

python manage.py makemigrations --dry-run

11. No issues are found with the new code, so I run these properly with:

python manage.py makemigrations

12. I then migrate these using:

python manage.py migrate

13. I am then going to commit my changes once migrations have completed successfully:

git add .
git commit -m "Created checkout app and models"
git push origin main
git push heroku main

---

## Checkout App - Admin for Orders

1. Now that I have created my models for the Orders and OrderLineItems, I am going to add them to my admin panel. In checkout/admin.py, I import the Order and OrderLineItem models at the top of the file:

from .models import Order, OrderLineItem

2. I then create a new class OrderAdmin:

class OrderAdmin(admin.ModelAdmin):

- Which contains read-only fields that will be calculated using the methods I set up earlier in my Order model, this prevents people from editing these options as it could compromise the integrity of an order if they were changeable fields:

readonly_fields = ('order_number', 'date', 'delivery_cost', 'order_total','grand_total',)

3. I also use the fields option to allow me to specify the order of the fields in the admin interface; these would otherwise be adjusted by Django as I am using read-only fields:

    fields = ('order_number', 'date', 'full_name', 'email', 'phone_number', 'country', 'postcode',      'town_or_city', 'street_address1', 'street_address2', 'county', 'delivery_cost', 'order_total', 'grand_total',)


4. Next, I use the List Display option in the class so that it restricts the columns in the order list to only a few key items and set them to date in rever chronological order to show most recent orders at the top of the list:

    list_display = ('order_number', 'date', 'full_name',
                    'order_total', 'delivery_cost',
                    'grand_total',)

    ordering = ('-date',)

5. I am then going to create another class called OrderLineItemAdminInline which inherits from admin.TabularInline; this inline item allows us to add and edit line items in the admin right from inside the order model. Now when we look at an order we can see a list of editable line items on the same page:

class OrderLineItemAdminInline(admin.TabularInline):
    model = OrderLineItem

6. This class will make the line item total in the form read-only using the below code:

    readonly_fields = ('lineitem_total',)

7. I then need to update the OrderAdmin class to add the new OrderLineItemAdminInline class to the order admin interface. To do this, I add the inlines option to the OrderAdmin class using:

inlines = (OrderLineItemAdminInline,)

8. Now I need to register the Order model and OrderAdmin model but avoid registering the OrderLineItem model as its accessible using Inline on the Order model:

admin.site.register(Order, OrderAdmin)

9. I have a look at the admin panel on my local dev server to see how this is looking. I can now see the option for 'Orders' under 'Checkout' when I login to the Admin panel as my superuser:

![Admin Panel showing Orders](/static/images//Checkout/Screenshot%20Checkout%20Orders%20Admin%20Panel%201.png)

10. If I click 'Add' on 'Orders', then on the next page I can see that it has made then appropriate fields read-only, according to the code we set, then it also has an interface at the bottom which allows adding and adjusting line items where needed:

![Admin Panel creating orders fields readonly](/static/images//Checkout/Screenshot%20checkout%20orders%20admin%20panel%202.png)

11. I now want to look at setting up a way to update the order total, delivery cost and grand_total for each order as the users add line items to their orders. The process is to first create an order, then iterate through each prodcut in the shopping bag and add line items to it one by one so it updates the various costs along the way. The method to update the total like this is already contained within the Order model so just needs be called each time a new line item is added to the order. In order to call the method within the model, I am going to follow Code Institute and call upon the Django feature signals. 

Within my checkout app, I create a new file in the root of the directory called signals.py. Then within this file, I import 2 x signals; these signals are sent by Django to the entire application after a model instance is saved and after its deleted respectively:

from django.db.models.signals import post_save, post_delete

12. Then to receive these signals, I import the receiver:

from django.dispatch import receiver

13. Then I want to listen for signals from the OrderLineItem so I import the model into the file:

from .models import OrderLineItem

14. Then I need to write a function within the new signals file defined as 'update_on_save' which will take in the parameters of sender, instance, created and keyword arguments. This is a special type of function which will handle signals from the post_save event. These parameters refer to the sender of the signal, the OrderLineItem:

def update_on_save(sender, instance, created, **kwargs):

15. Then the code for the method is simple, we access instance.order, which refers to the order this specific line item is realted to and calls the update_total method on it:

instance.order.update_total()

16. Now I need to execute this function any time that the post_save signal is sent so we use the receiver decorator and tell it that we are receiving post saved signals from the OrderLineItem model:

@receiver(post_save, sender=OrderLineItem)

17. Then to handle the various totals when a line item is deleted, I copy the whole function, including receiver decorator, and change the signal like below. And remove the created parameter as its not used here and then paste this below the post_save function:

@receiver(post_delete, sender=OrderLineItem)
def update_on_delete(sender, instance, **kwargs):
    """ Update order total on lineitem delete"""
    instance.order.update_total()

18. Finally, I update my apps.py file in checkout app to let Django know that there is a new signals module containing listeners. To do this I override the ready method and import the signals module. This means that every time a line item is saved or deleted then the custom update total model method will be called and update the order totals automatically:

    def ready(self):
        import checkout.signals

19. Next I am going to create the checkout form. To do this I create a new forms.py file and import forms forms from Django and our Order model:

from django import forms
from .models import Order

20. I then create a new OrderForm class and give it some meta options telling Django which model it'll be associated with and which fields to render, none of the fields rendered will be those which are automatically calculated as users won't be populating this information and it will be done bia the model methods we have created:

class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ('full_name', 'email', 'phone_number',
                  'street_address1', 'street_address2',
                  'town_or_city', 'postcode', 'country',
                  'county',)

21. Then I am going to override the init method of the form to allow us to customize it further. I am going to copy and paste this method from Boutique Ado. This has a dictionary of placeholders which will show up in the form fields rather than being a clunky label and empty text box in the template. This sets the autofocus attribute on the full name field to true so the cursor will start in the full name field when the user loads the page. Then it finally interates through the forms fields, adding a star to the placeholder if it is a required field on the model and setting all the placeholder attributes to their values in the dictionary above and using a new css class I need to add later. This also removes the form fields labels as these are not required:

  def __init__(self, *args, **kwargs):
        """
        Add placeholders and classes, remove auto-generated
        labels and set autofocus on first field
        """
        super().__init__(*args, **kwargs)
        placeholders = {
            'full_name': 'Full Name',
            'email': 'Email Address',
            'phone_number': 'Phone Number',
            'country': 'Country',
            'postcode': 'Postal Code',
            'town_or_city': 'Town or City',
            'street_address1': 'Street Address 1',
            'street_address2': 'Street Address 2',
            'county': 'County',
        }

        self.fields['full_name'].widget.attrs['autofocus'] = True
        for field in self.fields:
            if self.fields[field].required:
                placeholder = f'{placeholders[field]} *'
            else:
                placeholder = placeholders[field]
            self.fields[field].widget.attrs['placeholder'] = placeholder
            self.fields[field].widget.attrs['class'] = 'stripe-style-input'
            self.fields[field].label = False

22. I am now going to commit my changes and get ready to create my first view for my checkout system.

---

## Checkout App - Creating Views and Templates

1. I now need to create the view for the checkout app. In my checkout/views.py file, I create a simple checkout view. Below code will get the bag from session and if bag is empty then give an error message. Then it will redirect back to the Merchandise page, preventing users from manually accessing the url using '/checkout':

def checkout(request):
    shoppingbag = request.session.get('bag', {})
    if not shoppingbag:
        messages.error(request, "Your bag is currently empty.")
        return redirect(reverse('merchandise'))

2. I then need to create an instance of the order form which will be empty for the moment:

order_form = OrderForm()

3. Then I create the template and the context containing the order form and finally render this on the page:

template = 'checkout/checkout.html'
context = {
  'order_form': order_form,
}

return render(request, template, context)

4. Then finally at the top of the file I need to import redirect, reverse and then messages from django.contrib and the orderform:

from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from .forms import OrderForm

5. Once the new file is saved, I then create a checkout/urls.py file. I copy the contents from home/urls.py and paste this into the new urls file and update the view and name to checkout in place of home:

from django.urls import path
from . import views

urlpatterns = [
    path("", views.checkout, name="checkout"),
]

6. Then in my project level urls file, I update this to include the checkout urls:

    path("checkout/", include("checkout.urls")),

7. I now need to create the template. I create a templates directory in the new checkout app directory, with a subfolder within it called 'checkout' (checkout/templates/checkout). Next I create a new file for the template in the new folder structure and call it checkout.html. I am going to borrow Code Institute's Boutique Ado checkout.html code to populate this file:

{% extends "base.html" %}
{% load static %}

{% block extra_css %}
    <link rel="stylesheet" href="{% static 'checkout/css/checkout.css' %}">
{% endblock %}

{% block page_header %}
    <div class="container header-container">
        <div class="row">
            <div class="col"></div>
        </div>
    </div>
{% endblock %}

{% block content %}
    <div class="overlay"></div>
    <div class="container">
        <div class="row">
            <div class="col">
                <hr>
                <h2 class="logo-font mb-4">Shopping Bag</h2>
                <hr>
            </div>
        </div>

        <div class="row">
            <div class="col-12 col-lg-6">
                <p class="text-muted">Please fill out the form below to complete your order</p>
            </div>
        </div>
    </div>
{% endblock %}

8. I am now going to include a separate css block into my project just for the checkout file. I am going to add a static folder into the checkout app directory. Then within that folder I will create a new folder for 'checkout' and finally a css folder within this folder where I will create a new css file exclusively for the checkout page.

9. I now create a new file called checkout.css which I will populate with some styles exlcusive to the checkout app. 

10. Next, I update my settings.py file underneath context processors in the template setting, I add a list called built-ins which will contain all the tags I want available in my templates by default. I want to add the crispy_forms_tags and crispy_forms fields. This will give us access to everything we need from crispy forms across all templates by default:

'builtins': [
  'crispy_forms.templatetags.crispy_forms_tags',
  'crispy_forms.templatetags.crispy_forms_field',
]

11. Now that is done, I need to render the form in the checkout template. Back in checkout.html, within the last div in the template under the p element, I use the form element with an action url of 'checkout', a method of POST and an ID of payment_form, I also add the CSRF token as the POST method is being called on:

        <div class="row">
            <div class="col-12 col-lg-6">
                <p class="text-muted">Please fill out the form below to complete your order</p>
                <form action="{% url 'checkout' %}" method="POST" id="payment-form">
                {% csrf_token %}
            </div>
        </div>

12. Instead of rendering the whole form, I am going to render the fields individually and divide them into three fieldsets. The first fieldset will have a legend label of details which includes the users full_name and email address. To render the fields I will just access the form and call them by name and type them into the as_crispy_field template tag:

                <form action="{% url 'checkout' %}" method="POST" id="payment-form">
                {% csrf_token %}
                <fieldset class="rounded px-3 mb-5">
                    <legend class="fieldset-label small text-black px-2 w-auto">Details</legend>
                    {{ order_form.full_name | as_crispy_field }}
                    {{ order_form.email | as_crispy_field }}
                </fieldset>
                <fieldset class="rounded px-3 mb-5"></fieldset>
                <fieldset class="px-3"></fieldset>

13. The next fieldset will have the rest of the forms fields all rendered as crispy fields and will have a label of delivery, assigning this fieldset to be where the users delivery information will be held. I update the legend content from 'Details' to 'Delivery' and then copy and paste the order_form django tag from the Details fieldset until I have 7 instances of the Django tag which account for: phone number, country, postcode, town_or_city, street_address1, street_address2, county:

                        {{ order_form.phone_number | as_crispy_field }}
                        {{ order_form.country | as_crispy_field }}
                        {{ order_form.postcode | as_crispy_field }}
                        {{ order_form.town_or_city | as_crispy_field }}
                        {{ order_form.street_address1 | as_crispy_field }}
                        {{ order_form.street_address2 | as_crispy_field }}
                        {{ order_form.county | as_crispy_field }}

14. I am then going to borrow Code Institute's code which provides an inline checkbox for allowing authenticated users to save the information from the checkout form to their profiles . If not authenticated then this gives the user a link to signup or login - this will be handy once I have created the profiles app:

 <div class="form-check form-check-inline float-right mr-0">
							{% if user.is_authenticated %}
								<label class="form-check-label" for="id-save-info">Save this delivery information to my profile</label>
                                <input class="form-check-input ml-2 mr-0" type="checkbox" id="id-save-info" name="save-info" checked>
							{% else %}
								<label class="form-check-label" for="id-save-info">
                                    <a class="text-info" href="{% url 'account_signup' %}">Create an account</a> or 
                                    <a class="text-info" href="{% url 'account_login' %}">login</a> to save this information
                                </label>
							{% endif %}
						</div>

15. Then the final fieldset will be for the user's payment information. This will not use form fields as I am going to use Stripe like Code Institute's Boutique Ado. There will simply be two empty divs which will hold the stripe elements. The first will have an ID of card-element and the second will have an ID of card-errors:

                <fieldset class="px-3">
                    <legend class="fieldset-label small text-black px-2 w-auto">Payment</legend>
                        <!-- A Stripe card element will go here -->
                        <div class="mb-3" id="card-element"></div>
                        <!-- Used to display form errors -->
                        <div class="mb-3 text-danger" id="card-errors" role="alert"></div>
                </fieldset>

16. Then I need to create a submit button which has an ID I will access using Javascript in order to submit the checkout form:

                    <div class="submit-button text-right mt-5 mb-2">                    
						<a href="{% url 'view_bag' %}" class="btn btn-outline-black rounded-0">
							<span class="icon">
								<i class="fas fa-chevron-left"></i>
							</span>
							<span class="font-weight-bold">Adjust Bag</span>
						</a>
						<button id="submit-button" class="btn btn-black rounded-0">
							<span class="font-weight-bold">Complete Order</span>
							<span class="icon">
								<i class="fas fa-lock"></i>
							</span>
						</button>

17. Finally I add a small notification at the bottom to alert users that the card is about to be charged:

						<p class="small text-danger my-0">
							<span class="icon">
								<i class="fas fa-exclamation-circle"></i>
							</span>
							<span>Your card will be charged <strong>${{ grand_total|floatformat:2 }}</strong></span>
						</p>
					</div>

18. I now want to add an order summary to the top of our checkout page. I am again going to borrow Code Institute's code for this and create a new div with column class above our form. I will give this div the order-lg-last class so it shows up on the right on a larger screen:

<div class="col-12 col-lg-6 order-lg-last mb-5">

19. Then within this div I will copy and paste the below content from Boutique Ado/checkout.html:

                <p class="text-muted">Order Summary ({{ product_count }})</p>
                <div class="row">
                    <div class="col-7 offset-2">
                        <p class="mb-1 mt-0 small text-muted">Item</p>
                    </div>
                    <div class="col-3 text-right">
                        <p class="mb-1 mt-0 small text-muted">Subtotal</p>
                    </div>
                </div>
                {% for item in bag_items %}
                    <div class="row">
                        <div class="col-2 mb-1">
                            <a href="{% url 'product_detail' item.product.id %}">
                                {% if item.product.image_src %}
                                    <img class="w-100" src="{{ item.product.image_src }}" alt="{{ product.title }}">
                                {% else %}
                                    <img class="w-100" src="{{ MEDIA_URL }}noimage.png" alt="{{ product.title }}">
                                {% endif %}
                            </a>
                        </div>
                        <div class="col-7">
                            <p class="my-0"><strong>{{ item.product.title }}</strong></p>
                            <p class="my-0 small">Size: {% if item.product.has_sizes %}{{ item.size|upper }}{% else %}N/A{% endif %}</p>
                            <p class="my-0 small text-muted">Qty: {{ item.quantity }}</p>
                        </div>
                        <div class="col-3 text-right">
                            <p class="my-0 small text-muted">${{ item.product.price | calc_subtotal:item.quantity }}</p>
                        </div>
                    </div>
                {% endfor %}
                <hr class="my-0">
                <div class="row text-black text-right">
                    <div class="col-7 offset-2">
                        <p class="my-0">Order Total:</p>
                        <p class="my-0">Delivery:</p>
                        <p class="my-0">Grand Total:</p>
                    </div>
                    <div class="col-3">
                        <p class="my-0">${{ total | floatformat:2 }}</p>
                        <p class="my-0">${{ delivery | floatformat:2 }}</p>
                        <p class="my-0"><strong>${{ grand_total | floatformat:2 }}</strong></p>
                    </div>
                </div>

20. I go through this and tweak according to my own code. Inside this code are three main components. First there is an order summary header and a row containing a couple simple column headers. Next, as the bagged items are still accessible thanks to the context processor, we can loop through each item creating a row with the image with some information about it and the subtotal. THere is a marginless horizontal rule and a summary row containing the tools and delivery cost for the order:

<div class="col-12 col-lg-6 order-lg-last mb-5">
                                <p class="text-muted">Order Summary ({{ product_count }})</p>
                <div class="row">
                    <div class="col-7 offset-2">
                        <p class="mb-1 mt-0 small text-muted">Item</p>
                    </div>
                    <div class="col-3 text-right">
                        <p class="mb-1 mt-0 small text-muted">Subtotal</p>
                    </div>
                </div>
                {% for item in bag_items %}
                    <div class="row">
                        <div class="col-2 mb-1">
                            <a href="{% url 'product_detail' item.product.id %}">
                                {% if item.product.image %}
                                    <img class="w-100" src="{{ item.product.image.url }}" alt="{{ product.title }}">
                                {% else %}
                                    <img class="w-100" src="{{ MEDIA_URL }}noimage.jgp" alt="{{ product.title }}">
                                {% endif %}
                            </a>
                        </div>
                        <div class="col-7">
                            <p class="my-0"><strong>{{ item.product.title }}</strong></p>
                            <p class="my-0 small">Size: {% if item.product.has_sizes %}{{ item.size|upper }}{% else %}N/A{% endif %}</p>
                            <p class="my-0 small text-muted">Qty: {{ item.quantity }}</p>
                        </div>
                        <div class="col-3 text-right">
                            <p class="my-0 small text-muted">${{ item.product.price | calc_subtotal:item.quantity }}</p>
                        </div>
                    </div>
                {% endfor %}
                <hr class="my-0">
                <div class="row text-black text-right">
                    <div class="col-7 offset-2">
                        <p class="my-0">Order Total:</p>
                        <p class="my-0">Delivery:</p>
                        <p class="my-0">Grand Total:</p>
                    </div>
                    <div class="col-3">
                        <p class="my-0">${{ total | floatformat:2 }}</p>
                        <p class="my-0">${{ delivery | floatformat:2 }}</p>
                        <p class="my-0"><strong>${{ grand_total | floatformat:2 }}</strong></p>
                    </div>
                </div>

21. Finally, I load bagtools at the top of the file using:

{% load bag_tools %}

22. I need to add the below to my TEMPLATE context_processors in settings, which adds a media context processor so that the media URL template tag will work:

'django.template.context_processors.media',

23. Now that is done, I need to add the checkout URL to the shopping bag templates secure checkout button and see how the checkout page looks:

{% url 'checkout' %}

24. I run my local dev server and see what the checkout app looks like, however, straight away there are errors in the terminal:

  File "C:\Users\leila\OneDrive\Desktop\Documents\vscode-projects\working_out_gym\checkout\urls.py", line 2, in <module>
    from . import views
  File "C:\Users\leila\OneDrive\Desktop\Documents\vscode-projects\working_out_gym\checkout\views.py", line 3, in <module>
    from .forms import OrderForm
  File "C:\Users\leila\OneDrive\Desktop\Documents\vscode-projects\working_out_gym\checkout\forms.py", line 12
    def __init__(self, *args, **kwargs):
                                        ^
IndentationError: unindent does not match any outer indentation level

25. I look at line 12 on my checkout forms.py file and can see the indentation is wrong so resolve this. 

26. I save the file but now there are new errors in the terminal:

  File "C:\Users\leila\OneDrive\Desktop\Documents\vscode-projects\working_out_gym\checkout\urls.py", line 5, in <module>
    path("", views.home, name="home"),
             ^^^^^^^^^^
AttributeError: module 'checkout.views' has no attribute 'home'

27. I realise that I didn't update the urls file I copied over from my home app with checkout as I thought so I update this and refresh now. I can get back onto my page but when I click Secure Checkout from the shopping bag I am being presented with the below error:

![bag tools template syntax error](/static/images//Checkout/Screenshot%20bag_tools%20not%20registered.png)

28. I consult ChatGPT who advises that I should have a bag_tools.py file in templatetags folder in my shoppingbag app. I create these now and populate with Code Institute bag_tools.py code:

from django import template


register = template.Library()

@register.filter(name='calc_subtotal')
def calc_subtotal(price, quantity):
    return price * quantity

29. I cancel and re-run the local dev server and then encounter another error on line 43 of my checkout.html:

NoReverseMatch at /checkout/
Reverse for 'product_detail' not found. 'product_detail' is not a valid view function or pattern name.

30. I update this to:

<a href="{% url 'merchandise:product_detail' item.product.id %}">

31. The next url error appears, this time for:

<a href="{% url 'view_bag' %}" class="btn btn-outline-black rounded-0">

- I update this to:

<a href="{% url 'shoppingbag:view_bag' %}" class="btn btn-outline-black rounded-0">

31. The page has finally loaded:

![checkout page successfully loaded](/static/images//Checkout/Screenshot%20checkout%20page%20finally%20loaded.png)

32. I also update the url on my toast_success.html so that the secure checkout button in the shopping bag preview takes us to the checkout. I test this and it works successfully. The only problem now is that the checkout page doesn't really carry all the styling I need it to, mainly the navbar stylings and item images. I update my checkout.html to use the block.super django tag in my block extra css block like below so that the checkout css doesn't override my base css styles:

{{ block.super }}

33. I reload my page and can see my navbar again but no images on the products still:

![checkout page no images](/static/images//Checkout/Screenshot%20checkout%20navbar%20restored%20no%20images.png)

34. I update my image code in my checkout.html to include an elif statement like that that I used in my toast_success.html as it looks at two different pieces of data to find the images in my code:

{% if item.product.variants.first.image_src %}
    <img class="w-100" src="{{ item.product.variants.first.image_src }}" alt="{{ item.product.title }}">
{% elif item.product.image_src %}
    <img class="w-100" src="{{ item.product.image_src }}" alt="{{ item.product.title }}">
{% else %}
    <img class="w-100" src="{% static 'images/noimage.jpg' %}" alt="{{ item.product.title }}">
{% endif %}

35. I cancel the server and reload and can see the images in my checkout page now:

![Styles and images now showing](/static/images//Checkout/Screenshot%20styles%20and%20images%20now%20showing.png)

36. I do not have any subtotals showing against my individual items in the cart so I query ChatGPT as to why this would be and they advise I need to have a __init__.py file in my templatetags folder with my bag_tools.py file and that there should be a function like below in the bag_tools.py file:

@register.filter(name='calc_subtotal')
def calc_subtotal(price, quantity):
    try:
        return float(price) * int(quantity)
    except (TypeError, ValueError):
        return 0

37. I create the init py file and then update my calc_subtotal filter in bag_tools.py file to the code above and then re-run the page and can now see £0 on each item under subtotals which is wrong. I then update the code in my checkout.html file to use the below calculation instead, updating the price code:

item.product.variants.first.price | calc_subtotal:item.quantity

38. Now when I refresh the checkout app I can see the subtotals. I am going to commit my code here ready for setting up Stripe payments next.

---

## Stripe Payments Setup

1. To start with, I am going to create a checkout.css file in the newly created static/css/checkout folder I created earlier in my checkout app. I am then going to populate this with some styles for the payment form, this will set all form controls as well as the card element div to have black text and a solid black border:

#payment-form, form-control,
#card-element {
  color: #000;
  border: 1px solid #000;
}

2. Next I am going to adjust the position of the fieldset labels slighltly using the below css:

.fieldset-label {
  position: relative;
  right: .5rem;
}

3. I update my project on my dev server and go to the checkout page to see how this looks. This looks good to me. I move on to setting up stripe by navigating to the below link and clicking 'Get Started':

www.stripe.com

![Stripe website](/static/images/Stripe/Screenshot%20stripe%20website.png)

4. I am then going to create an account with stripe using my personal email address, name, password:

![Stripe account](/static/images/Stripe//Screenshot%20stripe%20account%20registration.png)

5. I verify my email address with Stripe and go back to Stripe, I skip the steps to set this up as a live payment system and go to the Sandbox:

![Stripe sandbox](/static/images/Stripe/Screenshot%20Stripe%20sandbox.png)

6. I am now going to implement a Stripe element that will add a prebuilt credit card input to my form. I look through the Stripe docs for accepting a payment at: https://docs.stripe.com/payments/accept-a-payment?payment-ui=elements&api-integration=checkout and find the Javascript for Stripe:

<script src="https://js.stripe.com/dahlia/stripe.js"></script>

7. In my base.html file, I paste the javascript link for Stripe into my corejs block:

    {% block corejs %}
    <!-- Stripe-->
    <script src="https://js.stripe.com/dahlia/stripe.js"></script>
    {% endblock %}

8. With this added to my base.html file, I am now going to go to my checkout.html template and add a new postload js block at the bottom and render a block.super:

{% block postloadjs %}
    {{ block.super }}
{% endblock %}

9. Next, I am going to use a built-in template filter called json_script to render the Django template variables so they can then be accessed in the external file. One will be rendered and called stripe_public_key abd the other will be called client_secret:

{{ stripe_public_key|json_script:"id_stripe_publick_key" }}
{{ stripe_client_secret|json_script:"id_client_secret" }}

10. I then need to go to Stripe and copy the public key. I go 'Settings' > 'Developers' and click the 'Manage API Keys' link:

![Stripe Manage API Keys](/static/images/Stripe/Screenshot%20stripe%20finding%20public%20key.png)

11. On the next page I copy the key which is the Publishable Key and then go the Checkout apps views and add this to the context dictionary, I also add a test value for client secret to

    context = {
      'order_form': order_form,
      'stripe_public_key': 'pk_test_51THL0p1urpY1vbdfqWYuHsp6HQutigXittGOBRve9PjZ2K7vjPCGSksrJt74ADa1QAdCOIV6SDj2Nx7X0mP5hegD00cn8Pec6c',
      'client_secret': 'test client secret',
    }

12. Next I am going to create a static js folder within the checkout/static folder structure. Then within the new js folder I create a Javascript file called stripe_elements.js which I am then going to populate with some js code which first gets the stripe public key and the client secret from the template using a little jquery. These script elements contain the values that we need as their text - so we can get these by getting their ids and using the .text function. I also slice off the first and last character on each since they'll have quotation marks from the context that I don't want to show:

var stripe_public_key = $('#id_stripe_public_key').text().slice(1, -1);
var client_secret = $('#id_client_secret').text().slice(1, -1);

13. Then finally, underneath the 2 x new variables, I create a variable using my Stripe public key using:

var stripe = Stripe(stripe_public_key);

14. Next, I can use this to create an instance of Stripe Elements:

var elements = stripe.elements();

15. Then use that to create a card element:

var card = elements.create('card');

16. Then finally, I mount the card element to the div that I previously created for card-element:

card.mount('#card-element');

17. The card element can also accept a style argument, I am going to use the var style and invalid basic styles from the Stripe js docs and then tweak accordingly:

var style = {
    base: {
        color: '#000',
        fontFamily: '"PT Serif", serif',
        fontSmoothing: 'antialiased',
        fontSize: '16px',
        '::placeholder': {
            color: '#aab7c4'
        }
    },
    invalid: {
        color: '#dc3545',
        iconColor: '#dc3545'
    }

18. I copy some basic css styles for the Stripe Elements from the Stripe documentation, as below, and paste these into the checkout.css file:

.StripeElement,
.stripe-style-input {
  box-sizing: border-box;
  height: 40px;
  padding: 10px 12px;
  border: 1px solid transparent;
  border-radius: 0px;
  background-color: white;
  box-shadow: 0 1px 3px 0 #e6ebf1;
  -webkit-transition: box-shadow 150ms ease;
  transition: box-shadow 150ms ease;
}

.StripeElement--focus,
.stripe-style-input:focus,
.stripe-style-input:active {
  box-shadow: 0 1px 3px 0 #cfd7df;
}

.StripeElement--webkit-autofill {
  background-color: #fefde5 !important;
}

.stripe-style-input::placeholder {
    color: #aab7c4;
}

19. Once the css and javascript is in place, I load up my dev server and go to Checkout to see the new payment information we have coded in. I want to test that it picks up invalid card numbers if a full card number isn't entered. However, I am not seeing the payment information in Checkout as I would expect:

![Payment Information Not Showing on Checkout](/static/images/Stripe/Screenshot%20payment%20information%20not%20showing%20on%20checkout.png)

20. I inspect the page on devtools and can see that the Javascript for stripe_elements.js isn't being loaded anywhere so take a look at my checkout.html file again and can see I haven't included it in the postloadjs block so I add this now:

{% block postloadjs %}
    {{ block.super }}
    {{ stripe_public_key|json_script:"id_stripe_public_key" }}
    {{ stripe_client_secret|json_script:"id_client_secret" }}
    <script src="{% static 'checkout/stripe_elements/js/stripe_elements.js' %}"></script>
{% endblock %}

21. This still isn't loading so I consult ChatGPT who advises that the Stripe script is wrong in my base.html template, it should be:

<script src="https://js.stripe.com/v3/"></script>

22. However, this still isn't loading on the screen. I inspect on devtools and see what it is saying in the console and find the below errors:

Failed to load resource: the server responded with a status of 404 (Not Found)Understand this error
checkout/:1 Refused to execute script from 'http://127.0.0.1:8000/static/checkout/stripe_elements/js/stripe_elements.js' because its MIME type ('text/html') is not executable, and strict MIME type checking is enabled.

23. ChatGPT advises that the cause of the issue is this path in my template:

{% static 'checkout/stripe_elements/js/stripe_elements.js' %}

24. It recommends fixing it by updating the script path in my template to:

<script src="{% static 'checkout/js/stripe_elements.js' %}"></script>

25. I update this and run my dev server again and can now see the card element field is loading successfully and is responsive:

![Payment Information Showing on Checkout](/static/images/Stripe/Screenshot%20card%20element%20now%20showing.png)

26. I have been following Code Institute in their Boutique Ado project for setting up Stripe, so will need to update my stipe_elements.js code as below like they have done so that the styling on the card element will work:

var card = elements.create('card', {style: style});

27. I refresh this again and everything matches up now:

![Stripe Payment Stylings](/static/images/Stripe/Screenshot%20stripe%20payment%20stylings.png)

28. I switch Debug to False and run a collectstatic before committing my changes to Github and Heroku.

---

## Stripe - Adding functionality to Card Element

1. First I will need to add a listener on the card element for the change event and everytime it changes, I will check and see if there are any errors:

// Handle Realtime Validation Errors on Card Element */
card.addEventListener('change', function (event) (
    var errorDiv = document.getElementById('card-errors');
))

2. If so then we will display them in the card errors div that I created by the card element on the checkout html page. This will make it clearer to the user what the issue is if they have an error when using the payment system. The error is rendered from Stripe with an icon next to it:

// Handle Realtime Validation Errors on Card Element */
card.addEventListener('change', function (event) (
    var errorDiv = document.getElementById('card-errors');
    if (event.error) {
        var html = `
            <span class="icon" role="alert">
                <i class="fas fa-times"></i>
            </span>
            <span>${event.error.message}</span>
        `;
        $(errorDiv).html(html);
    } else {
        errorDiv.textContent = '';        
    }
});

3. If i rerun my server now and go to payment, its clear what is wrong when nothing is entered, etc.. This works in steps. It will first create the Stripe paymentIntent from the Checkout view. Next, Stripe returns client_secret, which is returned to the template. Then in the Javascript on the client side, it uses the client_secret variable to call confirmCardPayment() and verifies the card number. 
The next thing needed is a function to calculate the current bag total in the view. I can do this using the bag_contents function in contexts.py. I go to my checkout/views file and import this at the top of the file using:

from shoppingbag.contexts import bag_contents

4. Next, I update my function for checkout so that I include the bag_contents data in a variable within the function. I call the variable current_bag:

current_bag = bag_contents(request)

5. Directly under the new line of code, I also add the below to get the total, doing this by getting the grand_total key from the current_bag variable:

total = current_bag('grand_total')

6. Then beneath this I add the code for a stripe_total as Stripe will require the amount to charge as an integer. I create a variable called stripe_total and multiply the total by a hundred and round it to 0 decimal places using the round function:

stripe_total = round(total * 100)

7. Once I have done this, I install Stripe using the below cmd:

pip3 install stripe

8. I add this to my requirements.txt file once I can see this has successfully installed in the terminal using the below cmd. I open the file and check it is now showing there.

pip3 freeze > requirements.txt

9. I then import Stripe at the top of my views.py file in my checkout app:

import stripe

10. I will also import settings from django.conf as I will be needing these soon:

from django.conf import settings

11. Once the views file is saved, I am going to go to my settings file and add a few things. At the bottom of the file, I am going to add a setting called STRIPE_CURRENCY which I will give a value of usd for the time being:

STRIPE_CURRENCY = 'usd'

12. Then directly below it, I create another two. One for STRIPE_PUBLIC_KEY which we will get from the environment by giving it an empty default value and the same is true for the second we will create which is STRIPE_SECRET_KEY. We get these from the environment because even though the public key is already in Github from my last commit, we don't want the secret key in there because the secret key can be used to do everything on stripe including creating charges, making payments, issuing refunds and even updating the account information. So the client secret key needs to be kept out of version control. 

STRIPE_PUBLIC_KEY = os.getenv('STRIPE_PUBLIC_KEY', '')
STRIPE_SECRET_KEY = os.getenv('STRIPE_SECRET_KEY', '')

13. Next, I set the environment variable up for my STRIPE_SECRET_KEY and STRIPE_PUBLIC_KEY in my env.py file. 

14. Now that I have set up my variables and updated my settings, I can create my paymentIntent in my checkout/views file. Within my checkout function, I first set the variables for the public and secret keys at the top of the file:

stripe_public_key = settings.STRIPE_PUBLIC_KEY
stripe_secret_key = settings.STRIPE_SECRET_KEY

15. Then underneath my stripe_total variable, I set the secret key on stripe:

stripe.api_key = stripe_secret_key

16. Then below this, I can create the paymentIntent with stripe.paymentintent.create giving it the amount and currency. For the time being I will just print this value out

    intent = stripe.PaymentIntent=create(
        amount=stripe_total,
        currency=settings.STRIPE_CURRENCY,
    )

    print(intent)

17. I reload my page on the dev server and go to the checkout page to see what I am working with but I am presented with a server 500 error. I turn Debug to True and reload to see what the issue is. The error is as below:

![Checkout Error dict](/static/images/Stripe/Screenshot%20checkout%20error%20dict.png)

18. I consult ChatGPT as I have not come across this error before and it advises that I have used the wrong parentheses for my dictionary in my current_bag grand_total function and advises me to update this to:

current_bag['grand_total'] 

19. I go to my checkout/views file and update the code accordingly and then reload my checkout page. However, I am now presented with a new error:

NameError at /checkout/
name 'stripe_secret_key' is not defined
Request Method:	GET
Request URL:	http://127.0.0.1:8000/checkout/
Django Version:	6.0.2
Exception Type:	NameError
Exception Value:	
name 'stripe_secret_key' is not defined
Exception Location:	C:\Users\leila\OneDrive\Desktop\Documents\vscode-projects\working_out_gym\checkout\views.py, line 20, in checkout
Raised during:	checkout.views.checkout

20. I realise that my settings file has not saved with the variable information for my stripe public key and secret key so update this again as below:

STRIPE_PUBLIC_KEY = os.getenv('STRIPE_PUBLIC_KEY', '')
STRIPE_SECRET_KEY = os.getenv('STRIPE_SECRET_KEY', '')

21. I refresh the page but I am still getting the same error. I consult ChatGPT who advises I haven't defined the key as a variable in my checkout function so need to add the below at the top of the function:

stripe_public_key = settings.STRIPE_PUBLIC_KEY
stripe_secret_key = settings.STRIPE_SECRET_KEY

22. I refresh the page again but this time I receive the following error and straight away I know it is that the settings file didn't save earlier with this variable added so I readd and then reload the page:

AttributeError at /checkout/
'Settings' object has no attribute 'STRIPE_CURRENCY'

23. It is now not showing the payment section at all so I inspect the page on devtools and can see the following error in the console:

Uncaught SyntaxError: Unexpected token '(' (at stripe_elements.js:24:50)

24. I take a look at my stripe_elements.js file and realise that the open curly bracket that should be opening the statment is just a standard bracket so update this and then hard reload the page and can see the card element again. 

25. I am now going to go back to my contexts file and update it so that my public key uses the variable set higher up the file:

      'stripe_public_key': stripe_public_key,

26. I also update the client secret to the below using intent:

'client_secret': intent.client_secret,

27. Finally I will add a convenient message which alerts you if you forget to set your public key:

if not stripe_public_key:
    messages.warning(request, 'Stripe public key is missing. Did you forget to set it in your environment?')

---    

## Stripe - Building Checkout Flow

1. Now that I have set up my view to return the correct secrets, the last step to get this working is to add an event listener to the payment forms submit event. I am going to copy the Stripe docs code for submitting a payment and paste this into my current stripe_elements.js file after making some tweaks as per Code Institute's Boutique Ado:

// Handle form submit
var form = document.getElementById('payment-form');

form.addEventListener('submit', function(ev) {
    ev.preventDefault();
    card.update({ 'disabled': true});
    $('#submit-button').attr('disabled', true);
    stripe.confirmCardPayment(clientSecret, {
        payment_method: {
            card: card,
        }
    }).then(function(result) {
        if (result.error) {
            var errorDiv = document.getElementById('card-errors');
            var html = `
                <span class="icon" role="alert">
                <i class="fas fa-times"></i>
                </span>
                <span>${result.error.message}</span>`;
            $(errorDiv).html(html);
            card.update({ 'disabled': false});
            $('#submit-button').attr('disabled', false);
        } else {
            if (result.paymentIntent.status === 'succeeded') {
                form.submit();
            }
        }
    });
});

2. Now this is in place I can test the basic functionality of my payment method on my site. I rerun the page and then go to checkout and populate the payment form. I use the following number to produce a successful card payment as this is the test Stripe card number for successful payments: 4242 4242 4242 4242:

![Payment information populated](/static/images/Stripe/Screenshot%20populating%20checkout%20info.png)

3. I click 'Complete Order' after populating the payment information but the page has frozen and doesn't appear to be doing anything. I can see this error in my terminal:

[01/Apr/2026 17:38:10] "GET /static/checkout/js/stripe_elements.js HTTP/1.1" 304 0

4. I turn debug to true and refresh and try and complete the order but the page is just frozen. I have a look in devtools at the error and this is what I can see:

stripe_elements.js:47 Uncaught ReferenceError: clientSecret is not defined
    at HTMLFormElement.<anonymous> (stripe_elements.js:47:31)

5. I query this with ChatGPT who advises that my template reference to client_secret is incorrect as is using the wrong variable name, I need to change:

{{ stripe_client_secret|json_script:"id_client_secret" }}

To:

{{ client_secret|json_script:"id_client_secret" }}

- I also need to update my javascript as that is using the wrong variable also:

stripe.confirmCardPayment(clientSecret, {

To:

stripe.confirmCardPayment(clientSecret, {42

6. To see if this has now worked, as all the order information has gone now after hitting complete order, I go to my Stripe dashboard and go to Transactions and can see the purchase has gone through:

![Stripe successful transaction](/static/images/Stripe/Screenshot%20successful%20transaction.png)

7. I change Debug back to False, run collectstatic and then commit my changes to Git and Heroku.

8. Even though I have verified that the form on the checkout page was submitted with the order to Stripe and that I am able to make payments on the site to Stripe, the form data isn't being submitted anywhere as my checkout view doesn't have any handling in place for the POST method so I am going to update checkout/views to include this now so that when the user submits their payment information it will create their order in the database and redirect them to a success page.

9. In my checkout views in the checkout function, under my key variables, I check whether the method is POST using the belown and add the current code into an else block to handle the GET requests:

if request.method == 'POST':
else:

10. Then within the code we have just set for the POST method, I copy and paste the code I have to get the shopping bag and paste this on the first line:

    if request.method == 'POST':
        shoppingbag = request.session.get('bag', {})

    else: 

11. Next, I put the form data for the order into a dictionary, borrowing the code from Code Institute's Boutique Ado:

form_data = {
            'full_name': request.POST['full_name'],
            'email': request.POST['email'],
            'phone_number': request.POST['phone_number'],
            'country': request.POST['country'],
            'postcode': request.POST['postcode'],
            'town_or_city': request.POST['town_or_city'],
            'street_address1': request.POST['street_address1'],
            'street_address2': request.POST['street_address2'],
            'county': request.POST['county'],
}

12. Then below the dictionary for form_data, I create an instance of the form using the form data and if the form is valid then I save the order:

 order_form = OrderForm(form_data)
        if order_form.is_valid():
            order = order_form.save()

13. Then below this, I iterate through the bag items to create each line item in the shopping bag. I am going to borrow Code Institute's code for this. This first gets the product ID from the bag and then if its value is an integer then we know we're working with an item that doesn't have sizes so the quantity will only include item data. Otherwise if it does have a size then it iterates through all sizes and creates the apppropriate line item. Then in the unlikely case that the product isn't found then an error message is given to the user and the order is deleted and the user is returned to the shopping bag page:

            for item_id, item_data in bag.items():
                try:
                    product = Product.objects.get(id=item_id)
                    if isinstance(item_data, int):
                        order_line_item = OrderLineItem(
                            order=order,
                            product=product,
                            quantity=item_data,
                        )
                        order_line_item.save()
                    else:
                        for size, quantity in item_data['items_by_size'].items():
                            order_line_item = OrderLineItem(
                                order=order,
                                product=product,
                                quantity=quantity,
                                product_size=size,
                            )
                            order_line_item.save()
                except Product.DoesNotExist:
                    messages.error(request, (
                        "One of the products in your bag wasn't found in our database. "
                        "Please call us for assistance!")
                    )
                    order.delete()
                    return redirect(reverse('view_bag'))

14. Then at the bottom of the above code, at the same indentation asn the for-loop, we then attach whether or not user wants to save their profile information to this session and redirect them to a new page which I am yet to create which will be called checkout_success.html. The code below passes the order number as an argument, if the order form is invalid then it attaches a message to user to advise them and they will be returned to the checkout page at the bottom of the view with the form errors below:


            request.session['save_info'] = 'save-info' in request.POST
            return redirect(reverse('checkout_success', args=[order.order_number]))
        else:
            messages.error(request, 'There was an error with your form. \
                Please double check your information.')

15. Finally, I need to import the product model from my Merchandise app and the OrderLineItem from the Checkout app so I import these like so below:

from .models import Order, OrderLineItem
from merchandise.models import Product

16. Now thats in place, I can create my checkout_success view in my checkout/views file. I define a new function under my checkout function and call it checkout_success and pass it the parameters of 'request' and 'order number', I add a comment to advise what the function is for

def checkout_success(request, order_number):
    """
    Handle successful checkouts
    """

17. Then I am going to add the below code from Code Institute to save time. This code first checks if the user wants to save their information just like when getting the shopping bag - this will be required once profile app is created. Then the order number created in the previous view will be sent back to the template and attach a success message letting the user know their orderr number and then this will also be sent to the email that they use in the form. Then the shopping bag is deleted from the session as the order has now been stored in the database under the order number so its no longer required. It lastly sets the template and context and renders the template:

    save_info = request.session.get('save_info')
    order = get_object_or_404(Order, order_number=order_number)
    messages.success(request, f'Order successfully processed! \
        Your order number is {order_number}. A confirmation \
        email will be sent to {order.email}.')
    
    if 'bag' in request.session:
        del request.session['bag']

    template = 'checkout/checkout_success.html'
    context = {
        'order': order,
    }
    return render(request, template, context)

18. I now need to import the order model the top of the file and the get_object_or_404 method:

from django.shortcuts import render, redirect, reverse, get_object_or_404

19. Now thats in place, I need to create my url for the new page so I go to checkout/urls and set the below up in my url paths. Using the order number as an argument, it will generate the checkout_success view whenever a new order number is generated:

    path('checkout_success/<order_number>', views.checkout_success, name='checkout_success'),

20. I am now going to create my checkout_success.html template. I create this new file in the templates/checkout folder. The basis of my template will be almost identical to my checkout.html template so I am going to copy the contents from that file and paste into my checkout_success.html file and then make some changes. To save some time I will copy and paste the version from Code Institute Boutique Ado source code. This removes the unneccessary code for bag tools and changes the main text to thank you and and then gives a small message about the user's order. The second row is deleted and replaced with an empty column. The postload js block is removed as there is no extra js in this template. Then in the empty column is where the order summary will be rendered:

{% extends "base.html" %}
{% load static %}

{% block extra_css %}
    <link rel="stylesheet" href="{% static 'checkout/css/checkout.css' %}">
{% endblock %}

{% block page_header %}
    <div class="container header-container">
        <div class="row">
            <div class="col"></div>
        </div>
    </div>
{% endblock %}

{% block content %}
    <div class="overlay"></div>
    <div class="container">
        <div class="row">
            <div class="col">
                <hr>
                <h2 class="logo-font mb-4">Thank You</h2>
                <hr>
                <p class="text-black">Your order information is below. A confirmation email will be sent to <strong>{{ order.email }}</strong>.</p>
            </div>
        </div>

        <div class="row">
            <div class="col-12 col-lg-7"></div>
        </div>
        <div class="row">
			<div class="col-12 col-lg-7 text-right">
				<a href="{% url 'products' %}?category=new_arrivals,deals,clearance" class="btn btn-black rounded-0 my-2">
					<span class="icon mr-2">
						<i class="fas fa-gifts"></i>
					</span>
					<span class="text-uppercase">Now check out the latest deals!</span>
				</a>
			</div>
		</div>
    </div>
{% endblock %}

21. I next need to make a couple of changes to ensure that my signals are working okay. In my checkouts/__init.py__ file I need to tell Django the name of the default config class for the app. This is the class used in the apps.py file where I imported the signals module, without this line in the init file, Django cannot see the custom ready method and the signals won't work:

default_app_config = 'checkout.apps.CheckoutConfig'

22. I am then going to update my Order model's update_total method by adding 'or 0' at the end of the line which aggregates all the line item totals. By including this we stop it from erroring because otherwise it would try to determine if none is less than or equal to the delivery threshold:

        self.order_total = self.lineitems.aggregate(Sum('lineitem_total'))['lineitem_total__sum'] or 0

23. With this updated I can now run my local server and see the page in action. I go to Secure Checkout and then populate my information and the Stripe test card information and then when I hit 'complete order' I am taking to a Server 500 page. I switch debug mode on and then refresh the page to see what is happening.

24. I am receiving the following error message:

NameError at /checkout/
name 'bag' is not defined
Request Method:	POST
Request URL:	http://127.0.0.1:8000/checkout/
Django Version:	6.0.2
Exception Type:	NameError
Exception Value:	
name 'bag' is not defined
Exception Location:	C:\Users\leila\OneDrive\Desktop\Documents\vscode-projects\working_out_gym\checkout\views.py, line 36, in checkout
Raised during:	checkout.views.checkout
Python Executable:	C:\Users\leila\OneDrive\Desktop\Documents\vscode-projects\working_out_gym\.venv\Scripts\python.exe
Python Version:	3.12.8
Python Path:	
['C:\\Users\\leila\\OneDrive\\Desktop\\Documents\\vscode-projects\\working_out_gym',
 'C:\\Program Files\\Python312\\python312.zip',
 'C:\\Program Files\\Python312\\DLLs',
 'C:\\Program Files\\Python312\\Lib',
 'C:\\Program Files\\Python312',
 'C:\\Users\\leila\\OneDrive\\Desktop\\Documents\\vscode-projects\\working_out_gym\\.venv',
 'C:\\Users\\leila\\OneDrive\\Desktop\\Documents\\vscode-projects\\working_out_gym\\.venv\\Lib\\site-packages']
Server time:	Thu, 02 Apr 2026 12:12:34 +0000

25. I go to the offending line in question and update 'bag.items' to 'shoppingbag.items' and refresh. This has removed the previous error and generated a new one:

AttributeError at /checkout/
'Product' object has no attribute 'price'
Request Method:	POST
Request URL:	http://127.0.0.1:8000/checkout/
Django Version:	6.0.2
Exception Type:	AttributeError
Exception Value:	
'Product' object has no attribute 'price'
Exception Location:	C:\Users\leila\OneDrive\Desktop\Documents\vscode-projects\working_out_gym\checkout\models.py, line 71, in save
Raised during:	checkout.views.checkout
Python Executable:	C:\Users\leila\OneDrive\Desktop\Documents\vscode-projects\working_out_gym\.venv\Scripts\python.exe
Python Version:	3.12.8
Python Path:	
['C:\\Users\\leila\\OneDrive\\Desktop\\Documents\\vscode-projects\\working_out_gym',
 'C:\\Program Files\\Python312\\python312.zip',
 'C:\\Program Files\\Python312\\DLLs',
 'C:\\Program Files\\Python312\\Lib',
 'C:\\Program Files\\Python312',
 'C:\\Users\\leila\\OneDrive\\Desktop\\Documents\\vscode-projects\\working_out_gym\\.venv',
 'C:\\Users\\leila\\OneDrive\\Desktop\\Documents\\vscode-projects\\working_out_gym\\.venv\\Lib\\site-packages']
Server time:	Thu, 02 Apr 2026 12:13:56 +0000

26. This is likely due to me using a different variable for price. I have a look at my contexts file to see what I set this as. I need to use ProductVariant model as this is where I have set the price of my products in my app. I update 'Product' to 'ProductVariant' on the offending line of code above and I also import the model at the top of the file:

from merchandise.models import Product, ProductVariant

27. I refresh my page again but this time I am receiving this error:

DoesNotExist at /checkout/
ProductVariant matching query does not exist.
Request Method:	POST
Request URL:	http://127.0.0.1:8000/checkout/
Django Version:	6.0.2
Exception Type:	DoesNotExist
Exception Value:	
ProductVariant matching query does not exist.
Exception Location:	C:\Users\leila\OneDrive\Desktop\Documents\vscode-projects\working_out_gym\.venv\Lib\site-packages\django\db\models\query.py, line 639, in get
Raised during:	checkout.views.checkout
Python Executable:	C:\Users\leila\OneDrive\Desktop\Documents\vscode-projects\working_out_gym\.venv\Scripts\python.exe
Python Version:	3.12.8
Python Path:	
['C:\\Users\\leila\\OneDrive\\Desktop\\Documents\\vscode-projects\\working_out_gym',
 'C:\\Program Files\\Python312\\python312.zip',
 'C:\\Program Files\\Python312\\DLLs',
 'C:\\Program Files\\Python312\\Lib',
 'C:\\Program Files\\Python312',
 'C:\\Users\\leila\\OneDrive\\Desktop\\Documents\\vscode-projects\\working_out_gym\\.venv',
 'C:\\Users\\leila\\OneDrive\\Desktop\\Documents\\vscode-projects\\working_out_gym\\.venv\\Lib\\site-packages']
Server time:	Thu, 02 Apr 2026 12:23:38 +0000

28. I then need to update my OrderLineModel to use ProductVariant instead of Product:

self.lineitem_total = self.product_variant.price * self.quantity

29. I replace the code for product in OrderLineItem with the code for ProductVariant:

product_variant = models.ForeignKey(ProductVariant, null=False, blank=False, on_delete=models.CASCADE)

30. I import the ProductVariant model into the file from merchandise app:

from merchandise.models import Product, ProductVariant

31. However, I refresh the page and this is still not resolving me to checkout_success.:


Request Method:	POST
Request URL:	http://127.0.0.1:8000/checkout/
Django Version:	6.0.2
Exception Type:	DoesNotExist
Exception Value:	
ProductVariant matching query does not exist.
Exception Location:	C:\Users\leila\OneDrive\Desktop\Documents\vscode-projects\working_out_gym\.venv\Lib\site-packages\django\db\models\query.py, line 639, in get
Raised during:	checkout.views.checkout
Python Executable:	C:\Users\leila\OneDrive\Desktop\Documents\vscode-projects\working_out_gym\.venv\Scripts\python.exe
Python Version:	3.12.8
Python Path:	
['C:\\Users\\leila\\OneDrive\\Desktop\\Documents\\vscode-projects\\working_out_gym',
 'C:\\Program Files\\Python312\\python312.zip',
 'C:\\Program Files\\Python312\\DLLs',
 'C:\\Program Files\\Python312\\Lib',
 'C:\\Program Files\\Python312',
 'C:\\Users\\leila\\OneDrive\\Desktop\\Documents\\vscode-projects\\working_out_gym\\.venv',
 'C:\\Users\\leila\\OneDrive\\Desktop\\Documents\\vscode-projects\\working_out_gym\\.venv\\Lib\\site-packages']
Server time:	Thu, 02 Apr 2026 12:27:58 +0000

32. I query this with ChatGPT who asks me to add the below print statement before my for loop for item_id:

print("BAG CONTENTS:", shoppingbag)

- We add it here because this is where the error is occurring in our code and this print statement will show exactly what item_id values are being used.

- Next I re-run the dev server and go through checkout again. I scroll through the feedback on my terminal and find the below code:

BAG CONTENTS: {'9177': 1, '11659': {'items_by_size': {'m': 1}}, '9698': {'items_by_size': {'m': 2}}, '11469': {'items_by_size': {'m': 1}}}

- This tells ChatGPT that these are Product ID's and not ProductVariant ID's which is why my code will be breaking. I need to update the below code from:

product = ProductVariant.objects.get(id=item_id)

- To the below so that it bridges the Product > Variant inside checkout so it doesn't crash:

product = Product.objects.get(id=item_id)
product_variant = product.variants.first()

- It also advises me to update the below on my checkoutviews:

order_line_item = OrderLineItem(
    order=order,
    product_variant=product_variant,
    quantity=item_data,
)

- And:

for size, quantity in item_data['items_by_size'].items():
    order_line_item = OrderLineItem(
        order=order,
        product_variant=product_variant,
        quantity=quantity,
        product_size=size,
    )

- There are also a number of bugs it has identified. For instance I need to update my exception to use ProductVariant instead of Product in the below code:

except Product.DoesNotExist:

- Then I need to update my function that returns the string to:

def __str__(self):
    return f'SKU {self.product_variant.sku} on order {self.order.order_number}'

33. After making these tweaks I reload my server and try to go through checkout again. However, I am recieiving the below error:

ProgrammingError at /checkout/
column "product_variant_id" of relation "checkout_orderlineitem" does not exist
LINE 1: INSERT INTO "checkout_orderlineitem" ("order_id", "product_v...
                                                          ^
Request Method:	POST
Request URL:	http://127.0.0.1:8000/checkout/
Django Version:	6.0.2
Exception Type:	ProgrammingError
Exception Value:	
column "product_variant_id" of relation "checkout_orderlineitem" does not exist
LINE 1: INSERT INTO "checkout_orderlineitem" ("order_id", "product_v...
                                                          ^
Exception Location:	C:\Users\leila\OneDrive\Desktop\Documents\vscode-projects\working_out_gym\.venv\Lib\site-packages\django\db\backends\utils.py, line 105, in _execute
Raised during:	checkout.views.checkout
Python Executable:	C:\Users\leila\OneDrive\Desktop\Documents\vscode-projects\working_out_gym\.venv\Scripts\python.exe
Python Version:	3.12.8
Python Path:	
['C:\\Users\\leila\\OneDrive\\Desktop\\Documents\\vscode-projects\\working_out_gym',
 'C:\\Program Files\\Python312\\python312.zip',
 'C:\\Program Files\\Python312\\DLLs',
 'C:\\Program Files\\Python312\\Lib',
 'C:\\Program Files\\Python312',
 'C:\\Users\\leila\\OneDrive\\Desktop\\Documents\\vscode-projects\\working_out_gym\\.venv',
 'C:\\Users\\leila\\OneDrive\\Desktop\\Documents\\vscode-projects\\working_out_gym\\.venv\\Lib\\site-packages']
Server time:	Thu, 02 Apr 2026 15:42:21 +0000

34. I realise that I have made changes to the product model that I haven't migrated so I makemigrations but I am seeing the below message when I run this:

 python3 manage.py makemigrations
It is impossible to add a non-nullable field 'product_variant' to orderlineitem without specifying a default. This is because the database needs something to populate existing rows.
Please select a fix:
 1) Provide a one-off default now (will be set on all existing rows with a null value for this column)
 2) Quit and manually define a default value in models.py.

 - I cancel this as I want a cleaner approach to the code. I decide to delete my Postgre SQL database and rebuild it. I install Postgre SQL locally using the following link:

(https://www.postgresql.org/download/windows/)

- I click the download installer link and choose the latest version for Windows and download the installer. Once its finished downloading, I then run the installer and click next, leaving most options at default. I enter the superuser password for my fitnessguru account and click next, next and install the software. Then I create a new file to store the local database that I am going to build with the updated models in a new local_settings.py file in my project folder.

- I request a new PostgreSQL database link from Code Institute on this link: (https://dbs.ci-dbs.net/) 

- Once I have a new database link, I populate my database information in local_settings.py as below but with the information in my new database link:

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'your_db_name',
        'USER': 'your_username',
        'PASSWORD': 'your_password',
        'HOST': 'your_host',
        'PORT': '5432',
    }
}

- At the bottom of my settings.py file, I add the following code:

try:
    from .local_settings import *
except ImportError:
    pass

- Then finally I add the file to my .gitignore file to protect it from being published to Github.

- I now try to run makemigrations and migrate but still seeing the same prompt asking for a default value to be provided. I delete all migration files in checkout, merchandise and shoppingbag leaving just __init__.py.

- I update my local_settings.py with the below code, replacing the text in the brackets with my new Code Institute database link:

import dj_database_url

DATABASES = {
    'default': dj_database_url.parse(
        ''
    )
}

- I now run my makemigrations and migrate successfully.

- As the database has been reset, all of my products have also been removed from the database so I need to readd these again using the fixtures file cleanly. To do this, I locate the 2 x fixtures files in my Merchandise app: merchandise/fixtures/categories.json and merchandise/fixtures/products.json. Then I run the following cmds in this order as categories is the parent as products.json depends on categories:

python manage.py loaddata categories
python manage.py loaddata products

- However, when I run loaddate for products it has failed with the error:

"server closed the connection unexpectedly. This probably means the server terminated abnormally before or while processing the request."

- I consult ChatGPT about this who recommends regenerating clean fixtures file using the below cmd as it currently contains productvariants in here:

python manage.py dumpdata merchandise.Product --indent 2 > merchandise/fixtures/products.json

- I then run the loaddata for categories:

python manage.py loaddata categories

- And then the fixture for Products:

python manage.py loaddata products

- However, this error with:

UnicodeDecodeError: 'utf-8' codec can't decode byte 0xff in position 0: invalid start byte

- I check my products.json file and its currently encoded with UTF-16 so I update this to UTF-8, save the file and then try to run loaddata on categories and products again. However, looking in my products.json file it appears to be empty so in the process of regenerating the fixtures in my project it appears to be have corrupted the file.

- I first check that my local_settings.py has the correct DATABASE settings with the new PostgreSQL link which it does. I run makemigrations and migrate to make sure that the database is clean and not waiting on any migrations but no changes need to be made. I then run the below cmd to load the categories:

python manage.py loaddata categories

- Then once this has ran successfully, I run the below in my terminal to confirm that the categories are correctly loaded:

python manage.py shell
>>> from merchandise.models import Category
>>> Category.objects.all()

- This returns the following results so it appears as though Category has loaded successfully:

<QuerySet [<Category: Womens Crop Tops>, <Category: Womens Sports Bras>, <Category: Womens Leggings>, <Category: Womens Ss Tops>, <Category: Headwear>, <Category: Womens Sleeveless Tops>, <Category: Womens Shorts>, <Category: Socks>, <Category: Bags>, <Category: Womens Pullovers>, <Category: Womens Jackets / Outerwear>, <Category: Womens Ls Tops>, <Category: Womens Pants>, <Category: Accessories>, <Category: Womens Underwear>, <Category: Womens Bottoms>, <Category: mens unisex Bottoms>, <Category: Mens Hoodie>, <Category: Mens Pants>, <Category: Mens Ss Tops>, '...(remaining elements truncated)...']>

- I then need to recreate the corrupted json file for products using:

python manage.py dumpdata merchandise.Product --indent 2 > merchandise/fixtures/products.json

- This is failing to recreate the file as my database is empty. I decide to recreate the fixtures using my Kaggle dataset. ChatGPT provides me with the below script which I populate into a create_fixtures.py file in the root of my project. This will create the json files for categories, product and ProductVariant:

import csv
import json

INPUT_CSV = "gymshark_products.csv"

categories = {}
products = {}
variants = []

category_map = {}
product_map = {}

category_id = 1
product_id = 1
variant_id = 1

with open(INPUT_CSV, newline='', encoding='utf-8') as csvfile:
    reader = csv.DictReader(csvfile)

    for row in reader:
        # --- CATEGORY ---
        category_name = (row.get("product_type") or "Uncategorized").strip()

        if category_name not in category_map:
            category_map[category_name] = category_id

            categories[category_id] = {
                "model": "merchandise.category",
                "pk": category_id,
                "fields": {
                    "name": category_name,
                    "slug": category_name.lower().replace(" ", "-"),
                }
            }

            category_id += 1

        cat_id = category_map[category_name]

        # --- PRODUCT ---
        product_key = row["handle"]  # UNIQUE + CLEAN

        if product_key not in product_map:
            product_map[product_key] = product_id

            variant_title = row.get("variant_title", "")
            has_sizes = "/" in variant_title  # simple heuristic

            products[product_id] = {
                "model": "merchandise.product",
                "pk": product_id,
                "fields": {
                    "title": row["title"],
                    "handle": row["handle"],
                    "slug": row["handle"],  # safe since unique
                    "category": cat_id,
                    "vendor": row.get("vendor", ""),
                    "tags": row.get("tags", ""),
                    "image_src": row.get("image_src", ""),
                    "has_sizes": has_sizes,
                    "is_active": True,
                }
            }

            product_id += 1

        prod_id = product_map[product_key]

        # --- VARIANT ---
        variant = {
            "model": "merchandise.productvariant",
            "pk": variant_id,
            "fields": {
                "product": prod_id,
                "variant_title": row.get("variant_title", ""),
                "sku": row.get("sku") or None,
                "price": float(row.get("price") or 0),
                "inventory_quantity": int(row.get("inventory_quantity") or 0),
                "image_src": row.get("image_src", ""),
                "is_active": True,
            }
        }

        variants.append(variant)
        variant_id += 1

--- SAVE FILES ---
with open("categories.json", "w", encoding="utf-8") as f:
    json.dump(list(categories.values()), f, indent=2)

with open("products.json", "w", encoding="utf-8") as f:
    json.dump(list(products.values()), f, indent=2)

with open("variants.json", "w", encoding="utf-8") as f:
    json.dump(variants, f, indent=2)

print("✅ Fixtures generated successfully!")

- I populate the file with this script and then run the following:

python create_fixtures.py

- Fixtures runs successfully is returned in the terminal so I then create my json files using:

python manage.py loaddata categories.json
python manage.py loaddata products.json
python manage.py loaddata variants.json

- However, when I run the loaddate for categories,json file it says the categories already exist and then the product.json file fails to run as a result. The cleanest approach now would be to reset the database and start fresh again. To reset the database, I run:

python manage.py flush

- Then to reload everything clean I run the loaddata cmds on the fixture files again:

python manage.py loaddata categories.json

- However, upon running the loaddata categories.json I am receiving the below error:

django.db.utils.IntegrityError: Problem installing fixture 'C:\Users\leila\OneDrive\Desktop\Documents\vscode-projects\working_out_gym\merchandise\fixtures\categories.json': Could not load merchandise.Category(pk=48): duplicate key value violates unique constraint "merchandise_category_slug_key"
DETAIL:  Key (slug)=(womens-socks) already exists.

- I consult ChatGPT about this who advises adding the below to my create_fixtures.py script underneath my imports as my model produces a unique slug and my fixtures need to match this:

from django.utils.text import slugify

existing_category_slugs = set()

def unique_slug(name, existing_slugs):
    base = slugify(name) or "category"
    slug = base
    i = 1

    while slug in existing_slugs:
        i += 1
        slug = f"{base}-{i}"

    existing_slugs.add(slug)
    return slug

- Then in the category section of my script, I need to replace this:

"slug": category_name.lower().replace(" ", "-"),

- With this:

slug = unique_slug(category_name, existing_category_slugs)

- I also need to add existing_category_slugs to my global variables so I add this above category_id at the top of my file:

existing_category_slugs = set()

- Now I will flush the database again using the below cmd and typing yes on the prompt to delete the files:

python manage.py flush

- Once that has ran successfully, I create my fixtures again using:

python create_fixtures.py

- Once that says it has generated the fixtures successfully, I can recreate the categories.json file using:

python manage.py loaddata categories

- This installs successfully so I then populate the products.json file using:

python manage.py loaddata products

- This finally installs successfully too, so I load my final json file for variants using:

python manage.py loaddata variants

- This installs successfully too. 

- I run my page on my local dev server and try going to my admin pages first but realise that my superuser has been deleted as a result of the database purge. I run the below cmd and then populate the details for my superuser:

python manage.py createsuperuser

- I login to the admin page with the details and check that the changes I have made haven't created any unwanted duplicates, this looks fine, there is a section for variants now under Merchandise but this is to be expected:

![Admin Panel okay after db rebuild](/static/images/Stripe/Screenshot%20admin%20okay%20after%20rebuild%20-%20no%20duplicates.png)

- However, when I then look in each of the menus for Product, Categories and Variant there is only one item in each of these lists. I consult ChatGPT about this who advises that the script looks as though it is treating all rows as the same product with this line of code:

product_key = row["handle"]

- I check what data is actually in my database currently using the below:

python manage.py shell

from merchandise.models import Product, ProductVariant

Product.objects.count()

- This returns 1, I then run the below to see what the ProductVariant count is which is also 1:

ProductVariant.objects.count()

- ChatGPT recommends updating the product_key to make it more robust and not rely only on a handle but also on a fallback. I update the below in my create_fixtures script:

product_key = row["handle"]

To:

product_key = (row.get("handle") or row.get("title") or "").strip().lower()

- Now I need to flush my database again using:

python manage.py flush#

- I delete the current fixture json files I had previously created and then run:

python create_fixtures.py

- This tells me the fixtures have generated successfully, I can see the three files again in the root of my project folder. I check the products.json file and this is still only showing 1 product. I consult ChatGPT who advises it is an indentation issue in my create_fixtures.py file and to resolve to the below then delete the fixtures and run again:

with open(INPUT_CSV, newline='', encoding='utf-8') as csvfile:
    reader = csv.DictReader(csvfile)

    for row in reader:
        # --- CATEGORY ---
        category_name = (row.get("product_type") or "Uncategorized").strip()

        if category_name not in category_map:
            category_map[category_name] = category_id

            slug = unique_slug(category_name, existing_category_slugs)

            categories[category_id] = {
                "model": "merchandise.category",
                "pk": category_id,
                "fields": {
                    "name": category_name,
                    "slug": slug,
                }
            }

            category_id += 1

        cat_id = category_map[category_name]

        # --- PRODUCT ---
        product_key = (row.get("handle") or row.get("title") or "").strip().lower()

        if product_key not in product_map:
            product_map[product_key] = product_id

            variant_title = row.get("variant_title", "")
            has_sizes = "/" in variant_title

            products[product_id] = {
                "model": "merchandise.product",
                "pk": product_id,
                "fields": {
                    "title": row["title"],
                    "handle": row["handle"],
                    "slug": row["handle"],
                    "category": cat_id,
                    "vendor": row.get("vendor", ""),
                    "tags": row.get("tags", ""),
                    "image_src": row.get("image_src", ""),
                    "has_sizes": has_sizes,
                    "is_active": True,
                }
            }

            product_id += 1

        prod_id = product_map[product_key]

        # --- VARIANT ---
        variant = {
            "model": "merchandise.productvariant",
            "pk": variant_id,
            "fields": {
                "product": prod_id,
                "variant_title": row.get("variant_title", ""),
                "sku": row.get("sku") or None,
                "price": float(row.get("price") or 0),
                "inventory_quantity": int(row.get("inventory_quantity") or 0),
                "image_src": row.get("image_src", ""),
                "is_active": True,
            }
        }

        variants.append(variant)
        variant_id += 1

- I update create_fixtures as above and then delete the three files and run:

python create_fixtures.py

- Now when I check the products.json file, I can see a large number of items in here as I would expect to see. Now the json files are loaded with the correct data, I can run my loaddata cmds:

python manage.py loaddata categories
python manage.py loaddata products
python manage.py loaddata variants

- These all run successfully and I can see the correct data in each of these files now.

35. I now want to remove the local_settings.py file and store my new database url in my env.py file in the DATABASE_URL in place of the old link. I first need to update my DATABASE_URL variable with the new link. I do this now in env.py. Then in settings.py I make sure that the below is set which it is:

import dj_database_url

DATABASES = {
    'default': dj_database_url.parse(os.environ.get("DATABASE_URL"))
}

35. I can now delete the below block from my settings.py file:

try:
    from .local_settings import *
except ImportError:
    pass

36. Then I can run migrations on my new database using:

python manage.py migrate

- This advises there is no migrations to apply. To confirm that it has already run these I run:

python manage.py showmigrations

- This shows me a list with x's in the checkboxes so it looks safe to say it has made the migrations. 

37. Now I can run the loaddata cmds on my json files as below:

python manage.py loaddata categories
python manage.py loaddata products
python manage.py loaddata variants

38. These all load in successfully showing that the correct amount of items has been installed this time. I now want to verify that I am using the new correct database so run:

from django.db import connection

39. I create superuser again using: 

python manage.py createsuperuser

40. I run my page on my local server and go to admin panel and check the menus for categories, products and variants.

- My categories list looks correct, as you can see from the below screenshot. The categories list loads, there are no duplicates (the slug list is unique) and names look clean:

![DB rebuild admin category list](/static/images/Stripe/Screenshot%20db%20rebuild%20category%20list.png)

- If I click into one of the categories then I can save this without any errors:

![DB rebuild admin category item saved](/static/images/Stripe/Screenshot%20%20db%20rebuild%20category%20items%20saving%20without%20error.png)

- If I click into Products then it is showing me a list of over 7000 products now as opposed to 1. The titles look correct and they have a category assigned:

![DB rebuild admin product list](/static/images/Stripe/Screenshot%20db%20rebuild%20product%20admin%20list.png)

- If I click into some of the products then I see they have a slug generated and an img and also Product Variants associated with the product:

![DB rebuild product admin](/static/images/Stripe/Screenshot%20DB%20rebuild%20product%20item.png)

- Then if I go into my ProductVariants list, this looks good too. There are multiple variants now showing in the list, each variant appears linked to a product when I have clicked into them, the prices are all different and the inventory values look realistic:

![DB rebuild productvariants admin](/static/images/Stripe/Screenshot%20db%20rebuild%20product%20variants.png)

41. I now want to test out the actual page and make sure that nothing has broken here. I first check the Homepage is rendering correctly which it is. I test out the feedback form which sends the form and gives a success message to say it is sent.

- I next check out the Discussion Board. This all looks good, it has actually retained all of the data from the previously posted posts and users which is good. I can post a new post and delete previous posts so I am happy with this.

- Next I check the Merchandise page, I can still see all the categories in my Navbar menu under the main Merchandise menu. If I click into these then I am taken to a page with the relevant products. My menu which sorts into price and categories both work okay too. If I click on the individual items then these are loading up nicely. I can add the items to my bag and then toast success shopping bag preview renders on the page nicely, it shows the correct images and the Secure Checkout button directs me to the checkout page.

- I next view my Shopping Bag. This is rendering all the products I have just added nicely. I can update the size and quantities on items or delete them if I choose.

- If I click Secure Checkout then this takes me tothe Checkout page with the shipping and payment forms along with the order summary. I can populate the forms and then click complete order and this is where I was falling down last time.

42. I am going to update my DATABASE_URL in my app's settings on Heroku as I am going to commit my changes after doing my database rebuild and change of URL. First, I will go to Heroku.com and go to Working-out-gym's settings and update the Config Vars for DATABASE_URL to my new url. 

43. Once I have updated this on Heroku, I then need to push my code using the below cmds which will push to Github and then deploy and build on Heroku:

git add .
git commit -m "Switch to new database"
git push origin main
git push heroku main

44. Once these have run successfully, I then need to run the migrations on Heroku using:

heroku run python manage.py migrate -a working-out-gym

- However, this advises that there is no migrations to apply.

45. I then run the below cmds in the written order so loaddata from the new fixtures created onto the Heroku app:

heroku run python manage.py loaddata categories -a working-out-gym
heroku run python manage.py loaddata products -a working-out-gym
heroku run python manage.py loaddata variants -a working-out-gym

46. These all run successfully and install the products on Heroku, so I launch the app now to see how this is looking. The homepage looks fine, I log into the admin panel with the superuser credentials and these are letting me logon. I can see 'Products', 'ProductVariants' and 'Categories' under the merchandise section of my admin panel. If I click inton these the lists look okay and the items themselves seem fine also.

- I then check the frontend of the production app, looking at Merchandise and making sure all sorting menus work. These are all working okay. I can add products to the bag and then go the shopping bag and then when I try to complete checkout to go to the checkout page I am getting the following error:

AuthenticationError at /checkout/
You did not provide an API key. You need to provide your API key in the Authorization header, using Bearer auth (e.g. 'Authorization: Bearer YOUR_SECRET_KEY'). See https://stripe.com/docs/api#authentication for details, or we can help at https://support.stripe.com/.
Request Method:	GET
Request URL:	https://working-out-gym-aaf119c10db9.herokuapp.com/checkout/
Django Version:	6.0.2
Exception Type:	AuthenticationError
Exception Value:	
You did not provide an API key. You need to provide your API key in the Authorization header, using Bearer auth (e.g. 'Authorization: Bearer YOUR_SECRET_KEY'). See https://stripe.com/docs/api#authentication for details, or we can help at https://support.stripe.com/.
Exception Location:	/app/.heroku/python/lib/python3.12/site-packages/stripe/_api_requestor.py, line 353, in handle_error_response
Raised during:	checkout.views.checkout
Python Executable:	/app/.heroku/python/bin/python
Python Version:	3.12.13
Python Path:	
['/app/.heroku/python/bin',
 '/app',
 '/app/.heroku/python/lib/python312.zip',
 '/app/.heroku/python/lib/python3.12',
 '/app/.heroku/python/lib/python3.12/lib-dynload',
 '/app/.heroku/python/lib/python3.12/site-packages']
Server time:	Fri, 03 Apr 2026 11:17:15 +0000

- I consult ChatGPT who advises that as my Stripe keys are set in an env.py file, I need to set these up on the config vars setttings of my Heroku app so it can see them. To set these I run the following cmds but with the key values applied:

heroku config:set STRIPE_PUBLIC_KEY=your_public_key -a working-out-gym
heroku config:set STRIPE_SECRET_KEY=your_secret_key -a working-out-gym

- I reload my page on Heroku and see if it is letting me checkout now but it is saying the API key is invalid. I am going to go back to resolving payment checkout flow on my dev server and see if fixing the full flow will then fix on Heroku once changes are deployed to it.

47. I load up my dev server and go to Checkout and I am receiving the following error after populating the forms and hitting 'complete order':

ProgrammingError at /checkout/
column "product_variant_id" of relation "checkout_orderlineitem" does not exist
LINE 1: INSERT INTO "checkout_orderlineitem" ("order_id", "product_v...
                                                          ^
Request Method:	POST
Request URL:	http://127.0.0.1:8000/checkout/
Django Version:	6.0.2
Exception Type:	ProgrammingError
Exception Value:	
column "product_variant_id" of relation "checkout_orderlineitem" does not exist
LINE 1: INSERT INTO "checkout_orderlineitem" ("order_id", "product_v...
                                                          ^
Exception Location:	C:\Users\leila\OneDrive\Desktop\Documents\vscode-projects\working_out_gym\.venv\Lib\site-packages\django\db\backends\utils.py, line 105, in _execute
Raised during:	checkout.views.checkout
Python Executable:	C:\Users\leila\OneDrive\Desktop\Documents\vscode-projects\working_out_gym\.venv\Scripts\python.exe
Python Version:	3.12.8
Python Path:	
['C:\\Users\\leila\\OneDrive\\Desktop\\Documents\\vscode-projects\\working_out_gym',
 'C:\\Program Files\\Python312\\python312.zip',
 'C:\\Program Files\\Python312\\DLLs',
 'C:\\Program Files\\Python312\\Lib',
 'C:\\Program Files\\Python312',
 'C:\\Users\\leila\\OneDrive\\Desktop\\Documents\\vscode-projects\\working_out_gym\\.venv',
 'C:\\Users\\leila\\OneDrive\\Desktop\\Documents\\vscode-projects\\working_out_gym\\.venv\\Lib\\site-packages']
Server time:	Fri, 03 Apr 2026 10:37:09 +0000

48. ChatGPT advises that this is a database mismatch, the error means that the column 'product_variant_id' does not exist so Django is trying to insert into a column that my database doesn't have. My models have the following code:

product_variant = models.ForeignKey(...)

- But my database table has the below which doesn't have that column:

checkout_orderlineitem

- The database was never updated with a migration so I need to create migrations:

python manage.py makemigrations

- However, this runs and still picks up no changes. I consult ChatGPT who advises I need to rollback the migrations for the checkout app and then reapply them using the below cmds:

python manage.py migrate checkout zero
python manage.py migrate checkout

- These both run successfully so I run the below now to verify thatb the column exists. First I run:

python manage.py shell

- Then I run the below:

from django.db import connection

cursor = connection.cursor()
cursor.execute("SELECT column_name FROM information_schema.columns WHERE table_name = 'checkout_orderlineitem';")

columns = cursor.fetchall()
print(columns)

- This prints out the 'product_variant_id' column in the printout so I am going to test my checkout again. I can checkout now but notice that the size selector has been removed from the product_details and checkout views. The only thing that has really changed code wise is the fixtures so I troubleshoot this with ChatGPT who recommends querying the database in a Django shell using:

python manage.py shell

from merchandise.models import Product

Product.objects.filter(has_sizes=True).count()

- The value returned is 27 so this isn't right. ChatGPT recommends replacing the below code in my create_fixtures.py script:

variant_title = row.get("variant_title", "")
has_sizes = "/" in variant_title

With:

variant_title = row.get("variant_title", "")

size_keywords = ["xs", "s", "m", "l", "xl", "xxl"]
variant_title_clean = (variant_title or "").lower()

has_sizes = any(size in variant_title_clean for size in size_keywords)

- Once I have updated my create_fixtures code, I then rerun the script using:

python create_fixtures.py

- I then flush my database out after confirming the json files have created and populated correctly. I click yes to the prompt on flushing the database:

python manage.py flush

- Then once that has ran, I migrate the data:

python manage.py migrate

- Then i run the loaddata cmds on each of the newly created json files as below:

python manage.py loaddata categories
python manage.py loaddata products
python manage.py loaddata variants

- Once each of the above cmds has ran and installed each of the three datasets successfully, I then oipen a Django shell with the below cmd and then query the data to see if the amount of products with sizes has drastically increased as I am expecting it to:

python manage.py shell

from merchandise.models import Product
Product.objects.filter(has_sizes=True).count()

- This is now returning a value of 7396 which is much better. So I run my app on my dev server again to see what is coming through now on the product details and checkout pages and make sure size displays and is a changeable field for the user. I can see the size selector again on clothing now but I check non clothing items and these also have the size selector so I update my create_fixtures script with the below in place of my current code:

variant_title = row.get("variant_title", "")
category_name = (row.get("product_type") or "").lower()

clothing_keywords = ["shirt", "top", "tank", "hoodie", "jacket", "shorts", "leggings", "joggers"]
size_keywords = ["xs", "s", "m", "l", "xl", "xxl"]

variant_title_clean = variant_title.lower()

is_clothing = any(word in category_name for word in clothing_keywords)
has_size_word = any(size in variant_title_clean for size in size_keywords)

has_sizes = is_clothing and has_size_word

- I run my create_fixtures script again using:

python create_fixtures.py

- The terminal tells me this has generated successfully so I flush the database again using the below and typing yes to the prompt:

python manage.py flush

- I then migrate the tables in the database using:

python manage.py migrate

- And finally run the following cmds to install the new fixture files:

python manage.py loaddata categories
python manage.py loaddata products
python manage.py loaddata variants

- These finish running successfully so I launch my dev server to see if this has brought back sizes and retained checkout success functionality too. I can see that the size selector is now back only on the appropriate items, I have looked at non-clothing items and they do not have a size anymore. I can add items of different sizes to the bag and check these out successfully now.

- Now that the code is all working as it should be, I want to now reflect these changes on Heroku also. I first commit the changes to Github and Heroku using:

git add .
git commit -m "Fix size detection logic and regenerate fixtures"
git push origin main
git push heroku main

- I now need to reset my Heroku database as it is still using the old bad data. I do this using the following cmd and typing yes on the prompt:

heroku run python manage.py flush -a working-out-gym

- Next, I run migrations on my Heroku database using:

heroku run python manage.py migrate -a working-out-gym

- Finally, I load the new fixtures on Heroku using:

heroku run python manage.py loaddata categories -a working-out-gym
heroku run python manage.py loaddata products -a working-out-gym
heroku run python manage.py loaddata variants -a working-out-gym

49. I now test my production app on Heroku but I realise that the price is now removed. I check the dev version and this is the same. I consult ChatGPT about this who advise that on my Product page my template tries product.price but this doesn't exist and shows 'price unavailable' as when I am in the Merchandise listing view all products show 'price unavailable'. Then in my bag I am using item.price but I am not pulling from the variant so it defaults to 0.

50. The first step I do is confirm that my data is correct:

python manage.py shell

from merchandise.models import ProductVariant
ProductVariant.objects.exclude(price=0).count()

- This returns a value of 0

51. ChatGPT recommends that I update my create_fixtures file as below and remove the code beneathe it for now:

with open(INPUT_CSV, newline="", encoding="utf-8") as csvfile:
    reader = csv.DictReader(csvfile)

    for row in reader:
        print(row.get("price"))
        break

52. I then run:

python create_fixtures.py

- This gives: '35.00' as the value returned in the terminal so I delete the two new lines of code in the script and replace with the loop I had previously:

for row in reader:
    # --- CATEGORY ---
    category_name = (row.get("product_type") or "Uncategorized").strip()

    if category_name not in category_map:
        category_map[category_name] = category_id

        slug = unique_slug(category_name, existing_category_slugs)

        categories[category_id] = {
            "model": "merchandise.category",
            "pk": category_id,
            "fields": {
                "name": category_name,
                "slug": slug,
            },
        }

        category_id += 1

    cat_id = category_map[category_name]

- I confirm that there is a price being generated in the variants.json file against the products so ChatGPT recommends a proper reload of the database. To do this, I first run the below and type yes:

python manage.py flush

- I then re-run migrations:#

python manage.py migrate

- Next, I reload all the fixtures again:

python manage.py loaddata categories
python manage.py loaddata products
python manage.py loaddata variants

- These install successfully, and then I run the following in the terminal to verify the data, expecting to see a number surplus of 7000:

python manage.py runserver

from merchandise.models import ProductVariant
ProductVariant.objects.exclude(price=0).count()

- This returns the result of 44830. I will now run the local dev server and see if this has resolved the pricing issue. It has brought the price back but removed the size selector again.

53. I run the Django shell again and check if my data still has sizes using:

python manage.py shell

from merchandise.models import Product

Product.objects.filter(has_sizes=True).count()

- This returns a value of 4453 so the data is fine and I don't need to regenerate my fixtures again.

54. Then back in the shell I run the below to check a specific product for sizes:

p = Product.objects.filter(has_sizes=True).first()
p.variants.all()[:5]

- This returns the following results meaning that the issue is due to my template logic:

<QuerySet [<ProductVariant: Gymshark Vital Crop Top - Base Green Marl — Extra Small>, <ProductVariant: Gymshark Vital Crop Top - Base Green Marl — Small>, <ProductVariant: Gymshark Vital Crop Top - Base Green Marl — Medium>, <ProductVariant: Gymshark Vital Crop Top - Base Green Marl — Large>, <ProductVariant: Gymshark Vital Crop Top - Base Green Marl — Extra Large>]>

- I need to update my product_detail.html template to use variants directly and not just the has_sizes variable. To do this, I will replace the below code, which uses hardcoded sizes and ignores my ProductVariant data:

{% with product.has_sizes as s %}
{% if s %}
    <div class="me-2 mb-2" style="min-width: 100px;">
        <label for="id_product_size" class="form-label"><strong>Size:</strong></label>
        <select class="form-control form-control-sm rounded-0" name="product_size" id="id_product_size">
            <option value="xs">XS</option>
            <option value="s">S</option>
            <option value="m" selected>M</option>
            <option value="l">L</option>
            <option value="xl">XL</option>
        </select>
    </div>
{% endif %}
{% endwith %}

= With this: 

{% if product.variants.all %}
    <div class="me-2 mb-2" style="min-width: 150px;">
        <label for="id_variant" class="form-label"><strong>Size:</strong></label>
        <select class="form-control form-control-sm rounded-0" name="variant_id" id="id_variant">
            {% for variant in product.variants.all %}
                <option value="{{ variant.id }}">
                    {{ variant.variant_title }} - £{{ variant.price }}
                </option>
            {% endfor %}
        </select>
    </div>
{% endif %}

- Then after making the updates to the product_detail template, I need to update shoppingbag/views and update my add_to_bag function so that it uses the correct logic to obtain the sizes of the clothing items. My current bag structure is as follows so it is breaking the sizes and prices:

bag = {
    product_id: {
        "items_by_size": {
            "m": 2
        }
    }
}

- The correct structure should be:

bag = {
    product_id: {
        "items_by_size": {
            "m": 2
        }
    }
}

- The first thing I do is import ProductVariant at the top of the file with Product:

from merchandise.models import Product, ProductVariant

- ChatGPT recommends replacing my add_to_bag function code with the below so I do this:

def add_to_bag(request, product_id):
    quantity = int(request.POST.get('quantity', 1))
    redirect_url = request.POST.get('redirect_url', '/')
    variant_id = request.POST.get('variant_id')

    variant = get_object_or_404(ProductVariant, pk=variant_id)

    bag = request.session.get('bag', {})

    variant_id = str(variant_id)

    if variant_id in bag:
        bag[variant_id] += quantity
        messages.success(
            request,
            f'Updated {variant.product.title} ({variant.variant_title}) quantity to {bag[variant_id]}'
        )
    else:
        bag[variant_id] = quantity
        messages.success(
            request,
            f'Added {variant.product.title} ({variant.variant_title}) to your bag'
        )

    request.session['bag'] = bag
    return redirect(redirect_url)

- It also recommends that I update my adjust_bag function code with the below so I update this as well:

def adjust_bag(request, product_id):
    quantity = int(request.POST.get('quantity'))
    variant_id = request.POST.get('variant_id')

    bag = request.session.get('bag', {})
    variant_id = str(variant_id)

    variant = get_object_or_404(ProductVariant, pk=variant_id)

    if quantity > 0:
        bag[variant_id] = quantity
        messages.success(
            request,
            f'Updated {variant.product.title} ({variant.variant_title}) quantity to {quantity}'
        )
    else:
        bag.pop(variant_id)
        messages.success(
            request,
            f'Removed {variant.product.title} ({variant.variant_title}) from your bag'
        )

- And finally replace my remove_from_bag with the below code:

def remove_from_bag(request, product_id):
    try:
        variant_id = request.POST.get('variant_id')
        variant_id = str(variant_id)

        bag = request.session.get('bag', {})

        variant = get_object_or_404(ProductVariant, pk=variant_id)

        bag.pop(variant_id)

        messages.success(
            request,
            f'Removed {variant.product.title} ({variant.variant_title}) from your bag'
        )

        request.session['bag'] = bag
        return HttpResponse(status=200)

    except Exception as e:
        messages.error(request, f'Error removing item: {e}')
        return HttpResponse(status=500)

- I now also need to make sure that I am using variant_id in place of product_size anywhere that the latter is on my templates. I update the product_size line of code in shoppingbag.html to:

<select name="variant_id" value="{{ item.variant.id }}"" class="form-control form-control-sm rounded-0">

- I test adding to the bag to see what happens, expecting a break but I can now see the size selector again, however, the sizes also contain the price so this isn't right:

![Size selector also contains price](/static/images/Stripe/Screenshot%20price%20and%20size%20selector%20showing%20together.png)

55. I consult ChatGPT about this and thery advise me to remove 'From £' in if statement for price on my product_detail template. I update this from:

{% if product.from_price %}
    <p class="lead fw-bold">From £{{ product.from_price }}</p>
{% endif %}


To: 

<p class="lead fw-bold">Select a size to see price</p>

- Also in the file, I remove price from the dropdownm by removing the below line of code froim the option dropdown for sizes:

- £{{ variant.price }}

- I refresh my dev server to see how this is looking now and can see this has removed the price from the dropdown now:

![Size selector no longer has price](/static/images/Stripe/Screenshot%20price%20now%20removed%20from%20size%20dropdow.png)

- I have tested checking out an order and this looks good now apart from the fact that the navbar styles aren't rendering on checkout_success page. I consult ChatGPT about this who advises that the issue is in my checkout_successs.html code below:

<div class="overlay"></div>

- ChatGPT thinks this is sitting on top of my navbar and stopping it from rendering so I remove the line of code from checkout_success and then test checkout again to see if this change is right. I have  tried adding a couple of different items to the bag and they were adding successfully but now I am receiving errors of 'Product Not Found'. I have now tried cancelling and rerunning my server but I am getting the following page now:

![Page not found error](/static/images/Stripe/Screenshot%20page%20not%20found%20error.png)

- I consult ChatGPT about this is not a routing issue but that my home view is trying to fetch a product that doesn't exist. It believes that my home/views is likely using the below code:

Product.objects.get(...)

- After some troubleshooting, ChatGPT has identified the issue as being my bag context processor. I have recently switched variables in the fixtures data from product_size > variant_id. It thinks that the session may be containing old and new strucutural data that are conflicting with one another. To resolve this, it recommends replacing the below line of code from:

product = get_object_or_404(Product, pk=product_id)

To: 

product = Product.objects.filter(pk=product_id).first()
if not product:
    continue

- I reload the page with the new code but it is not right, the indentation is wrong and the for loop wasn't inside the function so I have rectified this by replacing the contexts.py file with the below:

from decimal import Decimal
from django.conf import settings
from merchandise.models import Product

def bag_contents(request):
    bag_items = []
    total = Decimal('0.00')
    product_count = 0
    bag = request.session.get('bag', {})

    for product_id, item_data in bag.items():
        product = Product.objects.filter(pk=product_id).first()

        if not product:
            continue  # skip broken/old session items

        if isinstance(item_data, int):
            # Non-sized product
            quantity = item_data
            price = product.variants.first().price if product.variants.exists() else Decimal('0.00')
            subtotal = quantity * price
            total += subtotal
            product_count += quantity

            bag_items.append({
                'product_id': product_id,
                'quantity': quantity,
                'product': product,
                'price': price,
                'subtotal': subtotal,
            })

        else:
            # Product with sizes
            for size, quantity in item_data['items_by_size'].items():
                price = product.variants.first().price if product.variants.exists() else Decimal('0.00')
                subtotal = quantity * price
                total += subtotal
                product_count += quantity

                bag_items.append({
                    'product_id': product_id,
                    'quantity': quantity,
                    'product': product,
                    'size': size,
                    'price': price,
                    'subtotal': subtotal,
                })

    # Delivery calculations
    if total < settings.FREE_DELIVERY_THRESHOLD:
        delivery = total * Decimal(settings.STANDARD_DELIVERY_PERCENTAGE / 100)
        free_delivery_delta = settings.FREE_DELIVERY_THRESHOLD - total
    else:
        delivery = 0
        free_delivery_delta = 0

    grand_total = total + delivery

    return {
        'bag_items': bag_items,
        'total': total,
        'product_count': product_count,
        'delivery': delivery,
        'free_delivery_delta': free_delivery_delta,
        'free_delivery_threshold': settings.FREE_DELIVERY_THRESHOLD,
        'grand_total': grand_total,
    }

- I then run Django shell and import the session using the below cmd and then delete all session objects too:

python manage.py shell
from django.contrib.sessions.models import Session
Session.objects.all().delete()

- I test my Homepage to see if this is now rendering but when I add this product to the bag it is not showing it as being added to the bag even though it says it has but then when I go to the bag I cannot see the product I added to the bag, it is showing me different products:

![Product added to the bag](/static/images/Stripe/Screenshot%20items%20added%20to%20bag%20not%20right.png)

![Shopping Bag Preview](/static/images/Stripe/Screenshot%20items%20added%20to%20bag%20not%20right%20shoppingbag%20preview.png)

![Checkout showing wrong items added](/static/images/Stripe/Screenshot%20wrongn%20products%20added%20to%20bag.png)

- I consult ChatGPT about this who advises that the following line of code in my context processor is the problem:

price = product.variants.first().price

- I am not storing the variant which was selected as my bag currently uses:

bag = {
    "product_id": {
        "items_by_size": {
            "XS": 1
        }
    }
}

- However, now I have changed how the database reads in the data, i.e. Product has many variants and each variant has size and price variables to it. But my bag only stores size and doesn't store variant_id so Django just grabs:

product.variants.first()

- This could contain the wrong sizing, pricing or variant so on. Also my products is looking wrong as it is still holding on to old data. I send over my shopppingbag views file to ChatGPT and it advises that my python code for the bag looks like this:

{
    "12": 2,   # variant_id
    "45": 1
}

- But my contexts.py file contradicts this as it is treating variant_id as the product_id, so when the completely wrong product is being returned. To resolve this I need to update my contexts file as below:


from decimal import Decimal
from django.conf import settings
from merchandise.models import ProductVariant


def bag_contents(request):
    bag_items = []
    total = Decimal('0.00')
    product_count = 0
    bag = request.session.get('bag', {})

    for variant_id, quantity in bag.items():
        variant = ProductVariant.objects.filter(pk=variant_id).first()

        if not variant:
            continue  # skip broken/old session items

        product = variant.product
        price = variant.price
        subtotal = quantity * price

        total += subtotal
        product_count += quantity

        bag_items.append({
            'variant_id': variant_id,
            'quantity': quantity,
            'product': product,
            'variant': variant,
            'size': variant.variant_title,
            'price': price,
            'subtotal': subtotal,
        })

    # Delivery calculations
    if total < settings.FREE_DELIVERY_THRESHOLD:
        delivery = total * Decimal(settings.STANDARD_DELIVERY_PERCENTAGE / 100)
        free_delivery_delta = settings.FREE_DELIVERY_THRESHOLD - total
    else:
        delivery = Decimal('0.00')
        free_delivery_delta = Decimal('0.00')

    grand_total = total + delivery

    return {
        'bag_items': bag_items,
        'total': total,
        'product_count': product_count,
        'delivery': delivery,
        'free_delivery_delta': free_delivery_delta,
        'free_delivery_threshold': settings.FREE_DELIVERY_THRESHOLD,
        'grand_total': grand_total,
    }

- This completely deletes the Product import, product_id logic, items_by_size logic so that my system is 100% variant based. I update my contexts file with this code and then run the below to clear my sessions again:

python manage.py shell

from django.contrib.sessions.models import Session
Session.objects.all().delete()

- However, I am still seeing issues so I consult ChatGPT again who advises that the form action in my template is wrong - it is still using product_id whereas it should be using variant_id, so I update this now from:

action="{% url 'shoppingbag:adjust_bag' item.product_id %}"

To:

action="{% url 'shoppingbag:adjust_bag' item.product_id %}"

- Then still in the form I add the below line just below the csrf token import, I add the new line of code to add a hidden variant_id input:

<input type="hidden" name="variant_id" value="{{ item.variant_id }}">

- Then I want to remove the size dropdown in place of a simple display usiong this line of code:

<p class="my-0">
    <strong>Size:</strong> {{ item.size|upper }}
</p>

- Then I want to fix the quantity buttons using variant_id again, so I replace the following code:

<p class="my-0">
    <strong>Size:</strong> {{ item.size|upper }}
</p>

With:

data-item_id="{{ item.product.id }}"
id="id_qty_{{ item.product.id }}"


- I then need to fix the remove button as it is currently:

data-item_id="{{ item.variant_id }}"
id="id_qty_{{ item.variant_id }}"

I change this to:

<a
  class="remove-item text-danger float-right"
  id="remove_{{ item.variant_id }}"
>
  <small>Remove</small>
</a>

- I also need to update my 'remove-item' Javascript code with the below:

$('.remove-item').click(function(e) {
    var csrfToken = "{{ csrf_token }}";
    var itemId = $(this).attr('id').split('remove_')[1];
    var url = "{% url 'shoppingbag:remove_from_bag' 0 %}".replace('0', itemId);

    var data = {
        'csrfmiddlewaretoken': csrfToken,
        'variant_id': itemId
    };

    $.post(url, data)
     .done(function() {
         location.reload();
     });
});

- Finally I update my template tag for SKU so it is using the variant id over product id:

{{ item.variant.sku }}

- After making all these changes to the template so that it matches my new views, I run my page on the dev server again. Everything looks a lot better. I can add a product to the bag and it adds the correct product now, I can see this product at the checkout and it has a price. The only thing that I have an issue with is that the user isn't being shown a price on the product detail page. They have to select a size and add to bag before they can then see the price in the shopping bag preview or if they go to the checkout view:

![Product Details page doesn't show price](/static/images/Stripe/Screenshot%20price%20doesn't%20show.png)

![Price shows in shopping bag preview](/static/images/Stripe/Screenshot%20price%20shown%20in%20shopping%20bag%20preview.png)

- After consulting with ChatGPT I decide to go back to showing a 'From price' as this is what will work best with the data I have used in my fixtures as there is so many variants. To do this, I need to update my product_detail view in the merchandise app, to add the below line of code under my product variable within the function:

min_price = product.variants.order_by('price').first().price if product.variants.exists() else None

- Then I need to update my context dictionary with the below so it reads the new code:

'min_price': min_price,

- Finally, in my product_detail.html template, I replace the text for 'Select a size to see a price' with this new code so that it looks at our new min_price context:

{% if min_price %}
    <p class="lead mb-0 text-left font-weight-bold">
        From £{{ min_price|floatformat:2 }}
    </p>
{% endif %}

- Now that I have made these changes, I run my dev server again and see how this is looking now.

![Price shows on product_detail page again](/static/images/Stripe/Screenshot%20price%20now%20shows%20on%20product_detail%20page.png)

- I notice that there oa a stray piece of code on the product_detail page after the footer, so I look for this code in the product_detail.html file and remove it:

{% include 'merchandise/includes/quantity_input_script.html' %}

- Now when I refresh the view looks great:

![Unneccessary tag removed from product detail template](/static/images/Stripe/Screenshot%20unneccessary%20script%20tag%20removed%20from%20product_detail%20template.png)

- I want to test that checkout is still working so I test this now. If I click 'Secure Checkout' then this takes me to the checkout view. I can populate the checkout form with all the relevant details, however, when I click 'Complete Order' I am taken to an error page:

![Error at Checkout product matching query doesn't exist](/static/images/Stripe/Screenshot%20checkout%20product%20matching%20query%20doesn't%20exist%20error.png)

- This is happening because somewhere in my checkout view I am using this code:

product = Product.objects.get(pk=item_id)

- But now I am using:

item_id = variant_id

- I go to my checkout/views file and replace this logic:

for item_id, item_data in bag.items():
    product = Product.objects.get(pk=item_id)#

- With:

for variant_id, quantity in bag.items():
    variant = get_object_or_404(ProductVariant, pk=variant_id)

    order_line_item = OrderLineItem(
        order=order,
        product=variant.product,
        variant=variant,  # if your model supports it
        quantity=quantity,
        lineitem_total=variant.price * quantity,
    )

    order_line_item.save()


- I try to go through Checkout again but this time experience a different error:

![Type error at checkout](/static/images/Stripe/Screenshot%20type%20error%20at%20checkout.png)

- I consult ChatGPT who advises that the error means: OrderLineItem() got unexpected keyword arguments: 'product' but my model doesn't have a product field and my view is trying to do:

OrderLineItem() got unexpected keyword arguments: 'product'

- I need to update my order_line_item context and remove the product_variant=variant, line of code:

order_line_item = OrderLineItem(
    order=order,
    product=variant.product,
    product_variant=variant,
    quantity=quantity,
)

- I update thisn and can now checkout successfully. The next issue I have spotted is that the 'update button' has gone from the checkout view so need to recitfy this before moving on. I go to my shoppingbag.html template and go to the code for the remove button and can see that the code for 'update' has gone. I copy and paste the code for my remove button just above it and tweak accordingly:

<a class="update-link text-info">
  <small>Update</small>
</a>

- I refresh and can see the 'Update' button again, however, when I try using the quantity selector buttons they do not work. I also spot that there is 2 x fields for size with one populated with the selected size and the other is empty. The size field isn't changeable as I would like it to be either. And the quantity and size fields are sitting in the same column which doesn't work so I want to rectify this. Looking at my code in shoppingbag.html I can see that I have this code in my size selector section:

                 <!-- Size selector - ChatGPT -->
                  {% with item.product.has_sizes as s %} {% if s %}
                  <div class="me-2 mb-2" style="min-width: 100px">
                    <label for="id_product_size" class="form-label">
                      <strong>Size:</strong>
                    </label>
                    <p class="my-0">
                      <strong>Size:</strong> {{ item.size|upper }}
                    </p>
                  </div>

- So first thing I need to do is remove the label for element as this is from the old code before I updates fixtures and database. Now when I refresh there is only 1 x size field:

![Extra size field removed](/static/images/Stripe/Screenshot%20extra%20size%20field%20removed%20from%20shoppingbag.png)

- The next thing I want to look at is the fact that the size and quantity fields sit in the same column so I inspect on devtools to see where these two pieces of code sit on the template and can see that they both sit in this div together:

<div class="d-flex align-items-end flex-wrap mb-3">
                  {% with item.product.has_sizes as s %} {% if s %}
                  <div class="me-2 mb-2" style="min-width: 100px">
                    <p class="my-0">
                      <strong>Size:</strong> {{ item.size|upper }}
                    </p>
                  </div>
                  {% endif %} {% endwith %}

                  <!-- Quantity selector -->
                  <div class="me-2 mb-2">
                    <label
                      for="id_qty_{{ item.variant_id }}"
                      class="form-label d-block"
                    >
                      <strong>Quantity:</strong>
                    </label>

- I remove the code for them within the div and replace with the below cleaner layout which will stack them vertically instead of squashing:

                  {% with item.product.has_sizes as s %} {% if s %}
                  <div class="me-2 mb-2" style="min-width: 100px">
                    <p class="my-0">
                      <strong>Size:</strong> {{ item.size|upper }}
                    </p>
                  </div>
                  {% endif %} {% endwith %}

                  <!-- Quantity selector -->
                  <div class="me-2 mb-2">
                    <label
                      for="id_qty_{{ item.variant_id }}"
                      class="form-label d-block"
                    >
                      <strong>Quantity:</strong>
                    </label>
To:

<div class="mb-2">
  <p class="my-0">
    <strong>Size:</strong> {{ item.variant.variant_title|upper }}
  </p>
</div>

<div class="mb-2">
  <label for="id_qty_{{ item.variant_id }}" class="form-label">
    <strong>Quantity:</strong>
  </label>

- I refresh but its still keeping the code in one column. ChatGPT recommends I update my bag_contents contents append statement to include variant so I update the product to:

    'product': variant.product,

- I remove this line of code completely:

            'size': variant.variant_title,

- And update the price and subtotals to:

    'price': variant.price,
    'subtotal': quantity * variant.price,

- I also fix the update totals with the below code in place of what I currently have set:

        subtotal = quantity * variant.price
        total += subtotal
        product_count += quantity

- I need to fix the structure of the shopping bag so that I have a size column in my header, adding another table header column for size into the below code:

<th scope="col">Price</th>
<th scope="col">Size</th>
<th scope="col">Qty</th>
<th scope="col">Subtotal</th>

- Then I need to split the table row as I have one td element doing too much:

<td class="py-3 w-25">
  <!-- size + quantity + form all here -->
</td>

- I remove size from this block:

<td class="py-3 w-25">
  <!-- size + quantity + form all here -->
</td>

- And create a new size column and add this after the price td element:

<p class="my-0">
  <strong>Size:</strong> {{ item.variant.variant_title|upper }}
</p>

- This is giving me errors so I consult ChatGPT who advises I have placed the code wrong in the wrong element so provides me with what full shoppingbag.html should be, I copy this in as below and reload the page:

{% extends "base.html" %}
{% load static %}

{% block page_header %}
<div class="container header-container">
  <div class="row">
    <div class="col"></div>
  </div>
</div>
{% endblock %}

{% block content %}
<div class="container mb-2">
  <div class="row">
    <div class="col">
      <hr />
      <h2 class="logo-font mb-4">Shopping Bag</h2>
      <hr />
    </div>
  </div>

  <div class="row">
    <div class="col">

      {% if bag_items %}
      <div class="table-responsive rounded">
        <table class="table table-sm table-borderless">

          <!-- HEADER -->
          <thead class="text-black">
            <tr>
              <th scope="col">Product</th>
              <th scope="col"></th>
              <th scope="col">Price</th>
              <th scope="col">Size</th>
              <th scope="col">Qty</th>
              <th scope="col">Subtotal</th>
            </tr>
          </thead>

          <!-- ITEMS -->
          <tbody>
          {% for item in bag_items %}
            <tr>

              <!-- Image -->
              <td class="p-3 w-25">
                {% if item.product.image_src %}
                  <img class="img-fluid rounded" src="{{ item.product.image_src }}">
                {% endif %}
              </td>

              <!-- Product Info -->
              <td class="py-3">
                <p class="my-0"><strong>{{ item.product.title }}</strong></p>
                <p class="my-0 small text-muted">SKU: {{ item.variant.sku }}</p>
              </td>

              <!-- Price -->
              <td class="py-3">
                <p class="my-0">£{{ item.price|floatformat:2 }}</p>
              </td>

              <!-- Size -->
              <td class="py-3">
                <p class="my-0">
                  {{ item.variant.variant_title|upper }}
                </p>
              </td>

              <!-- Quantity -->
              <td class="py-3">
                <form
                  class="form update-form"
                  method="POST"
                  action="{% url 'shoppingbag:adjust_bag' item.variant_id %}"
                >
                  {% csrf_token %}
                  <input type="hidden" name="variant_id" value="{{ item.variant_id }}">

                  <div class="input-group input-group-sm" style="width: 120px">

                    <button type="button"
                      class="decrement-qty btn btn-black rounded-0"
                      data-item_id="{{ item.variant_id }}"
                      id="decrement-qty_{{ item.variant_id }}">
                      <i class="fas fa-minus"></i>
                    </button>

                    <input
                      class="form-control text-center qty_input"
                      type="number"
                      name="quantity"
                      value="{{ item.quantity }}"
                      min="1"
                      max="99"
                      data-item_id="{{ item.variant_id }}"
                      id="id_qty_{{ item.variant_id }}"
                    />

                    <button type="button"
                      class="increment-qty btn btn-black rounded-0"
                      data-item_id="{{ item.variant_id }}"
                      id="increment-qty_{{ item.variant_id }}">
                      <i class="fas fa-plus"></i>
                    </button>
                  </div>

                  <div class="mt-2">
                    <a class="update-link text-info"><small>Update</small></a>
                    <a class="remove-item text-danger" id="remove_{{ item.variant_id }}">
                      <small>Remove</small>
                    </a>
                  </div>

                </form>
              </td>

              <!-- Subtotal -->
              <td class="py-3">
                <p class="my-0">£{{ item.subtotal|floatformat:2 }}</p>
              </td>

            </tr>
          {% endfor %}
          </tbody>

          <!-- TOTALS -->
          <tr>
            <td colspan="6" class="pt-5 text-right">
              <h6><strong>Bag Total: £{{ total|floatformat:2 }}</strong></h6>
              <h6>Delivery: £{{ delivery|floatformat:2 }}</h6>
              <h4 class="mt-4">
                <strong>Grand Total: £{{ grand_total|floatformat:2 }}</strong>
              </h4>

              {% if free_delivery_delta > 0 %}
              <p class="mb-1 text-danger">
                You could get free delivery by spending just
                <strong>£{{ free_delivery_delta }}</strong> more!
              </p>
              {% endif %}
            </td>
          </tr>

          <!-- BUTTONS -->
          <tr>
            <td colspan="6" class="text-right">
              <a href="{% url 'merchandise:products' %}"
                 class="btn btn-outline-black rounded-0 btn-lg">
                <i class="fas fa-chevron-left"></i>
                Keep Shopping
              </a>

              <a href="{% url 'checkout' %}"
                 class="btn btn-black rounded-0 btn-lg">
                Secure Checkout
                <i class="fas fa-lock"></i>
              </a>
            </td>
          </tr>

        </table>
      </div>

      {% else %}
        <p class="lead mb-5">Your bag is empty.</p>

        <a href="{% url 'merchandise:products' %}"
           class="btn btn-outline-black rounded-0 btn-lg">
          <i class="fas fa-chevron-left"></i>
          Keep Shopping
        </a>
      {% endif %}

    </div>
  </div>
</div>
{% endblock %}

{% block postloadjs %}
{{ block.super }}

<script>
  $(".update-link").click(function () {
    $(this).closest("form").submit();
  });

  $(".remove-item").click(function () {
    var csrfToken = "{{ csrf_token }}";
    var itemId = $(this).attr("id").split("remove_")[1];
    var url = "{% url 'shoppingbag:remove_from_bag' 0 %}".replace("0", itemId);

    $.post(url, {
      csrfmiddlewaretoken: csrfToken,
      variant_id: itemId,
    }).done(function () {
      location.reload();
    });
  });
</script>

{% endblock %}

- Refreshing the page shows that the shoppingbag looks as I want it to now, with all the fields having their own columns. I do a quick test of everything and find that removing the items from shoppingbag works, however, the quantity selector buttons aren't changing the number on the items in shoppingbag anymore. I realise that my quality_input_script.html is now longer in the shoppingbag template so I add this back in below my postloadjs block:

{% include 'merchandise/includes/quantity_input_script.html' %}

- I reload the page and now can see that the quantity increases/decreases and I can select 'Update' and the quantity is updated and reflected in final shoppingbag view:

![Shopping Bag View and Functionality working](/static/images/Stripe/Screenshot%20shopping%20bag%20view%20fixed%20and%20quantity%20update%20working.png)

55. I have made a lot of changes to the code so I am going to commit my changes here before taking a look at my toast_success html code as it appears to be using wrong code to show my size.

56. After pushing the code to Heroku, I test the app there to make sure that nothing has broken during any of the database rebuilds and changes in the code I have made.

57. Heroku is fine and working the same as the dev version.

58. I go back to my dev version and update the code on my toast_success.html file and look at the code I am using to get the size. This is currently:

          <p class="my-0"><strong>{{ item.product.title }}</strong></p>
          <p class="my-0 small">
            Size: {% if item.product.has_sizes %} 
            {{ item.size|upper }} 
              {% else%} N/A 
              {% endif %}

- I update this to:

          <p class="my-0"><strong>{{ item.product.title }}</strong></p>
          <p class="my-0 small">
            Size: {% if item.product.has_sizes %} 
            {{ item.size|upper }} 
              {% else%} N/A 
              {% endif %}

- I test adding an item to the bag again now and can see this shows size correctly now:

![Toast Success Size not populated correctly](/static/images/Stripe/size%20is%20now%20empty.png)

- However, now there is no size populated at all. I realise I hadn't saved the code so do this now. This is now showing the size correctly in the shoppingbag preview from toast_success.html:

![Toast Success Size populated correctly](/static/images/Stripe/Screenshot%20correct%20size%20now%20showing%20in%20toast%20success%20message.png)

59. Now everything looks good on the shoppingbag and toast messages again, I will go through checkout and complete the order. The checkout page is okay, looks good and lets me populate details and payment forms successfully and lets me complete the order. However, there is no styling being applied so I take a look at this now:

![Checkout_Success no styles being applied](/static/images/Stripe/Screenshot%20checkout%20dev%20version%20styles%20not%20applied#.png)

60. I open devtools and go to the network tab, I can see it is only loading my checkout/static/css/checkout.css file and not the static/css/style.css that applies to the rest of my site. I look at my base.html and can see that I have placed my static css inside my extra_css block so when my checkout_success.html page tries to load the checkout.css file from that extra_css block in the checkout_success.html it overwrites my static styles.css file for the rest of the site. I take the link for my static css in base.html from the extra_css block and place above it instead with a comment:

<!-- MAIN SITE CSS-->
<link rel="stylesheet" href="{% static 'css/style.css' %}" />

<!-- Page-specific CSS -->
{% block extra_css %}{% endblock %}

61. I hard refresh my page and see if this is applying the styles to checkout_success now but I am receiving a server 500 error. I turn Debug mode to true and see what the error is. It says there is a missing endblock tag after my css link in base.html, I add this after the link for static styles.css and reload and this has resolved now. I add some items to bag and then complete checkout and can see the styles are now applying correctly:

![Checkout_Success styles now applied](/static/images/Stripe/Screenshot%20checkout%20success%20looks%20good%20now.png)

62. I turn debug to false, commit my code to Github and Heroku. 

63. I now login to Stripe and check my dashboard to see if all the payments have been coming through when I have been completing my orders. I can see that they have when I click 'Payments' down the left hand side:

![Successful Payments on Stripe](/static/images/Stripe/Screenshot%20payments%20working%20on%20Stripe.png)

64. Next I login to the admin panel of my site as my superuser and check that the orders are being created correctly. I realise that I haven't recreated my superuser since the last db rebuild so I try doing this now but I am receiving an error in the terminal when I try to run the cmd:

KeyboardInterrupt
PS C:\Users\leila\OneDrive\Desktop\Documents\vscode-projects\working_out_gym> python3 manage.py createsuperuser
Traceback (most recent call last):
  File "C:\Users\leila\OneDrive\Desktop\Documents\vscode-projects\working_out_gym\manage.py", line 22, in <module>
    main()
  File "C:\Users\leila\OneDrive\Desktop\Documents\vscode-projects\working_out_gym\manage.py", line 18, in main
    execute_from_command_line(sys.argv)
  File "C:\Users\leila\AppData\Roaming\Python\Python312\site-packages\django\core\management\__init__.py", line 419, in execute_from_command_line
    utility.execute()
  File "C:\Users\leila\AppData\Roaming\Python\Python312\site-packages\django\core\management\__init__.py", line 413, in execute
    self.fetch_command(subcommand).run_from_argv(self.argv)
  File "C:\Users\leila\AppData\Roaming\Python\Python312\site-packages\django\core\management\base.py", line 354, in run_from_argv
    self.execute(*args, **cmd_options)
  File "C:\Users\leila\AppData\Roaming\Python\Python312\site-packages\django\contrib\auth\management\commands\createsuperuser.py", line 79, in execute
    return super().execute(*args, **options)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\leila\AppData\Roaming\Python\Python312\site-packages\django\core\management\base.py", line 393, in execute
    self.check()
  File "C:\Users\leila\AppData\Roaming\Python\Python312\site-packages\django\core\management\base.py", line 419, in check
    all_issues = checks.run_checks(
                 ^^^^^^^^^^^^^^^^^^
  File "C:\Users\leila\AppData\Roaming\Python\Python312\site-packages\django\core\checks\registry.py", line 76, in run_checks
    new_errors = check(app_configs=app_configs, databases=databases)
                 ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\leila\AppData\Roaming\Python\Python312\site-packages\django\core\checks\urls.py", line 13, in check_url_config
    return check_resolver(resolver)
           ^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\leila\AppData\Roaming\Python\Python312\site-packages\django\core\checks\urls.py", line 23, in check_resolver
    return check_method()
           ^^^^^^^^^^^^^^
  File "C:\Users\leila\AppData\Roaming\Python\Python312\site-packages\django\urls\resolvers.py", line 416, in check
    for pattern in self.url_patterns:
                   ^^^^^^^^^^^^^^^^^
  File "C:\Users\leila\AppData\Roaming\Python\Python312\site-packages\django\utils\functional.py", line 48, in __get__
    res = instance.__dict__[self.name] = self.func(instance)
                                         ^^^^^^^^^^^^^^^^^^^
  File "C:\Users\leila\AppData\Roaming\Python\Python312\site-packages\django\urls\resolvers.py", line 602, in url_patterns
    patterns = getattr(self.urlconf_module, "urlpatterns", self.urlconf_module)
                       ^^^^^^^^^^^^^^^^^^^
  File "C:\Users\leila\AppData\Roaming\Python\Python312\site-packages\django\utils\functional.py", line 48, in __get__
    res = instance.__dict__[self.name] = self.func(instance)
                                         ^^^^^^^^^^^^^^^^^^^
  File "C:\Users\leila\AppData\Roaming\Python\Python312\site-packages\django\urls\resolvers.py", line 595, in urlconf_module
    return import_module(self.urlconf_name)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Program Files\Python312\Lib\importlib\__init__.py", line 90, in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "<frozen importlib._bootstrap>", line 1387, in _gcd_import
  File "<frozen importlib._bootstrap>", line 1360, in _find_and_load
  File "<frozen importlib._bootstrap>", line 1331, in _find_and_load_unlocked
  File "<frozen importlib._bootstrap>", line 935, in _load_unlocked
  File "<frozen importlib._bootstrap_external>", line 999, in exec_module
  File "<frozen importlib._bootstrap>", line 488, in _call_with_frames_removed
  File "C:\Users\leila\OneDrive\Desktop\Documents\vscode-projects\working_out_gym\working_out_gym\urls.py", line 24, in <module>
    path("checkout/", include("checkout.urls")),
                      ^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\leila\AppData\Roaming\Python\Python312\site-packages\django\urls\conf.py", line 34, in include
    urlconf_module = import_module(urlconf_module)
                     ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Program Files\Python312\Lib\importlib\__init__.py", line 90, in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "<frozen importlib._bootstrap>", line 1387, in _gcd_import
  File "<frozen importlib._bootstrap>", line 1360, in _find_and_load
  File "<frozen importlib._bootstrap>", line 1331, in _find_and_load_unlocked
  File "<frozen importlib._bootstrap>", line 935, in _load_unlocked
  File "<frozen importlib._bootstrap_external>", line 999, in exec_module
  File "<frozen importlib._bootstrap>", line 488, in _call_with_frames_removed
  File "C:\Users\leila\OneDrive\Desktop\Documents\vscode-projects\working_out_gym\checkout\urls.py", line 2, in <module>
    from . import views
  File "C:\Users\leila\OneDrive\Desktop\Documents\vscode-projects\working_out_gym\checkout\views.py", line 12, in <module>
    import stripe
ModuleNotFoundError: No module named 'stripe'

- I query ChatGPT about this who advises I haven't installed the Stripe module so to do this now using:

pip install stripe

- Once this installs successfully, I then add to my requirements.txt file:

pip3 freeze > requirements.txt

- I notice I am being asked to upgrade pip so do this now and then add to requirements.txt:

python.exe -m pip install --upgrade pip

- I try creating superuser again and this time can do so successfully. I login to the admin panel on the dev console and can see Checkout and Orders:

![Admin Panel Checkout Orders](/static/images/Stripe/Screenshot%20admin%20panel%20orders%20showing.png)

- If I click 'Change' then I am redirected to a page containing a list of the created orders:

![Admin Panel Checkout Orders List](/static/images/Stripe/Screenshot%20admin%20orders%20list.png)

- Then if I click into one of these, then I nothing happens and I just have a loading circle in the browser tab. I consult ChatGPT about this who identifies this line of code in checkout/models as the cause of this:

return f'SKU {self.product_variant.sku} on order {self.order.order_number}'

- in Django admin this can cause multiple database lookups, recursive loading via relationships and admin trying to render many of these at once; especially with inlines. This goes through the following steps which cause it to break:

Django loads the Order
Then loads all lineitems (because of inline)
Then calls __str__() on each one
Each call hits:
self.product_variant.sku (DB lookup)
self.order.order_number (DB lookup)

- I replace this with the below code:

def __str__(self):
    return f'LineItem {self.id}'

- I save the code and restart the server but the orders are still hanging. ChatGPT recommends commenting out the inlines code on my checkout/admin file OrderAdmin class as below:

inlines = (OrderLineItemAdminInline,)

- I comment this out and reload the page and can see the orders now and see these have all the expected line items and the order total and delivery cost are being correctly calculated:

![Admin Panel Checkout Order](/static/images/Stripe/Screenshot%20indivual%20orders%20showing%20in%20admin.png)

- The only issue now is that I cannot edit the quantity and size at the bottom of the orders so look to see how I could make this happen now. ChatGPT advises me to update my OrderLineItemAdminInline as below in checkout/admin:

class OrderLineItemAdminInline(admin.TabularInline):
    model = OrderLineItem
    extra = 0

    # 👇 THIS makes fields editable
    fields = ('product_variant', 'quantity', 'lineitem_total')
    readonly_fields = ('lineitem_total',)


- And in the same file to update my OrderAdmin as below:

class OrderAdmin(admin.ModelAdmin):
    inlines = (OrderLineItemAdminInline,)

    readonly_fields = (
        'order_number',
        'date',
        'delivery_cost',
        'order_total',
        'grand_total',
    )

    fields = (
        'order_number',
        'full_name',
        'email',
        'phone_number',
        'country',
        'postcode',
        'town_or_city',
        'street_address1',
        'street_address2',
        'county',
        'date',
        'delivery_cost',
        'order_total',
        'grand_total',
    )

- It also recommends that I update my save function in checkout/models as it needs to force recalculation when it saves:

def save(self, *args, **kwargs):
    self.lineitem_total = self.product_variant.price * self.quantity
    super().save(*args, **kwargs)
    self.order.update_total()  

- I make the changes and refresh but now the order is hanging before like the last time I had inlines in the code. ChatGPT now recommends updating my OrderLineItemAdminInline class in checkout/admin to:

class OrderLineItemAdminInline(admin.TabularInline):
    model = OrderLineItem
    extra = 0

    fields = ('product_variant', 'quantity', 'lineitem_total')
    readonly_fields = ('lineitem_total',)

    def get_queryset(self, request):
        queryset = super().get_queryset(request)
        return queryset.select_related('product_variant', 'product_variant__product')

- It also advises that my product_variant field is a dropdown and if I have too many variants then it can try loading all of them so to resolve this I need to replace this line of code in my checkout/admin for OrderLineItemAdminLine:

fields = ('product_variant', 'quantity', 'lineitem_total')

To:

autocomplete_fields = ['product_variant']
fields = ('product_variant', 'quantity', 'lineitem_total'


- I then also need to updat my ProductVariantAdmin class search fields code to the below:

search_fields = ['product__name', 'sku']

- I also need to update OrderLineItemAdminInline as below:

class OrderLineItemAdminInline(admin.TabularInline):
    model = OrderLineItem
    extra = 0
    fields = ('product_variant', 'quantity', 'lineitem_total')
    readonly_fields = ('lineitem_total',)
    autocomplete_fields = ['product_variant']

    def get_queryset(self, request):
        return super().get_queryset(request).select_related(
            'product_variant', 'product_variant__product'
        )

- I make these changes and reload the server and find I can now edit the line items on the orders and save these successfully. If I check the checkbox next to an item for 'delete' and click save then it successfully removes that line item.

![Admin Panel Checkout Order Inline Items showing and editable](/static/images/Stripe/Screenshot%20admin%20order%20line%20items%20editable.png)

- I run collectstatic and then commit to Git and Heroku before finalising my checkout success and payment process next.

- I am receiving an error when I try to push my code to Heroku:

remote: The conflict is caused by: remote: The user requested Django==3.2.25 remote: crispy-bootstrap5 0.7 depends on django>=3.2 remote: django-allauth 0.57.2 depends on Django>=3.2 remote: django-crispy-forms 2.5 depends on django>=4.2 remote: remote: Additionally, some packages in these conflicts have no matching distributions available for your environment: remote: django remote: remote: To fix this you could try to: remote: 1. loosen the range of package versions you've specified remote: 2. remove package versions to allow pip to attempt to solve the dependency conflict remote: remote: ERROR: ResolutionImpossible: for help visit https://pip.pypa.io/en/latest/topics/dependency-resolution/#dealing-with-dependency-conflicts remote: remote: ! Error: Unable to install dependencies using pip. remote: ! remote: ! See the log output above for more information. remote: remote: ! Push rejected, failed to compile Python app. remote: remote: ! Push failed remote: remote: ! Push rejected to working-out-gym. remote: To https://git.heroku.com/working-out-gym.git ! [remote rejected] main -> main (pre-receive hook declined

- I consult ChatGPT who advises that this is a dependency conflict and easy to fix. I need to first update my requirements.txt file and replace this line:

django-crispy-forms==2.5

With:

django-crispy-forms==1.14.0

- Then reinstall Crsipyforms locally using:

pip install django-crispy-forms==1.14.0

- I then need to freeze my requirements.txt file again using:

pip install django-crispy-forms==1.14.0

- I commit my code and push again using:

git add requirements.txt
git commit -m "Fix crispy forms version for Django 3.2 compatibility"
git push origin main
git push heroku main

- I have also accidentally committed staticfiles/ which should never be in Git so I add this it .gitignore and then remove from Git using the below cmds in the terminal:

git rm -r --cached staticfiles
git commit -m "Remove staticfiles from repo"
git push origin main

- I can now push my code to Heroku:

git push heroku main

- A quick check over my production app shows everything working as it should.

---

## Checkout Success - Order Summary

1. I first go to my checkout_success html template and inside the empty column below my order information paragraph, I am going to create a bordered wrapper that will go around the order confirmation. Then inside the wrapper I am going to create 4 x rows with full width columns containing small muted text for each of the sections, as below. The first row will be called 'Order Info':

                <div class="order-confirmation-wrapper p-2 border">
                    <div class="row">
                        <div class="col">
                            <small class="text-muted">Order Info</small>
                        </div>    
                    </div>

2. I copy and paste the Order Info div three more times as below, updating 'Order Info' to 'Order Details', 'Delivery Address' and 'Billing Details':

                    <div class="row">
                        <div class="col">
                            <small class="text-muted">Order Details</small>
                        </div>    
                    </div>

                    <div class="row">
                        <div class="col">
                            <small class="text-muted">Delivery Address</small>
                        </div>    
                    </div>

                    <div class="row">
                        <div class="col">
                            <small class="text-muted">Billing Details</small>
                        </div>    
                    </div>

3. Then underneath the Order Info section I create a new single row split into 2 columns: 1/3 and 2/3. The second column will use right-aligned text:

<div class="row">
    <div class="col-12 md-4"></div>
    <div class="col-12 md-4 text-md-right"></div>
</div>

4. I then add a paragraph element to each of the columns. The first column will contain the label for the order number and the second column will display the actual order number:

                        <div class="col-12 md-4">
                            <p class="mb-0 text-black font-weight-bold">Order Number:</p>
                        </div>
                        <div class="col-12 md-4 text-md-right">
                            <p class="mb-0>">{{ order.order_number}}</p>
                        </div>

5. I am then going to copy this entire row and paste back in directly below the Order Number row and change accordingly for the Order Date:

                    <div class="row">
                        <div class="col-12 md-4">
                            <p class="mb-0 text-black font-weight-bold">Order Date:</p>
                        </div>
                        <div class="col-12 md-4 text-md-right">
                            <p class="mb-0>">{{ order.date }}</p>
                        </div>
                    </div>

6. As this is going to be a bit tedious typing out each row, I am going to borrow Code Institute's Boutique Ado code for checkout_success.html and tweak according to my own code and paste this in below the code I have already created for Order Info:

 

          <div class="row">
          <div class="col-12 col-md-4">
            <p class="mb-0 text-black font-weight-bold">Order Number</p>
          </div>
          <div class="col-12 col-md-4 text-md-right">
            <p class="mb-0">{{ order.order_number }}</p>
          </div>
        </div>

        <div class="row">
          <div class="col-12 col-md-4">
            <p class="mb-0 text-black font-weight-bold">Order Date</p>
          </div>
          <div class="col-12 col-md-4 text-md-right">
            <p class="mb-0">{{ order.date }}</p>
          </div>
        </div>

        <div class="row">
          <div class="col">
            <small class="text-muted">Order Details:</small>
          </div>
        </div>

        {% for item in order.lineitems.all %}
        <div class="row">
          <div class="col-12 col-md-4">
            <p class="small mb-0 text-black font-weight-bold">
              {{ item.product.name }}{% if item.product_size %} - Size {{
              item.product_size|upper }}{% endif %}
            </p>
          </div>
          <div class="col-12 col-md-4 text-md-right">
            <p class="small mb-0">
              {{ item.quantity }} @ £{{ item.product.price }} each
            </p>
          </div>
        </div>
        {% endfor %}

        <div class="row">
          <div class="col">
            <small class="text-muted">Delivery Address</small>
          </div>
        </div>

        <div class="row">
          <div class="col-12 col-md-4">
            <p class="mb-0 text-black font-weight-bold">Full Name</p>
          </div>
          <div class="col-12 col-md-4 text-md-right">
            <p class="mb-0">{{ order.full_name }}</p>
          </div>
        </div>

        <div class="row">
          <div class="col-12 col-md-4">
            <p class="mb-0 text-black font-weight-bold">Address 1</p>
          </div>
          <div class="col-12 col-md-4 text-md-right">
            <p class="mb-0">{{ order.street_address1 }}</p>
          </div>
        </div>

        <div class="row">
          <div class="col-12 col-md-4">
            <p class="mb-0 text-black font-weight-bold">Address 2</p>
          </div>
          <div class="col-12 col-md-4 text-md-right">
            <p class="mb-0">{{ order.street_address2 }}</p>
          </div>
        </div>

        <div class="row">
          <div class="col-12 col-md-4">
            <p class="mb-0 text-black font-weight-bold">County</p>
          </div>
          <div class="col-12 col-md-4 text-md-right">
            <p class="mb-0">{{ order.county }}</p>
          </div>
        </div>

        <div class="row">
          <div class="col-12 col-md-4">
            <p class="mb-0 text-black font-weight-bold">Town or City</p>
          </div>
          <div class="col-12 col-md-4 text-md-right">
            <p class="mb-0">{{ order.town_or_city }}</p>
          </div>
        </div>

        <div class="row">
          <div class="col-12 col-md-4">
            <p class="mb-0 text-black font-weight-bold">Postal Code</p>
          </div>
          <div class="col-12 col-md-4 text-md-right">
            <p class="mb-0">{{ order.postcode }}</p>
          </div>
        </div>

        <div class="row">
          <div class="col-12 col-md-4">
            <p class="mb-0 text-black font-weight-bold">Country</p>
          </div>
          <div class="col-12 col-md-4 text-md-right">
            <p class="mb-0">{{ order.country }}</p>
          </div>
        </div>

        <div class="row">
          <div class="col-12 col-md-4">
            <p class="mb-0 text-black font-weight-bold">Phone Number</p>
          </div>
          <div class="col-12 col-md-4 text-md-right">
            <p class="mb-0">{{ order.phone_number }}</p>
          </div>
        </div>

        <div class="row">
          <div class="col">
            <small class="text-muted">Billing Details:</small>
          </div>
        </div>

        <div class="row">
          <div class="col-12 col-md-4">
            <p class="mb-0 text-black font-weight-bold">Order Total</p>
          </div>
          <div class="col-12 col-md-4 text-md-right">
            <p class="mb-0">£{{ order.order_total }}</p>
          </div>
        </div>

        <div class="row">
          <div class="col-12 col-md-4">
            <p class="mb-0 text-black font-weight-bold">Delivery</p>
          </div>
          <div class="col-12 col-md-4 text-md-right">
            <p class="mb-0">£{{ order.delivery_cost }}</p>
          </div>
        </div>

7. Some of the order fields are not required fields so need to be wrapped in 'if statements'  so these parts of the summary are only renders if the user has populated them. I need an if statement around Street Address 2, County and postcode as below:

        {% if order.street_address2 %}
        <div class="row">
          <div class="col-12 col-md-4">
            <p class="mb-0 text-black font-weight-bold">Address 2</p>
          </div>
          <div class="col-12 col-md-4 text-md-right">
            <p class="mb-0">{{ order.street_address2 }}</p>
          </div>
        </div>
        {% endif %}

        {% if order.county %}
        <div class="row">
          <div class="col-12 col-md-4">
            <p class="mb-0 text-black font-weight-bold">County</p>
          </div>
          <div class="col-12 col-md-4 text-md-right">
            <p class="mb-0">{{ order.county }}</p>
          </div>
        </div>
        {% endif %}

        {% if order.postcode %}
        <div class="row">
          <div class="col-12 col-md-4">
            <p class="mb-0 text-black font-weight-bold">Postal Code</p>
          </div>
          <div class="col-12 col-md-4 text-md-right">
            <p class="mb-0">{{ order.postcode }}</p>
          </div>
        </div>
        {% endif %}

        {% if order.postcode %}
        <div class="row">
          <div class="col-12 col-md-4">
            <p class="mb-0 text-black font-weight-bold">Postal Code</p>
          </div>
          <div class="col-12 col-md-4 text-md-right">
            <p class="mb-0">{{ order.postcode }}</p>
          </div>
        </div>
        {% endif %}                

8. Once I have added my if statements to the non-required fields, I run my dev server and make an order to see how this looks now on my checkout success page. This looks good:

![Successful order summary Checkout Success](/static/images/Stripe/Screenshot%20successful%20order%20with%20order%20summary.png)

9. The columns are slightly off within the Order Summary and should be smaller, the second column in each of the rows should be col-md-8 and not col-md-4 so I go through and update these now as below:

  <div class="row">
    <div class="col-12 col-lg-7">
      <div class="order-confirmation-wrapper p-2 border">
        <div class="row">
          <div class="col">
            <small class="text-muted">Order Info</small>
          </div>
        </div>
<!-- Code Institute - Boutique Ado -->
        <div class="row">
          <div class="col-12 col-md-4">
            <p class="mb-0 text-black font-weight-bold">Order Number</p>
          </div>
          <div class="col-12 col-md-8 text-md-right">
            <p class="mb-0">{{ order.order_number }}</p>
          </div>
        </div>

        <div class="row">
          <div class="col-12 col-md-4">
            <p class="mb-0 text-black font-weight-bold">Order Date</p>
          </div>
          <div class="col-12 col-md-8 text-md-right">
            <p class="mb-0">{{ order.date }}</p>
          </div>
        </div>

        <div class="row">
          <div class="col">
            <small class="text-muted">Order Details:</small>
          </div>
        </div>

        {% for item in order.lineitems.all %}
        <div class="row">
          <div class="col-12 col-md-4">
            <p class="small mb-0 text-black font-weight-bold">
              {{ item.product.name }}{% if item.product_size %} - Size {{
              item.product_size|upper }}{% endif %}
            </p>
          </div>
          <div class="col-12 col-md-8 text-md-right">
            <p class="small mb-0">
              {{ item.quantity }} @ £{{ item.product.price }} each
            </p>
          </div>
        </div>
        {% endfor %}

        <div class="row">
          <div class="col">
            <small class="text-muted">Delivery Address</small>
          </div>
        </div>

        <div class="row">
          <div class="col-12 col-md-4">
            <p class="mb-0 text-black font-weight-bold">Full Name</p>
          </div>
          <div class="col-12 col-md-8 text-md-right">
            <p class="mb-0">{{ order.full_name }}</p>
          </div>
        </div>

        <div class="row">
          <div class="col-12 col-md-4">
            <p class="mb-0 text-black font-weight-bold">Address 1</p>
          </div>
          <div class="col-12 col-md-8 text-md-right">
            <p class="mb-0">{{ order.street_address1 }}</p>
          </div>
        </div>

        {% if order.street_address2 %}
        <div class="row">
          <div class="col-12 col-md-4">
            <p class="mb-0 text-black font-weight-bold">Address 2</p>
          </div>
          <div class="col-12 col-md-8 text-md-right">
            <p class="mb-0">{{ order.street_address2 }}</p>
          </div>
        </div>
        {% endif %}

        {% if order.county %}
        <div class="row">
          <div class="col-12 col-md-4">
            <p class="mb-0 text-black font-weight-bold">County</p>
          </div>
          <div class="col-12 col-md-8 text-md-right">
            <p class="mb-0">{{ order.county }}</p>
          </div>
        </div>
        {% endif %}

        <div class="row">
          <div class="col-12 col-md-4">
            <p class="mb-0 text-black font-weight-bold">Town or City</p>
          </div>
          <div class="col-12 col-md-8 text-md-right">
            <p class="mb-0">{{ order.town_or_city }}</p>
          </div>
        </div>

        {% if order.postcode %}
        <div class="row">
          <div class="col-12 col-md-4">
            <p class="mb-0 text-black font-weight-bold">Postal Code</p>
          </div>
          <div class="col-12 col-md-8 text-md-right">
            <p class="mb-0">{{ order.postcode }}</p>
          </div>
        </div>
        {% endif %}

        <div class="row">
          <div class="col-12 col-md-4">
            <p class="mb-0 text-black font-weight-bold">Country</p>
          </div>
          <div class="col-12 col-md-8 text-md-right">
            <p class="mb-0">{{ order.country }}</p>
          </div>
        </div>

        <div class="row">
          <div class="col-12 col-md-4">
            <p class="mb-0 text-black font-weight-bold">Phone Number</p>
          </div>
          <div class="col-12 col-md-8 text-md-right">
            <p class="mb-0">{{ order.phone_number }}</p>
          </div>
        </div>

        <div class="row">
          <div class="col">
            <small class="text-muted">Billing Details:</small>
          </div>
        </div>

        <div class="row">
          <div class="col-12 col-md-4">
            <p class="mb-0 text-black font-weight-bold">Order Total</p>
          </div>
          <div class="col-12 col-md-8 text-md-right">
            <p class="mb-0">£{{ order.order_total }}</p>
          </div>
        </div>

        <div class="row">
          <div class="col-12 col-md-4">
            <p class="mb-0 text-black font-weight-bold">Delivery</p>
          </div>
          <div class="col-12 col-md-8 text-md-right">
            <p class="mb-0">£{{ order.delivery_cost }}</p>
          </div>
        </div>

        <div class="row">
          <div class="col-12 col-md-4">
            <p class="mb-0 text-black font-weight-bold">Grand Total</p>
          </div>
          <div class="col-12 col-md-8 text-md-right">
            <p class="mb-0">£{{ order.grand_total }}</p>
          </div>
        </div>

10. I refresh my checkout success page from earlier to see how this looks now and notice that my Order Details isn't populating correctly. I should be seeing a list of the items titles that I ordered in one columns and the correct price alongside in the next column. I update my size and quantity sections as below so the tags match my code instead of Code Institute's:

          <div class="col-12 col-md-4">
            <p class="small mb-0 text-black font-weight-bold">
              {{ item.product.title }}
              {% if item.product_size %} 
                - Size {{ item.variant.variant_title|upper }}
              {% endif %}
            </p>
          </div>
          <div class="col-12 col-md-8 text-md-right">
            <p class="small mb-0">
              {{ item.quantity }} × £{{ item.product.price }} = £{{ item.lineitem_total }}
            </p>
          </div>
        </div>

11. I refresh the page and this looks slightly better as I can see a price instead of £0 but it still doesn't look right:

![Order Summary no items and price is wrong](/static/images/Stripe/Screenshot%20order%20summary%20price%20wrong.png)

12. I consult ChatGPT who advises that the template is wrong as it is using:

{{ item.product.title }}
{{ item.product.price }}
{{ item.variant.variant_title }}

- But my model structure doesn't match this, I am using:

class OrderLineItem(models.Model):
    product_variant = models.ForeignKey(ProductVariant, ...)

- It recommends updating my entire loop with:

{% for item in order.lineitems.all %}
<div class="row">
  <div class="col-12 col-md-4">
    <p class="small mb-0 text-black font-weight-bold">
      {{ item.product_variant.product.title }}
      {% if item.product_variant.variant_title %}
        - {{ item.product_variant.variant_title|upper }}
      {% endif %}
    </p>
  </div>
  <div class="col-12 col-md-8 text-md-right">
    <p class="small mb-0">
      {{ item.quantity }} × £{{ item.product_variant.price }} = £{{ item.lineitem_total }}
    </p>
  </div>
</div>
{% endfor %}

- I update this and refresh but get a server 500 error so I switch debug on and see what is happening and can see I have the following error:

TemplateSyntaxError at /checkout/checkout_success/0EB040D6383C4537BB433F9C888266AA
Invalid block tag on line 63: 'endif', expected 'empty' or 'endfor'. Did you forget to register or load this tag?

- I update my template so that the faulting if tag is no longer split across 2 x lines like below:

              {{ item.product_variant.product.title }} 
              {% if item.product_variant.variant_title %} 
              - {{item.product_variant.variant_title|upper }} 
              {% endif %}

- I refresh the page and this looks slightly better but the price still looks wrong:

![Checkout Success Order Summary shows order item titles](/static/images/Stripe/Screenshotcheckout%20success%20now%20shows%20order%20items%20but%20not%20price.png)

- I consult ChatGPT about this who recommends updating the code as below:

<p class="small mb-0">
  {{ item.quantity }} × £{{ item.product_variant.price }} = £{{ item.lineitem_total }}
</p>

13. I refresh and the price now looks okay so I commit my code:

![Checkout Success Order Summary now correct](/static/images/Stripe/Screenshot%20order%20summary%20now%20correct.png)

14. I now want to add a loading overlay div underneath my main container in the checkout.html that will contain a big gaint spinner icon in the center of the screen with a blue overlay to cover the page and indicate that the payment is being processed. I am going to copy and paste this code from Code Institute's Boutique Ado to save time:

    <div id="loading-overlay">
        <h1 class="text-light logo-font loading-spinner">
            <span class="icon">
                <i class="fas fa-3x fa-sync-alt fa-spin"></i>
            </span>
        </h1>
    </div>

15. Then I am also going to borrow their css styles for the div and paste these into my checkout.css file at the very bottom:

#loading-overlay {
	display: none;
	position: fixed;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    background: rgba(23, 162, 184, .85);
    z-index: 9999;
}

.loading-spinner {
	display: flex;
    align-items: center;
    justify-content: center;
    margin: 0;
    height: 100%;
}

16. Next I will update my checkout/static/checkout/stripe_elements.js file as Code Institute have with theirs so it triggers the overlay and fade out form when the user clicks the submit button and reverse it if there's any errors. Underneath the line of code for submit button ($('#submit-button').attr('disabled', true);) I add the below two lines of code directly beneath it. I copy and paste the 2 x line of code below and also paste them further down the line above the code for card.update (card.update({ 'disabled': false});):

    $('#payment-form').fadeToggle(100);
    $('#loading-overlay').fadeToggle(100);

17. I save this and submit another order but use a different test card number to trigger a different authentication from Stripe to ensure that the pop-up stays above the loading overlay. I am going to do a hard refresh and clear the cache in devtools before updating my details and completing the order.

The test card number I am using is: 4000 0025 0000 3155

18. I complete the order using my test card number and do not see the blue overlay screen but do get a Stripe popup as shown below:

![Checkout Success stripe popup no loading overlay](/static/images/Stripe/Screenshot%20stripe%20popup.png)

19. I can see that something isn't right as when I look at my checkout page I can see the code for the loading overlay div being displayed as text on the page, see below:

![Checkout showing code for div overlay](/static/images/Stripe/Screenshot%20div%20id%20for%20loading%20overlay%20wrong.png)

20. I take a look at the code in my checkout.html file for the loading-overlay div and realise I haven't contained the div in an opening arrow so update this now and then refresh my page and try checking out again but its still showing the loading cursor running on the main checkout screen before I complete order and then not showing the blue loading overlay screen when I click complete order:

![Checkout showing loading cursor](/static/images/Stripe/Screenshot%20loading%20cursor%20on%20checkout.png)

21. I consult ChatGPT who advises that fadetoggle() is causing the overlay to be hidden so recommends using fadeIn when submitting and fadeOut when there is an error and it needs to hide the overlay. I replace this code:

$('#loading-overlay').fadeToggle(100);

With the below updates:

    $('#payment-form').fadeOut(100); // ChatGPT Code
    $('#loading-overlay').fadeIn(200); //ChatGPT Code
    stripe.confirmCardPayment(client_secret, {
        payment_method: {
            card: card,
        }
    }).then(function(result) {
        if (result.error) {
            var errorDiv = document.getElementById('card-errors');
            var html = `
                <span class="icon" role="alert">
                <i class="fas fa-times"></i>
                </span>
                <span>${result.error.message}</span>`;
            $(errorDiv).html(html);
            $('#payment-form').fadeIn(100);
            $('#loading-overlay').fadeOut(200);
            card.update({ 'disabled': false});

22. I save the new code and then refresh to see how this looks now, however, I am still seeing the loading cursor on the checkout page permanently and seeing no overlay when I go to 'Complete Order'. The Javascript is correct now so ChatGPT recommends updating my loading-overlay css to this instead of usign cursor-wait as if there's any issues with the overlay not hiding it will affect the page. This adds !important to the display attribute to force it to hide on load:

#loading-overlay {
    display: none !important; 
    position: fixed;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;

    background: rgba(23, 162, 184, 0.85);
    z-index: 9999;
}

23. I hard reload the page again but still getting the same. I inspect the page on devtools and click the loading-overlay div html and then check computed styles and can see that display is set to 'block' instead of 'none'. I open devtools console and refresh and then run the following, which returns a 'true' result, meaning that Javascript made it visible:

('#loading-overlay').is(':visible')

24. I therefore add the following to the very top of the stripe_elements.js file to force hide on page load:

$(document).ready(function() {
    $('#loading-overlay').hide();
});

25. I hard reload the page and test to see if this has fixed the issue but it still hasn't. I inspect in devtools and can see that I have display block but it's not got the !important meaning that checkout.css isn't being served somehow:

![loading overlay inspect devtools](/static/images/Stripe/Screenshot%20loading%20overlay%20inspect%20devtools%20elements.png)

26. I check the Devtools > Network tab and filter on css but can see the checkout.css file is in there. I then check my template for checkout.html and make sure that that my checkout.css is contained within an extra_css block which it is:

{% block extra_css %}
    {{ block.super }}
    <link rel="stylesheet" href="{% static 'checkout/css/checkout.css' %}">
{% endblock %}

- I also make sure that my base.html contains an empty block for extra css after my core css block which it does:

    <!-- MAIN SITE CSS -->
    <link rel="stylesheet" href="{% static 'css/style.css' %}"/>
    {% endblock %}
    
    <!-- Page-specific CSS -->
    {% block extra_css %}{% endblock %}

- I do a hard reload and empty cache but its still not picking up the checkout.css display !important code. I consult ChatGPT who checks out my checkout.html file and spots the issue. The div overlay is being affected by this line of code at the top of the file:

<div class="overlay"></div>

- This is causing it to conflict with the div overlay at the bottom of the file because of the css rule I created for overlay. I remove this line and reload my page. However, its still showing the cursor on my checkout page. I take a look at the checkout.css file being served on the code but it stops at the #payment-form styles and doesn't have any of my rules for the overlay below it. I am going to trey recursing the static files, as I have checked that I am editing the correct file, and then I will collectstatic files again:

Remove-Item -Recurse -Force staticfiles

python manage.py collectstatic 

- I have refreshed the page and now the loading cursor is removed. I want to update the background on the loading overlay so its not blue and instead blurred so ChatGPT provides me some css rules for this and I update the loading-overlay id rules:

    /* ✨ Blur effect */
    backdrop-filter: blur(6px);
    -webkit-backdrop-filter: blur(6px);

    /* Optional: slight dim so text is readable */
    background: rgba(255, 255, 255, 0.3);

- Now when I load the page and complete order, I can see a blurred background while I am waiting to confirm the order.

![Loading overlay blurred background](/static/images/Stripe/Screenshot%20loading%20overlay%20works%20with%20blurred%20background.png)

- I commit my code to Git and Heroku ready for implementing Webhooks next.

---

## Checkout - Webhooks for Payment Status Tracking

1. So from the tests done previously, I can see that my orders are being created and stored in the database after checking my Admin panel. However, if a user closes the browser after the payment is confirmed and sent to Stripe but before form is submitted then there will be no order in the database. Things like internal email notificaitons would not be triggered because the user never fully completes their order. Which could result in charges to the user with no confirmation email or getting wrong orders. To prevent this, I will add redundancy and each time and event occurs on Stripe such as a payment intent being created, a payment being completed, etc. then Stripe will send out a Webhook to listen for. (Webhooks are the signal that Django sends each time a model is saved or deleted).

2. In order to handle the new webhooks I will be creating, I need to create my first custom class. I start by creating a new file called webhook_handler.py in the root of my checkout app directory. At the top of this file, I import the HttpResponse from Django.http:

from django.http import HttpResponse

3. Next I am going to create a class called StripeWH_Handler and pass the init method to this with 'self' and 'request' attributes. The init method of the class is a setup method that's called every time an instance of the class is created. The request attribute allows us to access any attributes of the request coming from Stripe:

class StripeWH_Handler:
    """Handle Stripe Webhooks"""

    def __init__(self, request):
        self.request = request

4. Next I will create a class method called handle event which will take the event that Stripe is sending us and simply return an HTTP reponse to indicate that it was received:

    def handle_event(self, event):
        """Handle generic, unknown & unexpected Webhook events"""
        return HttpResponse(
            content=f'Webhook received: {event["type"]}',
            status=200)

5. Now that's added I will commit my changes and then look at adding the methods needed to start using it on my site.

6. I am now going to add a couple more methods to my Webhook Handler class and then set it up so it can actually listen for the Webhooks. To create the new methods I am just going to copy and paste the handle_event code and paste it again twice and then change the names accordingly. For each different event of Webhook I want its own method that's easy to manage and is easy to add more as Stripe creates new ones. The first method I create is called handle_payment_intent_succeeded which will handle the payment intent succeeded Webhook from Stripe and will be sent each time a user completes the payment process:

    def handle_payment_intent_succeeded(self, event):
        """Handle the payment_intent.succeeded Webhook from Stripe"""
        return HttpResponse(
            content=f'Webhook received: {event["type"]}',
            status=200)   

7. Then I create another method which occurs in the event of their payment failing which listens for this webhook:

    def handle_payment_intent_payment_failed(self, event):
        """Handle the payment_intent.payment_failed Webhook from Stripe"""
        return HttpResponse(
            content=f'Webhook received: {event["type"]}',
            status=200) 

8. Then back in the handle_event method I update content to 'unhandled webhook receive':

    def handle_event(self, event):
        """Handle generic, unknown & unexpected Webhook events"""
        return HttpResponse(
            content=f'Unhandled Webhook received: {event["type"]}',
            status=200)

9. Now I want to get my new class listening so I create the URL for this in my checkout/urls file. The path will be called 'WH' which returns a function called Webhook with the name of Webhook:

path('wh/', webhook, name='webhook'),

10. Then the function for Webhook will come from a file called webhooks.py so I import this function from .webhooks at the top of the file:

from .webhooks import webhook

11. I now create this file for webhooks in the root of my checkout app directory again. The file is called webhooks.py. Then inside this file I am going to create the webhook function which takes in request and the code I am using for this has come from Stripe (Handle Webhook Events) (via Code Institute) which I have then tweaked as Code Institute did for their Boutique Ado. The name will be wh_secret, it will have a generic exception handler to catch any exceptions other than the two that Stripe has provided. Then the last part of code will be given an event and will get its type to decide which method from the webhook handler will be called to handle it:

def webhook(request):
    """Listen for webhooks from Stripe"""
    # Setup


    # get the webhook data and verify its signature
    payload = request.body
    sig_header = request.META['HTTP_STRIPE_SIGNATURE']
    event = None

    try:
        event = stripe.Webhook.construct_event(
            payload, sig_header, settings.STRIPE_WH_SECRET
        )
    except ValueError as e:
        # Invalid payload
        return HttpResponse(status=400)
    
    except stripe.error.SignatureVerificationError as e:
        # Invalid signature
        return HttpResponse(status=400)
    
    except Exception as e:
        return HttpResponse(content=e, status=400)

12. I now need to set up the Stripe API key and the Webhook Secret at the top of the file so they can be used to verify that the Webhook actually came from Stripe:

def webhook(request):
    """Listen for webhooks from Stripe"""
    # Setup
    wh_secret = settings.STRIPE_WH_SECRET
    stripe.api_key = settings.STRIPE_SECRET_KEY


    # get the webhook data and verify its signature
    payload = request.body
    sig_header = request.META['HTTP_STRIPE_SIGNATURE']
    event = None

    try:
        event = stripe.Webhook.construct_event(
            payload, sig_header, settings.STRIPE_WH_SECRET
        )
    except ValueError as e:
        # Invalid payload
        return HttpResponse(status=400)
    
    except stripe.error.SignatureVerificationError as e:
        # Invalid signature
        return HttpResponse(status=400)
    
    except Exception as e:
        return HttpResponse(content=e, status=400)

13. Then at the top of the file I need to make some imports. I will need to import my settings file to get the webhook and Stripe API secrets and I need HttpResponse so that the exception handler will work with the Webhook class and Stripe too:

from django.conf import settings
from django.http import HttpResponse

from checkout.webhook_handler import StripeWH_Handler

import Stripe

14. Then above the import for StripeWH_Handler class, I import 2 x decorators: require_post (This will make this view require a post request and reject get requests) and CSRF exempt since Stripe will not send a CSRF token to as we normally would need:

from django.views.decorators.http import require_POST
from django.views.decorators.csrf import csrf_exempt

- Then add the below above the method for webhook:

@require_POST
@csrf_exempt

15. I save this and then go to my settings file and add new environment variable called stripe webhook secret which I will get from Stripe next. I add this new variable at the bottom of the file with the other Stripe variables in the Stripe section:

STRIPE_WH_SECRET = os.getenv('STRIPE_WH_SECRET ', '')

16. I now need to test my webhook. To do this my website needs a URL that Stripe can access to send the webhooks to and from. In order to get this functionality in my local IDE environment, I need to use Stripe CLI in my Visual Studio Code's terminal. To start with, I am going to install Stripe CLI for Windows using the steps in the installation guide here: 

https://codeinstitute.s3.eu-west-1.amazonaws.com/vscode-migration-pdf-guides/stripe-cli-installation-guide-windows.pdf

17. I scroll down the page and find the section for '1. Install the Stripe CLI' and click the Windows tab and then click the Github link there to download the latest Windows zip file from the Github library:

https://github.com/stripe/stripe-cli/releases/tag/v1.40.3

18. Once on the link, I click the stripe_1.40.3_windows_x86_64.zip file and once downloaded, I unzip this to a more suitable location than downloads, I unzip to this path:

C:\Users\leila\Documents\stripe-cli

19. I then add the path to the unzipped stripe.exe file to my Path environment variable, I copy the below path and then search for Environment Variables on Windows and then click the option for 'Edit the system environment variables' that appears. Then in the 'Advanced' tab at the bottom is an option for 'Environment Variables', I click this and then I am taken to a menu with the Environment Variables settings. I click the option for 'Path' in the list and then click the 'Edit' button below this. Then in the new window, I click 'New' and add the path I pasted above for 'stripe-cli' and then hit 'OK'. Then I need to restart my machine for this to take affect. 

20. Now when I run the below a version for Stripe is being returned so I know the install has been successful:

stripe version
stripe version 1.40.3

21. Next, I type stripe login and press enter. I click the browser prompt when it appears to open the link in Chrome and then follow the on-screen instructions on the next page, allowing Stripe CLI access ny clicking 'Allow Access' in the prompt shown below:

![Stripe CLI Allow Access](/static/images/Stripe/Screenshot%20stripe%20cli%20install%20allow%20access.png)

22. After allowing access, I close the window and return to my terminal and can see I have a pairing code and confirmation that the Stripe CLI is now configured for bsuiness sandbox with its own account id. This will be valid for 90 days but now I have Stripe CLI installed on my machine and I can start testing my webhooks. 

23. To confirm that my webhook is working, I am going to add a print statement and return a 200 response. In my webhooks.py file, I am going to add this at the end of my webhook function as below:

print('Success!')
return HttpResponse(status=200)

24. Then in settings.py, I updated my ALLOWED_HOSTS so that both the VS Code preview and the Stripe portal will work:

    'localhost',

25. Then in order to then test my webhook, I opem three terminals at once within my local IDE: Python server - to run my local preview of the webpage, Stripe portal to generate a url that Stripe can send and receive webhooks from and Terminal to send the test webhook cmds. 

26. First, I run my Python server to display my local webpage using:

python manage.py runserver

- This opens up successfully.

27. Then, I open a new terminal for my Stripe portal and then enter the following code into the cmd and hit enter. This command opens the Stripe portal:

stripe listen --forward-to localhost:8000/checkout/wh/

- I then copy the webhook signing secret generated in the terminal.

- I add the signing secret to env.py as below:

os.environ.setdefault("STRIPE_WH_SECRET", "your signing secret here")

28. Now that my STRIPE_WH_SECRET value has been created in the environment, I need to restart my Python server to ensure that the project can access this. I go to the terminal for my Python server and hit CTRL + C to cancel the server, then go up on the keyboard to bring the cmd back and run the server again.

29. Next, I need to open the last terminal needed where I will enter my Stripe webhook triggers. I open a new terminal and enter the following cmd and hit enter which will trigger a webhook:

stripe trigger payment_intent.created

- This sets up the fixture for payment_intent, then runs it and shows that the trigger has succeeded and advises to check the dashboard for event details.

- However, when I return to the first Python terminal where I am running my server from I see the following response instead of 'Success' as I would of expected. 

- I take a look at my settings.py variables again and realise there is a space at the end of the 'STRIPE_WH_SECRET ' variable, so I remove this and save and then restart my Python server. Now when I run the below, I can see a success message on my first python server:

stripe trigger payment_intent.created

30. With this returned, I have confirmed that anytime Stripe sends a webhook that the webhook view will be executed and any event will be handled accordingly. I have set up a listener to listen to messages from Stripe. I will next look at customising the webhook handler even more to handle even more types of webhook requests and responses.

31. The webhook handler class retruns a response directly from the webhook view and if I use an if statement to check what kind of event is being seen then there could be a hundred different webhooks returned due to the hundred of different possibilities available. So to make this cleaner, I pass the event to the webhook handler with a more convenient method written up for the different types of webhooks. By using a class, I can import into other projects and subclass it to override the methods to suit the project. 

I am now going to moderate my webhook view to use the webhook handler. To do this, I first create an instance of it passing in the request and then create a dictionary called event map where the dictionary keys will be the names of the webhooks coming from stripe and its values will be the actual methods inside the handler:

    # Set up a webhook handler
    handler = StripeWH_Handler(request)

    # Map webhook events to relevant handler functions
    event_map = {
        'payment_intent.succeeded': handler.handle_payment_intent_succeeded,
        'payment_intent.payment_failed': handler.handle_payment_intent_payment_failed,
    }    

32. Next, I want to get the type of the event from Stripw and store this ina key called type. This returns something like payment intent.succeeded or payment intent.payment failed:

    #Get the webhook type from Stripe
    event_type = event['type']

33. Then I want to look up the key in the dictionary and assign its value to a variable called event handler which is nothing more than an alias for whatever function was just pulled from the dictionary:

    #If there's a handler for it, get it from the event map
    #Use the generic one by default
    event_handler = event_map.get(event_type, handler.handle_event)

34. Then finally, we can call it just like any other function, call the event handler and pass it the event and return the response to Stripe as below:

    #Call the event handler with the event
    response = event_handler(event)
    return response

35. I now want to test my webhooks again using the same process as before. I have 3 x terminals open:

- One Python terminal to run my local server using:

python manage.py runserver

- 1 x terminal running my Stripe portal:

 stripe listen --forward-to localhost:8000/checkout/wh/

 - 1 x Python terminal which is blank where I can trigger my webhook from.

 36. I have the three terminals open, I am going to confirm the 'Unhandled webhook event'. In my third terminal, I type the below:

 stripe trigger payment_intent.created

- This successfully sets up and runs the fixtures and tells me the trigger has succeeded. 

37. Next, I login to the Stripe dashboard, go to Settings > Developers and then search Events and click to go to the Events tab.

- I select the top event for payment_intent.created and then scroll to the bottom of the page and look under 'Webhook CLI responses' and click the chevron next to my device name to expand the information about my webhook attempt.

38. I now want to confirm the payment intent succeeded event. I return to the third terminal where I have been writing my Stripe triggers and test the payment intent succeeded webhook using:

stripe trigger payment_intent.succeeded

- This sets up and runs the fixtures and then tells me the trigger has succeeded.

39. I check Events and scroll to the top and can see the event for payment succeeded.

40. I repeat the same steps to confirm the payment failed event now works, running the following cmd in the third terminal now:

- This sets up and runs the fixtures successfully and tells me that the trigger has succeeded

41. I check the events on Stripe again and can see this has generated the event for payment failed.

42. Now I have confirmed everything is working as should be, I will save and commit my changes to Git and Heroku.

43. I now want to write the code for my payment intent succeeded webhook handler which will ensure that the payment process is reliable by always guaranteeing, no matter the action of the user, that during checkout that if Stripe successfully processes their payment then the order will definitely be processed.

44. The payment system for my e-commerce store is almost complete. I now need to write the code to create any necessary database objects in the webhook handler. The first thing I will do is update the stripe_elements.js file as the payment intent.succeeded webhook will be coming from Stripe and not from my code into the webhook handler so I want to put the form data into the payment intent object so that I can retrieve it once I have the webhook. I can mostly achieve this simply adding the form data to the confirmed card payement method like below. If you look at the structure of the payment intent object in Stripe then you can see it has a space for billing details object that can be added below the card. The fields it can take are name, email, phone number and address - which are pretty much the sam details as are in the form. I add the fields in and get the data from the form and use the trim method to strip off any excess whitespace:

            billing_details: {
                name: $.trim(form.full_name.value),
                phone: $.trim(form.phone_number.value),
                email: $.trim(form.email.value),
                address:{
                    line1: $.trim(form.street_address1.value),
                    line2: $.trim(form.street_address2.value),
                    city: $.trim(form.town_or_city.value),
                    country: $.trim(form.country.value),
                    state: $.trim(form.county.value),
                }
            }

55. I then do the same for shipping_details but remove the attribute for email address:

        shipping: {
            name: $.trim(form.full_name.value),
            phone: $.trim(form.phone_number.value),
            address: {
                line1: $.trim(form.street_address1.value),
                line2: $.trim(form.street_address2.value),
                city: $.trim(form.town_or_city.value),
                country: $.trim(form.country.value),
                postal_code: $.trim(form.postcode.value),
                state: $.trim(form.county.value),
            }
        },

56. Next I am going to create a new view in checkout/views which will allow use to determine in the webhook whether a user had the 'save info' checkbox ticked. I create a new view called cache_checkout_data which expects the POST method and use the require_POST decorator:

@require_POST
def cache_checkout_data(request):

57. Then at the top of the file, I import the decorator and HttpResponse at the top of the file:

from django.shortcuts import render, redirect, reverse, get_object_or_404, HttpResponse
from django.views.decorators.http import require_POST

58. What this will do is call the confirm card payment method from the stripe_elements.js, it will make a POST request to this view and give it the client secret from payment intent:

        pid = request.POST.get('client_secret').split('_secret')[0]

59. Next, I set up Stripe with the secret key so we can modify the payment intent:

        stripe.api_key = settings.STRIPE_SECRET_KEY

60. This is done below by calling the stripe.PayementIntent.modify give it the pid and tell it what we want to modify and then pass the metadata for what we want as below (this add the user who places the order, whether they clicked save info and a json dump of their shopping bag)

        stripe.PaymentIntent.modify(pid, metadata={
            'shoppingbag': json.dumps(request.session.get('shoppingbag', {})),
            'save_info': request.POST.get('save_info'),
            'username': request.user,
        })

61. Then I want to return an HttpResponse with the status 200 for okay and wrap it in an except block and if anything faults then it will retrun an response with the error message content and status of 400 for bad request and then this way we can post to the view from Javascript:

        return HttpResponse(status=200)
    except Exception as e:
        messages.error(request, 'Sorry, your payment cannot be \
            processed right now. Please try again later.')
        return HttpResponse(content=e, status=400)

62. I now want to create a new url to access the new view and then create some new variables in my stripe_elements.js file. In my checkouts/url file I update my paths to:

    path('cache_checkout_data/', views.cache_checkout_data, name='cache_checkout_data'),

63. Then in stripe_elements.js, I get the boolean value of the saved info box by looking at the checked attribute like below:

    var saveInfo = Boolean($('#id-save-info').attr('checked'));

64. Then I also need to get the CSRF Token which will be obtained from the input that Django generates on the form. This will have a nam,e of csrfmiddleware token:

    // From using {% csrf_token %} in the form
    var csrfToken = $('input[name="csrfmiddlewaretoken"]').val();

65. I then create a small object to pass the information to the new view and pass the client secret for payment intent:

    var postData = {
        'csrfmiddlewaretoken': csrfToken,
        'client_secret': clientSecret,
        'save_info': saveInfo,
    };

66. I then create a variable for the new url:

    var url = '/checkout/cache_checkout_data/';

67. And the last thing I want to update here is to post the data to the view with the POST method built into jQuery. We tell it we are posting to the url and want to post the data above it. It then waits for a response that the payment intent was updated before calling the confirmed payment method by tacking on the .done method and executing the callback function:

    $.post(url, postData).done(function ()

68. I then attach a failure function at the end of the code which will be triggered if the view sends a 400 bad request response. In this case it will reloadf the page to show the error message from the view:

    }).fail(function () {
        // just reload the page, the error will be in django messages
        location.reload();
    })
});

69. Next I go back to my webhook_handler file and print out the payment intent coming from stripe and once the user makes a payment it should have the metadata I just set attached. The payment intent will be saved in a key called event.data.object so I will store that and then print it out:

    def handle_payment_intent_succeeded(self, event):
        """
        Handle the payment_intent.succeeded webhook from Stripe
        """
        intent = event.data.object
        print("*********************")
        print(intent)

70. I am now going to try and submit an order and make sure that everything works.

71. My dev server won't start, I am receiving an error as below:

File "...checkout\views.py", line 26
    except Exception as e:
    ^^^^^^
SyntaxError: invalid syntax

72. I query this with ChatGPT who thinks the error is due to a missing 'try' statement in my view file. I compare my code to Code Institute's Boutique Ado and can see they have a 'try' statement above the pid variable so I add this in and it lets me run the page locally again now.

73. I complete an order but my webhook output isn't showing the metadata and shipping keys. The output in my terminal is:

[09/Apr/2026 21:08:32] "POST /checkout/wh/ HTTP/1.1" 200 50 ********************* { "amount": 4400, "amount_capturable": 0, "amount_details": { "tip": {} }, "amount_received": 4400, "application": null, "application_fee_amount": null, "automatic_payment_methods": { "allow_redirects": "always", "enabled": true }, "canceled_at": null, "cancellation_reason": null, "capture_method": "automatic_async", "client_secret": "pi_3TKOsN1urpY1vbdf0dpWGAA8_secret_iubgqQhIddloVeiLTANCKS3YA", "confirmation_method": "automatic", "created": 1775765311, "currency": "usd", "customer": null, "customer_account": null, "description": null, "excluded_payment_method_types": null, "id": "pi_3TKOsN1urpY1vbdf0dpWGAA8", "last_payment_error": null, "latest_charge": "ch_3TKOsN1urpY1vbdf0zqyHhAa", "livemode": false, "metadata": {}, "next_action": null, "object": "payment_intent", "on_behalf_of": null, "payment_method": "pm_1TKOty1urpY1vbdfIdUJJBQc", "payment_method_configuration_details": { "id": "pmc_1THL1N1urpY1vbdfH3zC4fLc", "parent": null }, "payment_method_options": { "amazon_pay": { "express_checkout_element_session_id": null }, "card": { "installments": null, "mandate_options": null, "network": null, "request_three_d_secure": "automatic" }, "link": { "persistent_token": null } }, "payment_method_types": [ "card", "link", "amazon_pay" ], "processing": null, "receipt_email": null, "review": null, "setup_future_usage": null, "shipping": null, "source": null, "statement_descriptor": null, "statement_descriptor_suffix": null, "status": "succeeded", "transfer_data": null, "transfer_group": null

74. This shows that the webhook is firing up correctly but missing the keys for the metadata and shipping info as below:

"metadata": {},
"shipping": null,

- I query with ChatGPT who advises it means that Stripe never received the form data so the webhook has nothing to print. It asks me to add this at the top of the checkout/views to see if it prints in the terminal which I do and it does:

print("CACHE VIEW HIT")


- I then update my except block temporarily to:

except Exception as e:
    print("ERROR:", e)
    return HttpResponse(content=str(e), status=400)

- I paste the output to ChatGPT who advises I am not wrapping the payment in a done() wrapper so to update my stripe_elements.js to:

$.post(url, postData).done(function () {
    stripe.confirmCardPayment(clientSecret, {
        payment_method: {
            card: card,
            billing_details: {
                name: $.trim(form.full_name.value),
                phone: $.trim(form.phone_number.value),
                email: $.trim(form.email.value),
                address: {
                    line1: $.trim(form.street_address1.value),
                    line2: $.trim(form.street_address2.value),
                    city: $.trim(form.town_or_city.value),
                    country: $.trim(form.country.value),
                    state: $.trim(form.county.value),
                }
            }
        },
        shipping: {
            name: $.trim(form.full_name.value),
            phone: $.trim(form.phone_number.value),
            address: {
                line1: $.trim(form.street_address1.value),
                line2: $.trim(form.street_address2.value),
                city: $.trim(form.town_or_city.value),
                country: $.trim(form.country.value),
                postal_code: $.trim(form.postcode.value),
                state: $.trim(form.county.value),
            }
        },
    }).then(function(result) {
        if (result.error) {
            $('#card-errors').text(result.error.message);
            $('#loading-overlay').fadeOut(200);
            $('#payment-form').show();
            card.update({ 'disabled': false});
            $('#submit-button').attr('disabled', false);
        }
    });

}).fail(function () {
    location.reload();
});

- I refresh and try to complete an order now and see what the output is but its still giving empty responses for billing and shipping. ChatGPT also recommends updating username as Stripe cannot store objects:

'username': request.user.username if request.user.is_authenticated else 'Anonymous',

- ChatGPT advises that I am using this code in my checkout/views but not importing json at the top of the file so recommends doing this now:

'bag': json.dumps(request.session.get('bag', {})),

75. I consult with ChatGPT again as now when I complete a checkout there is no webhook output coming back at all. ChatGPT advises that the bug is here:

var client_secret = $('#id_client_secret').text().slice(1, -1);

- But then later I use the below and Javascript is case sensiitive:

clientSecret

- I update the variable so it matches with what I have defined:

var clientSecret = $('#id_client_secret').text().slice(1, -1);

- It also recommends that I update my safeinfo variable as its cleaner and more reliable, I update this to:

var saveInfo = $('#id-save-info').is(':checked');

- I save, hard refresh and then run my server and then my stripe listening cmd. However, now when I try to complete the order it is giving me this error after entering my information and trying to complete:

![Complete order error](/static/images/Stripe/Screenshot%20payment%20form%20error.png)

- I query with ChatGPT who advises this is an error in my Django forms and recommends installing Django countries and using django-countries and updating my code accordingly once its installed.

76. To install django-countries I run the following cmd:

pip install django-countries

77. Once it's saying its successfully installed in the terminal, I add to my requirements.txt file using:

pip3 freeze > requirements.txt

78. Then I add it to my settings.py in INSTALLED APPS:

pip3 freeze > requirements.txt

79. I then need to add this to my checkout/models using:

from django_countries.fields import CountryField

country = CountryField(blank_label='Country *')

80. After updating my models, I make migrations and migrate using:

python manage.py makemigrations
python manage.py migrate

- However, running migrate gives the following error:

django.db.utils.DataError: value too long for type character varying(2)

- ChatGPT advises updating the country in models to the below and delete the 002 checkout/migrations file:

country = models.CharField(max_length=50)

- Then running: python manage.py migrate

- I can then make changes in shell to fix my data by running:

python manage.py shell

from checkout.models import Order

for order in Order.objects.all():
    if order.country == "United Kingdom":
        order.country = "GB"
        order.save()

- I update the country field in the model to, again:

country = CountryField(blank_label='Country *')

- Now I run makemigrations and migrate successfully.

81. With these changes in place, I will run my dev server again and see if it now lets me checkout and see the correct output from my webhooks in the terminal. I run the dev server and stripe listening again across my 2 x terminals.

82. Checkout is looking better now and has the 'Save Info' checkbox showing against delivery:

![Save Info Checkbox](/static/images/Stripe/Screenshot%20save%20info%20checkbox%20now%20appears%20at%20checkout.png)

83. I can now complete the checkout successfully, the bag clears down the items that were in there and I can see this response in the Python terminal:

WARNING: This is a development server. Do not use it in a production setting. Use a production WSGI or ASGI server instead.
For more information on production servers see: https://docs.djangoproject.com/en/6.0/howto/deployment/
[10/Apr/2026 12:57:46] "GET / HTTP/1.1" 200 12566
Not Found: /.well-known/appspecific/com.chrome.devtools.json
[10/Apr/2026 12:57:48] "GET /.well-known/appspecific/com.chrome.devtools.json HTTP/1.1" 404 3670
[10/Apr/2026 12:57:51] "GET / HTTP/1.1" 200 12566
Not Found: /.well-known/appspecific/com.chrome.devtools.json
[10/Apr/2026 12:57:51] "GET /.well-known/appspecific/com.chrome.devtools.json HTTP/1.1" 404 3670
[10/Apr/2026 12:57:51] "GET /static/images/favicon.png HTTP/1.1" 200 1246
[10/Apr/2026 12:57:51] "GET /static/css/style.css HTTP/1.1" 200 6838
[10/Apr/2026 12:57:51] "GET /static/images/Homepage/pexels-anete-lusina-4793215.jpg HTTP/1.1" 200 1539754
Not Found: /favicon.ico
[10/Apr/2026 12:57:51] "GET /favicon.ico HTTP/1.1" 404 3559
[10/Apr/2026 12:57:54] "GET /shoppingbag/ HTTP/1.1" 200 21761
[10/Apr/2026 12:57:57] "POST /checkout/wh/ HTTP/1.1" 200 50
[10/Apr/2026 12:57:57] "GET /checkout/ HTTP/1.1" 200 33977
[10/Apr/2026 12:57:57] "GET /static/checkout/js/stripe_elements.js HTTP/1.1" 200 3776
[10/Apr/2026 12:57:57] "GET /static/checkout/css/checkout.css HTTP/1.1" 200 1358
UPDATING PAYMENT INTENT: pi_3TKdhA1urpY1vbdf1oxScTmE
METADATA: {'7': 1, '9': 1}
[10/Apr/2026 12:58:35] "POST /checkout/cache_checkout_data/ HTTP/1.1" 200 0
*********************
{
  "amount": 8000,
  "amount_capturable": 0,
  "amount_details": {
    "tip": {}
  },
  "amount_received": 8000,
  "application": null,
  "application_fee_amount": null,
  "automatic_payment_methods": {
    "allow_redirects": "always",
    "enabled": true
  },
  "canceled_at": null,
  "cancellation_reason": null,
  "capture_method": "automatic_async",
  "client_secret": "pi_3TKdhA1urpY1vbdf1oxScTmE_secret_K1JLqBC1L35t023gFb6I49Tad",
  "confirmation_method": "automatic",
  "created": 1775822276,
  "currency": "usd",
  "customer": null,
  "customer_account": null,
  "description": null,
  "excluded_payment_method_types": null,
  "id": "pi_3TKdhA1urpY1vbdf1oxScTmE",
  "last_payment_error": null,
  "latest_charge": "ch_3TKdhA1urpY1vbdf156tMNLu",
  "livemode": false,
  "metadata": {
    "bag": "{\"7\": 1, \"9\": 1}",
    "save_info": "true",
    "username": "fitnessguru"
  },
  "next_action": null,
  "object": "payment_intent",
  "on_behalf_of": null,
  "payment_method": "pm_1TKdhn1urpY1vbdfoaxNIh3o",
  "payment_method_configuration_details": {
    "id": "pmc_1THL1N1urpY1vbdfH3zC4fLc",
    "parent": null
  },
  "payment_method_options": {
    "amazon_pay": {
      "express_checkout_element_session_id": null
    },
    "card": {
      "installments": null,
      "mandate_options": null,
      "network": null,
      "request_three_d_secure": "automatic"
    },
    "link": {
      "persistent_token": null
    }
  },
  "payment_method_types": [
    "card",
    "link",
    "amazon_pay"
  ],
  "processing": null,
  "receipt_email": null,
  "review": null,
  "setup_future_usage": null,
  "shipping": {
    "address": {
      "city": "Barrow-in-Furness",
      "country": "GB",
      "line1": "31 Goldsmith Street",
      "line2": "",
      "postal_code": "LA14 5RJ",
      "state": ""
    },
    "carrier": null,
    "name": "leilah hodgson",
    "phone": "07857895351",
    "tracking_number": null
  },
  "source": null,
  "statement_descriptor": null,
  "statement_descriptor_suffix": null,
  "status": "succeeded",
  "transfer_data": null,
  "transfer_group": null
}
Internal Server Error: /checkout/wh/
Traceback (most recent call last):
  File "C:\Users\leila\OneDrive\Desktop\Documents\vscode-projects\working_out_gym\.venv\Lib\site-packages\django\core\handlers\exception.py", line 55, in inner
    response = get_response(request)
               ^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\leila\OneDrive\Desktop\Documents\vscode-projects\working_out_gym\.venv\Lib\site-packages\django\core\handlers\base.py", line 205, in _get_response
    self.check_response(response, callback)
  File "C:\Users\leila\OneDrive\Desktop\Documents\vscode-projects\working_out_gym\.venv\Lib\site-packages\django\core\handlers\base.py", line 333, in check_response
    raise ValueError(
ValueError: The view checkout.webhooks.webhook didn't return an HttpResponse object. It returned None instead.
[10/Apr/2026 12:58:36] "POST /checkout/wh/ HTTP/1.1" 500 73498
[10/Apr/2026 12:58:36] "POST /checkout/wh/ HTTP/1.1" 200 44
[10/Apr/2026 12:58:37] "POST /checkout/ HTTP/1.1" 302 0
[10/Apr/2026 12:58:37] "GET /checkout/checkout_success/851FFFC838804390AC988E525E820FC9 HTTP/1.1" 200 17629
[10/Apr/2026 12:58:39] "POST /checkout/wh/ HTTP/1.1" 200 42

84. As my Stripe webhooks appear to be fully flowing now, I will turn Debug to false and commit my code.

85. I can now pass customer information through a Stripe payment intent as metadata which ensures that all orders are entered into the database, even in the event of a user error during the checkout process. In my payment intent succeeded webhook handler it contains the payment intent which has all the customers information in it. This is so if the form isn't submitted for some reason. In my webhook_handler in the handle_payment_intent_succeeded and get the payment intent id as well as the shopping bag and the users save preference from the metadata I have added:

        pid = intent.id
        bag = intent.metadata.bag
        save_info = intent.metadata.save_info

86. Then I also want to store the billing details, shipping details and grand total:

        billing_details = intent.charges.data[0].billing_details
        shipping_details = intent.shipping
        grand_total = round(intent.data.charges[0].amount / 100, 2)

87. Next I want to ensure that the data is in the same form as I want in my database so I replace any empty strings in the shipping details with 'none' and as Stripe stores these as blank strings which is not the same as the null value used in the database:

        for field, value in shipping_details.address.items():
            if value == "":
                shipping_details.address[field] = None

88. I now need to look at what should happen if an order doesn't exist which I can do by setting order_exists variable to 'False':

        order_exists = False

- Then under the new variable, I will create a new try statement which tries to get the order using all the information gathered from the payment intent, using the iexact lookup field to make it an exact match but case insensitive:

        try:
            order = Order.objects.get(
                full_name__iexact=shipping_details.name,
                    email__iexact=shipping_details.email,
                    phone_number__iexact=shipping_details.phone,
                    country__iexact=shipping_details.country,
                    postcode__iexact=shipping_details.postal_code,
                    town_or_city__iexact=shipping_details.city,
                    street_address1__iexact=shipping_details.line1,
                    street_address2__iexact=shipping_details.line2,
                    county__iexact=shipping_details.state,
                grand_total=grand_total,
            )

- Then if the order is found, I'll set order_exists to true and and return a 200 http response to Stripe with a message that the order already exists:

            order_exists = True
            return HttpResponse(
                content=f'Webhook received: {event["type"]} | SUCCESS: Verified order already in database',
                status=200)

- And if it doesn't exist yet then it will be created as if the form was submitted:

        except Order.DoesNotExist:
            try:
                order = Order.objects.create(
                    full_name=shipping_details.name,
                    email=shipping_details.email,
                    phone_number=shipping_details.phone,
                    country=shipping_details.country,
                    postcode=shipping_details.postal_code,
                    town_or_city=shipping_details.city,
                    street_address1=shipping_details.line1,
                    street_address2=shipping_details.line2,
                    county=shipping_details.state,
                    grand_total=grand_total,
                )

- I want to iterate through all the bag items next but I am going to load the bag from the json version from the payment intent rather than using the bag in my session. I will borrow the code from Code Institute for this from their Boutique Ado. Then after iterating through, as there is no form to save in this webhook then I will do this with order.objects.create. Then if anything goes wrong, there is a statement at the bottom to delete the order if it gets created and return a 500 server error response to Stripe (this will cause Stripe to automatically try the webhook again later):

                for item_id, item_data in json.loads(bag).items():
                    product = Product.objects.get(id=item_id)
                    if isinstance(item_data, int):
                        order_line_item = OrderLineItem(
                            order=order,
                            product=product,
                            quantity=item_data,
                        )
                        order_line_item.save()
                    else:
                        for size, quantity in item_data['items_by_size'].items():
                            order_line_item = OrderLineItem(
                                order=order,
                                product=product,
                                quantity=quantity,
                                product_size=size,
                            )
                            order_line_item.save()
            except Exception as e:
                if order:
                    order.delete()
                return HttpResponse(
                    content=f'Webhook received: {event["type"]} | ERROR: {e}',
                    status=500)
    
        return HttpResponse(
            content=f'Webhook received: {event["type"]}',
            status=200)

- I also need to import Stripe at the top of my webhook_handler.py file and update my payment_intent_succeeded method within my StripeWH_Handler class to:

intent = event.data.object
pid = intent.id
bag = intent.metadata.bag
save_info = intent.metadata.save_info

#Get the Charge object
stripe_charge = stripe.Charge.retrieve(
    intent.latest_charge
)

billing_details = stripe_charge.billing_details # updated
shipping_details = intent.shipping
grand_total = round(stripe_charge.amount / 100, 2) # updated

- If the view is slow and hasn't created the order by the time that the webhook is retrieved from Stripe then everything will look okay in the view and it will create the order but be a few seconds late. This is bad as the webhook handler will not find the order when it gets the webhook from Stripe and thus not create the order, resulting in the same order being added to the database twice once the view completes. I now want to implement some more functionality which would help in this scenario. To do this, I need to introduce a delay in case of an order not being found in the database rather than the order always being instantly created. 

- To start, I create a simple variable called attempt and set it to 1 underneath my variable for order_exists:

        attempt = 1

- I am then going to create a while loop that will execute up to 5 times:

        while attempt <= 5:

- I am then going to move the code in the first try block into the loop but will also update the code so that now instead of creating the order if its not found the first time then it's increment the attempt by 1 and use Python's time module to sleep for one second which will in affect cause the webhook handler to try and find the order five times over five seconds before giving up and creating the order itself:

    try:
        order = Order.objects.get(
            full_name__iexact=shipping_details.name,
            email__iexact=billing_details.email,
            phone_number__iexact=shipping_details.phone,
            country__iexact=shipping_details.address.country,
            postcode__iexact=shipping_details.address.postal_code,
            town_or_city__iexact=shipping_details.address.city,
            street_address1__iexact=shipping_details.address.line1,
            street_address2__iexact=shipping_details.address.line2,
            county__iexact=shipping_details.address.state,
            grand_total=grand_total,
        )
        order_exists = True
        break

    except Order.DoesNotExist:
        attempt += 1
        time.sleep(1)

- I import the time module at the top of the file:

import time

- Then after the loop above I add an if statement if the order does exist:

if order_exists:
    return HttpResponse(
        content=f'Webhook received: {event["type"]} | SUCCESS: Order already exists',
        status=200
    )

- Then after this I can create the order.

89. Another caveat to the payment process is that a user can purchase the same items on seperate occasions and this results in us finding the first order in the database when they place the second one and the second order never being created. To resolve this, I need to add 2 x new fields in the Order model. I go to checkout/models.

- The first field I am adding, is a text field that contains the shopping bag that created it. I add this directly under the grand_total field in Order model:

    original_bag = models.TextField(null=False, blank=False, default='')

- The second is a character field that contains the stripe payment intent id that is guaranteed to be unique:

    stripe_pid = models.CharField(max_length=254, null=False, blank=False, default='')

- After making changes to my model, I now need to run makemigrations and migrate:

python3 manage.py makemigrations
python3 manage.py migrate

- I then need to add the new fields to checkout/admin, I update readonly_fields with:

'original_bag', 'stripe_pid',

- And then in the same file, I also update the 'fields' list with:

'original_bag', 'stripe_pid',

- Then I need to update the view so that it adds those fields when the form is submitted. To do this I add a hidden input to the form in the checkout.html containing the client secret and then it goes to views and gets it if the order form is valid. I add this before the closing fieldset tag for payment. 

<input type="hidden" value="{{ client_secret }}" name="client_secret">#

- Then in checkout/views, I need to split it to get the payment intent id like I did in the cache checkout data view. I add the below lines of code below my 'order = order_form.save()'. This dumps the shoppingbag to a json string, sets it on the order and then saves the order: 

pid = request.POST.get('client_secret').split('_secret')[0]
            order.stripe_pid = pid
            order.original_bag = json.dumps(bag)
            order.save()

- I then update the code I have for 'order = order_form.save()' and add the commit equals false method to prevent multiple save events from being executed on the database. This method prevents the first save event from happening:

           order = order_form.save(commit=False)

- Then to ensure that I am looking for the correct order in the webhook handler, I add the shoppingbag and the Stripe pid to the list of attributes to match on in my order.objects.get brackets:

                    original_bag=bag,
                    stripe_pid=pid,

- Then if its not found, I want to create the order using those items like would appear in the view. So add the below also to my order.objects.create brackets:

                    original_bag=bag,
                    stripe_pid=pid,

- Adding this code makes that when we receive a webhook from Stripe that a payment has been processed successfully then it tries to find an order with the same customer information and the same grand total which was created with the same items in the shopping bag and its associated with the same payment intent. It will also be attempted multiple times before giving up to create the order in the webhook. There may still be cases where this fails but in most cases this will guarantee that if the order isn't found in the database then its safe to then create it. 

- Last thing I do here is import the Order, OrderLineItem and product models:

from .models import Order, OrderLineItem
from merchandise.models import Product

- I also want to import json:

import json

90. I am now going to test my new changes with a test purchase and check what the stripe webhook response is. I run my dev server and make a purchase through the site. However, this purchase appears to fail as I am redirected to a Server 500 page. I turn Debug on to see what the issue is. I am getting this error:

ValueError at /checkout/
save() prohibited to prevent data loss due to unsaved related object 'order'.
Request Method:	POST
Request URL:	http://127.0.0.1:8000/checkout/
Django Version:	6.0.2
Exception Type:	ValueError
Exception Value:	
save() prohibited to prevent data loss due to unsaved related object 'order'.
Exception Location:	C:\Users\leila\OneDrive\Desktop\Documents\vscode-projects\working_out_gym\.venv\Lib\site-packages\django\db\models\base.py, line 1261, in _prepare_related_fields_for_save
Raised during:	checkout.views.checkout
Python Executable:	C:\Users\leila\OneDrive\Desktop\Documents\vscode-projects\working_out_gym\.venv\Scripts\python.exe
Python Version:	3.12.8
Python Path:	
['C:\\Users\\leila\\OneDrive\\Desktop\\Documents\\vscode-projects\\working_out_gym',
 'C:\\Program Files\\Python312\\python312.zip',
 'C:\\Program Files\\Python312\\DLLs',
 'C:\\Program Files\\Python312\\Lib',
 'C:\\Program Files\\Python312',
 'C:\\Users\\leila\\OneDrive\\Desktop\\Documents\\vscode-projects\\working_out_gym\\.venv',
 'C:\\Users\\leila\\OneDrive\\Desktop\\Documents\\vscode-projects\\working_out_gym\\.venv\\Lib\\site-packages']
Server time:	Fri, 10 Apr 2026 15:33:07 +0000

- I realise there is nothing to save the order before creating the line items so update my checkout/views as below:

order.stripe_pid = pid
order.original_bag = json.dumps(bag)

order.save()

51. I run my dev server and the Stripe listen cmd below in the 2nd terminal:

 stripe listen --forward-to localhost:8000/checkout/wh/

52. I then am able to make a purchase successfully through the site. I then go to Stripe.com to my dashboard and then check out the Webhooks section under Developers. I click the event for payment_intent.succeeded and can see this has failed:

![Stripe webhook payment intent succeeded failed](/static/images/Stripe/Screenshot%20stripe%20payment%20intent%20succeeded%20failed.png)

53. I query this with ChatGPT who advises that this line of code is crashing:

for field, value in shipping_details.address.items():

- It advises that 'shipping_details.address' is not a normal Python dictionary, its a Stripe object so does not support .items(). It recommends replacing the following code:


for field, value in shipping_details.address.items():
    if value == "":
        shipping_details.address[field] = None

To: 

address = shipping_details.address.to_dict()

for field, value in address.items():
    if value == "":
        address[field] = None

- I update this in my webhook_handler file and update all my address references to use the correct code for 'address' and not 'shipping_details.address' like I was using:

country__iexact=address.get('country'),
postcode__iexact=address.get('postal_code'),
town_or_city__iexact=address.get('city'),
street_address1__iexact=address.get('line1'),
street_address2__iexact=address.get('line2'),
county__iexact=address.get('state'),

- Once I have updated my code, I restart my dev server and then the Stripe listening cmd and then make another purchase. Now when I check my Stripe Dashboard webhook events, I can see that the latest purchase that I made is now showing a successful 'Payment Intent.Succeeded' event:

![Stripe webhook payment intent succeeded successful](/static/images/Stripe/Screenshotstripe%20successful%20payment%20intent%20succeeded.png)

54. I now run collectstatic, commit my changes to Git and Heroku before creating my Profile app.

55. Before moving on to creating my profile app, I want to update my checkout view so that the shipping details fields appear more logically. In my checkout.html template, I update these to the order below:

                        {{ order_form.phone_number | as_crispy_field }}
                        {{ order_form.street_address1 | as_crispy_field }}
                        {{ order_form.street_address2 | as_crispy_field }}
                        {{ order_form.postcode | as_crispy_field }}
                        {{ order_form.town_or_city | as_crispy_field }}
                        {{ order_form.county | as_crispy_field }}
                        {{ order_form.country | as_crispy_field }}

- If I refresh my checkout view on my dev server then I can see this looks much better, with the country drop-down appearing at the bottom of the form:

![Checkout Delivery Fields Presented in Logical Order](/static/images/Stripe/Screenshot%20checkout%20delivery%20fields%20more%20logical.png)

---

## Profile App - App Creation and Wiring

1. Now that I have setup and tested my payment system, I want to look at giving the user their own personalised user profile so that they can track and view past orders, save default delivery information and see what fitness/nutrition plans they are currently on. Before I start, I am going to create a new base.html in the templates/allauth folder. Then in the file itself I am going to populate it with the html from Code Institute's Boutique Ado project:

<!DOCTYPE html>
<html>
  <head>
    <title>{% block head_title %}{% endblock %}</title>
    {% block extra_head %}
    {% endblock %}
  </head>
  <body>
    {% block body %}

    {% if messages %}
    <div>
      <strong>Messages:</strong>
      <ul>
        {% for message in messages %}
        <li>{{message}}</li>
        {% endfor %}
      </ul>
    </div>
    {% endif %}

    <div>
      <strong>Menu:</strong>
      <ul>
        {% if user.is_authenticated %}
        <li><a href="{% url 'account_email' %}">Change E-mail</a></li>
        <li><a href="{% url 'account_logout' %}">Sign Out</a></li>
        {% else %}
        <li><a href="{% url 'account_login' %}">Sign In</a></li>
        <li><a href="{% url 'account_signup' %}">Sign Up</a></li>
        {% endif %}
      </ul>
    </div>
    {% block content %}
    {% endblock %}
    {% endblock %}
    {% block extra_body %}
    {% endblock %}
  </body>
</html>

2. Next I replace the current code in my templates/allauth/account/base.html with:

{% extends "base.html" %}

3. Then I create my new app for profiles using:

python3 manage.py startapp profiles

4. I add this to my INSTALLED APPS section of the settings file as below:

    'profiles',

5. Next, I am going to look at the profiles/models. I need a user profile model which is attached to the logged in user which also links to all of their past orders. I will import the user model at the top of the file and then create a user profile model which has a one-to-one field attached to the user (this works the same as a foreign key except it ensures that user can only have 1 x profile). 

from django.contrib.auth.models import user

class UserProfile(models.Model):
     user = models.OneToOneField(User, on_delete=models.CASCADE)

6. Then the rest of the fields in the model are all the delivery information fields that the user should be allowed to be provide defaults for which come from the Order model; so I copy these from the model itself and then paste these into the new UserProfile class:

    phone_number = models.CharField(max_length=20, null=False, blank=False)
    country = CountryField(blank_label='Country *')
    postcode = models.CharField(max_length=20, null=True, blank=True)
    town_or_city = models.CharField(max_length=40, null=False, blank=False)
    county = models.CharField(max_length=80, null=True, blank=True)
    street_address1 = models.CharField(max_length=80, null=False, blank=False)
    street_address2 = models.CharField(max_length=80, null=True, blank=True)

7. I then update the fields so they have 'default' at the beginning to make clear what they are and provide null equals true and blank equals true values for each of them as below:

    default_phone_number = models.CharField(max_length=20, null=True, blank=True)
    default_country = CountryField(blank_label='Country *', null=True, blank=True)
    default_postcode = models.CharField(max_length=20, null=True, blank=True)
    default_town_or_city = models.CharField(max_length=40, null=True, blank=True)
    default_county = models.CharField(max_length=80, null=True, blank=True)
    default_street_address1 = models.CharField(max_length=80, null=True, blank=True)
    default_street_address2 = models.CharField(max_length=80, null=True, blank=True)

8. As I am using Django Countries, I will need to import this at the top of the profiles/models file so do this now with:

from django_countries.fields import CountryField

9. Then under the fields for my UserProfile, I create a string method which will return the username:

    def __str__(self):
        return self.user.username

10. Then below this, I add a quick receiver for the post save event generated by the user model so that whenever a user object is saved, it will automatically either create a profile for them if the user has only just been created. Or save the profile if the user already exists. As there is only one signal, there doesn't need to be a separate signals.py module as was done on the Order model:

@receiver(post_save, sender=User)
def create_or_update_user_profile(sender, instance, created, **kwargs):
    """
    Create or update the user profile
    """
    if created:
        UserProfile.objects.create(user=instance)
    # Existing users: just save the profile
    instance.userprofile.save()

11. Then the last thing I need to do in order gor the signal to work on my receiver is import the post.save and receiver:

from django.db.models.signals import post_save
from django.dispatch import receiver

12. I now have a UserProfile model which will create a profile for everyone who signs up for a new account. I now need to attach the user profile to my Order model before making migrations on the new model changes. In checkout/models, I first import the UserProfile model at the top of the file using:

from profiles.models import UserProfile

13. Then, within the Order model itself, I create a new foreign key for it using the below. I have use models.set_null so if the profile is deleted that we can still keep track of the user's order history in the Admin panel. I allow this to be either null or blank so that users without an account are still able to make purchases. Finally, there is a 'related_name' of orders so that I can access the user's orders:

user_profile = models.ForeignKey(UserProfile, on_delete=models.SET_NULL, null=True, blank=True, related_name='orders')

14. Once these changes are done, I can then run migrations on changes using:

python3 manage.py makemigrations

python3 manage.py migrate

15. These run successfully so I am now going to look at setting up some basic urls, views and templates for the Profiles app. I am going to start in profiles/views and create a basic intitial view so I can see my profiles app as I am building it. In my views file, I create a simple view called 'profile' which just returns the profile.html template with an empty context (for now):

def profile(request):
    """ Display the user's profile. """

    template = 'profiles/profile.html'
    context = {}
    
    return render(request, template, context)

16. Next, I create the url for the new view so it can be accessed, I go to profiles and create a urls.py file in the directory and update the file as below. This imports the view file from profiles directory and then looks at the profile view in the file to create the URL pattern:

from django.urls import path
from . import views

urlpatterns = [
    path('', views.profile, name='profile')
]

17. Next, I need to create the url path in my project level urls path, I update the paths to include the below for profiles:

    path('profile/', include('profiles.urls')),

18. I then look at the template for my new app. In my profiles app directory, I create a new folder called templates with a subfolder for profiles inside this. And then I create a new file for the template called profile.html inside of the templates/profiles folder. Then I will copy my html from checkout.html and paste this into the new file, adjusting accordingly for my profiles app:

- I do not need bagtools so remove this from the top of the file.
- I update the extra css block to use a profiles.css file that I will create in future.
- I then remove all other content, apart from the header, which I update to 'My Profile'.

{% extends "base.html" %}
{% load static %}

{% block extra_css %}
    {{ block.super }}
    <link rel="stylesheet" href="{% static 'profiles/css/profiles.css' %}">
{% endblock %}

{% block page_header %}
    <div class="container header-container">
        <div class="row">
            <div class="col"></div>
        </div>
    </div>
{% endblock %}

{% block content %}
    <!-- Code Institute - Boutique Ado -->
    <div class="container">
        <div class="row">
            <div class="col">
                <hr>
                <h2 class="logo-font mb-4">My Profile</h2>
                <hr>
            </div>
        </div>

 
{% endblock %}

19. Next I create the css directory within the 'profiles' app and then create an empty profiles.css file within here which I can update as I make changes to the profile app:

profiles/static/profiles/css/profiles.css

20. I refresh my dev server and add /profiles to the end of the url to see how this looks at the moment:

![Profile first view = basic template](/static/images/Profiles/Screenshot%20first%20view%20basic%20template.png)

21. This is how I would expect it to look, it's very basic and ready for me to start building it with all the functionality it needs. I run collectstatic, commit to Git and Heroku and then get ready to start integrating the users profile throughout my app.

22. I am doing some testing to see how my login/logout/signup templates look and I decide to fix the issue with my toast notification 'x' button not working. I query with ChatGPT who advises I am not running the script for it in base.html, and to add these above my toast show script:

<script src="https://code.jquery.com/jquery-3.5.1.slim.min.js"></script>
<script src="https://cdn.jsdelivr.net/npm/bootstrap@4.6.2/dist/js/bootstrap.bundle.min.js"></script>

- I do this and then reload my page and test, however, the buttons still do not work. I query further with ChatGPT who advises that it looks like I have a versioning conflict. My toast html uses 'data-dismiss="toast"' which is a Bootstrap 4 syntax but in my base.html I am loading Bootstrap 5.1.3 which uses data-bs-dismiss instead. It advises me to remove jquery completely from the bottom of my base.html. Then to update all my toast templates to use data-bs-dismiss="toast" instead of data-dismiss="toast". I update toast_error, toast_info, toast_success and toast_warning to use the corect data-dismiss class for Bootstrap 5.

- I also need to update the close class on all of the templates from class="close" to class="btn-close", so I update the 4 x toast templates with this now.

- It also advises me to replace my jQuery script 

- I save and refresh my server to see how this looks now, I login and can now click the 'X' on my toast notifications to remove the alerts.

23. I am now going to test logging in and seeing whether I can access the simple profiles page I have just created. Luckily, as I have rebuilt my database several times I now only have 1 x superuser account so don't need to adjust the signal on pre-existing user accounts, I can just create some new accounts now and they should have a profile created with the new signal in place. I sign up for an account on the site:

![Account Signup - initial profile testing](/static/images/Profiles/Screenshot%20account%20signup.png)

24. I am then asked to verify my e-mail address so I will go to the admin panel and login as the superuser. However, after I enter my details and hit logon I am hit with a server 500 error so will set debug to True and reload. The error I am getting is this:

RelatedObjectDoesNotExist at /admin/login/
User has no userprofile.
Request Method:	POST
Request URL:	http://127.0.0.1:8000/admin/login/?next=/admin/
Django Version:	6.0.2
Exception Type:	RelatedObjectDoesNotExist
Exception Value:	
User has no userprofile.
Exception Location:	C:\Users\leila\OneDrive\Desktop\Documents\vscode-projects\working_out_gym\.venv\Lib\site-packages\django\db\models\fields\related_descriptors.py, line 520, in __get__
Raised during:	django.contrib.admin.sites.login
Python Executable:	C:\Users\leila\OneDrive\Desktop\Documents\vscode-projects\working_out_gym\.venv\Scripts\python.exe
Python Version:	3.12.8
Python Path:	
['C:\\Users\\leila\\OneDrive\\Desktop\\Documents\\vscode-projects\\working_out_gym',
 'C:\\Program Files\\Python312\\python312.zip',
 'C:\\Program Files\\Python312\\DLLs',
 'C:\\Program Files\\Python312\\Lib',
 'C:\\Program Files\\Python312',
 'C:\\Users\\leila\\OneDrive\\Desktop\\Documents\\vscode-projects\\working_out_gym\\.venv',
 'C:\\Users\\leila\\OneDrive\\Desktop\\Documents\\vscode-projects\\working_out_gym\\.venv\\Lib\\site-packages']
Server time:	Mon, 13 Apr 2026 07:13:53 +0000

- So I will have to adjust my signal slightly so it'll create a user profile for my superuser account and let me logon. I go to profiles/models and comment out the code under my create_or_update_user_profile function like below:

def create_or_update_user_profile(sender, instance, created, **kwargs):
    """
    Create or update the user profile
    """
    #if created:
        #UserProfile.objects.create(user=instance)
    # Existing users: just save the profile
    #instance.userprofile.save()

- I reload the page and try to logon again and it is now letting me logon so has created me a profile. I can uncomment the code above and then verify my other user's email address and my superusers in the admin panel:

![Profile created successful login](/static/images/Profiles//Screenshot%20profile%20created%20successful%20login.png)

![Verified email addresses](/static/images/Profiles/Screenshot%20verified%20email%20address.png)

- I uncomment the code in profiles/models and then reload my page and login as the standard user.

25. Once logged in as my standard user, I open up 'My Account' from the navbar and click the link to 'My Profile' but nothing happens. I need to update the href on 'My Profile' in the main-nav.html as below so it now directs to the new profile app I have just created:

              <a href="{% url 'profile' %}" class="dropdown-item">My Profile</a>

26. I test again and this now works:

![My Profile My Account Link works](/static/images/Profiles/Screenshot%20my%20profile%20link%20from%20my%20account%20works.png)

27. I now want to go to my profiles/views file and import the user profile model and then get the profile for the current logged in user and then return it to the template:

from django.shortcuts import render, get_object_or_404

from .models import UserProfile


def profile(request):
    """ Display the user's profile. """
    profile = get_object_or_404(UserProfile, user=request.user)

    template = 'profiles/profile.html'
    context = {
        'profile': profile,
    }
    
    return render(request, template, context)

28. Then in profile.html, I will just render the profile where we will see the username printed out:  

        {{ profile }}

29. Now when I reload the profile page I see the username printed out:

![Profile username printed out](/static/images/Profiles/Screenshot%20profile%20initial%20username%20printed%20out.png)

30. With these changes in place, I will save and commit my code to Git and Heroku after running collectstatic.

---

## Profile App - User Profile Form and Views

1. I am now going to build the user profile form. As its very similar to the Order form and the profile model is almost the same as the order model, I am just going to start by copying the checkout/forms content into a forms.py file in the profiles app. I make some tweaks to the code from checkout/forms as below:

- I update the model import to UserProfile
- I update the name of the class and the model in the metaclass
- I remove the fields attribute and replace with the exclude attribute and render all fields except the user field as this shouldn't change. 
- Then in the init function, I remove the full name and email placeholders as these fields don't exist on this model. 
- I then add default in front of the remaining field names to make them match the model.
- In the self.fields I update the autofocus to use the default_phone_number
- I update the country field to default_country 
- Finally I update the classes that we're adding to make the form match the rest of the app

from django import forms
from .models import UserProfile


class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        exclude = ('user',)

    def __init__(self, *args, **kwargs):
        """
        Add placeholders and classes, remove auto-generated
        labels and set autofocus on first field
        """
        super().__init__(*args, **kwargs)
        placeholders = {
            'default_phone_number': 'Phone Number',
            'default_postcode': 'Postal Code',
            'default_town_or_city': 'Town or City',
            'default_street_address1': 'Street Address 1',
            'default_street_address2': 'Street Address 2',
            'default_county': 'County, State or Locality',
        }

        self.fields['default_phone_number'].widget.attrs['autofocus'] = True
        for field in self.fields:
            if field != 'default_country':
                if self.fields[field].required:
                    placeholder = f'{placeholders[field]} *'
                else:
                    placeholder = placeholders[field]
                self.fields[field].widget.attrs['placeholder'] = placeholder
            self.fields[field].widget.attrs['class'] = 'border-black rounded-0 profile-form-input'
            self.fields[field].label = False

2. I go back to profiles/views and import the new profile form at the top of my file:

from .forms import UserProfileForm

3. Then in the profile function, I import the form here and populate it with the current user's profile information and then return it to the template:

    form = UserProfileForm(instance=profile)

4. I can then remove the profile from the context and then use the profile and the related name on the order model to get the users orders and return these to the template instead:

    orders = profile.orders.all()

    template = 'profiles/profile.html'
    context = {
        'form': form,
        'orders': orders,
    }

5. Now I need to render this form in the profile template so I go to profile.html and create a new row above the profile tag. Half of my page will be a profile and the other half will be order history so within the row I then need 2 x columns:

        <div class="row">
            <div class="col-12 lg-6"></div>
            <div class="col-12 lg-6"></div>
        </div>
        {{ profile }}

- In the first column I am going to add a small paragraph heading and a form, I am going to borrow Code Institute's Boutique Ado code for this to save time. The form submits to the profile URL using the POST method, which I will write soon, it has an ID of profile-update-form to make it easily identifiable and inside it renders as a crispy-form. There is also a submit button styled in the way of the rest of the buttons, that floats on the right of the column:

                <p class="text-muted">Delivery Details</p>
                <form class="mt-3" action="{% url 'profile' %}" method="POST" id="profile-update-form">
                    {% csrf_token %}
                    {{ form|crispy }}
                    <button class="btn btn-black rounded-0 text-uppercase float-right">Update Information</button>
                </form>

- Then in the second column I add a paragraph element containing the second column heading of 'Order History' and then a tag to get all user's orders if they have made any:

                <p class="text-muted">Order History</p>
                {{ orders }}

6. I am now going tro run my dev server and go to the profile while logged on as the user to see how this looks:

![Profile Order and Delivery Update not in 2 x columns](/static/images/Profiles/Screenshot%20profile%20updated%20but%20not%20in%202%20x%20columns.png)

7. I realise that my div classes are wrong for my columns on my2 x divs:

            <div class="col-12 lg-6">

- It is missing the column defintion for my large 6 column class, I update to:

            <div class="col-12 col-lg-6">

- I refresh the page and this looks right now:

![Profile Order and Delivery Update now in 2 x columns](/static/images/Profiles//Screenshot%20my%20profile%20now%20in%202%20x%20colsusmns.png)

8. The order of the fields on the 'Delivery Details' form could be more logical and I am going to remove the asterisk from the country field as it's not required on this form. In my profiles/models file, I rearrange the 'Delivery Details' fields accordingly:

class UserProfile(models.Model):
    """User Profile model to allow users to track orders and plans and maintain delivery details"""
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    default_phone_number = models.CharField(max_length=20, null=True, blank=True)
    default_street_address1 = models.CharField(max_length=80, null=True, blank=True)
    default_street_address2 = models.CharField(max_length=80, null=True, blank=True)
    default_postcode = models.CharField(max_length=20, null=True, blank=True)
    default_town_or_city = models.CharField(max_length=40, null=True, blank=True)
    default_county = models.CharField(max_length=80, null=True, blank=True)
    default_country = CountryField(blank_label='Country', null=True, blank=True)

9. Now when I refresh this looks more professional:

![Profile Delivery Details Fields Logical Order](/static/images/Profiles/Screenshot%20updated%20fields%20on%20profile%20delivery%20details.png)

10. I now want to make sure that the profile forms placeholders are coloured correctly so use the below css in my profiles.css file. I have borrowed this from Code Institute:


#profile-update-form .form-control {
    color: #000;
}

#profile-update-form input::placeholder {
    color: #aab7c4;
}

11. I am then going to update the profiles.css further by adding a rule that makes the country field itself as well as all its options black, except the first option, by default. I then make another rule below this one which makes the first option element the colour of the placeholder:

#id_default_country,
#id_default_country option:not(:first-child) {
    color: #000;
}

#id_default_country option:first-child {
    color: #aab7c4;
}

12. This looks good when I restart and refresh the page. However, the first option is not showing as grey when selected so I remedy this in the profile.html template and open a new postload js block at the bottom of the file and then borrow Code Institute's Boutique Ado Javascript. The script will first get the value of the country field whem the page loads and then will store this in a variable - the value will be an empty string if the first option is selected. To determine if this has been selected it then uses a boolean - so if country is selected = false then the colour of this element should be grey:

{% block postloadjs %}
    {{ block.super }}
    <script type="text/javascript">
        let countrySelected = $('#id_default_country').val();
        if(!countrySelected) {
            $('#id_default_country').css('color', '#aab7c4');
        }
    </script>
{% endblock %}

13. Then, still inside the script tags, I want to capture the change event so that everytime the box changes we get the value of it:

        $('#id_default_country').change(function() {
            countrySelected = $(this).val();

        })

- And then I need to determine the proper colour:

    if(!countrySelected) {
        $(this).css('color', '#aab7c4');
    } else {
        $(this).css('color', '#000');
    }
        });

14. I then create a 'js' folder within my profiles/static/profiles folder where I then create new file called 'countryfield.js' and I cut and paste the javascript I just wrote at the bottom of my profile.html into this new separate Javascript file. Then back in my profile template in my postload js block, I call the file using the src method, as below:

<script type="text/javascript" src="{% static 'profiles/js/countryfield.js' %}"></script>

15. However, when I reload the page it isn't applying the changes I wanted. If I inspect the page in devtools, go to the Network tab and then refresh the page I can see that the countryfield.js file is failing:

![Devtools countryfield Javascript failing](/static/images/Profiles/Screenshot%20devtools%20countryfield%20js%20failing.png)

16. I query this with ChatGPT who advises that it is most likely due to the that the code in my countryfield.js file requires jQuery which I removed from my Project earlier. I add the below line above my script src for countryfield.js:

<script src="https://code.jquery.com/jquery-3.6.0.min.js"></script>

17. I hard reload the site to see whether its now loading my Javascript file but I am still seeing the error. ChatGPT recommends updating the code in my countryfield.js so that it doesn't use jQuery. I update this and test now but it's still not loading the file. I then run a collectstatic and then restart the dev server and can see this is now taking affect.

18. Next I am going to write the post handler for the profile view. In profile/views at the top of my profile function, i set an if statement that says, if the request method is POST then create a new instance of the user profile using the post data and tell it the instance we're updating is the profile just retrieved above. Then if the form is valid, save and add a success message

    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            messages.success(request, 'Profile updated successfully')

- Then at the top of the file I will need to import messages:

from django.contrib import messages

- The rest of the logic stays the same as all we're doing is replacing the form variable with the user's updated profile and returning the same template. I test this out on the dev server. I add an item to my cart and then update my delivery details on my Profile. When I save the details to my profile, I receive a toast message saying that the profile has updated but it also contains a preview of my bag:

![Toast Profile Update Msg Cart Preview](/static/images/Profiles/Screenshot%20bag%20details%20showing%20on%20profile%20update%20message.png)

- To resolve this, I need to go back into profile/views and then add another context variable called 'on_profile_page' which is set to true:

'on_profile_page': True

- Then I go to my toast_success.html template in templates/includes/toasts. Then in the section with my if statement for grand_total, I will also check that I am not on the profile page to make it so that the shopping bag preview only shows up in the success message if we're not on the profile page:

    {% if grand_total and not on_profile_page %}

- Now if I refresh and update the profile, the toast message looks much better:

![Toast Profile Update Msg Cleaner](/static/images/Profiles/Screenshot%20clean%20profile%20toast%20message%20success.png)

19. I now run collectstatic and commit my changes to Git and Heroku before looking at setting up user's order histories in their profiles and setting up checkout so it autofills payment and delivery forms.

20. In my profile.html template, I am going to add the section below for my 'Order History' using a simple reponsive Bootstrap table so it'll expand cleanly with each new order that the user makes. 
The table will be small and have no borders with 4 x columns in the head: Order number, date, items and the order total. 
Then in the table body, it will iterate through the orders returned from the profile view and generate a new row for each one. 
The order number cell will be a link to a url for the 'order history which is passed the order number. Then the link is given a title so that when hovered over it gives the whole order number. To condense this down a little, I will pipe the order number into the built-in truncate characters filter to limit it to 6 x characters. 
Then the order date and grand_total are straight forward tags which are added below the order number code. The items in the shopping bag will be found using an unordered unstyled list and then for each item in the orders list of the line-items it will make a small text summary of it with the size, where applicable, then the product name and the quantity being purchased:

                <div class="order-history table-responsive">
                    <table class="table table-sm table-borderless">
                        <thead>
                            <tr>
                                <th>Order Number</th>
                                <th>Date</th>
                                <th>Items</th>
                                <th>OrderTotal</th>
                            </tr>
                        </thead>
                        <tbody>
                            {% for order in orders %}
                                <tr>
                                    <td>
                                        <a href="{% url 'order_history' order.order_number %}"
                                        title="{{ order.order_number }}">
                                            {{ order.order_number|truncatechars:6 }}
                                        </a>
                                    </td>
                                    <td>{{ order.date }}</td>
                                    <td>
                                        <ul class="list-unstyled">
                                            {% for item in order.lineitems.all %}
                                                <li class="small">
                                                    {% if item.product.has_sizes %}
                                                        Size {{ item.product.size|upper }}
                                                    {% endif %}{{ item.product.name }} x{{ item.quantity }}
                                                </li>
                                            {% endfor %}
                                        </ul>
                                    </td>
                                    <td>${{ order.grand_total }}</td>
                                </tr>
                            {% endfor %}
                        </tbody>
                    </table>
                </div>

21. I now need to set a max-height for the Order History form in case user has a lot of orders. In the profiles.css file, I add the below rules which is 416px for the height of the form and the submit button in the adjacent column so anything above the height of 416px will have a scrollbar:

.order-history {
    max-height: 416px; /* height of profile form + submit button */
    overflow-y: auto;
}

22. The template will not open until I have created the Order History url and view. I start by creating this in profile/views file. I create a new view called 'order_history' which takes the order number as thhe parameter:

def order_history(request, order_number):

- I then get the order using below simple logic:

    order = get_object_or_404(Order, order_number=order_number)

- As I am retrieving the order, I will need to import the Order model at the top of the file:

from checkout.models import Order

- Then I will add a message which lets the user know they are looking at a past order confirmation:

    messages.info(request, (
        f'This is a past confirmation for order number {order_number}.'
        'A confirmation email was sent on the order date.'
    ))

- Then the last thing I need to do is give it a template and context which includes the order number. It will use the checkout_success template as that template already has the layout for rendering order confirmation. I have added another variable to the context called from_profile so we can check in this template whether the user accessed this via the 'order history' view:


    template = 'checkout/checkout_success.html'
    context = {
        'order': order,
        'from_profile': True,
    }

    return render(request, template, context)

23. With the views file now updated, I can go create my url for this view now. In profiles/urls, I create a new path for 'Order History'. The url will be order_history followed by the order_number, the view will return the order_history view and then have a matching name of order_history:

    path('order_history/<order_number>', views.order_history, name='order_history'),

24. Now I go to my checkout_success template and at the bottom of my template with the order confirmation, I add a check of whether user has come from the profile page and if they have I will render them a button taking them back to this page if they wish:

           {% if from_profile %}
              <a href="{% url 'profile' %}" class="btn btn-black rounded-0 my-2">
                  <span class="icon mr-2">
                      <i class="fas fa-angle-left"></i>
                  </span>
                  <span class="text-uppercase">Back to Profile</span>
              </a>
           {% else %}

25. I now need to implement the mechanism to assign orders to specific user profiles. To start with, I am going to make the user profile field available in the admin panel. To do this I go to checkout/admin and then add the user profile field as below:

        'user_profile',

26. Now what I need is a way to associate the order with the user's profile when the order is created. The most appropriate place for this then would be the checkout_success view as we know the form has been submitted and the order has been successfully processed so this is a good place to add the user's profile. 

In checkout/views, in my view for checkout_success, as we already have the order, I just need to add the profile by checking if the user is authenticated. 
Then I can get the user's profile and set it on the order and save it. 
I can also use the 'save info' box, first determining whether it was checked and if so, pull the data to go into the user's profile off the order into a dictionary of profile data. The dictionaries' keys will match the fields on the user profile model, such as the default phone number, country, postcode, etc. 

    if request.user.is_authenticated:
        profile = UserProfile.objects.get(user=request.user)
        # Attach the user's profile to the order
        order.user_profile = profile
        order.save()

        # Save the user's info
        if save_info:
            profile_data = {
                'default_phone_number': order.phone_number,
                'default_country': order.country,
                'default_postcode': order.postcode,
                'default_town_or_city': order.town_or_city,
                'default_street_address1': order.street_address1,
                'default_street_address2': order.street_address2,
                'default_county': order.county,
            }

27. Then I want to create my own instance of the user profile form using the profile data and then tell it that it will update the profile just obtained and then to save it:

            user_profile_form = UserProfileForm(profile_data, instance=profile)
            if user_profile_form.is_valid():
                user_profile_form.save()

28. Then because I am using the profile model and user profile form, I need to import both of these files at the top of checkout/views:

from profiles.models import UserProfile
from profile.forms import UserProfileForm

29. I now test this by removing all the details from my user profile and clicking 'Update Information' once it has been removed. I then go to checkout an order but notice that the 'Payment' stripe element is gone and it just has text saying payment. I inspect devtools on the element to see what is happening. I can see that I am getting this error in the console:

stripe_elements.js:2 Uncaught ReferenceError: $ is not defined at stripe_elements.js:2:1

- I query this with ChatGPT who advises that the stripe_element.js is loading jQuery but I removed this globally from my app earlier. The best fix to resolve this would be to add it back in so I will do this now and add above my Bootstrap link in base.html:

<script src="https://code.jquery.com/jquery-3.6.0.min.js"></script>

- After updating base.html and reloading my app and doing a hard refresh, I can see the payment link again. I tick the 'Save this delivery information to my profile' and then complete the order:

![Checkout order save info](/static/images/Profiles/Screenshot%20checkout%20saving%20information%20to%20profile.png)

- After I complete the order I get redirected to a server 500 page, so I turn Debug on to see what is happening. I refresh and looks like there is an invalid endblock in my checkout_success.html. I update this now but it is still erroring. It seems there is another issue with a broken if statement across two lines in my for loop on OrderLineItems so I rectify this:

              {{ item.product_variant.product.title }} 
              {% if item.product_variant.variant_title %}
              -{{item.product_variant.variant_title|upper }} 
              {% endif %}

- Then I add an {% endblock %} tag at the bottom of the file and reload and this has been successful now but the styling is a bit off:

![Checkout success view messed up](/static/images/Profiles/Screenshot%20checkout%20success%20page%20looks%20wrong.png)

- I take a look at my checkout_success.html file again and realise there is open divs so close these and then make a new order but the page still doesn't look right. I query with ChatGPT who advises I am loading my Bootstrap 5 css in the wrong place in base.html, this should be loading in my corecss block instead of the extra css block. I remove from the extra css block and place in the corecss block and hard reload my page and can now see the correct view for checkout success:

![Checkout success view resolved](/static/images/Profiles/Screenshot%20checkout%20success%20view%20fixed.png)

30. I now go to 'My Profile' page under 'Account' and can see the 2 x new orders I have just made and that my delivery details were updated and saved to the profile when the order was made, through ticking the 'Save Delivery Info' box:

![Order History and Delivery Info saving to profile](/static/images/Profiles/Screenshot%20order%20history%20and%20delivery%20details%20saving%20to%20profile.png)

- Also if I hover over the 'Order Number' link, I can then see the whole order number. If I click the order number link then this redirects to the correct Order History URL:

![Order History URL working](/static/images/Profiles/Screenshot%20order%20history%20click%20redirect%20working.png)

- The 'Back to Profile' button works too.

31. Now that I have confirmed that the delivery details are saving to user's profiles. I want to further expand on this by using the user's default delivery details saved to their profile to pre-fill the delivery details form on the checkout page.

Back in checkout/views, in the checkout view above the if not stripe_public_key statement, I add the below code. This checks whether the user is authenticated and if so, then it gets the user's profile and uses the intiial parameter on the order form to pre-fill all the fields with its information from the profile. I will use the full_name with the built-in get_full_name method on their user account, their email address from their user account asnd then everything else from the default information stored in their profiles. Then if the user is not authenticatred then it will just render an empty form:

        if request.user.is_authenticated:
            try:
                profile = UserProfile.objects.get(user=request.user)
                order_form = OrderForm(initial={
                    'full_name': profile.user.get_full_name(),
                    'email': profile.user.email,
                    'phone_number': profile.default_phone_number,
                    'country': profile.default_country,
                    'postcode': profile.default_postcode,
                    'town_or_city': profile.default_town_or_city,
                    'street_address1': profile.default_street_address1,
                    'street_address2': profile.default_street_address2,
                    'county': profile.default_county,
                })
            except UserProfile.DoesNotExist:
                order_form = OrderForm()
        else:
            order_form = OrderForm()

32. I now want to test this so I go back through Checkout and see whether it has automatically populated the Delivery Details on the form. I can see it has populated everything apart from full_name. I think this is because there is no full name populated for my user. I go to the admin panel logged in as my superuser and check whether full name is populated for my standard user, which they do not so I populate this now:

![Populating full name for standard user in admin](/static/images/Profiles/Screenshot%20populating%20full%20name%20standard%20user%20admin%20panel.png)

33. Once this is saved, I log back in as my standard user and go to Checkout and can see this has populated a full name now too:

![Full name populated in checkout form](/static/images/Profiles/Screenshot%20full%20name%20now%20populated%20in%20checkout%20details%20form.png)

34. Now that the profile is nearly setup and complete, I will collectstatic and commit my changes to Git and Heroku.

---

## Profile App - Webhooks for Card Details

1. I now want to update my webhook handler to be able to handle user profiles so that if the checkout view fails then it can depend on the webhook handler to perform all the same functionality. In my checkout/views in the payment intent succeeded handle method, I added the key in the payment intent for metadata; this contains the username of the user who placed the order and whether they want to save their info. I now want to handle that in my webhook_handler above my order_exists = false statement.

- I start with a comment to say this section of code is for updating profile information.
- Then in my code itself I set the profile to none ( this is to still allow anonymouse users to checkout)
- Then I retrieve the username from itent.metadata.username and then if the username isn't 'AnonymousUser' then we know the user isn't authenticated.
- Then as an alternative method to checking whether the user is authenticated, I use request.user as we can get the request method from the init method above.
- Then if they're not anonymous, it will try and get the profile using their username
- If it finds that the user has got the 'Save Delivery Info' box checked, which also comes from the Metadata I added, then it will update their profile by adding the shipping details as their default delivery details. 
- Finally, I save the profile.

        # Update profile information if save_info was checked
        profile = None
        username = intent.metadata.username
        if username != 'AnonymousUser':
            profile = UserProfile.objects.get(user__username=username)
            if save_info:
                profile.default_phone_number = shipping_details.phone
                profile.default_country = shipping_details.address.country
                profile.default_postcode = shipping_details.address.postal_code
                profile.default_town_or_city = shipping_details.address.city
                profile.default_street_address1 = shipping_details.address.line1
                profile.default_street_address2 = shipping_details.address.line2
                profile.default_county = shipping_details.address.state
                profile.save()

2. Further down the webhook_handler file where I define my else statement for if the order DoesNotExist, I will update this, as we already have their profile and if they weren't logged in it gets defined as none so I will just add it to their order when the webhook creates it. This way the webhook handler can create orders for both authenticated users by attaching their profile and for anonymous users by setting this field to none by adding user_profile=profile to the order statement below:

            except Order.DoesNotExist:
                attempt += 1
                time.sleep(1)
            if order_exists:
                return HttpResponse(
                    content=f'Webhook received: {event["type"]} | SUCCESS: Order already exists',
                    status=200
                )
            try:
                order = Order.objects.create(
                    full_name=shipping_details.name,
                    user_profile=profile,

3. Now I just need to import the UserProfile model at the top of the file:

from profiles.models import UserProfile

4. I now want to test my new webhook_handler code is working. To do this, I will need to first comment out the submission of the form in my stripe_elements.js file to ensure that the checkout view will fail and that I never reach the checkout success page. In stripe_elements.js I comment out the form.submit() code. If my code is working then this shouldn't pose an issue as the webhook handler should catch the payment intent succeeded webhook from Stripe and then handle it all for me.

- I run my page on my devserver and go to Checkout and try to complete checkout. This completes the order successfully, taking me to the checkout success page and providing me with an order number showing that even with the form completely broken that my payments can still work. I can also see that Stripe has posted to my terminal to say the order was completed successfully too:

UPDATING PAYMENT INTENT: pi_3TM4BG1urpY1vbdf0W2M0wXB
METADATA: {'1': 1}
[14/Apr/2026 12:19:27] "POST /checkout/cache_checkout_data/ HTTP/1.1" 200 0
[14/Apr/2026 12:19:28] "POST /checkout/wh/ HTTP/1.1" 200 44
[14/Apr/2026 12:19:28] "POST /checkout/ HTTP/1.1" 302 0
[14/Apr/2026 12:19:29] "GET /checkout/checkout_success/6DC42D66B44546FFBCC1D353D52AFEA5 HTTP/1.1" 200 16720

![Payment form broken checkout successful](/static/images/Profiles/Screenshot%20payment%20form%20broken%20successful%20order.png)

- Then if I also check in the admin panel, I can see the order was created successfully and attached the user profile here too:

![Payment form broken admin successful order and profile attachment](/static/images/Profiles/Screenshot%20payment%20form%20broken%20admin%20order%20success.png)

- The user can also see it themselves under their Profile Order History:

![Payment form broken order in user profile](/static/images/Profiles/Screenshot%20payment%20form%20broken%20order%20in%20user%20order%20history.png)

5. Now that I have tested this successfully, I can uncomment the form submit on my stripe_elements.js code and then run a collectstatic before committing my code to Git and Heroku. 

6. I now want to finalise my payment system so that users are sent a confirmation email when their order has completed. I need to do this in webhook_handler, as this is the best point to send the email after we know the payment has definitely been made as the only thing that can trigger it here is a webhook from Stripe. The first thing that I want to do is write a confirmation email which will be split into two text files in the checkout/templates folder: one called confirmation_email_subject and the other called confirmation_email_body. These will be in a subfolder under the templates folder called 'confirmation_emails':

![Confirmation email structure](/static/images/Profiles/Screenshot%20confirmation%20email%20structure.png)

7. In The confirmation_email_subject.txt file, it will say Working Out Gym and then include the order number with a django template syntax:

Working Out Gym Confirmation for Order Number {{ order.order_number }}

8. I then populate the confirmation_email_body.txt with what I would like the order confirmation emails to say to each user, using django template tags where the values are changeable:

Hi there, {{ order.full_name }}!

This is a confirmation of your order at WORKING OUT GYM. 

Your order information is below:

Order Number: {{ order.order_number }}
Order Date: {{ order.date }}

Order Total: ${{ order.order_total }}
Delivery: ${{ order.delivery_cost }}
Grand Total: ${{ order.grand_total }}

Your order will be shipped to {{ order.street_address1 }} in {{ order.town_or_city }}, {{ order.country }}.

We've got your phone number on file as {{ order.phone_number }}.

If you have any questions, feel free to contact us at {{ contact_email }}.

Thank you for your order from all of us at,

WORKING OUT GYM

9. Once these 2 x files are in place, I can then look at my webhook_handler file to write a new private method called _send_confirmation_email that takes in 'self' and 'order' parameters. It will take in self as part of the class. It starts with an underscore as it will only be in this class:

def _send_confirmation_email(self, order):
    """Sends user confirmation email"""

10. Then to make this code functional and allow emails to be sent, I need to import the send mail function from django.core, the render_to_string from django.template.loader and the settings file from django.conf:

from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.conf import settings

11. Then back in my method for _send_confirmation_email I get the customers email from the order and then store it in a variable using:

cust_email = order.email

12. Then below this, I use the render_to_string method to render both the files I just created two strings for. The first parameter will be the file we want to render and the second is a context to render the various context variables in the confirmation email. Then it passes the order to 'subject':

      subject = render_to_string(
          'checkout/confirmation_emails/confirmation_email_subject.txt',
          {'order': order})

13. Then for body, I pass the order as well as a contact email which will be added to the settings file soon

    body = render_to_string(
        'checkout/confirmation_emails/confirmation_email_body.txt',
        {'order': order, 'contact_email': settings.DEFAULT_FROM_EMAIL})   

14. Then to actually send the email, I use the send mail function, giving it the body and the email I want to send from and a list of emails we're sedning to - the customer's:

        send_mail(
            subject,
            body,
            settings.DEFAULT_FROM_EMAIL,
            [cust_email]
        )   

15. Now I want to call it twice, further down the webhook_handler file, to send en email. Where I have my if statement for if the order_exists because it was already created by the form and if the order was created by the webhook_handler, I will insert the below code which will call the the send email method before returning the response to Stripe:

        self._send_confirmation_email(order)

16. Now I need to add the DEFAULT_FROM_EMAIL attribute to my settings file. I will set this as workingoutgym@example.com. I add this at the bottom of the file with the rest of my Stripe attributes:

DEFAULT_FROM_EMAIL = 'workingoutgym@example.com'

17. I run my dev server but get the following error:

  File "C:\Users\leila\OneDrive\Desktop\Documents\vscode-projects\working_out_gym\checkout\webhook_handler.py", line 22
    """Sends user confirmation email"""
    ^
IndentationError: expected an indented block after function definition on line 21

18. I go to my webhook_handler and resolve the indentation issue now. I reload the server and then test making a purchase. I can see this has successfully processed the email in the terminal when I make a purchase now:

"POST /checkout/ HTTP/1.1" 302 0
[14/Apr/2026 13:39:24] "GET /checkout/checkout_success/F89BC327FA0247F580360F4CFC792B3F HTTP/1.1" 200 16726
Content-Type: text/plain; charset="utf-8"
Content-Transfer-Encoding: quoted-printable
MIME-Version: 1.0
Subject: Working Out Gym Confirmation for Order Number
 F89BC327FA0247F580360F4CFC792B3F
From: workingoutgym@example.com
To: leilahhodgson@gmail.com
Date: Tue, 14 Apr 2026 12:39:25 +0000
Message-ID: <177617036542.40752.9617390663972877806@Jinx>

Hi there, Leilah Hodgson!

This is a confirmation of your order at WORKING OUT GYM.=20

Your order information is below:

Order Number: F89BC327FA0247F580360F4CFC792B3F
Order Date: April 14, 2026, 12:39 p.m.

Order Total: $32.00
Delivery: $3.20
Grand Total: $35.20

Your order will be shipped to 31 Goldsmith Street in Barrow-in-Furness, GB.

We've got your phone number on file as 07857895351.

If you have any questions, feel free to contact us at workingoutgym@example.c=
om.

Thank you for your order from all of us at,

WORKING OUT GYM

19. It will not actually send the email yet as the project does not yet have this functionality, I will add this in later down the line. I run collectstatic and then commit my changes to Git and Heroku.

---

## Fitness and Nutrition Plans - App Creation and Wiring

1. I create a new app for my 'Fitness and Nutritions Plans' page to be contained within called 'plans' using Python:

python manage.py startapp plans

2. After creating my new app, I need to then add this to INSTALLED APPS in settings:

'plans',

3. Once I can see my new 'plans' app directory has been created, I go to plans/models and add the below code which ChatGPT has generated for me:. This defines the two different choices of plans: fitness and nutrition and the associated fields. I want the plans to have a title for what kind of nutrition/fitness plan it is, a description to give the users a bit more detail about it, a generic image either of food or exercise and then the price. The plan_type variable has a max character length of 10 and then links to the PLAN_TYPE_CHOICES defined above@

from django.db import models
from django.contrib.auth.models import User

class Plan(models.Model):
    PLAN_TYPE_CHOICES = [
        ('fitness', 'Fitness'),
        ('nutrition', 'Nutrition'),
    ]

    title = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ImageField(upload_to='plans/')
    price = models.DecimalField(max_digits=6, decimal_places=2)

    plan_type = models.CharField(max_length=10, choices=PLAN_TYPE_CHOICES)

    def __str__(self):
        return self.title        

4. I want to enforce a rule on the users that they can only purchase 1 x nutrition and/or 1 x fitness plan at a time and if they want to change these they would need to contact the superuser of the page. Therefore, below my new class for Plan in the plans/models, I will define a new class for UserPlan which enforces this:

class UserPlan(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    plan = models.ForeignKey(Plan, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user} - {self.plan}"

5. Now that I have finished making my intial changes to the plans/models, I need to run makemigrations and migrate.

6. In my plans directory I create a utils.py file and wuithin it create a view which enforces the restriction. I call this view can_purchase_plan and set some if statements to check whether user already has a pre-existing nutrition or fitness plan:

def can_purchase_plan(user, plan):
    if plan.plan_type == 'fitness':
        return not UserPlan.objects.filter(
            user=user,
            plan__plan_type='fitness'
        ).exists()

    if plan.plan_type == 'nutrition':
        return not UserPlan.objects.filter(
            user=user,
            plan__plan_type='nutrition'
        ).exists()

    return False

- Then at the top of the file I import the UserPlan class from models so my view can function.

from .models import UserPlan

7. I now need to look at the purchase flow for my plans app. I have decided to keep it separate from the merchandise app as it will be complicated and messy. Plans will be treated like direct purchases, so the user would click 'Buy Plan' , go to the Checkout and then purchase the plans here and save it to UserPlan so flow will look like:

- User goees to the 'Fitness and Nutritions Plans' page
- User clicks 'Buy Plan'
- User is then redirected to the Checkout page
- User pays via Stripe method I already have in place
- Upon successful purchase, UserPlan is then saved to the user's profile and shows the checkout_success page

8. In plans/views I create the below view which imports the Plan model I have just created and then pulls these through on the plans_list view and returns them in the plans/html template:

from .models import Plan

def plans_list(request):
    plans = Plan.objects.all()

    fitness_plans = plans.filter(plan_type='fitness')
    nutrition_plans = plans.filter(plan_type='nutrition')

    has_fitness_plan = False
    has_nutrition_plan = False

    if request.user.is_authenticated:
        user_plans = UserPlan.objects.filter(user=request.user)

        has_fitness_plan = user_plans.filter(plan__plan_type='fitness').exists()
        has_nutrition_plan = user_plans.filter(plan__plan_type='nutrition').exists()

    return render(request, 'plans/plans.html', {
        'fitness_plans': fitness_plans,
        'nutrition_plans': nutrition_plans,
        'has_fitness_plan': has_fitness_plan,
        'has_nutrition_plan': has_nutrition_plan,
    })

9. Next I need to create a urls.py file in my new plans app directory and populate with the code below with the 2 x imports and the new urlpattern for plans that looks at the new plans_list view that I just created:

from django.urls import path
from . import views

urlpatterns = [
    path('', views.plans_list, name='plans'),
]

10. Next I need to update my template so there is a 'Buy' button on the plans themselves. I do not have a templates directory created yet so create this now in plans/templates/plans and then create the template itself in the plans subfolder called plans.html. Then in the new template, I want a header with a paragraph element explaining what the page is about and the rule around only being allowed to purchase one of each type of plan per customer. I then want 2 x rows with 3 columns in each row that will contain the 3 x nutrition plans and then 3 x fitness plans in the row for each type. Then the content for the plans themselves will include a title, image, description with 2 x href elements: one with a 'Buy Plan' option and the other which will show if the if user is authenticated statement doesn't detect the user as logged in which asks user to login. It also disables the already owned plans:

{% extends "base.html" %}
{% load static %}

{% block content %}

      <img src="{{ plan.image.url }}" class="card-img-top" alt="{{ plan.title }}">

      <div class="card-body d-flex flex-column">
        <h5 class="card-title">{{ plan.title }}</h5>

        <p class="card-text">
          {{ plan.description }}
        </p>

        <p class="mt-auto"><strong>£{{ plan.price }}</strong></p>

        {% if user.is_authenticated %}
        {% if has_fitness_plan %}
            <button class="btn btn-secondary w-100" disabled>
            Already Own a Fitness Plan
            </button>
        {% else %}
            <a href="{% url 'buy_plan' plan.id %}" class="btn btn-black w-100">
            Buy Plan
            </a>
        {% endif %}
        {% else %}
        <a href="{% url 'account_login' %}" class="btn btn-outline-dark w-100">
            Login to Purchase
        </a>
        {% endif %}
      </div>

    </div>
  </div>
{% endfor %}
      <img src="{{ plan.image.url }}" class="card-img-top" alt="{{ plan.title }}">

      <div class="card-body d-flex flex-column">
        <h5 class="card-title">{{ plan.title }}</h5>

        <p class="card-text">
          {{ plan.description }}
        </p>

        <p class="mt-auto"><strong>£{{ plan.price }}</strong></p>

        {% if user.is_authenticated %}
        {% if has_nutrition_plan %}
            <button class="btn btn-secondary w-100" disabled>
            Already Own a Nutrition Plan
            </button>
        {% else %}
            <a href="{% url 'buy_plan' plan.id %}" class="btn btn-black w-100">
            Buy Plan
            </a>
        {% endif %}
        {% else %}
        <a href="{% url 'account_login' %}" class="btn btn-outline-dark w-100">
            Login to Purchase
        </a>
        {% endif %}
      </div>

    </div>
  </div>
{% endfor %}

11. I now need to create my buy_plan view in plans/views. ChatGPT has generated me the code for this. It checks the restrictions I have set, whether the user already owns plans and if they are authenticated as users cannot purchase plans without first being logged in. It stores the plan in their session and redirects them to the checkout page on success. I have import the get_object_or_404 method, django messages and the .utils view i created earlier for can_purchase_plan where I defined my restrictions:

def buy_plan(request, plan_id):
    plan = get_object_or_404(Plan, id=plan_id)

    if not request.user.is_authenticated:
        messages.error(request, "You must be logged in to purchase a plan.")
        return redirect('account_login')

    if not can_purchase_plan(request.user, plan):
        messages.error(request, "You already own this type of plan.")
        return redirect('plans')

    # store plan in session
    request.session['plan_purchase_id'] = plan.id

    return redirect('checkout')

12. Then I update my plans/urls file with the path for the new buy_plan I have just created:

path('buy/<int:plan_id>/', views.buy_plan, name='buy_plan'),

13. Then over in my project urls.py file, I add the new path to include all of my plans urls as below:

path('plans/', include('plans.urls')),

14. I now need to look at my current checkout view to split this so that it looks at the plans and products from merchandise as two separate checkouts. In my checkout/views in the checkout view, I replace the following code:

shoppingbag = request.session.get('bag', {})

if not shoppingbag:
    messages.error(request, "Your bag is currently empty.")
    return redirect(reverse('merchandise'))

- With:

shoppingbag = request.session.get('bag', {})
plan_id = request.session.get('plan_purchase_id')

#Allow checkout if EITHER bag OR plan exists
if not shoppingbag and not plan_id:
    messages.error(request, "Your bag is currently empty.")
    return redirect(reverse('merchandise'))

- Then still in the checkout view where I calculate the total, I replace the following code:

current_bag = bag_contents(request)
total = current_bag['grand_total']
stripe_total = round(total * 100)

- With this:

plan = None

if plan_id:
    from plans.models import Plan
    plan = Plan.objects.get(id=plan_id)
    total = plan.price
else:
    current_bag = bag_contents(request)
    total = current_bag['grand_total']

stripe_total = round(total * 100)

- Then still in my checkout view, I need to update the context passed to my checkout template to include the plan:

'plan': plan if plan_id else None,

- Then in my checkout view where it checks if the order form is valid, I add the below logic to occur before my bag loop so it looks at plans before products:

    plan_id = request.session.get('plan_purchase_id')

    if plan_id:
        from plans.models import Plan, UserPlan

        plan = Plan.objects.get(id=plan_id)

        # Save ownership of plan
        UserPlan.objects.create(
            user=request.user,
            plan=plan
        )

- Then in the same file in my checkout_success view, I want to clear the session after successs so replace this code:

if 'bag' in request.session:
    del request.session['bag']

- With:

if 'bag' in request.session:
    del request.session['bag']

if 'plan_purchase_id' in request.session:
    del request.session['plan_purchase_id']

15. Then in my checkout.html template, I need to update it so this shows the plans in order for my new updates to work. Above my for loop that iterates through my bag items, I will add the below if statement for my plans - this way if a user is buying a plan it will show the plan and if a user is buying products then it will show the bag items:

{% if plan %}
  <div class="mb-3 p-3 border">
    <p><strong>{{ plan.title }}</strong></p>
    <p>£{{ plan.price }}</p>
  </div>
{% endif %}

16. Now that my views and templates are set-up, my restrictions in place and the plans have been hooked into checkout and checkout_success, I want to then start adding the plans and testing the new page. I will add the below code to plans/admin so that I can then login as my superuser and create some plans:

from .models import Plan, UserPlan

@admin.register(Plan)
class PlanAdmin(admin.ModelAdmin):
    list_display = ('title', 'plan_type', 'price')


@admin.register(UserPlan)
class UserPlanAdmin(admin.ModelAdmin):
    list_display = ('user', 'plan')

17. I update my main-nav.html ahref url with the path for my new plans page:

"{% url 'plans:plans' %}"

18. I now run my dev server but encounter a server 500 error as soon as I load the page so I turn debug on and reload to see what is happening:

NoReverseMatch at /
'plans' is not a registered namespace

19. I realise I haven't created a namespace for 'plans' app in my plans/urls file so add this now and then reload:

app_name = 'plans'

20. I can now load my page back up on my dev server again. I go to test my new 'Fitness and Nutritions Plans' update in main-nav.html by seeing if it will load from clicking the option for it in the navbar menu. However, it does not, it instead gives me this error:

TemplateSyntaxError at /plans/
Invalid block tag on line 37: 'endfor', expected 'endblock'. Did you forget to register or load this tag?
Request Method:	GET
Request URL:	http://127.0.0.1:8000/plans/
Django Version:	6.0.2
Exception Type:	TemplateSyntaxError
Exception Value:	
Invalid block tag on line 37: 'endfor', expected 'endblock'. Did you forget to register or load this tag?

- I query this with ChatGPT after troubleshooting and being unable to find the cause of the issue, ChatGPT advised the structure and no iteration had broken the template and to replace with the below:

{% extends "base.html" %}
{% load static %}

{% block content %}

<div class="container mt-5">

  <!-- ✅ NEW: PAGE HEADER -->
  <h2 class="text-center mb-3">Fitness & Nutrition Plans</h2>
  <p class="text-center mb-5">
    Choose from our exclusive fitness and nutrition plans. You may only purchase
    one of each type. To switch plans, please contact admin.
  </p>

  <!-- ================= FITNESS PLANS ================= -->
  <div class="row">
    {% for plan in fitness_plans %}  <!-- ✅ ADDED LOOP -->
      <div class="col-md-4 mb-4">
        <div class="card h-100">

          <img src="{{ plan.image.url }}" class="card-img-top" alt="{{ plan.title }}">

          <div class="card-body d-flex flex-column">
            <h5 class="card-title">{{ plan.title }}</h5>

            <p class="card-text">
              {{ plan.description }}
            </p>

            <p class="mt-auto"><strong>£{{ plan.price }}</strong></p>

            {% if user.is_authenticated %}
              {% if has_fitness_plan %}
                <button class="btn btn-secondary w-100" disabled>
                  Already Own a Fitness Plan
                </button>
              {% else %}
                <!-- ✅ FIXED URL NAMESPACE -->
                <a href="{% url 'plans:buy_plan' plan.id %}" class="btn btn-black w-100">
                  Buy Plan
                </a>
              {% endif %}
            {% else %}
              <a href="{% url 'account_login' %}" class="btn btn-outline-dark w-100">
                Login to Purchase
              </a>
            {% endif %}
          </div>

        </div>
      </div>
    {% endfor %} <!-- ✅ NOW VALID -->
  </div>

  <!-- ================= NUTRITION PLANS ================= -->
  <div class="row mt-4">
    {% for plan in nutrition_plans %} <!-- ✅ ADDED LOOP -->
      <div class="col-md-4 mb-4">
        <div class="card h-100">

          <img src="{{ plan.image.url }}" class="card-img-top" alt="{{ plan.title }}">

          <div class="card-body d-flex flex-column">
            <h5 class="card-title">{{ plan.title }}</h5>

            <p class="card-text">
              {{ plan.description }}
            </p>

            <p class="mt-auto"><strong>£{{ plan.price }}</strong></p>

            {% if user.is_authenticated %}
              {% if has_nutrition_plan %}
                <button class="btn btn-secondary w-100" disabled>
                  Already Own a Nutrition Plan
                </button>
              {% else %}
                <a href="{% url 'plans:buy_plan' plan.id %}" class="btn btn-black w-100">
                  Buy Plan
                </a>
              {% endif %}
            {% else %}
              <a href="{% url 'account_login' %}" class="btn btn-outline-dark w-100">
                Login to Purchase
              </a>
            {% endif %}
          </div>

        </div>
      </div>
    {% endfor %} <!-- ✅ NOW VALID -->
  </div>

</div>

{% endblock %}

21. Now when I refresh I can see my new plans page:

![Plans Initital View](/static/images/FitnessPlans/Screenshot%20initial%20view%20of%20plans%20page.png)

22. I am going to populate this with some basic fitness and nutrition plans manually from the admin panel. I change the url to http://127.0.0.1:8000/admin/login/?next=/admin/ and log in as the superuser. I can see in the admin panel here that I now have a section called 'PLANS':

![Plans in Admin Panel](/static/images/FitnessPlans/Screenshot%20plans%20now%20showing%20in%20admin%20panel.png)

23. If I click 'Add' on 'Plans' then I am taken to the page below, where I can create a new fitness or nutrition plan - this is decided through the type selector below. I can populate a title, description and then choose a file for the image of the plan here as well. I populate my first nutrition plan and then click 'Save and add another' and do this twice more for nutrition plans and then three times more for fitness plans:

![Adding first nutrition plan and saving](/static/images/FitnessPlans/keto%20nutrition%20plan.jpg)

24. Once I have manually added all of my fitness and nutrition plans, I go back to the 'Plans' in the Admin Panel and can now see all of these hae been created:

![Admin Plans all created](/static/images/FitnessPlans/Screenshot%20admin%20plans%20all%20created.png)

25. Now if i go back to the website and then go to the 'Fitness and Nutrition Plans' page I am presented with an error:

NameError at /plans/
name 'UserPlan' is not defined
Request Method:	GET
Request URL:	http://127.0.0.1:8000/plans/
Django Version:	6.0.2
Exception Type:	NameError
Exception Value:	
name 'UserPlan' is not defined
Exception Location:	C:\Users\leila\OneDrive\Desktop\Documents\vscode-projects\working_out_gym\plans\views.py, line 17, in plans_list
Raised during:	plans.views.plans_list
Python Executable:	C:\Users\leila\OneDrive\Desktop\Documents\vscode-projects\working_out_gym\.venv\Scripts\python.exe
Python Version:	3.12.8
Python Path:	
['C:\\Users\\leila\\OneDrive\\Desktop\\Documents\\vscode-projects\\working_out_gym',
 'C:\\Program Files\\Python312\\python312.zip',
 'C:\\Program Files\\Python312\\DLLs',
 'C:\\Program Files\\Python312\\Lib',
 'C:\\Program Files\\Python312',
 'C:\\Users\\leila\\OneDrive\\Desktop\\Documents\\vscode-projects\\working_out_gym\\.venv',
 'C:\\Users\\leila\\OneDrive\\Desktop\\Documents\\vscode-projects\\working_out_gym\\.venv\\Lib\\site-packages']
Server time:	Wed, 15 Apr 2026 14:11:44 +0000

26. I check my plans/views file and can see I am not importing the UserPlan model so update this now:

from .models import Plan, UserPlan

27. Now when I refresh my page, I can see the plans I have just created. However, the images could do with being set to always being the same size and the price should be centered. Also I would like for there to be a more obvious split between the two sets of plans - this can be achieved by putting a small heading at the top of each of the sets of cards with a small paragraph description:

![Plans showing on page but image sizing wrong](/static/images/FitnessPlans/Screenshot%20fitness%20and%20nutrition%20plans%20image%20sizing%20issue%20price%20not%20centered.png)

- I will look at this in a moment but for now I am going to test whether the 'Buy Plan' works but this does not, it throws up this error message:

NameError at /plans/buy/4/
name 'redirect' is not defined

Request Method:	GET
Request URL:	http://127.0.0.1:8000/plans/buy/4/
Django Version:	6.0.2
Exception Type:	NameError
Exception Value:	
name 'redirect' is not defined
Exception Location:	C:\Users\leila\OneDrive\Desktop\Documents\vscode-projects\working_out_gym\plans\views.py, line 44, in buy_plan
Raised during:	plans.views.buy_plan

- I realise I haven't imported redirect at the top of my plans/views file so do this now:

from django.shortcuts import render, get_object_or_404, redirect

- Now when I reload I can see that I have been taken to the 'Checkout' page where I can enter my details and then checkout the plan, however, I have noticed that the 'Order Total', 'Delivery' and 'Grand Totals' are not being worked out at all:

![Plan buy now goes to checkout](/static/images/FitnessPlans/Screenshot%20plan%20goes%20to%20checkout%20page.png)

- I go back to my plans page and fix the styling and appearance issues here first and then will move back to the checkout to resolve this next. I need to first create a static/css folder in my plans directory so do this now. Then within the new css folder, I create my 'plans' page specific css called plans.css:

.plan-card img {
    height: 220px;
    object-fit: cover;
    width: 100%;
}

- Then in the plans.html template I update with my extra css block containing the new css file:

{% block extra_css %}
<link rel="stylesheet" href="{% static 'plans/css/plans.css' %}">
{% endblock %}

- I now contain the page title and description in its own div
- I also add a h3 and paragraph element above both the fitness and nutrition plans card sets as below and contain these in their own div
- I have now contained the plan elements in their own divs
- I have updated the class on my price django tag to use text-center so it's centered

<div class="container mt-4">

  <!-- PAGE TITLE -->
  <div class="text-center mb-5">
    <h2 class="logo-font">Fitness & Nutrition Plans</h2>
    <p class="text-muted">
      Choose from our expert-designed fitness and nutrition plans.  
      You may purchase one of each type.  
      To change your plan, please contact admin.
    </p>
  </div>

  <!-- ================= FITNESS PLANS ================= -->
  <div class="mb-5">
    <h3 class="mb-2">Fitness Plans</h3>
    <p class="text-muted mb-4">
      Structured workout programmes designed to help you build strength,
      improve endurance, and reach your fitness goals.
    </p>

    <div class="row">
      {% for plan in fitness_plans %}
      <div class="col-12 col-md-6 col-lg-4 mb-4">
        <div class="card h-100 plan-card">

          <!-- IMAGE -->
          <img src="{{ plan.image.url }}" alt="{{ plan.title }}">

          <div class="card-body d-flex flex-column">
            <h5 class="card-title">{{ plan.title }}</h5>

            <p class="card-text">
              {{ plan.description }}
            </p>

            <!-- PRICE -->
            <p class="mt-auto text-center">
              <strong>£{{ plan.price }}</strong>
            </p>

            <!-- BUTTON LOGIC -->
            {% if user.is_authenticated %}
              {% if has_fitness_plan %}
                <button class="btn btn-secondary w-100" disabled>
                  Already Own a Fitness Plan
                </button>
              {% else %}
                <a href="{% url 'plans:buy_plan' plan.id %}" class="btn btn-black w-100">
                  Buy Plan
                </a>
              {% endif %}
            {% else %}
              <a href="{% url 'account_login' %}" class="btn btn-outline-dark w-100">
                Login to Purchase
              </a>
            {% endif %}
          </div>

        </div>
      </div>
      {% endfor %}
    </div>
  </div>

  <!-- ================= NUTRITION PLANS ================= -->
  <div class="mb-5">
    <h3 class="mb-2">Nutrition Plans</h3>
    <p class="text-muted mb-4">
      Tailored meal plans to support your fitness journey,
      improve health, and optimise performance.
    </p>

    <div class="row">
      {% for plan in nutrition_plans %}
      <div class="col-12 col-md-6 col-lg-4 mb-4">
        <div class="card h-100 plan-card">

          <!-- IMAGE -->
          <img src="{{ plan.image.url }}" alt="{{ plan.title }}">

          <div class="card-body d-flex flex-column">
            <h5 class="card-title">{{ plan.title }}</h5>

            <p class="card-text">
              {{ plan.description }}
            </p>

            <!-- PRICE -->
            <p class="mt-auto text-center">
              <strong>£{{ plan.price }}</strong>
            </p>

            <!-- BUTTON LOGIC -->
            {% if user.is_authenticated %}
              {% if has_nutrition_plan %}
                <button class="btn btn-secondary w-100" disabled>
                  Already Own a Nutrition Plan
                </button>
              {% else %}
                <a href="{% url 'plans:buy_plan' plan.id %}" class="btn btn-black w-100">
                  Buy Plan
                </a>
              {% endif %}
            {% else %}
              <a href="{% url 'account_login' %}" class="btn btn-outline-dark w-100">
                Login to Purchase
              </a>
            {% endif %}
          </div>

        </div>
      </div>
      {% endfor %}
    </div>
  </div>

</div>
{% endblock %}

28. I reload the page to see the changes to my template come into play but it has only added the h3 headings and centered my price but not updated my image sizing:

![Fitness and Nutrition Plans Page css not applying](/static/images/FitnessPlans/Screenshot%20css%20not%20applying.png)

29. When I inspect the images in devtools, I can see that I am getting an error against my plans.css in console:

Failed to load resource: the server responded with a status of 404 (Not Found)

30. I try cancelling my server, reloading and then hard reloading and emptying the cache on the browser but this makes no difference. I then try deleting all static files using:

Remove-Item -Recurse -Force staticfiles 

31. I collect my static files again using:

python manage.py collectstatic

32. I refresh but the css is still not being found in the console and the images haven't updated. I take a closer look at my folder structure for my static files in my plans directory and realise that I haven't created a subfolder for 'plans' in static and then placed 'css' in the plans subfolder. I update this now as shown below:

![Plans static folder structure update](/static/images/FitnessPlans/Screenshot%20plans%20static%20folder%20structure%20update.png)

33. Now when I refresh it can find the css file as its now in the correct folder structure: 

![Plans css now applying](/static/images/FitnessPlans/Screenshot%20fitness%20and%20nutrition%20css%20now%20applying.png)

34. The last thing I want to do before I move onto the checkout view and resolving the totals not updating correctly, is just to centralise all my headings on my plans.html and any p elements as well. To do this, I will just add the text-center class to each of my divs in the plan.html page containing headers and paragraph elements. I also add this to the h5 elements classes too, so I can centralise my headings on the plan cards. I refresh the page once the changes are made and this looks much better:

![Centralised headings on plans page](/static/images/FitnessPlans/Screenshot%20centralising%20text%20on%20fitness%20nutrition%20plans%20template#.png)

35. Next I want to resolve the issue with the totals on the checkout page for my plans. I click 'Buy Plan' on any of the plans and inspect the total with devtools on the next page. I try to troubleshoot but not sure what could be going wrong. I query this with ChatGPT who advises that my checkout is currently only calculating totals from:

bag = request.session.get('bag', {})

- However, I am not storing my plan in the bag session, I am storing it here:

request.session['plan_purchase_id']

- ChatGPT advises that I nheed to update my checkout view with a new block of code which includes the plan_id session and overrides the totals when it is a plan purchase:

plan_id = request.session.get('plan_purchase_id', None)

plan = None
if plan_id:
    from plans.models import Plan
    plan = Plan.objects.get(id=plan_id)

    # Override totals for plan purchase
    total = plan.price

stripe_total = round(total * 100)

- Then in my checkout.html template, I need to wrap my totals like below to include the logic for my plan pricing, replacing the current code I was using for my totals in the template:

<div class="row text-black text-right">

    {% if plan %}
        <!-- PLAN TOTALS -->
        <div class="col-7 offset-2">
            <p class="my-0">Order Total:</p>
            <p class="my-0">Delivery:</p>
            <p class="my-0">Grand Total:</p>
        </div>
        <div class="col-3">
            <p class="my-0">£{{ plan.price }}</p>
            <p class="my-0">£0.00</p>
            <p class="my-0"><strong>£{{ plan.price }}</strong></p>
        </div>

    {% else %}
        <!-- EXISTING BAG TOTALS -->
        <div class="col-7 offset-2">
            <p class="my-0">Order Total:</p>
            <p class="my-0">Delivery:</p>
            <p class="my-0">Grand Total:</p>
        </div>
        <div class="col-3">
            <p class="my-0">£{{ total | floatformat:2 }}</p>
            <p class="my-0">£{{ delivery | floatformat:2 }}</p>
            <p class="my-0"><strong>£{{ grand_total | floatformat:2 }}</strong></p>
        </div>
    {% endif %}

</div>

- Then still in my checkout.html, at the bottom of the file, I replace the following as it will still show £0 for my plans total:

<strong>${{ grand_total|floatformat:2 }}</strong>

With: 

{% if plan %}
    <span>Your card will be charged <strong>£{{ plan.price }}</strong></span>
{% else %}
    <span>Your card will be charged <strong>£{{ grand_total|floatformat:2 }}</strong></span>
{% endif %}

- I also need to update my buy_plan views so that users' bags are cleared after they have purchased a plan so that they cannot add items and a plan to the bag and have issues:

request.session['bag'] = {}

36. I reload my page and then try to 'Buy Plan' on any of the plans but I am presented with an error page:

UnboundLocalError at /checkout/
cannot access local variable 'stripe_total' where it is not associated with a value
Request Method:	GET
Request URL:	http://127.0.0.1:8000/checkout/
Django Version:	6.0.2
Exception Type:	UnboundLocalError
Exception Value:	
cannot access local variable 'stripe_total' where it is not associated with a value
Exception Location:	C:\Users\leila\OneDrive\Desktop\Documents\vscode-projects\working_out_gym\checkout\views.py, line 141, in checkout
Raised during:	checkout.views.checkout
Python Executable:	C:\Users\leila\OneDrive\Desktop\Documents\vscode-projects\working_out_gym\.venv\Scripts\python.exe
Python Version:	3.12.8
Python Path:	
['C:\\Users\\leila\\OneDrive\\Desktop\\Documents\\vscode-projects\\working_out_gym',
 'C:\\Program Files\\Python312\\python312.zip',
 'C:\\Program Files\\Python312\\DLLs',
 'C:\\Program Files\\Python312\\Lib',
 'C:\\Program Files\\Python312',
 'C:\\Users\\leila\\OneDrive\\Desktop\\Documents\\vscode-projects\\working_out_gym\\.venv',
 'C:\\Users\\leila\\OneDrive\\Desktop\\Documents\\vscode-projects\\working_out_gym\\.venv\\Lib\\site-packages']
Server time:	Wed, 15 Apr 2026 19:42:16 +0000

- I query this with ChatGPT who advises that my checkout view is trying to get the total before Stripe has been set to obtain it so I need to update my code so it sets Stripe_total for both cases of checkout, i.e. plans and items. I replace the below code from:

plan = None

if plan_id:
    from plans.models import Plan
    plan = Plan.objects.get(id=plan_id)
    total = plan.price
else:
    current_bag = bag_contents(request)
    total = current_bag['grand_total']

    #ChatGPT Code
    plan_id = request.session.get('plan_purchase_id', None)

    plan = None
    if plan_id:
        from plans.models import Plan
        plan = Plan.objects.get(id=plan_id)

        # Override totals for plan purchase
        total = plan.price

    # Stripe expects pence
    stripe_total = round(total * 100)

- With:

plan = None

if plan_id:
    from plans.models import Plan
    plan = Plan.objects.get(id=plan_id)
    total = plan.price
else:
    current_bag = bag_contents(request)
    total = current_bag['grand_total']

stripe_total = round(total * 100)

37. I refresh the page and can see the checkout again with the totals being calculated correctly now too. However, it has moved the order summary details and totals above the delivery and payment form when it should be showing in the second column on the right:

![Plans Checkout Page Wrong Layout](/static/images/FitnessPlans/Screenshot%20plans%20checkout%20showing%20correct%20totals%20wrong%20layout.png)

38. This is caused by the order-lg-last class on my order summary column div. Removing this class still doesn't resolve the issue but this is because the order summary code actually appears before the payment and delivery details form in my checkout.html, I re-order this so that the Order Summary now appears after my 'adjust bag' and 'complete order' buttons. Now when I refresh the Plans Checkout page looks good:

![Plans Checkout Page Layout Resolved](/static/images/FitnessPlans/Screenshot%20plans%20checkout%20view%20now%20resolved.png)

39. I can now complete order on the plan and I am taken to the checkout_success page and receive a receipt with an order number and my details but unfortunately the totals are showing as £0 here for everything:

![Plans Successful Checkout Wrong Totals](/static/images/FitnessPlans/Screenshot%20plans%20successful%20checkout.png)

40. I query why this would be with ChatGPT and it advises that my Order is still being saved with no monetary values for plan purchases; the totals are calculated in the checkout view then shown in the template but not stored on the Order model. To resolve this, in checkout/views on my if statement for order_form.is_valid, I need to replace this code:

if order_form.is_valid():
    order = order_form.save(commit=False)
    pid = request.POST.get('client_secret').split('_secret')[0]
    order.stripe_pid = pid
    order.original_bag = json.dumps(bag)

    order.save()

- With:

if order_form.is_valid():
    order = order_form.save(commit=False)

    pid = request.POST.get('client_secret').split('_secret')[0]
    order.stripe_pid = pid
    order.original_bag = json.dumps(bag)

    plan_id = request.session.get('plan_purchase_id')

    if plan_id:
        from plans.models import Plan
        plan = Plan.objects.get(id=plan_id)

        order.order_total = plan.price
        order.delivery_cost = 0
        order.grand_total = plan.price
    else:
        current_bag = bag_contents(request)
        order.order_total = current_bag['total']
        order.delivery_cost = current_bag['delivery']
        order.grand_total = current_bag['grand_total']

    order.save()

41. After updating my view, I cancel and reload my server and purchase another plan to see if this has now resolved my issue. I notice that my restrictions against user owning more than 1 x type of plan have come into play and is working:

![Disable Button preventing 2 x same plan type](/static/images/FitnessPlans/Screenshot%20disable%20button%20working%20for%20fitness%20plan%20being%20owned.png)

42. Now when I complete an order, I can see that it is calculating the correct totals now:

![Correct totals on checkout success for plans](/static/images/FitnessPlans/Screenshot%20plans%20checkout%20showing%20correct%20totals%20wrong%20layout.png)

43. As my Fitness and Nutrition Plan app is now setup and working correctly, I will now run a collectstatic and then commit my changes to Git and Heroku. 

---

## Heroku Checkout Broken

1. When I am testing my production app, I realise it is breaking at the checkout page and giving me a server 500 error. I query with ChatGPT who advises it's likely I haven't set my Stripe Public and Secret Keys in my Heroku config. I do this now by entering the following cmds into my terminal, replacing with my key info:

heroku config:set STRIPE_PUBLIC_KEY=your_public_key_here
heroku config:set STRIPE_SECRET_KEY=your_secret_key_here

2. I then restart the dynos on Heroku:

heroku restart

3. Now when I reload my production server, I can go to checkout and then checkout the order succesfully.

4. I realise that when I go to try and increase the quantity through the quantity selector buttons on items to Add to Bag that this is no longer working. I believe this is likely due to the fact that the product_detail.html still uses jQuery which my project no longer uses as I have switched to Bootstrap 5. ChatGPT recommends updating my base.html with the below code inside my script tags at the bottom of the file in my postload js block. By adding it to base.html it should also then work on items in shoppingbag too:

  // Increment quantity
  $('.increment-qty').click(function(e) {
    e.preventDefault();
    let itemId = $(this).data('item_id');
    let input = $('#id_qty_' + itemId);
    let currentVal = parseInt(input.val());
    let max = parseInt(input.attr('max'));

    if (currentVal < max) {
      input.val(currentVal + 1);
    }
  });

  // Decrement quantity
  $('.decrement-qty').click(function(e) {
    e.preventDefault();
    let itemId = $(this).data('item_id');
    let input = $('#id_qty_' + itemId);
    let currentVal = parseInt(input.val());
    let min = parseInt(input.attr('min'));

    if (currentVal > min) {
      input.val(currentVal - 1);
    }
  });

5. This works and I can update the quantity on my items on the product_detail view and add them to the shoppingbag, however, in the shoppingbag if I increase or decrease the quantity selector button is happening twice now. This means that there is two pieces of code doing the same thing on this page now so it might make more sense to add my script above to the product_detail.html template only. I remove the above code from base.html and then paste it into the postload js block at the bottom of my product_detail.html template. Now when I refresh the shoppingbag, I can increase and decrease by 1 again. I go back to a product_detail view and see if quantity selector is fixed here also, which it is. 

6. I commit my changes here and then look at my next issue which is the checkout appears to be broken after adding the separate flow for fitness and nutrition plans. 

7. I test checking out an order from the merchandise app but have no issues today whereas last night in testing found it was declining the Stripe test card (42 42). I have successfully checkout Merchandise and Plans through checkout this morning and all seems to be well. 

8. There are a couple more niggly issues that I would like to resolve before moving on. One of these is the fact that my Toast notifications still show $ instead of £ so I am going to have a quick look at these and update wherever I can see a $. I save and then test adding an item to the bag and can see this looks much better in the notification now:

![Toast Notification Currency Update](/static/images/Tidy-up/Screenshot%20toast%20currency%20update.png)

9. However, while the Toast currency now reflects the correct currency, the shopping bag total when updated still gives a $ sign. When it is empty it uses a £ sign, so I inspect the shoppingbag total to see where it is pulling the $ from. I can see this is coming from this span element in the main-nav.html template:

<span class="ms-2">${{ grand_total|floatformat:2 }}</span>

- I update the $ to a £ sign and then restart my dev server and reload my page and can see the total on shopping bag now shows as the correct currency:

![Shoppingbag Total Correct Currency in Navbar](/static/images/Tidy-up/Screenshot%20correct%20currency%20shoppingbag%20total%20navbar.png)

10. The last issue I have spotted is that the images are no longer showing for my plans page on either Heroku or my local server. This is likely due to the fact that I haven't set up Cloudinary in my project yet so I will commit my changes again and then look at setting that up now.

---

## Cloudinary Storage Setup

1. First I login to my account on Cloduinary at: https://cloudinary.com/ and go to my Dashboard to get my Cloud Name, API Key and API Secret.

2. Next, I install the package for Cloudinary into my project using the following cmd in my terminal:

pip install cloudinary django-cloudinary-storage

3. I then add it to the requirements.txt file using:

pip freeze > requirements.txt

4. Then I update my INSTALLED APPS section in settings to include the new Cloudinary apps:

    'cloudinary',
    'cloudinary_storage',

5. In my env.py I set environment variables for my CLOUDINARY_CLOUD_NAME, API_KEY and API_SECRET. Then in my settings.py I add the below to obtain the variables and contain in my storage settings:

CLOUDINARY_STORAGE = {
    'CLOUD_NAME': os.environ.get('CLOUDINARY_CLOUD_NAME'),
    'API_KEY': os.environ.get('CLOUDINARY_API_KEY'),
    'API_SECRET': os.environ.get('CLOUDINARY_API_SECRET'),
}

DEFAULT_FILE_STORAGE = 'cloudinary_storage.storage.MediaCloudinaryStorage'

6. I now need to update my plans/models so that the image field looks at the CloudinaryField attribute. I go to my plans/models and find the image field which is currently set to:

    image = models.ImageField(upload_to='plans/')

- And then I update this to:

image = CloudinaryField('image')

- And as I am using the CloudinaryField, I also need to import this at the top of the file now too:

from cloudinary.models import CloudinaryField

- After making changes to the model, I then need to makemigrations and migrate:

python manage.py makemigrations
python manage.py migrate

7. After these have ran successfully, I then need to reupload the images in the admin panel so do this now.

8. I check my plans page and can now see the images again:

![Images showing on Plans page again](/static/images/Tidy-up/Screenshot%20images%20showing%20for%20plans%20again.png)

9. Then finally I set my environment variables on Heroku as below:

heroku config:set CLOUDINARY_CLOUD_NAME=your-cloud-name
heroku config:set CLOUDINARY_API_KEY=your-api-key
heroku config:set CLOUDINARY_API_SECRET=your-api-secret

10. Once I have set the environment variables on Heroku, I run collectstatic and then commit my pages to Git and Heroku.

11. Once it has finished deploying to Heroku, I check that the Plans Images are now showing there too which they are. I check around the rest of the site seeing if I have missed anything and notice that the OrderTotal heading in Profile doesn't have a space between the words and that it's using dollar as the currency so I inspect on devtools, find the offending td element in profile.html and then update accordingly:

<td>£{{ order.grand_total }}</td>

12. This looks good now so I will commit my changes again and then move on to my Product Admin next.

---

## Product Admin - ProductForm / add_product View

1. Now that the frontend of my application is now setup and functional for the users. I now want to give the superusers the functionality to be able to add, update and delete products in the store. The infrastructure is mostly already built for this but just needs a few additional tweaks. The first thing I will need is a product form so I create a new forms.py file in the merchandise app. In the file itself, I then import what we need to make the forms work, i.e. the forms from Django and the Category and Product models from the merchandise app:

from django import forms
from .models import Product, Category

2. Then, I will create a new class ProductForm that extends the built-in forms.ModelForm:

class ProductForm(forms.ModelForm)

3. It will have an inner metaclass which defines the model and the fields I want to include. I am going to include all of the fields using a double underscore string called all:

    class Meta:
        model = Product
        fields = '__all__'

4. Next I will override the init method in order to be able to make some changes to the fields:

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

- Still in the method, I then set the below so that categories show up in the new form under their friendly names. I first get all the categories and then create a list of the tuples of the friendly names associated with their category ID's; this syntax is called list comprehension, a shorthand way of creating a loop that adds items to the list:

        categories = Category.objects.all()
        friendly_names = [(c.id, c.get_friendly_name()) for c in categories]

- Now that my method is getting the friendly names, I then update the category field to use these for choices instead of using the id. This will be seen in the select box that will generate in the form; instead of seeing the category ID or the name field, it will show the friendly name for categories:

        self.fields['category'].choices = friendly_names

- Then I will ierate through all the field names and then set classes on them to match the theme of the rest of the store:

        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'border-black rounded-0'

5. Now that I have my ProductForm set-up, I will commit my code to Git and Heroku and then next write my view and connect this to a template to then see the form.

6. After my code has successfully committed, I then look at creating a new view for the Product Form so that the superusers of the site can add new products to the store. In my merchandise/views file I create a new view and call this 'add_product'. It is going to be simple for now and just render an empty instance of the new productform so I can see how this looks initially. It will use a new template which I will create soon called 'add_product.html'. It will also include a context which includes the ProductForm

def add_product(request):
    """Add new product to Merchandise"""
    form = ProductForm()
    template = 'merchandise/add_product.html'
    context = {
        'form': form,
    }

    return render(request, template, context)

- Then at the top of the views file, I need to import the ProductForm at the top:

from .forms import ProductForm

7. Now I need to create a new url for my new view in merchandise urls. I call the new url 'add/' and point this to the add_product view:

    path("add/", views.add_product, name="add_product"),

8. Now I need to actually create the template I have been referencing for add_product. I will create the new file in the merchandise/templates/merchandise directory:

![add product template](/static/images/ProductAdmin/Screenshot%20add%20product%20template%20directory.png)

9. As it's going to have a similar appearance to my checkout page, I will copy and paste the contents of my checkout.html into this file so I can use it as a base for the new view. I make the following tweaks:

- I remove the entire postload js block at the bottom of my file.
- I remove the entire loading-overlay div containing the loading spinner.
- I remove all the content from the second row
- I update the header to say 'Product Management' instead of 'Checkout'
- I update the div classes that the header resides in to col-12 and col-md-6 so it takes up 50% width on medium and larger screens
- I then remove the extra css block and bag tools at the top of the file

10. I run my dev server and add '/products/add' to the end of my url so I can see how my Product Management is looking. However, this gives me the error page as below:

AttributeError at /merchandise/add/
'Category' object has no attribute 'get_friendly_name'
Request Method:	GET
Request URL:	http://127.0.0.1:8000/merchandise/add/
Django Version:	6.0.2
Exception Type:	AttributeError
Exception Value:	
'Category' object has no attribute 'get_friendly_name'
Exception Location:	C:\Users\leila\OneDrive\Desktop\Documents\vscode-projects\working_out_gym\merchandise\forms.py, line 13, in __init__
Raised during:	merchandise.views.add_product
Python Executable:	C:\Users\leila\OneDrive\Desktop\Documents\vscode-projects\working_out_gym\.venv\Scripts\python.exe
Python Version:	3.12.8
Python Path:	
['C:\\Users\\leila\\OneDrive\\Desktop\\Documents\\vscode-projects\\working_out_gym',
 'C:\\Program Files\\Python312\\python312.zip',
 'C:\\Program Files\\Python312\\DLLs',
 'C:\\Program Files\\Python312\\Lib',
 'C:\\Program Files\\Python312',
 'C:\\Users\\leila\\OneDrive\\Desktop\\Documents\\vscode-projects\\working_out_gym\\.venv',
 'C:\\Users\\leila\\OneDrive\\Desktop\\Documents\\vscode-projects\\working_out_gym\\.venv\\Lib\\site-packages']
Server time:	Thu, 16 Apr 2026 20:46:45 +0000

11. I take a look at my Category model in Merchandise and realise there is no friendly_name field set against this, if I were to add this to my Category model now then I would have to go through all my items in the admin panel and manually add a friendly name and there is a lot of products so I will stop using friendly_names and use name instead, in my merchandise/forms file replacing:

friendly_names = [(c.id, c.get_friendly_name()) for c in categories]

- With:

friendly_names = [(c.id, c.name) for c in categories]

12. I update this and then reload the dev server and add '/merchandise/add/' and now the page is loading for me:

![Add Product View Now Loading](/static/images/ProductAdmin/Screenshot%20add%20product%20view%20now%20loading.png)

13. I now want to render the product form as a Django Crispy form in the second row of my conten in the new template. I make another 50% width column to contain a form element which has a method of POST, action URL of add_product, a class to add a margin bottom and it also has an encoding type attribute on the form; this is as has the potential to submit images files and without this it cannot upload the images correctly. The CSRF token and django crispy form tag will be contained inside the form element and there is a cancel button to go back to the Merchandise page:

            <div class="col-12 col-md-6">
                <form method="POST" action="{% url 'merchandise:add_product' %}" class="form mb-2" enctype="multipart/form-data">
                    {% csrf_token %}
                    {{ form | crispy }}
                    <div class="text-right">
                        <a class="btn btn-outline-black rounded-0" href="{% url 'merchandise:products' %}">Cancel</a>
                        <button class="btn btn-black rounded-0" type="submit">Add Product</button>
                    </div>
                </form>

14. Now when I reload the page looks much more substantial:

![Add Product View Basically Complete](/static/images/ProductAdmin/Screenshot%20add%20buy%20view%20more%20polished.png)

15. I commit my changes here and then move on to looking at the post handler for my add products view.

---

## Product Admin - add_product Post Handler

1. I now write the Post Handler for the add_product view. In merchandise/views, I update the add_product view an if statement which says if the request method is POST then it will instantiate a new instance of the product form from request.POST and include request.FILES. In order to ensure that the image is captured for the product if one was submittedt then we can check if form.is_valid, and if so we'll save it. Then I add a success message and then redirect to the same view. If any errors appear on the form then I will attach a generic message telling user to check the form which will display any errors. Then I move the empty form into an else block so it doesn't wipe out the errors

    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully added product!')
            return redirect(reverse('add_product'))
        else:
            messages.error(request, 'Failed to add product. Please ensure the form is valid.')
    else:
        form = ProductForm()

2. I also put the empty form statement on my UserProfileForm in an else statement so this doesn't cause me issues later:

    else:
        form = UserProfileForm(instance=profile)

- And just above it, I add an error message so it matches the rest of my site in having notifications for everything:

        else:
            messages.error(request, 'Update failed. Please ensure the form is valid.')

3. Now I want to make sure that my add_product form is working. I will first test and see if it produces an error when invalid data is used such as too long of a price number. However, when I look at my view I realise that there is no field for price. When I look at the ProductForm, I realise I am importing the Product model on the ProductForm class which I know doesn't contain the price attribute so I change this to ProductVariant, in both the class and the import at the top:

from .models import ProductVariant, Category

class ProductForm(forms.ModelForm):
    
    class Meta:
        model = ProductVariant

4. I update this and refresh the server but I am presented with a server 500 error so I switch debug on and refresh to see what is happening:

KeyError at /merchandise/add/
'category'
Request Method:	GET
Request URL:	http://127.0.0.1:8000/merchandise/add/
Django Version:	6.0.2
Exception Type:	KeyError
Exception Value:	
'category'
Exception Location:	C:\Users\leila\OneDrive\Desktop\Documents\vscode-projects\working_out_gym\merchandise\forms.py, line 15, in __init__
Raised during:	merchandise.views.add_product
Python Executable:	C:\Users\leila\OneDrive\Desktop\Documents\vscode-projects\working_out_gym\.venv\Scripts\python.exe
Python Version:	3.12.8
Python Path:	
['C:\\Users\\leila\\OneDrive\\Desktop\\Documents\\vscode-projects\\working_out_gym',
 'C:\\Program Files\\Python312\\python312.zip',
 'C:\\Program Files\\Python312\\DLLs',
 'C:\\Program Files\\Python312\\Lib',
 'C:\\Program Files\\Python312',
 'C:\\Users\\leila\\OneDrive\\Desktop\\Documents\\vscode-projects\\working_out_gym\\.venv',
 'C:\\Users\\leila\\OneDrive\\Desktop\\Documents\\vscode-projects\\working_out_gym\\.venv\\Lib\\site-packages']
Server time:	Fri, 17 Apr 2026 00:54:48 +0000

5. I'm not sure why I have gotten this error after updating the code like I have so I query it with ChatGPT who advises that the error is saying there is no category field in my ProductVariant model so it crashes. The product holds the title, category info etc. and ProductVariant holds my size, price, etc. I need to revert my form back to using the Product instead of ProductVariant in my ProductForm. So I do this now and the page is reloading again now.

- ChatGPT advises I will need 2 x forms to handle everything, one for ProductForm that I already have in place and then a second for ProductVariantForm as below:

class ProductVariantForm(forms.ModelForm):
    class Meta:
        model = ProductVariant
        fields = ['price', 'size']

- Then in my merchandise/views, I need to import the new form at the top of the file:

from .forms import ProductForm, ProductVariantForm

- Then in my add_product view, I update this from:

def add_product(request):
    """Add new product to Merchandise"""
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully added product!')
            return redirect(reverse('add_product'))
        else:
            messages.error(request, 'Failed to add product. Please ensure the form is valid.')
    else:
        form = ProductForm()


    template = 'merchandise/add_product.html'
    context = {
        'form': form,
    }

    return render(request, template, context)

- To the below, so it also includes code for ProductVariantForm:

def add_product(request):
    if request.method == 'POST':
        product_form = ProductForm(request.POST, request.FILES)
        variant_form = ProductVariantForm(request.POST)

        if product_form.is_valid() and variant_form.is_valid():
            product = product_form.save()

            variant = variant_form.save(commit=False)
            variant.product = product
            variant.save()

            messages.success(request, 'Successfully added product!')
            return redirect(reverse('merchandise:add_product'))
        else:
            messages.error(request, 'Failed to add product.')
    else:
        product_form = ProductForm()
        variant_form = ProductVariantForm()

    context = {
        'product_form': product_form,
        'variant_form': variant_form,
    }

    return render(request, 'merchandise/add_product.html', context)

- Then finally, I update the Django form crispy tag in my add_product template to the below so it see's the two forms instead of just the one:

{{ product_form | crispy }}
{{ variant_form | crispy }}

6. After making these changes, I refresh my local server and can see a selector for 'Has Sizes' now but this is only a 'yes' or 'no' option which will be no good for product admin. It also still isn't showing me the price field. I query this with ChatGPT. It thinks that I've mixed ProductForm and ProductVariantForm and Django is now confused because my form is still tied to Product but I am trying to handle it as if it handles sizes and prices so my forms.py likely introduced an error hence the crash during system checks, which we can see from the traceback stopping here:

'self.func(instance)'

- ChatGPT recommends simplifying the ProductForm to:

class ProductForm(forms.ModelForm):
    price = forms.DecimalField(label='Price', max_digits=6, decimal_places=2)
    size = forms.CharField(label='Size', required=False)

    class Meta:
        model = Product
        fields = '__all__'

- Next I need to update my add_product view to:

from .models import ProductVariant

def add_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            product = form.save()

            # Create variant
            ProductVariant.objects.create(
                product=product,
                price=form.cleaned_data['price'],
                size=form.cleaned_data.get('size')
            )

            messages.success(request, 'Successfully added product!')
            return redirect('merchandise:add_product')
        else:
            messages.error(request, 'Failed to add product. Please ensure the form is valid.')
    else:
        form = ProductForm()

    return render(request, 'merchandise/add_product.html', {'form': form})

- However, when I reload the server, I am seeing the following error in the terminal:

(.venv) PS C:\Users\leila\OneDrive\Desktop\Documents\vscode-projects\working_out_gym> python manage.py runserver
Watching for file changes with StatReloader
Performing system checks...

Exception in thread django-main-thread:
Traceback (most recent call last):
  File "C:\Program Files\Python312\Lib\threading.py", line 1075, in _bootstrap_inner
    self.run()
  File "C:\Program Files\Python312\Lib\threading.py", line 1012, in run
    self._target(*self._args, **self._kwargs)
  File "C:\Users\leila\OneDrive\Desktop\Documents\vscode-projects\working_out_gym\.venv\Lib\site-packages\django\utils\autoreload.py", line 64, in wrapper
    fn(*args, **kwargs)
  File "C:\Users\leila\OneDrive\Desktop\Documents\vscode-projects\working_out_gym\.venv\Lib\site-packages\django\core\management\commands\runserver.py", line 134, in inner_run
    self.check(**check_kwargs)
  File "C:\Users\leila\OneDrive\Desktop\Documents\vscode-projects\working_out_gym\.venv\Lib\site-packages\django\core\management\base.py", line 496, in check
    all_issues = checks.run_checks(
                 ^^^^^^^^^^^^^^^^^^
  File "C:\Users\leila\OneDrive\Desktop\Documents\vscode-projects\working_out_gym\.venv\Lib\site-packages\django\core\checks\registry.py", line 89, in run_checks
    new_errors = check(app_configs=app_configs, databases=databases)
                 ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\leila\OneDrive\Desktop\Documents\vscode-projects\working_out_gym\.venv\Lib\site-packages\django\core\checks\urls.py", line 136, in check_custom_error_handlers
    handler = resolver.resolve_error_handler(status_code)
              ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\leila\OneDrive\Desktop\Documents\vscode-projects\working_out_gym\.venv\Lib\site-packages\django\urls\resolvers.py", line 743, in resolve_error_handler
    callback = getattr(self.urlconf_module, "handler%s" % view_type, None)
                       ^^^^^^^^^^^^^^^^^^^
  File "C:\Users\leila\OneDrive\Desktop\Documents\vscode-projects\working_out_gym\.venv\Lib\site-packages\django\utils\functional.py", line 47, in __get__
    res = instance.__dict__[self.name] = self.func(instance)
                                         ^^^^^^^^^^^^^^^^^^^
  File "C:\Users\leila\OneDrive\Desktop\Documents\vscode-projects\working_out_gym\.venv\Lib\site-packages\django\urls\resolvers.py", line 722, in urlconf_module
    return import_module(self.urlconf_name)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Program Files\Python312\Lib\importlib\__init__.py", line 90, in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "<frozen importlib._bootstrap>", line 1387, in _gcd_import
  File "<frozen importlib._bootstrap>", line 1360, in _find_and_load
  File "<frozen importlib._bootstrap>", line 1331, in _find_and_load_unlocked
  File "<frozen importlib._bootstrap>", line 935, in _load_unlocked
  File "<frozen importlib._bootstrap_external>", line 999, in exec_module
  File "<frozen importlib._bootstrap>", line 488, in _call_with_frames_removed
  File "C:\Users\leila\OneDrive\Desktop\Documents\vscode-projects\working_out_gym\working_out_gym\urls.py", line 27, in <module>
    path("merchandise/", include("merchandise.urls")),
                         ^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\leila\OneDrive\Desktop\Documents\vscode-projects\working_out_gym\.venv\Lib\site-packages\django\urls\conf.py", line 39, in include
    urlconf_module = import_module(urlconf_module)
                     ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Program Files\Python312\Lib\importlib\__init__.py", line 90, in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "<frozen importlib._bootstrap>", line 1387, in _gcd_import
  File "<frozen importlib._bootstrap>", line 1360, in _find_and_load
  File "<frozen importlib._bootstrap>", line 1331, in _find_and_load_unlocked
  File "<frozen importlib._bootstrap>", line 935, in _load_unlocked
  File "<frozen importlib._bootstrap_external>", line 999, in exec_module
  File "<frozen importlib._bootstrap>", line 488, in _call_with_frames_removed
  File "C:\Users\leila\OneDrive\Desktop\Documents\vscode-projects\working_out_gym\merchandise\urls.py", line 2, in <module>
    from . import views
  File "C:\Users\leila\OneDrive\Desktop\Documents\vscode-projects\working_out_gym\merchandise\views.py", line 5, in <module>
    from .forms import ProductForm, ProductVariantForm
  File "C:\Users\leila\OneDrive\Desktop\Documents\vscode-projects\working_out_gym\merchandise\forms.py", line 14, in <module>
    class ProductVariantForm(forms.ModelForm):
  File "C:\Users\leila\OneDrive\Desktop\Documents\vscode-projects\working_out_gym\.venv\Lib\site-packages\django\forms\models.py", line 336, in __new__
    raise FieldError(message)
django.core.exceptions.FieldError: Unknown field(s) (size) specified for ProductVariant

- I query this with ChatGPT who advises that after the changes made there is no size field and that is why Django is crashing:

class ProductVariant(models.Model):
    product = models.ForeignKey(Product, related_name='variants', on_delete=models.CASCADE)
    price = models.DecimalField(...)
    # maybe NO size field here

- It recommends updating my ProductVariant model with a size field as below:

size = models.CharField(max_length=10, blank=True, null=True)

- I add this to my merchandise/models ProductVariant model and then I run makemigrations and migrate:

python manage.py makemigrations
python manage.py migrate

- I then add the size field back into my ProductForm class in forms:

size = forms.CharField(required=False)

- And then update my add_product view in merchandise/views so it uses has_sizes properly in the view:

def add_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            product = form.save()

            size = form.cleaned_data.get('size')

            # Only use size if product has sizes
            if not product.has_sizes:
                size = None

            ProductVariant.objects.create(
                product=product,
                price=form.cleaned_data['price'],
                size=size,
            )

            messages.success(request, 'Successfully added product!')
            return redirect('merchandise:add_product')
    else:
        form = ProductForm()

    return render(request, 'merchandise/add_product.html', {'form': form})

- I also update my add_product template so that it uses just the form crispy tag instead of the t2 x forms crispy tags for ProductForm and ProductVariantForm. I also load the crispy forms tags at the top of the template file:

{% load crispy_forms_tags %}

<form method="POST" action="{% url 'merchandise:add_product' %}" class="form mb-2" enctype="multipart/form-data">
    {% csrf_token %}
    {{ form | crispy }}
    <div class="text-right">
        <a class="btn btn-outline-black rounded-0" href="{% url 'merchandise:products' %}">Cancel</a>
        <button class="btn btn-black rounded-0" type="submit">Add Product</button>
    </div>
</form>

- Now with these changes in place, the size is a free-form field and price is there too:

![Add Product View now showing Size and Price fields](/static/images/ProductAdmin/Screenshot%20add%20product%20view%20now%20showing%20size%20and%20price%20fields%20correctly.png)

7. Now that I can see those fields, I am going to test adding a product with too many digits for the price field and see if it causes the error notification to generate:

![Testing price field](/static/images/ProductAdmin/Screenshot%20too%20many%20digits.png)

- This works so now I will add a valid product and then try to search for it to ensure it appears. However, after I click 'add product' I am being taken to an error page:

DataError at /merchandise/add/
value too long for type character varying(10)
Request Method:	POST
Request URL:	http://127.0.0.1:8000/merchandise/add/
Django Version:	6.0.2
Exception Type:	DataError
Exception Value:	
value too long for type character varying(10)
Exception Location:	C:\Users\leila\OneDrive\Desktop\Documents\vscode-projects\working_out_gym\.venv\Lib\site-packages\django\db\backends\utils.py, line 105, in _execute
Raised during:	merchandise.views.add_product
Python Executable:	C:\Users\leila\OneDrive\Desktop\Documents\vscode-projects\working_out_gym\.venv\Scripts\python.exe
Python Version:	3.12.8
Python Path:	
['C:\\Users\\leila\\OneDrive\\Desktop\\Documents\\vscode-projects\\working_out_gym',
 'C:\\Program Files\\Python312\\python312.zip',
 'C:\\Program Files\\Python312\\DLLs',
 'C:\\Program Files\\Python312\\Lib',
 'C:\\Program Files\\Python312',
 'C:\\Users\\leila\\OneDrive\\Desktop\\Documents\\vscode-projects\\working_out_gym\\.venv',
 'C:\\Users\\leila\\OneDrive\\Desktop\\Documents\\vscode-projects\\working_out_gym\\.venv\\Lib\\site-packages']
Server time:	Fri, 17 Apr 2026 09:31:29 +0000

- ChatGPT advises it's likely due to a characterfield length issue of Size on my ProductVariantModel and that I should increase the max character allowed to resolve this so I do this now to:

size = models.CharField(max_length=50, blank=True, null=True)

- Then I run makemigrations and migrate and reload my page:

python manage.py makemigrations
python manage.py migrate

- Now when I reload the page, I can see the price and size fields for the form but it says there is already a product with the handle of 'wagyu' which I know isn't true. I check for it it admin/merchandise/product to be sure but now I am getting an error saying my django-countries module doesn't exist. 

- I make sure that my virtual environment is activated using the following cmd in my terminal:

.\.venv\Scripts\activate

- I then install the 'missing' package:

pip install django-countries

- I can then run my server again so I try to find 'wagyu' in admin. Sure enough, I do see it in admin so I select it and then choose to delete it here from the 'Action' dropdown:

![Wagu showing in admin/merchandise/products list](/static/images/ProductAdmin/Screenshot%20wagu%20showing%20in%20admin%20merchandise%20products.png)

![Deleting product from admin](/static/images/ProductAdmin/Screenshot%20deleting%20wagu.png)

- I also update my Product model's save method with the self.handle slugify method so that it will generate the handle for me using slugify, I import the slugify module at the top of the file:

from django.utils.text import slugify

def save(self, *args, **kwargs):
    # Generate handle if missing
    if not self.handle:
        base = slugify(self.title)[:240] or "product"
        handle = base
        i = 1
        while Product.objects.filter(handle=handle).exclude(pk=self.pk).exists():
            i += 1
            handle = f"{base[:235]}-{i}"
        self.handle = handle

    # Generate slug if missing
    if not self.slug:
        self.slug = self.handle

    super().save(*args, **kwargs)

8. I now reload my dev server and see if I can add the product now which I can:

![Adding products successfully](/static/images/ProductAdmin/Screenshot%20successfully%20added%20product.png)

9. I can see that showing as active now when I go to admin/merchandise/products:

![New product showing in admin panel](/static/images/ProductAdmin/Screenshot%20new%20product%20showing%20as%20active%20in%20admin%20panel.png)

10. Now if I search for the new product on the actual website itself and then try to add it to my bag then it adds successfully but I can see the image being used in the Toast Success notification is wrong:

![No image on items shows wrong in toast success notifications](/static/images/ProductAdmin/Screenshot%20new%20product%20showing%20as%20active%20in%20admin%20panel.png)

11. I take a look at the image element in my toast_success.html code and can see I have an if statement which should render my 'noimage.jpg' but it isn't working:

{% if item.product.variants.first.image_src %}
          <img
            class="w-100"
            src="{{ item.product.variants.first.image_src }}"
            alt="{{ item.product.title }}"
          />
          {% elif item.product.image_src %}
          <img
            class="w-100"
            src="{{ item.product.image_src }}"
            alt="{{ item.product.title }}"
          />
          {% else %}
          <img
            class="w-100"
            src="{% static 'images/noimage.jpg' %}"
            alt="{{ item.product.title }}"
          />
          {% endif %}

- I query this with ChatGPT who advises that my condition is passing when it shouldn't and advises that this line is at fault. The .first is not safe to use in Django templates as if there are multiple variants or cached querysets then it can behave inconsistently and even return an object when the img_src is empty or null. It recommends updating this code to:

<img class="w-100" src="{{ item.product.get_display_image }}" alt="{{ item.product.title }}">

- And then moving the logic into my Product model instead by adding the below method inside the model:

def get_display_image(self):
    variant = self.variants.first()
    if variant and variant.image_src:
        return variant.image_src
    if self.image_src:
        return self.image_src
    return '/static/images/noimage.jpg'

- Now when I reload and add the cap to the bag, it shows no image in the toast_success notification:

![No Image Update Toast Success Working](/static/images/ProductAdmin/Screenshot%20no%20image%20on%20toast%20success%20notfications.png)

12. Next I take a look at the items in my shoppingbag to ensure that the no image and product information is displaying as it shouldbe but this is also not showing the 'noimage.jpg':

![ShoppingBag No Image View Okay](/static/images/ProductAdmin/Screenshot%20shoppingbag%20no%20image%20added%20product%20okay.png)

13. I query with ChatGPT who advises me to add the logic into my shoppingbag.html:

{% if item.product.image_src %}
  <img class="img-fluid rounded" src="{{ item.product.image_src }}" alt="{{ item.product.title }}">
{% else %}
  <img class="img-fluid rounded" src="{% static 'images/noimage.jpg' %}" alt="No image available">
{% endif %}

14. And to also add the logic back into my toast_success.html template:

<div class="col-3 my-1">
  {% if item.product.image_src %}
    <img class="img-fluid rounded" src="{{ item.product.image_src }}" alt="{{ item.product.title }}">
  {% else %}
    <img class="img-fluid rounded" src="{% static 'images/noimage.jpg' %}" alt="No image available">
  {% endif %}
</div>

15. I test adding this again now and can see it shows the correct 'noimage.jpg' in my toast_success notification shopping preview:

![Toast Success Notification showing noimage correctly](/static/images/ProductAdmin/Screenshot%20noimage%20working.png)

16. Also if I look at the shoppingbag view now, it shows the correct image for the none imaged item:

![Shoppingbag view no image](/static/images/ProductAdmin/Screenshot%20shoppingbag%20noimage%20working.png)

17. Then in my main-nav.html template, I update the 'Product Management' ahref with the django url to the new app_product page as below:

<a href="{% url 'merchandise:add_product' %}" class="dropdown-item">Product Management</a>

18. If I test the link from the navbar this takes me to the Product Management page.

19. I now want to test that adding a product with an image works too so I do this now, however, I realise I cannot do this as the image field on my 'Add Product' is a free form text field rather than an uploadable field. I need to update my Product model image field to:

image = models.ImageField(upload_to='products/', blank=True, null=True)

- I make this change and then run makemigrations and migrate:

python3 manage.py makemigrations
python3 manage.py migrate

- I then update all of my templates which use product.image to use the below if statement around images:

{% if product.image %}
  <img src="{{ product.image.url }}">
{% elif product.image_url %}
  <img src="{{ product.image_url }}">
{% else %}
  <img src="{% static 'images/noimage.jpg' %}">
{% endif %}

- After applying these changes and refreshing my server, I can see that there is now an image upload box. However, if I go to my Merchandise page all the images are missing and in my console it says it cannot find the images:

![Merchandise Listings all images gone](/static/images/ProductAdmin/Screenshot%20product%20model%20update%20has%20removed%20all%20images%20from%20merchandise.png)

- I query this with ChatGPT who advises that I am getting the error because of this line in the updated code:

{% if product.image.url %}

- If a product has no image uploaded to it then Django throws up this error:

ValueError: The 'image' attribute has no file associated with it.

- I need to check my images, where product is concerned, using the below statement, so that it checks the image field itself and not the image URL:

{% if product.image %}
  <img
    class="card-img-top img-fluid"
    src="{{ product.image.url }}"
    alt="{{ product.title }}"
  />
{% else %}
  <img
    class="card-img-top img-fluid"
    src="{% static 'images/noimage.png' %}"
    alt="{{ product.title }}"
  />
{% endif %}

- I update products.html, product_detail.html, shoppingbag.html and checkout.html with this code instead of what I currently have on each for their images.

- ChatGPT also spots that I nested the get_display_image method inside the save method inside of the Product model so I move this out. 

- However, the errors in the console are the same on Merchandise when I rerun the server and I still cannot see the images. I query this with ChatGPT again who advises that I haven't updated this method in the Product model to use the correct image code:

def get_display_image(self):
    variant = self.variants.first()
    if variant and variant.image_src:
        return variant.image_src
    if self.image_src:   # ❌ THIS FIELD DOES NOT EXIST
        return self.image_src
    return '/static/images/noimage.jpg'

- I update this to:

def get_display_image(self):
    variant = self.variants.first()
    if variant and variant.image_src:
        return variant.image_src
    if self.image:
        return self.image.url
    return '/static/images/noimage.jpg'

- I have also used the wrong code in my shoppingbag and checkout templates, I have used  {% if product.image %} but inside their loops, there is no product variable so I am looping {% for item in bag_items %} and the correct object is item.product. I replace the following code in shoppingbag.html from:

{% if product.image %}
  <img src="{{ product.image.url }}">
{% else %}

- To: 

{% if item.product.image %}
  <img src="{{ item.product.image.url }}">
{% else %}
  <img src="{% static 'images/noimage.png' %}">
{% endif %}

- Then in checkout.html, I update the following code from:

{% if product.image %}

- To: 

{% if item.product.image %}

- This still hasn't resolved the issue with my images no longer displaying on the Merchandise page. To troubleshoot further, I login to the admin panel and go to Products and see whether the image field is empty.

- ChatGPT recommends having both an image and img_src field on the Product model as below:

image = models.ImageField(upload_to='products/', blank=True, null=True)
image_src = models.URLField(blank=True, null=True)

- I then run makemigrations and migrate as I have made changes to the model.

- Then to fix my helper method to the below so it works with both image fields:

def get_display_image(self):
    variant = self.variants.first()
    if variant and variant.image_src:
        return variant.image_src
    if self.image:
        return self.image.url
    if self.image_src:
        return self.image_src
    return '/static/images/noimage.jpg'

- Then finally, I need to go back through all my templates, the ones I updated earlier that use product, and delete the image logic and replace with, in product list:

<img src="{{ product.get_display_image }}">

- Still no difference. I ask ChatGPT again and it says this is what my model should be....

from django.templatetags.static import static

def get_display_image(self):
    variant = self.variants.first()

    if variant and variant.image_src:
        return variant.image_src

    if self.image:
        return self.image.url

    if self.image_src:
        return self.image_src

    return static('images/noimage.jpg')

- Next it advises me to update my products.html image logic from:

<img src="{{ product.get_display_image }}" alt="{{ product.title }}">

- To:

<img 
  src="{{ product.get_display_image }}" 
  class="card-img-top img-fluid"
  alt="{{ product.title }}"
>

- Then in my product_detail.html, I need to update from:

<img src="{{ product.get_display_image }}" alt="{{ product.title }}">

- Next I update my shoppingbag.html from:

<img src="{{ item.product.get_display_image }}" alt="{{ product.title }}">

- To: 

<img 
  src="{{ item.product.get_display_image }}" 
  class="img-fluid"
  alt="{{ item.product.title }}"
>

- Then finally in the checkout.html, I update from:

<img src="{{ item.product.get_display_image }}" alt="{{ product.title }}">>

- To:

<img 
  src="{{ item.product.get_display_image }}" 
  class="img-fluid"
  alt="{{ item.product.title }}"
>

- Then it recommends that I go to my merchandise/views and find the following line in my products view:

products = (
    Product.objects.filter(is_active=True)
    .select_related("category")
    .annotate(from_price=Min("variants__price"))
)

- And update it with:

.prefetch_related("variants")

- Then still in my views file, I need to go down to my product_details view and update my product variable with the new prefetch related code:

product = get_object_or_404(
    Product.objects.prefetch_related("variants").annotate(from_price=Min("variants__price")),
    pk=product_id
)

- However, the Merchandise page still will not load. After doing some troubleshooting and limiting the amount of items it could return it is now letting Merchandise load with the 20 items. I updated my all_products view in merchandise using this temporarily:

products = Product.objects.all()[:20]

- ChatGPT recommends that I replace my products queryset in my all_products view with the below code, removing the .annotate attribute as it can be dangerous with large datasets:

products = (
    Product.objects.filter(is_active=True)
    .select_related("category")
    .prefetch_related("variants")
)

- It also recommends fixing my price from the below code in products.html:

{{ product.from_price }}

- To:

{% with variant=product.variants.first %}
  {% if variant %}
    £{{ variant.price }}
  {% else %}
    <small class="text-muted">Price unavailable</small>
  {% endif %}
{% endwith %}

- Then in product_detail.html, I update:

{% if product.variants.all %}

- To:

{% if product.variants.exists %}

- However, the page will not load again. I decide to add pagination into my Merchandise app so import the Paginator at the top of my merchandise/views file:

from django.core.paginator import Paginator

- Then just before my context in all_products view I add the logic for pagination as below:

paginator = Paginator(products, 100) 

page_number = request.GET.get('page')
page_obj = paginator.get_page(page_number)

- Then I update my context changing the products key to:

"products": page_obj,

- And also add the following key to the contexts:

"page_obj": page_obj,

- Then I need to add the pagination controls so add the below code under my product grid: 

    <div class="row mt-4">
      <div class="col text-center">

        {% if page_obj.has_previous %}
          <a href="?{% if request.GET.q %}q={{ request.GET.q }}&{% endif %}
          {% if request.GET.category %}category={{ request.GET.category }}&{% endif %}
          {% if request.GET.sort %}sort={{ request.GET.sort }}&direction={{ request.GET.direction }}&{% endif %}
          page={{ page_obj.previous_page_number }}">
        {% endif %}

        <span class="mx-3">
          Page {{ page_obj.number }} of {{ page_obj.paginator.num_pages }}
        </span>

        {% if page_obj.has_next %}
          <a href="?{% if request.GET.q %}q={{ request.GET.q }}&{% endif %}
          {% if request.GET.category %}category={{ request.GET.category }}&{% endif %}
          {% if request.GET.sort %}sort={{ request.GET.sort }}&direction={{ request.GET.direction }}&{% endif %}
          page={{ page_obj.previous_page_number }}">
        {% endif %}

      </div>
    </div>

- I reload but the page is still hanging and I can see this Paginator warning in my terminal:

UnorderedObjectListWarning: Pagination may yield inconsistent results with an unordered object_list: <class 'merchandise.models.Product'> QuerySet. paginator = Paginator(products, 100)

- So I need to add ordering before pagination, I update:

products = Product.objects.all()

- To:

products = Product.objects.all().order_by('title')

- Now when I refresh the server and go to Merchandise I can see a list of 100 items showing their correct images again: 

![Merchandise Page Loading and Showing Images again](/static/images/ProductAdmin/Screenshot%20merchandise%20images%20now%20showing%20again.png)

- However, if I scroll to the bottom of the page the page numbers are missing and the footer is not fitting the whole width of the screen as it should be. I query this with ChatGPT who advises that the code for my pagination controls in products.html template is wrong as it was missing the ahref elements and advises me to update it to:

<div class="row mt-4">
  <div class="col text-center">

    {% if products.has_previous %}
      <a class="btn btn-outline-black rounded-0 mx-1"
         href="?page={{ products.previous_page_number }}">
        Previous
      </a>
    {% endif %}

    <span class="mx-3">
      Page {{ products.number }} of {{ products.paginator.num_pages }}
    </span>

    {% if products.has_next %}
      <a class="btn btn-black rounded-0 mx-1"
         href="?page={{ products.next_page_number }}">
        Next
      </a>
    {% endif %}

  </div>
</div>

20. Now when I reload I can see the page numbers and can click through these to see the next set of clothes. The only other issue now is that the footer is too small for the width of the screen so I need to resolve this:

![Merchandise Page Showing Pagination Footer Sizing Wrong](/static/images/ProductAdmin/Screenshot%20buttons%20now%20showing%20but%20fotter%20sizing%20wrong.png)

- There is a missing enddiv at the end of my endfor statement for my products. I update this and also tidy up the template so there is now descriptions for the differenct sections of code.

- Now when I reload my footer looks correct on my Merchandise page:

![Merchandise Footer Sizing Resolved](/static/images/ProductAdmin/Screenshot%20merchandise%20footer%20now%20correct.png)

21. I now go back to my testing of the add_product view and see if I can still upload an image to the image field. I find that I can now add a product with an image successfully. If I search for that product then it comes back in the search results as seen below:

![Added new product with image](/static/images/ProductAdmin/Screenshot%20freedom%20cap%20search.png)

22. However, if I click the hat to open the product detail view for it and add it to my bag it throws up this error:

TypeError at /merchandise/7430/
'bool' object is not iterable
Request Method:	GET
Request URL:	http://127.0.0.1:8000/merchandise/7430/
Django Version:	6.0.2
Exception Type:	TypeError
Exception Value:	
'bool' object is not iterable
Exception Location:	C:\Users\leila\OneDrive\Desktop\Documents\vscode-projects\working_out_gym\.venv\Lib\site-packages\django\template\defaulttags.py, line 201, in render
Raised during:	merchandise.views.product_detail
Python Executable:	C:\Users\leila\OneDrive\Desktop\Documents\vscode-projects\working_out_gym\.venv\Scripts\python.exe
Python Version:	3.12.10
Python Path:	
['C:\\Users\\leila\\OneDrive\\Desktop\\Documents\\vscode-projects\\working_out_gym',
 'C:\\Program Files\\Python312\\python312.zip',
 'C:\\Program Files\\Python312\\DLLs',
 'C:\\Program Files\\Python312\\Lib',
 'C:\\Program Files\\Python312',
 'C:\\Users\\leila\\OneDrive\\Desktop\\Documents\\vscode-projects\\working_out_gym\\.venv',
 'C:\\Users\\leila\\OneDrive\\Desktop\\Documents\\vscode-projects\\working_out_gym\\.venv\\Lib\\site-packages']
Server time:	Sat, 18 Apr 2026 13:29:50 +0000
Error during template rendering
In template C:\Users\leila\OneDrive\Desktop\Documents\vscode-projects\working_out_gym\merchandise\templates\merchandise\product_detail.html, error at line 53

'bool' object is not iterable
43	          {% if product.variants.exists %}
44	          <div class="me-2 mb-2" style="min-width: 150px">
45	            <label for="id_variant" class="form-label"
46	              ><strong>Size:</strong></label
47	            >
48	            <select
49	              class="form-control form-control-sm rounded-0"
50	              name="variant_id"
51	              id="id_variant"
52	            >
53	              {% for variant in product.variants.exists %}

- I query this with ChatGPT who advises that {% for variant in product.variants.exists %} should be {% for variant in product.variants.all %} instead so I update this now in product_detail.html. Now when I refresh I can see the view for my new product detail and add to my bag:

[!Freedom Cap Product Detail Toast Success Wrong Image ](/static/images/ProductAdmin/Screenshot%20merchandise%20footer%20now%20correct.png)

23. However, the wrong image is being generated in toast_success message, it shows the noimage.jpg that I generate when the image cannot be found. I query this with ChatGPT who advises that I update this block in my toast_success.html template:

{% if item.product.image_src %}
  <img class="img-fluid rounded" src="{{ item.product.image_src }}" alt="{{ item.product.title }}">
{% else %}
  <img class="img-fluid rounded" src="{% static 'images/noimage.jpg' %}" alt="No image available">
{% endif %}

- To this, so it matches the rest of my site's image logic:

<img 
  class="img-fluid rounded" 
  src="{{ item.product.get_display_image }}" 
  alt="{{ item.product.title }}"
>

24. Now that I have tested that I can add a product successfully with an image, I will run collectstatic and then commit my code to Git and Heroku.

---

## Product Admin - Edit Product Functionality

1. The first thing that I do to set up functionality so that the superusers can edit these products is duplicate the add_product.html template and then rename it to edit_product.html. In the content of the file, I update the header from 'Add a Product' to 'Edit a Product'. I update the button text to say 'update product'. Finally I update the form to send to a new url I am going to create called edit_product which includes product ID:

{% block content %}
    <div class="overlay"></div>
    <div class="container">
        <div class="row">
            <div class="col-12 col-md-6">
                <hr>
                <h2 class="logo-font mb-4">Product Management</h2>
                <h5 class="text-muted">Edit a Product</h5>
                <hr>
            </div>
        </div>

       <div class="row">
            <div class="col-12 col-md-6">
                <form method="POST" action="{% url 'merchandise:edit_product' product.id %}" class="form mb-2" enctype="multipart/form-data">
                    {% csrf_token %}
                    {{ form | crispy }}
                    <div class="text-right">
                        <a class="btn btn-outline-black rounded-0" href="{% url 'merchandise:products' %}">Cancel</a>
                        <button class="btn btn-black rounded-0" type="submit">Update Product</button>
                    </div>
                </form>      
            </div>
        </div>
    </div>

2. Now I need a new view to render the template so in my merchandise/views file I create a new view called edit_product which takes the request and product id that the user is going to edit. The form is pre-filled by getting the product using the get_object_or_404 method and then instantiating a product form using the product. Next I will write the Post Handler, which will be an if request.method = POST method with a form.is_valid statement which checks if the form is submitting any data and if they are, then it will iterate through and check if the form they are submitting is valid and respond accordingly. There is an else statement if no post request detected to return message advising user they are editing the product and its name. Finally, I tell it which template to use and then add a context with the relevant keys for the method's code and return render this all back:


def edit_product(request, product_id):
    """ Edit a product in the Merchandise app """
    product = get_object_or_404(Product, pk=product_id)
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully updated product!')
            return redirect(reverse('product_detail', args=[product.id]))
        else:
            messages.error(request, 'Failed to update product. Please ensure the form is valid.')
    else:
        form = ProductForm(instance=product)
        messages.info(request, f'You are editing {product.title}')

    template = 'merchandise/edit_product.html'
    context = {
        'form': form,
        'product': product,
    }

    return render(request, template, context)

3. Next, I go to my merchandise/urls file and create the url for the edit_products view:

    path('edit/<int:product_id>/', views.edit_product, name='edit_product'),

4. I test this on my server by going to my dev server and then /merchandise/edit/1 I am taken to the edit page for a product as shown below and given an alert that I am editing the product:

[!Edit Product First Look](/static/images/ProductAdmin/Screenshot%20edit%20product%20first%20view.png)

5. I am now going to update the price with too many digits to make sure that my code works whereby it picks up if the form data is invalid. This works as it fails to update the product with a warning below the field saying there are too many digits and also shows a Toast warning saying the data is invalid:

[!Edit Product Price Too Many Digits Toast Warning](/static/images/ProductAdmin/Screenshot%20price%20too%20many%20digits%20edit%20product%20warning.png)

[!Price Field Too Many Digits Warning](/static/images/ProductAdmin/Screenshot%20edit%20product%20price%20field%20too%20many%20digits%20warning.png)

6. I now try to submit the form after setting a valid price but the page takes me to a server 500 error so I turn debug on to see what is happening. The error I am receiving is below:

NoReverseMatch at /merchandise/edit/1/
Reverse for 'product_detail' not found. 'product_detail' is not a valid view function or pattern name.
Request Method:	POST
Request URL:	http://127.0.0.1:8000/merchandise/edit/1/
Django Version:	6.0.2
Exception Type:	NoReverseMatch
Exception Value:	
Reverse for 'product_detail' not found. 'product_detail' is not a valid view function or pattern name.
Exception Location:	C:\Users\leila\OneDrive\Desktop\Documents\vscode-projects\working_out_gym\.venv\Lib\site-packages\django\urls\resolvers.py, line 842, in _reverse_with_prefix
Raised during:	merchandise.views.edit_product
Python Executable:	C:\Users\leila\OneDrive\Desktop\Documents\vscode-projects\working_out_gym\.venv\Scripts\python.exe
Python Version:	3.12.10
Python Path:	
['C:\\Users\\leila\\OneDrive\\Desktop\\Documents\\vscode-projects\\working_out_gym',
 'C:\\Program Files\\Python312\\python312.zip',
 'C:\\Program Files\\Python312\\DLLs',
 'C:\\Program Files\\Python312\\Lib',
 'C:\\Program Files\\Python312',
 'C:\\Users\\leila\\OneDrive\\Desktop\\Documents\\vscode-projects\\working_out_gym\\.venv',
 'C:\\Users\\leila\\OneDrive\\Desktop\\Documents\\vscode-projects\\working_out_gym\\.venv\\Lib\\site-packages']
Server time:	Sat, 18 Apr 2026 20:32:39 +0000 

- I know that I need to update the code I have set for edit_product views as product_detail is probably not the same naming convention used for my views. I update the following:

return redirect(reverse('product_detail', args=[product.id]))

- To:

return redirect(reverse('merchandise:product_detail', args=[product.id]))

- After updating and refreshing the page after resubmitting the form, it has now loaded the product detail view:

[!Product Detail View Now Loading After Saving on Edit_Product](/static/images/ProductAdmin/Screenshot%20resolves%20to%20product%20detail%20view%20after%20saving%20edit%20product.png)

7. I notice however, that the price hasn't updated from what I set it to on edit_product and also the price is empty when viewing it on the edit_product view whereas it should be populated if there is a product set. I query this with ChatGPT who advises that my form in edit_product is using:

form = ProductForm(instance=product)

- However, my price is held here:

class ProductVariant(models.Model):
    price = models.DecimalField(...)

- It recommends updating the edit_product view and add the below block of code into my else block:

variant = product.variants.first()
initial_data = {}

if variant:
    initial_data['price'] = variant.price

form = ProductForm(instance=product, initial=initial_data)

- Still in the view, I also update my form.save() method to:

if form.is_valid():
    product = form.save()

    variant = product.variants.first()
    if variant:
        variant.price = form.cleaned_data['price']
        variant.save()

    messages.success(request, 'Successfully updated product!')
    return redirect(reverse('merchandise:product_detail', args=[product.id]))

8. Now when I refresh the page with the updated code, I can see that it shows the price:

[!Edit_product view now reflecting price](/static/images/ProductAdmin/Screenshot%20edit_product%20price%20now%20reflected.png) 

9. If I edit the price to a valid price and save then the new price is not being reflected in the product_detail page. I query this with ChatGPT who advises the issue is likely the merchandise/forms logic being too loose as price is required by default which can break edits silently, price is not a part of the ProductModel but the ProductVariant model does and the fieldsm = __all__ includes items that don't want editing. It recommends updating my ProductForm as below:

from django import forms
from .models import Product, ProductVariant


class ProductForm(forms.ModelForm):
    price = forms.DecimalField(
        label='Price',
        max_digits=10,
        decimal_places=2,
        required=False  # 🔴 important
    )
    size = forms.CharField(required=False)

    class Meta:
        model = Product
        fields = [
            'title',
            'category',
            'vendor',
            'has_sizes',
            'tags',
            'image',
            'image_src',
            'is_active',
        ]

10. I reload my page and test to see if I can edit the price in my edit_product view and save it with the updated changes in place. I notice that when I go into the merchandise/edit/1 view for the product that the price I set it at has remained, so it's saving in the edit view but then that change isn't being reflected in the product_detail template. I query this with ChatGPT who advises that the issue is with the data flow. My setup now is: 

- Price is stored on ProductVariant
- My edit view only saves Product
- Your product)detail reads the price from variants

So when I 'update price' I am not updating the actual thing which displays the price on the product in the product_detail view. In prodcut_detail, I show price using the below code; this comes from the ProductVariant.price:

min_price = product.variants.order_by('price').first().price

Then in edit_product I do 'form.save()' but this only saves Product fiels and NOT the variant. The result of this is that the form updates, the Variant price stays the same and the page still shows the old price. To fix this, I need to replace my POST section in my edit_product with:

if request.method == 'POST':
    form = ProductForm(request.POST, request.FILES, instance=product)

    if form.is_valid():
        product = form.save()

        variant = product.variants.first()
        if variant:
            variant.price = form.cleaned_data['price']
            variant.save()

        messages.success(request, 'Successfully updated product!')
        return redirect(reverse('merchandise:product_detail', args=[product.id]))
    else:
        messages.error(request, 'Failed to update product. Please ensure the form is valid.')

11. I reload the page and then save the price again to see if it is now reflecting this in the product_detail view but it still isn't. I query with ChatGPT who provides me with some options based on the fact there are multiple variants of the price for each item so my current code is only saving one version and the other variant is the one being presented back in the template still. I have decided that I will force update all variants when I make changes so there is only one variant per product. To do this, I need to update my merchandise/views edit_product view and add the below code under my product = form.save():

for variant in product.variants.all():
    variant.price = form.cleaned_data['price']
    variant.save()

12. After I save the file, I restart the server and then edit a product price to see if I can then see it reflected in the final template. This is great, I can now see the price update reflected on the final template:

[!Edit_product view now reflecting price update](/static/images/ProductAdmin/Screenshot%20successfully%20updated%20product%20price.png)

13. I change the price back to it's original price and then commit my changes before moving on to setting up my delete_view.

---

## Product Admin - Delete Product Functionality

1. For the final stage of my Product Admin, I will give user's the ability to delete products. I don't need a template for this, just the view and url. To start with, I create the delete url, copying the content of my edit url and tweaking for delete:

path('delete/<int:product_id>/', views.delete_product, name='delete_product'),

2. Then I go to my merchandise/views and add a new view for  delete_product, using edit_product view's code as a baseline and tweaking accordingly:

def delete_product(request, product_id):
    """Delete a product from the Merchandise app"""
    
    product = get_object_or_404(Product, pk=product_id)

    if request.method == 'POST':
        product.delete()
        messages.success(request, 'Product deleted successfully!')
        return redirect(reverse('merchandise:products'))

    messages.error(request, 'Invalid request')
    return redirect(reverse('merchandise:product_detail', args=[product.id]))

3. I update my add_product view so that I no longer have ton search for the newly added products after it's been added. I update my return redirect to:

return redirect('merchandise:product_detail', product_id=product.id)

4. I am now going to test by adding a new product and then calling the new delete view I have just created. I go to: http://127.0.0.1:8000/merchandise/add/ and then add a new product with a price and description:

[!Testing add_product](/static/images/ProductAdmin/Screenshot%20testing%20add%20product.png)

5. Once I hit save, I am redirected to the new products product_detail page. However, there is no image being displayed and I added an image to this. There is, however, a new ID created for it in the url:

[!Newly added product not showing image](/static/images/ProductAdmin/Screenshot%20add%20product%20successfully%20redirects%20to%20the%20product%20detail%20page.png)

6. I inspect devtools and can see that I have this error in the console regarding the image:

Failed to load resource: 404 (Not Found)

- ChatGPT recommends updating my project level urls file so it has an if statement with the static media settings:

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

- I update this and restart the server but the image is still not displaying. I query with ChatGPT who advises that I shouldn't be uploading the images on my site from the static directory and I should be uploading the image direct from my computer so that Django then saves it to /media/products in the project. I go to add a new product and upload the image from my PC instead this time to see if this changes things. But the new product is much the same as the last product I added as the image is still not being displayed. I check in my project after uploading the image to ensure that it has been uploaded to the /media/products directory as per my code which it has. I then test the following url for the file: http://127.0.0.1:8000/media/products/pexels-muhamad-guruh-budi-hartono-430167744-30202432.jpg which gives me a 404 not found error message.

- I troubleshoot this with ChatGPT again who advises that I change Debug to True and then try to upload my image when creating a new product, so I do this and now when the product is added I can see the image that I uploaded to it. ChatGPT advises that this happens because Django see's the app as being in production when Debug is set to False:

[!Newly added product showing image with debug on](/static/images/ProductAdmin/Screenshot%20image%20showing%20with%20added%20product.png)

7. I now want to check the delete functionality, I copy the product ID from the URL and enter /merchandise/delete/7433 to go to the delete view for the product but the page remains on the product's detail page and gives a toast notification that this is an invalid request. I query this with ChatGPT who advises that the delete should be triggered by a POST event and not a url visit and that better practise for a Production app would be to add a delete button via form so recommends that I update my delete_products views and my product_detail.html template to show this. I want the delete functionality to also show on my full product page listings from Merchandise app too but only when the user logged in is detected as a superuser. 

8. ChatGPT recommends updating my delete_product view to:

def delete_product(request, product_id):
    """Delete a product from the Merchandise app"""

    if not request.user.is_superuser:
        messages.error(request, "Sorry, only admins can do that.")
        return redirect(reverse('home'))

    product = get_object_or_404(Product, pk=product_id)

    if request.method == 'POST':
        product.delete()
        messages.success(request, 'Product deleted successfully!')
        return redirect(reverse('merchandise:products'))

    messages.error(request, 'Invalid request')
    return redirect(reverse('merchandise:product_detail', args=[product.id]))
    

- I then need to add the buttons to my product_detail.html template so I do this with the following code, using the Django if tag statement to restrict this to superusers only. I will add this under the code for my 'Add to Bag' button so it displays there:

{% if request.user.is_superuser %}
<hr>

<div class="d-flex gap-2">

  <a href="{% url 'merchandise:edit_product' product.id %}"
     class="btn btn-outline-black rounded-0">
    Edit
  </a>

  <form action="{% url 'merchandise:delete_product' product.id %}" method="POST">
    {% csrf_token %}
    <button type="submit"
            class="btn btn-danger rounded-0"
            onclick="return confirm('Are you sure you want to delete this product?');">
      Delete
    </button>
  </form>

</div>
{% endif %}

- Then in my products.html template, I add the below code inside the product cards before the closing div of .card-footer:

{% if request.user.is_superuser %}
<div class="mt-2 d-flex justify-content-between">

  <a href="{% url 'merchandise:edit_product' product.id %}"
     class="btn btn-sm btn-outline-black">
    Edit
  </a>

  <form action="{% url 'merchandise:delete_product' product.id %}"
        method="POST"
        style="display:inline;">
    {% csrf_token %}
    <button type="submit"
            class="btn btn-sm btn-danger"
            onclick="return confirm('Delete this product?');">
      Delete
    </button>
  </form>

</div>
{% endif %}

9. Now when I reload the Merchandise prducts listings page, I can see that the cards have 'edit' and 'delete' buttons on the product cards when I am logged in as a superuser:

[!Products listing cards showing edit and delete buttons](/static/images/ProductAdmin/Screenshot%20products%20template%20cards%20edit%20delete%20buttons.png)

- If I click the edit button from here, then it takes me to the edit_product view for the product:

[!Products listing card edit button works](/static/images/ProductAdmin/Screenshot%20products%20template%20edit%20button%20works.png)

- The case is the same with the delete button:

[!Products listing card delete button prompt](/static/images/ProductAdmin/Screenshot%20delete%20product%20button%20works%20from%20the%20full%20products%20page.png)

[!Products listing card delete toast notification](/static/images/ProductAdmin/Screenshot%20delete%20product%20successful%20toast%20notification%20product%20removed.png)

10. Also the products_details page shows the edit and delete buttons now and these work correctly:

[!Products details edit and delete buttons](/static/images/ProductAdmin/Screenshot%20product%20details%20edit%20and%20delete%20buttons.png)

[!Products details edit buttons](/static/images/ProductAdmin/Screenshot%20product%20details%20edit%20button.png)

[!Products details delete buttons](/static/images/ProductAdmin/Screenshot%20product%20delete%20from%20product%20details.png)

11. If I then logon as a normal user, I cannot see the edit or delete buttons on either the full products.html or product_details.html templates:

[!Standard users cannot see edit delete buttons on full products template](/static/images/ProductAdmin/Screenshot%20standard%20user%20unable%20to%20see%20edit%20and%20delete%20buttons%20on%20products%20template.png)

[!Standard users cannot see edit delete buttons on product details template](/static/images/ProductAdmin/Screenshot%20standard%20users%20unable%20to%20see%20edit%20delete%20buttons%20on%20product%20details.png)

12. Now that I have tested my delete_product functionality fully, I will commit my changes before moving on. 

---

## Product Admin - Securing my Views

1. Even though the 'edit and 'delete' buttons are hidden from anyone who is not a superuser, it is still possible for someone, if they knew the correct urls, to fabricate a POST request to add or update products on the page or to issue a get request to the delete view and then be able to delete products from the site. So I now need to tweak my views that I have just created so that this cannot happen. To start with, I am going to import the below decoarator for login_required which makes Django first check if a user is logged in before executing my view, and if they are not then they will be redirected to the login page:

from django.contrib.auth.decorators import login_required

- Then, still in my merchandise/views file, I will enforce the new import function against all my new product_admin views by adding the below line of code above each view for aa_product, edit_product and delete_product:

@login_required

2. I am also going to add this to the profile view as this view should only be available to logged in users as well. I import the below to my profiles/views file and add the decorator above my profile view:

from django.contrib.auth.decorators import login_required

@login_required

3. I want to test that the code I have used in my merchandise/views to restrict and notify standard users from accessing the productadmin view urls as a standard or non logged in user works. I first login as a standard user and attempt to access the url: http://127.0.0.1:8000/merchandise/edit/23/ and this allows me to access. The same is true of add_product url and delete_product url. I query this with ChatGPT who advises that I need to create a reusable check as @login_required only checks if the user is logged in but does not prevent normal users accessing admin views via URL so they will be able to access items through:

/merchandise/add/
/merchandise/edit/23/
/merchandise/delete/23/

- I update my merchandise/views with the below import for 'user_passes_test' and new helper called 'is_superuser':

from django.contrib.auth.decorators import login_required, user_passes_test

def is_superuser(user):
    return user.is_superuser

- I then need to apply this to all admin views, a.k.a. my add_product and edit_product view:

@user_passes_test(is_superuser)

- i remove this code from delete_product view as well:

if not request.user.is_superuser:

4. I reload the server and hard reload the page and empty the cache and then test as a non-logged in user and standard logged in user to access the following pages with the new code applied. This correctly redirects to the signin page for the non-logged in user on each of the add, edit and delete pages:

[!Merchandise add item non logged in user](/static/images/ProductAdmin/Screenshot%20non%20logged%20in%20user%20merchandise%20add.png)

[!Merchandise edit item non logged in user](/static/images/ProductAdmin/Screenshot%20merchandise%20edit%20item%20non%20logged%20in%20user.png)

[!Merchandise delete item non logged in user](/static/images/ProductAdmin/Screenshot%20merchandise%20delete%20item%20non%20logged%20in%20usere.png)

- However, when I try to access the add item url as a standard logged in user I get an error page and the terminal seems to be stuck in a loop:

[!Merchandise add item std logged in user](/static/images/ProductAdmin/Screenshot%20standard%20logged%20in%20user%20add%20item%20error.png)

5. I query this with ChatGPT who advises that I need to update my code so that Django tells it to block the users if they fail login as superuser and to update my views file with the below import so it no longer redirects silently but returns a 403 forbidden error:

from django.core.exceptions import PermissionDenied

- I also need to update my is_superuser helper to:

def is_superuser(user):
    if not user.is_superuser:
        raise PermissionDenied
    return True

- Now when I reload my page and try to go to any of the add, edit or delete views as a standard user that I am correctly blocked with a 403 forbidden error now:

[!Merchandise add item standard logged in user blocked](/static/images/ProductAdmin/Screenshot%20standard%20user%20add%20items%20blocked.png)

[!Merchandise edit item standard logged in user blocked](/static/images/ProductAdmin/Screenshot%20standard%20user%20edit%20items%20blocked.png)

[!Merchandise delete item standard logged in user blocked](/static/images/ProductAdmin/Screenshot%20standard%20user%20delete%20items%20blocked.png)

- I also want to make sure that the views still render and execute correctly when I am logged in as a superuser so do this now:

[!Superuser merchandise add view opens](/static/images/ProductAdmin/Screenshot%20superuser%20merchandise%20add%20view%20opens.png)

[!Superuser merchandise add view saves](/static/images/ProductAdmin/Screenshot%20superuser%20merchandise%20add%20view%20saves.png)

- The edit views open and save too:

[!Superuser merchandise edit view opens](/static/images/ProductAdmin/Screenshot%20superuser%20edit%20view%20opens.png)

[!Superuser merchandise edit view saves](/static/images/ProductAdmin/Screenshot%20superuser%20edit%20view%20saves.png)

- I finally test that the delete view works, however, this gives me the following notification when I go to the url http://127.0.0.1:8000/merchandise/delete/7434/:

[!Superuser merchandise delete url invalid request](/static/images/ProductAdmin/Screenshot%20superuser%20delete%20invalid%20request.png)

- However, I did decide not to use the delete URL and then test that the buttons still work as superuser for delete on the product which it does:

[!Superuser merchandise delete button notification](/static/images/ProductAdmin/Screenshot%20superuser%20delete%20button%20works.png)

[!Superuser merchandise deleted item successfully](/static/images/ProductAdmin/Screenshot%20superuser%20deleted%20item%20successfully.png)

6. There is one issue that I notice and that's that I'm not sure how I would set multiple sizes in the current set-up so query this with ChatGPT who advises that my data model for Product > ProductVariant is correct but that my form and view only creates one variant so no place for multiple sizes or different prices per size or proper variant system. I need to update my form input to allow multiple sizes as below:

size = forms.CharField(
    required=False,
    help_text="Enter sizes separated by commas (e.g. S,M,L,XL)"
)

- Then in my merchandise/views in my add_product view I need to update the below code from:

size = form.cleaned_data.get('size')

if not product.has_sizes:
    size = None

ProductVariant.objects.create(
    product=product,
    price=form.cleaned_data['price'],
    size=size,
)

To:

sizes = form.cleaned_data.get('size')

if product.has_sizes and sizes:
    size_list = [s.strip() for s in sizes.split(',') if s.strip()]

    for size in size_list:
        ProductVariant.objects.create(
            product=product,
            price=form.cleaned_data['price'],
            size=size,
            variant_title=size,
        )
else:
    # No sizes → single variant
    ProductVariant.objects.create(
        product=product,
        price=form.cleaned_data['price'],
        size=None,
        variant_title="Default",
    )

- I update this and then test adding a product with sizes on the new code and I now have a size selector with all the sizes I set using 'S,XS,M,L,XL' in the size field:

[!Superuser add item with sizes](/static/images/ProductAdmin/Screenshot%20superuser%20add%20product%20sizes%20works.png)

7. I am now going to run a collectstatic and then commit my code to Git and Heroku.

## AWS (Amazon Web Services) - Initial Set-up 

1. I am going to introduce Amazon Web Services into my Project now. To start with, I will create an account at aws.amazon.com. On the URL I click create an AWS account and then in the next window populate with my credentials:

![AWS Create Account](/static/images/AWS/Screenshot%20aws%20create%20account.png)

2. I then choose the free plan on the next screen, once I have proivided my verification code and then created a password for my new account:

![AWS Free Plan](/static/images/AWS/Screenshot%20free%20plan%20aws.png)

3. Then on the next screen, I populate the below form with all my contact details:

![AWS Details](/static/images/AWS/Screenshot%20account%20information%20aws.png)

4. Then I populate my billing details and approve in my banking app, although I will not be going above the agreed limit on my free account so shouldn't have to pay for anything. Once I have confirmed my billing details, I confirm my identity with an SMS to my mobile:

![AWS Confirm Identity](/static/images/AWS/Screenshot%20aws%20confirm%20identity.png)

5. On the next screen, I enter the verification code send to me from AWS via SMS:

![AWS Verification Code](/static/images/AWS/Screenshot%20AWS%20verification%20code.png)

6. Then once the SMS verification code has been entered correctly I will be able to access my AWS account and use the services. I go back to login on my new account and can now see everything AWS:

![AWS Dashboard Home](/static/images/AWS/Screenshot%20aws%20home.png)

7. I now want to create my AWS S3 bucket. To start, I need to do a search for S3 in 'Services':

![AWS S3 Search](/static/images/AWS/Screenshot%20aws%20s3%20service%20search.png)

8. I click on S3 from the list and then click the button to 'Create bucket' at the top of the screen on the next page:

![AWS S3 Create Bucket](/static/images/AWS/Screenshot%20AWS%20S3%20create%20bucket.png)

9. On the next page, I need to enter a bucket name so use the same name as I used for the Heroku version of the app, 'working-out=gym'. I set the bucket type to 'General Purpose' to allow me to store a mix of storage classes across multiple Availability Zones. In Object Ownership I set this to ACL's enabled:

![AWS S3 Bucket Creation Name](/static/images/AWS/Screenshot%20s3%20bucket%20creation%20name.png)

- Then still in the S3 creation, I scroll down and set the Object Ownership to 'Bucket Owner Preferred' and untick 'Block all public access settings for this bucket'. I disable Bucket Versioning to help prevent huge issues with unintended user actions as I can easily rollback to previous versions. I set the 'Default Encryption' to 'Server-side encryption with Amazon S3 managed keys' and leave Bucket Key as enabled. Once these options are populated, I click 'create bucket':

![AWS S3 Bucket Creation Populated Details](/static/images/AWS/Screenshot%20aws%20bucket%20creation%20populated%20details.png)

10. Once the bucket is created, on the next screen I click the bucket name to see the details and then click the 'Properties' tab:

![AWS S3 Bucket Properties Tab](/static/images/AWS/Screenshot%20new%20bucket%20properties%20tab.png)

11. On the next page, I scroll down to the very bottom to find the 'Static website hosting' section and click the 'Edit' button:

![AWS S3 Static website hosting](/static/images/AWS/Screenshot%20s3%20bucket%20static%20website%20hosting.png)

- On the next screen, I select 'enable' and then enter index.html into the index documment input, error.html into the error document input and then 'Save changes':

![AWS S3 Static website hosting enabled](/static/images/AWS/Screenshot%20s3%20bucket%20enable%20static%20website%20hosting.png)

12. Back on the S3 bucket homescreen, I need to then go into the 'Permissions' tab:

![AWS S3 Permissions Tab](/static/images/AWS/Screenshot%20S3%20Bucket%20Permissions%20Tab.png)

- Then once there, I scroll down to the bottom where the section for 'Cross-origin resource sharing (CORS)' and then click 'Edit' on this section:

![AWS S3 Permissions Tab CORS](/static/images/AWS/Screenshot%20permissions%20CORS%20.png)

- I then add the code as shown below in screenshot and then click 'Save changes':

![AWS S3 CORS code](/static/images/AWS/Screenshot%20code%20in%20CORS.png)

13. Next I add the bucket policy, still in the Permissions tab of my bucket, I go to the 'Bucket Policy' section and click 'Edit':

![AWS S3 Permissions Bucket Policy edit](/static/images/AWS/Screenshot%20S3%20Bucket%20Policy%20edit.png)

- Then in a separate window, I open the AWS Policy Generator using https://awspolicygen.s3.amazonaws.com/policygen.html. Once there, I choose ' S3 Bucket Policy' for the 'Type of Policy', I enter an asterisk into the 'Principal field' and for the action I select 'GetObject'. I copy the ARN number from the Bucket Policy tab that I opened first, and then paste this into the ARN input and then click 'Add Statement' and then scroll down and click 'Generate Policy':

![AWS S3 Policy Generator](/static/images/AWS/Screenshot%20policy%20generator.png)

- I then copy all of the text in the pop-up that appears and go back to my Policy Editor on the bcuket itself and paste the JSON code into the Policy window like below:

![AWS S3 Policy Added](/static/images/AWS/Screenshot%20new%20policy%20added.png)

- I then add '/*' to the end of the 'Resource' field in the policy to allow access to all objects within the bucket, then click 'Save changes':

![AWS S3 Policy Resource Field Updated](/static/images/AWS/Screenshot%20edit%20policy%20resource%20field%20updated.png)

14. Next I need to edit the ACL's (Access Control Lists). Still in the Permissions tab, I scroll and find the Access Control List section and click 'Edit':

![AWS S3 Permissions ACL edit](/static/images/AWS/Screenshot%20ACLs%20edit.png)

- I check the box for 'List' in 'Everyone (public access) and then the checkbox to say I understand the effects of the changes I am making and then I click 'Save changes':

![AWS S3 Permissions ACL list everyone](/static/images/AWS/Screenshot%20list%20everyone%20changes%20understood%20.png)

15. The next thing I am going to do is create a user group. To do this, in AWS< I search for 'iam' in the searchbar at the top and click on the icon that appears, as shown below:

![AWS IAM search](/static/images/AWS/Screenshot%20AWS%20iam%20search.png)

- Then on the page for Identity and Access Management (IAM), down the left hand side I click the option for 'User groups' under 'Access Management':

![AWS IAM user groups](/static/images/AWS/Screenshot%20iam%20user%20groups.png)

- Then on the next screen, I click 'Create group' and then on the next screen where it asks me for group name, I enter 'manage-working-out-gym' and then scroll to the bottom of the page and click 'Create user group':

![AWS IAM name and create user group](/static/images/AWS/Screenshot%20name%20and%20create%20user%20group.png)

16. Next, I create a policy. Still in the IAM screen, I then select 'Policies' from the 'Access Management' menu and then click 'Create policy' in the top right:

![AWS IAM create policy](/static/images/AWS/Screenshot%20iam%20create%20policy.png)

- On the next page, I select the JSON tab at the top, then click actions and then click 'Import Policy':

![AWS IAM import policy](/static/images/AWS/Screenshot%20import%20policy.png)

- Then in the new window that appears, I search for S3, select the option for 'AmazonS3FullAccess' and then click 'Import policy':

![AWS S3FullAccess Import Policy](/static/images/AWS/Screenshot%20s3fullacess%20import%20policy.png)

- Then I do a search for S3 in the bar at the top, then right-click S3 and open it in a new tab. Then once it opens, I select the bucket for working-out-gym and then copy the ARN number from the 'Properties' tab. Then back on the IAM policy editor, in my 'Resource' dictionary, I paste the ARN number twice and on the second iteration I add /* to the end so it looks like below:

![AWS Policy ARN Number Resource Update](/static/images/AWS/Screenshot%20arn%20policy%20resource%20update.png)

- I then scroll to the bottom and click 'Next' and on the next screen, enter a name and description:

![AWS Policy Name and Dsecription](/static/images/AWS/Screenshot%20policy%20name%20and%20description.png)

17. I get my success message on the next page and then move on to attaching my new policy to the user group. I click 'User Groups' from the left menu again:

![AWS Policy Successful Creation Message](/static/images/AWS/Screenshot%20policy%20successfully%20created.png)

- Then on the 'User Groups' screen, I select the new user group that I created earlier:

![AWS Selecting User Group](/static/images/AWS/Screenshot%20select%20created%20user%20group.png)

- Then in my group, I click the 'Permissions' tab and then click the 'Add Permissions' dropdown and then choose 'Attach policies':

![AWS Attach Policies User Group](/static/images/AWS/Screenshot%20user%20group%20permissions%20attach%20policies.png)

- Then on the next screen, I search for my new policy I have created and then select the checkbox next to it and then click 'Attach policies' at the bottom of the page:

![AWS Search and Attach policy](/static/images/AWS/Screenshot%20search%20and%20attach%20new%20policy.png)

18. I am redirected where I am presented with a success message re. the policies attaching to the user group. Therefore, I now create a new user. I select the 'Users' menu from the Access Management menu on the left:

![AWS Polciies Attached Successfully Users menu](/static/images/AWS/Screenshot%20policies%20attached%20users%20menu.png)

- On the next screen, I click 'Create User':

![AWS Create user](/static/images/AWS/Screenshot%20create%20user.png)

- I set a username and then click 'Next':

![AWS Set username on new user](/static/images/AWS/Screenshot%20set%20username.png)

- On the next screen, I select the user group that I created previously and then click 'Next':

![AWS Set user group](/static/images/AWS/Screenshot%20new%20user%20select%20user%20group.png)

- Then finally, I scroll to the bottom of the page and click 'Create User':

![AWS Create User Final](/static/images/AWS/Screenshot%20create%20user%20final.png)

19. Once I receive a message confirming the user was successfully created, I want to create an Access Key. To do this, I click on the newly created user:

![AWS Create Access Key Click User](/static/images/AWS/Screenshot%20create%20access%20key%20click%20user.png)

- On the next screen, I click 'Security Credentials', then in the tab, I scroll down to the 'Access Keys' section and then click 'Create Access Key':

![AWS New User Security Credentials Tab Create Access Key](/static/images/AWS/Screenshot%20security%20credentials%20create%20access%20key.png)

- On the next screen, I click the option for 'Application running outside AWS' and then click 'Next':

![AWS Application Running Outside of Best Practises](/static/images/AWS/Screenshot%20application%20running%20outside%20AWS.png)

- I leave description blank and then click 'Create Access key' on the new screen:

![AWS Create access key](/static/images/AWS/Screenshot%20create%20acess%20key%20no%20description.png)

- I receive a success message letting me know Access Key was created, I scroll down and click 'Download .csv file' and choose to open the .csv file in my notepad:

![AWS download csv file](/static/images/AWS/Screenshot%20download%20csv%20file.png)

- I then login to Heroku and go to my working-out-gym dashboard > Settings > Config Vars and set up the AWS_ACCESS_KEY_ID and AWS_SECRET_ACCESS_KEY using the values I have just been given.

---

## AWS - Connecting to Django

1. Now that I have created an S3 bucket in AWS with the appropriate user's groups and security policies for it, I can now connect Django to it. I first need to install 2 x new packages:

pip3 install boto3
pip3 install django-storages

2. Once I can see in my terminal that the two packages have both successfully installed, I then add these to the requirements file using:

pip3 freeze local > requirements.txt

3. I now need to update my INSTALLED APPS section in settings to include 'django-storages':

'storages',

4. Before moving on, I need to set my AWS_ACCESS_KEY_ID and AWS_SECRET_ACCESS_KEY as environment variables in env.py so do this now. I then borrow Code Institute's code for the if statement which will tell my project which S3 bucket to communicate with when on Heroku. I paste this into my code for MEDIA in settings:

if 'USE_AWS' in os.environ:
    # Bucket Config
    AWS_STORAGE_BUCKET_NAME = 'working-out-gym-126309364526-eu-north-1-an'
    AWS_S3_REGION_NAME = 'eu-north-1'
    AWS_ACCESS_KEY_ID = os.environ.get('AWS_ACCESS_KEY_ID')
    AWS_SECRET_ACCESS_KEY = os.environ.get('AWS_SECRET_ACCESS_KEY')
    AWS_S3_CUSTOM_DOMAIN = f'{AWS_STORAGE_BUCKET_NAME}.s3.amazonaws.com'

    # Static and media files
    STATICFILES_STORAGE = 'custom_storages.StaticStorage'
    STATICFILES_LOCATION = 'static'
    DEFAULT_FILE_STORAGE = 'custom_storages.MediaStorage'
    MEDIAFILES_LOCATION = 'media'

    # Override static and media URLs in production
    STATIC_URL = f'https://{AWS_S3_CUSTOM_DOMAIN}/{STATICFILES_LOCATION}/'
    MEDIA_URL = f'https://{AWS_S3_CUSTOM_DOMAIN}/{MEDIAFILES_LOCATION}/'


5. Once this is set, I then go back to my Heroku dashboard for working-out-gym, go to Settings > Config Vars and add the key for USE_AWS and set the value to True so that the settings file knows to use the AWS config when I deploy to Heroku. 

6. I now want to tell the project to use S3 to store the static files whenever collectstatic is ran and that any uploaded product images should be held in AWS also. To do this, I create a file called custom_storages.py in the root of the project folder and then borrow Code Institute's content for this again:

from django.conf import settings
from storages.backends.s3boto3 import S3Boto3Storage


class StaticStorage(S3Boto3Storage):
    location = settings.STATICFILES_LOCATION


class MediaStorage(S3Boto3Storage):
    location = settings.MEDIAFILES_LOCATION

7. Now that these changes are in place, I am going to commit the changes and push to Git and Heroku so I can test them. I check the build logs in Heroku and confirm it has collected the static files successfully. However, when I launch my app from Heroku it is not serving my static files anymore:

![Production App not serving static files](/static/images/AWS/Screenshot%20production%20not%20serving%20static%20files.png)

8. I query this with ChatGPT who recommends updating settings if 'USE_AWS' statement to the below:

if 'USE_AWS' in os.environ:
    AWS_STORAGE_BUCKET_NAME = 'working-out-gym-126309364526-eu-north-1-an'
    AWS_S3_REGION_NAME = 'eu-north-1'
    AWS_ACCESS_KEY_ID = os.environ.get('AWS_ACCESS_KEY_ID')
    AWS_SECRET_ACCESS_KEY = os.environ.get('AWS_SECRET_ACCESS_KEY')

    AWS_S3_CUSTOM_DOMAIN = f'{AWS_STORAGE_BUCKET_NAME}.s3.amazonaws.com'

    AWS_DEFAULT_ACL = 'public-read'
    AWS_QUERYSTRING_AUTH = False

    AWS_S3_OBJECT_PARAMETERS = {
        'CacheControl': 'max-age=86400',
    }

    STATICFILES_STORAGE = 'custom_storages.StaticStorage'
    STATICFILES_LOCATION = 'static'

    DEFAULT_FILE_STORAGE = 'custom_storages.MediaStorage'
    MEDIAFILES_LOCATION = 'media'

    STATIC_URL = f'https://{AWS_S3_CUSTOM_DOMAIN}/{STATICFILES_LOCATION}/'
    MEDIA_URL = f'https://{AWS_S3_CUSTOM_DOMAIN}/{MEDIAFILES_LOCATION}/'

- I then run a recurse staticfiles cmd and then collectstatic after this:

Remove-Item -Recurse -Force staticfiles

python manage.py collectstatic

- I redeploy the app to Heroku:

git push heroku main

- I then check my S3 bucket to make sure it has created a static folder but it has not:

![S3 Bucket not collecting static](/static/images/AWS/Screenshot%20S3%20bucket%20not%20collecting%20static.png)

- I confirm that my Heroku config vars are set correctly for USE_AWS and the 2 x AWS Keys. 

- I then force a rebuild of the Heroku app to force Heroku to re-run collectstatic with AWS enabled and notice this message for staticfile collection in the build logs:

894 static files copied to '/tmp/build_a18196d3/staticfiles'.

- This shows that Django is still using local file storage and not S3. When I query the logs with ChatGPT it advises that my AWS block is not being activated during build on Heroku which means this condition is failing:

if 'USE_AWS' in os.environ:

- It recommends I set the config vars from the terminal using:

heroku config:set USE_AWS=1

- It then recommends that I update:

if 'USE_AWS' in os.environ:

To:

if os.environ.get('USE_AWS') == '1':

- Then I push the build again:

git add .
git commit -m "Fix AWS env detection"
git push heroku main

- I check the build logs again but I am still seeing the following line:

895 static files copied to '/tmp/build_c74229be/staticfiles'.

- ChatGPT diagnoses again and advises that even though the logs shows that AWS os active the following line is being ignored:

STATICFILES_STORAGE = 'custom_storages.StaticStorage'

- It says that this is happening because in Django 4.2 it's deprecated so right now its ignoring my S3 storage class and failing back to local filesystem so thats why i see /tmp/. It advises me to update my AWS storage config with:

if os.environ.get('USE_AWS') == '1':
    AWS_STORAGE_BUCKET_NAME = 'working-out-gym-126309364526-eu-north-1-an'
    AWS_S3_REGION_NAME = 'eu-north-1'
    AWS_ACCESS_KEY_ID = os.environ.get('AWS_ACCESS_KEY_ID')
    AWS_SECRET_ACCESS_KEY = os.environ.get('AWS_SECRET_ACCESS_KEY')

    AWS_S3_CUSTOM_DOMAIN = f'{AWS_STORAGE_BUCKET_NAME}.s3.amazonaws.com'

    AWS_DEFAULT_ACL = 'public-read'
    AWS_QUERYSTRING_AUTH = False

    AWS_S3_OBJECT_PARAMETERS = {
        'CacheControl': 'max-age=86400',
    }

    STATICFILES_LOCATION = 'static'
    MEDIAFILES_LOCATION = 'media'

    STATIC_URL = f'https://{AWS_S3_CUSTOM_DOMAIN}/{STATICFILES_LOCATION}/'
    MEDIA_URL = f'https://{AWS_S3_CUSTOM_DOMAIN}/{MEDIAFILES_LOCATION}/'

    STORAGES = {
        "default": {
            "BACKEND": "custom_storages.MediaStorage",
        },
        "staticfiles": {
            "BACKEND": "custom_storages.StaticStorage",
        },
    }

- I also have a conflict with Cloudinary and it is overriding my storage, the below line of code in my settings is causing the conflict so I delete this line of code:

DEFAULT_FILE_STORAGE = 'cloudinary_storage.storage.MediaCloudinaryStorage'

- I also need to update my custom_storages.py to the below as in its current form it relies on settings variables:

from storages.backends.s3boto3 import S3Boto3Storage


class StaticStorage(S3Boto3Storage):
    location = 'static'


class MediaStorage(S3Boto3Storage):
    location = 'media'

- ChatGPT advises that I also need tob add a variable for AWS_S3_ADDRESSINGT_STYLE in my AWS block in settings:

AWS_S3_ADDRESSING_STYLE = "virtual"

- I also remove whitenoise as I am no longer using it:

'whitenoise.middleware.WhiteNoiseMiddleware',

- I then redeploy using the below:

git add .
git commit -m "Fix S3 storage config"
git push origin main
git push heroku main

- This runs now but hangs on this line: 

python manage.py collectstatic --noinput

- ChatGPT picked up that I have used the wrong custom domain for my region in my AWS block and advises to update this to:

AWS_S3_CUSTOM_DOMAIN = f'{AWS_STORAGE_BUCKET_NAME}.s3.{AWS_S3_REGION_NAME}.amazonaws.com'

- I update this and then run:

git add .
git commit -m "Fix S3 storage config"
git push origin main
git push heroku main

- Finally, I can see that the static files are serving on Heroku and I can see the static folder in my S3 bucket now too:

![Heroku app serving static files from S3 Bucket](/static/images/AWS/Screenshot%20heroku%20app%20now%20serving%20static%20filees.png)

![Heroku app serving static files from S3 Bucket](/static/images/AWS/Screenshot%20S3%20bucket%20static%20folder%20now%20created.png)

---

## Sending E-mails with Django

1. I am now going to set-up my project so that Django will send e-mails. To start with, I go to my personal account in gmail.com and then click the cog icon and then 'see all settings'.

2. I then click 'Accounts and Import' from the top navbar and then click 'Other Google account settings'.

3. I then click the 'Security' tab and then go to turn on 2-step verification so that I can create an app password specific to my Django app; the password allows it to authenticate and use my personal gmail address to send the e-mails from the app. On the page below, I click 'Turn on 2 step verification':

![Personal gmail setting up 2 step verification](/static/images/email/Screenshot%202%20step%20verification%20gmail.png)

4. After clicking 'done' on the prompt that tells me I have turned on 2 step verification, I then click the back button to return to the previous menu. Then in the search bar I look for 'App passwords' and click the option that appears:

![Personal gmail app passwords search](/static/images/email/Screenshot%20app%20passwords%20menu%20search.png)

5. On the new screen I set the name as 'working-out-gym-emails' and then click 'Create':

![Gmail App Passwords Names](/static/images/email/Screenshot%20app%20passwords%20create%20name.png)

6. Now that I have successfully set up 2 factor authentication on my personal gmail account. and my code, I go to Heroku and login and go to the dashboard of working-out-gym and set my config_vars for the new method calling this EMAIL_HOST_PASS and then setting the value as the 16 character generated by Gmail.

7. Then, still in config vars on my Heroku app settings, I will add another key called EMAIL_HOST_USER and the value will be my personal gmail address. 

8. The final step, is I take the code from Code Institute's Boutique Ado and paste into my settings around my variable for DEFAULT_FROM_EMAIL. This uses an if statment that says if development is in os.environ to determine which email setup it uses and then if its in dev there are only a few variables but if its in production then a great deal more variables are required:


if 'DEVELOPMENT' in os.environ:
    EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
    DEFAULT_FROM_EMAIL = 'workingoutgym@example.com'
else:
    EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
    EMAIL_USE_TLS = True
    EMAIL_PORT = 587
    EMAIL_HOST = 'smtp.gmail.com'
    EMAIL_HOST_USER = os.environ.get('EMAIL_HOST_USER')
    EMAIL_HOST_PASSWORD = os.environ.get('EMAIL_HOST_PASS')
    DEFAULT_FROM_EMAIL = os.environ.get('DEFAULT_FROM_EMAIL')

# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


9. To test this out, I need to deploy to Git and Heroku:

git add .
git commit -m "Added email send functionality from gmail"
git push origin main
git push heroku main

---

## Stripe - Testing Webhooks on Ecommerce Site

1. I now need to set up a new endpoint on Stripe for my production application on Heroku. To start, I login to Stripe: 

---



# 6. Credits and Acknowledgements

### Content

#### Code Institute Documentation

- Stripe CLI Installation Guide for Windows: https://codeinstitute.s3.eu-west-1.amazonaws.com/vscode-migration-pdf-guides/stripe-cli-installation-guide-windows.pdf

#### Bootstrap Documentation

The following parts of my Project were implemented using Bootstrap docs:

- Media Queries were used to present all pages in a readable format across all device sizes.
- Used Boostrap Images docs for alignment and positioning of images
- Used Bootstrap documentation for Products cards
- Used Bootstrap Toasts method to provide users with informative messages throughout their interactions with the site.
- Bootstrap Toasts html code for toast templates

#### Favicon

- Beating Heart emoji used for Navbar logo on smaller screens: https://favicon.io/emoji-favicons/beating-heart

#### Primary reference: 

- 

#### Google Fonts

- Boldonse Font from https://fonts.google.com/selection/embed
- PT Serif Font from https://fonts.google.com/selection/embed

#### Font Awesome


#### CSS Tricks

- css triangle: https://css-tricks.com/snippets/css/css-triangle/ */

#### Kaggle.com

- Gymshark Products Dataset - https://www.kaggle.com/datasets/ahrnishpdahal/gymshark-products-dataset

#### Stripe

- Documentation on accepting payments: https://docs.stripe.com/payments/accept-a-payment
- Basic Javascript styles for 'var' and 'invalid'
- CSS styles for Stripe Elements
- Handle Webhook Events code
- Stripe CLI Installation Guide for Windows

---

### Media

- Pexels Main Homepage Image: Photo by Anete Lusina: https://www.pexels.com/photo/man-with-strong-hands-lifting-dumbbells-4793215/

- Pexels Discussion Board Main Image: Photo by Andrea Piacquadio: https://www.pexels.com/photo/three-women-wearing-sports-bras-and-leggings-864078/

- Products Page Main Image: Photo by    www.kaboompics.com: https://www.pexels.com/photo/happy-young-sportswoman-doing-exercise-with-dumbbell-4498292/

- Fitness Plan Images: Photo by Andrea Piacquadio: https://www.pexels.com/photo/young-female-athlete-training-alone-on-treadmill-in-modern-gym-3768916/, Photo by cottonbro studio: https://www.pexels.com/photo/woman-practicing-plyometrics-7675414/, Photo by Ketut Subiyanto: https://www.pexels.com/photo/man-in-black-tank-top-and-blue-shorts-sitting-on-bench-lifting-a-dumbbell-4720756/

- Nutrition Plan Images: Photo by Abet Llacer: https://www.pexels.com/photo/assorted-fruits-3025236/, Photo by Pixabay: https://www.pexels.com/photo/grilled-meat-dish-served-on-white-plate-361184/, Photo by Vie Studio: https://www.pexels.com/photo/grains-and-seeds-in-glass-jars-and-on-bowls-7421448/ 

- Pexels Default No Image found: https://www.pexels.com/photo/question-mark-on-crumpled-paper-5428826/

- Pexels Keto Nutrition Plan Image: https://www.pexels.com/photo/vegetable-salad-on-white-ceramic-plate-10680710/

- Pexels Strength Training Plan: https://www.pexels.com/photo/black-dumbbell-lot-260352/

- Pexels Freedom Cap: https://www.pexels.com/photo/a-yellow-and-blue-fitted-cap-on-a-black-granite-in-dark-background-11463614/

- Pexels Clothing Rack: https://www.pexels.com/photo/vibrant-vintage-clothes-hanging-at-flea-market-30202432/

---

### Code

#### Claude AI Acknowledgements

- Merchandise views.py elif statement for for_price in all_products view.
- if statement for searching on products
- search bar form on main-nav.html
- sort and direction parameter code in products.html
- sort selector Javscript code in products.html
- jQuery Library loading code in base.html
- price low to high sorting if statements in all_products view
- back to top functionality in script.js
- account and shopping bag code main-nav.html
- shopping bag icon styles
- mobile css for navlinks
- css media queries for tablet and mobile for shopping bag and account items in navbar
- media query for small screen sizes for leading paragraph on index.html
- product_variant definition in contexts.py
- ShoppingBagItems model in shoppingbag app
- add_to_bag view in shoppingbag


#### Code Institute Acknowledgements

- Base.html Edge Code
- Index.html DTL Blocks
- Base.html DTL Blocks
- post_detail.html comments code
- comments.js file in static/js
- ProductAdmin and CategoryAdmin classes in Merchandise/admin.py
- CSS style for overlay class
- Used Django for loop for Products cards logic
- Used Code Institute product_details.html code for my own from their Boutique Ado project
- search query update in all_products view
- direction request.GET parameter in my all_products view defined in the views.py file in Merchandise app.
- product category sorting code in views.py
- for current_categories statement in products.html
- css for a.category-badge > span.badge:hover
- badge models in merchandise app
- badge views, url and template code
- code for badges in products.html and product_detail.html
- sort select options for merchandise products
- javascript for sorting products in products.html
- back to top html and javascript in products.html
- css styles for text-black, btt-button and btt-link
- shoppingbag.html initial code
- FREE_DELIVERY_THRESHOLD and STANDARD_DELIVERY_PERCENTAGE variables in settings
- shoppingbag contexts.py
- product_details.html quantity form
- btn-outline-black css classes
- has_size variable
- size selector html code in product_details and with statement
- shoppingbag html code for product.has_size
- quantity_input_script.html
- anchor elements for updating quantity and removing products shoppingbag.html
- javascript for click events shoppingbag.html
- Toast html code for toast_success, toast_warning, toast_info and toast_error templates
- css styles for toast
- javascript for toast method base.hml
- add_to bag and adjust_bag views with Toast message code
- Code Institute CSS code for convenience classes
- arrow css styles
- checkout app models.py order and orderlineitem classes
- checkout models.py functions for generate_order_number, update_total and save
- init function code for the checkout forms
- Code Institute Checkout.html
- form-check-inline code in checkout.html
- checkout.html submit button
- bag_tools.py code
- stripe_elements.js code and functions
- checkout views checkout function stripe updates
- checkout_success views
- checkout_success.html code
- checkout_success rows for Order Summary
- checkout.html loading-overlay div
- checkout.css loading-overlay and loading-spinner styles
- display css update for loading-cursor div
- handle webhooks event code - webhooks.py
- webhook_handler handle_payement_intent_succeeded updates
- select and select option css in checkout.css
- templates/allauth/base.html
- templates/allauth/account/base.html
- profile.html form updates 
- profiles.css profile-update-form rules
- order history bootstrap table profile.html
- add_product views
- edit_product views
- merchandise/forms ProductForm
- if statement in settings.py for AWS
- custom_storages.py file from Boutique Ado
- if statement in settings for email sending



#### ChatGPT Acknowledgements

- Navbar code reused from Project 3
- discussionboard urls.py file
- discussionboard post_list.html vote code
- discussionboard views.py file code with vote model
- vote_total code in Post model
- save function in discussionboard models.py
- post_detail.html in discussionboard app
- post_list.html is discussionboard app
- CRUD code for discussionboard app - new classes for create, edit and delete and url patterns
- post_form.html in discussionboard app
- post_confirm_delete.html in discussionboard app
- class based views for CommentOwnerOrSuperuserMixin and CommentDelete
- comment_confirm_delete.html 
- class based view for CommentUpdate
- Feedback model in home app
- FeedbackForm in forms.py in home app
- homepage view function code
- messages display block code in base.html
- footer authentication message code
- merchandise class based view for products
- merchandise management python code
- merchandise class based view for ProductsVariant
- merchandise Category model
- merchandise admin model for ProductVariantInline
- products variable in all_products function
- Template used for product_detail.html
- Template used for mobile-top-header.html
- Template used for main-nav.html
- Navbar css styles
- Homepage css styles
- Updates to index.html
- ChatGPT search form update
- dropdown menu code for Merchandise nav bar dropdowns
- css styles for navbar dropdown menu
- rewritten shoppingbag/contexts.py, views.py and urls.py
- product_detail.html form content
- shoppingbag.html if bag_items statement
- shoppingbag.html table
- view_bag view in shoppingbag app
- non_clothing shell cmds
- redefined bag_contents in contexts.py
- redefined view_bag views
- redefined add_to_bag views
- size selector and quantity selector html in product_detail.html
- btn-black and btn-black:hover css
- update_bag views and urls
- adjust_bag, update_bag and remove_from_Bag views and associated code in shoppingbag
- jquery and bootstrap js updates to base.html
- img_src html in toast_success.html
- for bag item in bag items image statement in toast_success.html
- if size statement block in add_to_bag view in shoppingbag app
- .custom-toast css styles
- calc_subtotal function code bag_tools.py
- checkout/views variant id updates
- merchandise/views and templates for product_detail with variiant id updates
- shoppingbag.html complete update after changes to database
- toast_success.html size update
- update to __str__ method in checkout/models OrderLineItem
- editable fields code in checkout/admin for OrderLineItemAdminInline class
- OrderAdmin class updates in chckoutadmin to make fields editable
- item price calculation paragraph in checkout_success
- loading overlay hide code in stripe_elements.js
- loading-overlay div css rules for blurred background
- stripe_elements.js in checkout update with done() wrapper
- var saveinfo stripe_elements.js
- address variable webhook handler update
- toast jquery base.html script
- countryfield.js update no jquery
- plans/models Plan class code
- UserPlan class in plans/models
- plans/views plans_list view code
- plans.html code
- checkout/views checkout view plans updates
- checkout/views checkout_success updates for plans
- checkout.html if plan statement update
- product_detail.html quantity selector script
- merchandise/forms ProductVariantForm code
- merchandise/views add_product ProductVariantForm updates
- ProductForm updates after ProductVariantForm created
- merchandise/views add_product ProductForm updates
- updated save method to generate handle with slugify on Product model in merchandise/models
- toast_success image if statement
- pagination controls products.html template
- edit_product views update to include correct model of ProductVariant which holds price
- edit_product views update with correct coding for ProductVariant price in POST method
- delete_product view in merchandise/views
- merchandise app template product_detail.html code for edit delete button views
- merchandise app template product.html code for edit delete buttons on product cards
- merchandise/views is_superuser helper
- merchandise/views add_product size update
- custom_storages.py updates to remove local setting reliance




---

# 7. Troubleshooting, Debugging & Tidy-up

