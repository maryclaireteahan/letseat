# Let's Eat

Let's Eat is a fully responsive full-stack website that I have built using the Django Full Stack framework for my Portfolio Project 4. This website gives the user the ability to browse recipies based on their category, comment on and like them.
  
![Am i responsive image]()  

[Click Here To Visit Live Site](https://maryclaireteahan-letseat-0b5910f8e882.herokuapp.com/)  

## Table Of Contents:
1. [Design & Planning](#design-&-planning)
    * [User Stories](#user-stories)
    * [Wireframes](#wireframes)
    * [Agile Methodology](#agile-methodology)
    * [Typography](#typography)
    * [Colour Scheme](#colour-scheme)
    * [Database Diagram](#database-diagram)
    
2. [Features](#features)
    * [Navigation](#Navigation-bar)
    * [Footer](#footer)
    * [Index page](#index-page)
    * [Recipes page](#recipes-page)
    * [Single recipe page](#single-recipe-page)
    * [Edit comment page](#edit-comment-page)
    * [Delete comment page](#delete-comment-page)
    * [Create recipe page](#create-recipe-page)
    * [Edit recipe page](#edit-recipe-page)
    * [Delete recipe page](#delete-recipe-page)
    * [Login page](#login-page)
    * [Logout page](#logout-page)
    * [Sign up page](#signup-page)

3. [Future Features](#future-features)
4. [Technologies Used](#technologies-used)
5. [Libraries](#libraries-used)
6. [Testing](#testing)
7. [Bugs](#bugs)
8. [Deployment](#deployment)
9. [Credits](#credits)
10. [Acknowledgements](#acknowledgements)

## Design & Planning:

### User Stories
#### First time visitor
- As a first-time visitor, I want to understand the purpose of the website and easily navigate through
- As a first-time visitor, I want to be able to view the posts so that I would get quick access to relevant information and get a better understanding of the content
- As a first-time visitor, I want to be able to see likes and comments for the posts to get some feedback from other users
- As a first-time visitor, I want to be able to register an account to have more access to the website
- As a first-time visitor, I want to be able to search posts by title name so I could get quick access to the relevant one
- As a first-time visitor, I want to be able to subscribe to the blog so I could get relevant information about future blog posts
#### Registred user
- As a registered user I want to be able to leave comments for posts so that I can engage with other users and, leave feedback about certain posts
- As a registered user I can update or delete my comments so that have more control over my content in case of errors, and to have better engagemant with other users
- As a registered user I want to be able to like/unlike posts so that I can support certain posts without providing comment
- As a registered user I want to be able to update my profile information so that I could change my first name, last name, email and password and add a profile picture, bio
#### Site owner
- As a site owner, I want to be able to create, update and delete posts so that I can control my website content
- As a site owner, I want to be able to approve or delete comments so that I can filter out objectionable comments
-As a site owner, I want to be able to access all subscribed emails so that I could send new information related to my website
- As a site owner, I want to be able to delete users so that I can receive several benefits such as: manage my data, reduce liability & resource optimization 


### Wireframes
Below are the wireframes for the site that I created using balsamiq. As I was developing my website I was using agile approach and adding/updating my website/elements so for that reason some wireframes are not matching my final product.
#### Desktop
<details><summary>Index</summary>
<img src="readme/documentation/wireframes/index.png">
</details>

<details><summary>Recipe Categories</summary>
<img src="readme/documentation/wireframes/all_recipes.png">
</details>

<details><summary>Single Recipe</summary>
<img src="readme/documentation/wireframes/single_recipe.png">
</details>

<details><summary>Edit Comment page</summary>
<img src="readme/documentation/wireframes/comment_edit.png">
</details>

<details><summary>Delete Comment and Delete Recipe</summary>
<img src="readme/documentation/wireframes/delete.png">
</details>

<details><summary>Create and Edit Recipe</summary>
<img src="readme/documentation/wireframes/add_edit_recipe.png">
</details>

<details><summary>Login page</summary>
<img src="readme/documentation/wireframes/login.png">
</details>

<details><summary>Logout page</summary>
<img src="readme/documentation/wireframes/logout.png">
</details>

<details><summary>Sign up page</summary>
<img src="readme/documentation/wireframes/signup.png">
</details>


### Agile Methodology
The Agile Methodology was used to plan this project. I found it hard to work parallel on agile and on my coding as I was team of 1 and was aware of the changes so I found that to be confusing. I had to add a few things at the end of my project in github repository. I did learn more towards the end of the project about the use of the agile develepment, and why it's important and usefull to keep track of the whole process and to implement as much as you can. 
I've used Github and the Project Board with use of the Kanban board.

I devided project board into 3 sections:

  -  To-Do- (All the User stories were initially entered in the 'To Do' column)
  -  In Progress- (then during development story they were moved into the 'In Progress' column)
  -  Done- (and then finally they get moved into 'Done' once the development completes)

<details><summary>Project board</summary>
<img src="readme_img/test/project_board.png">
</details>

- I've planned 5 itterations for this project. Four were completed as planned and fifth one is for future development of the webiste, which is described more in feature features in this document

<details><summary>Milestones</summary>
<img src="readme_img/test/milestone.png">
</details>

- Each milestone consist of user stories, which are displayed either open or closed depends on the progress.
Each user story is labeled either as 'must-have', 'should-have' or 'could-have'depending of the needs of the project with estimated story points attached.

<details><summary>Milestone detail</summary>
<img src="readme_img/test/mls_det.png">
</details>

- Each user story have acceptance criteria and tasks that needed to be done to accomplish  that criteria
 

<details><summary>User story detail</summary>
<img src="readme_img/test/user_story_detail.png">
</details>

### Typography
I chose to use "Dosis" font family beacuse it's easily readable on both small and large screens, making it a great option for websites and digital interfaces. It's clean with moder apperance. As a backdrop font I've used 'Sans-serif'.

### Colour Scheme
For this website, I decide to keep the main color scheme very simple.Text was either  white or black with background of certain cards and the footer beeing light red/orange color while the rest of the background is white.
I kept consistant colours for buttons and links on the website. All buttons have hover effect of "Robin egg blue" except 'Delete & Update' button which are standard red and blue colored.
  
<details><summary>Color palette</summary>
<img src="readme_img/page_screen/palete.png">
</details>


### DataBase Diagram
Below is the database diagram that I created using LucidCharts.

<details><summary>DataBase diagram</summary>
<img src="readme_img/wireframes/dtb.jpeg">
</details>

## Features:

### Navigation Bar
- The Navigation bar sits at the very top of each page, and it's sticky navbar which means when page is longer and user has to scroll down the navbar will stay on top of the page all the time! The logo is at the left side and the navigation links are in the middle with login/signup buttons on the right.
- Logo is clickable and redirects user back to the home page
- When logged in new link is displayed to the user: "Profile" ,and login/signup button is replaced with Logout button. Also user name is displayed next to the logo.
- The Navbar background is white with opacity set to 75%.
- On large to xx-large screens the navigation bar is in the center of the page and is sized by the bootstrap class.
- The active page (page that the user is currently on) is displayed in coloured text, this makes it stand out much more and is clear to the user which page they are on.
- When on medium to small screens the navigation menu changes to burger menu which shows all the nav links when clicked on.
  
<details><summary>Navbar</summary>
<img src="readme_img/test/navbar_login.png">
</details>

<details><summary>Navbar medium screens</summary>
<img src="readme_img/test/navbar_mob.png">
</details>

### Footer
- The footer is found at the bottom of every page and is responsive for tablet and mobile too in its orange color.
- It displays the logo in the left corner, social links (Youtube, Facebook, Twitter & Youtube) are in the middle of the footer and, the Subscription field is on the right side of the footer.
- When any of the icons are clicked the social media site opens on a separate tab, this way the user still has the main website open, also by clicking on thelogo the user is redirected to the home page.
- Copyright text sits at the bottom of the footer
  
<details><summary>Footer</summary>
<img src="readme_img/test/footer.png">
</details>

### Index Page
- The home page has a dark hero image with text gradually displaying and deleting indicating site purpose
- Bellow hero image there are two sections which describe the owner of the page and his reach to the community with icons and numbers
- map?
<details><summary>Index Hero</summary>
<img src="readme/documentation/features/index/hero.png">
</details>
<details><summary>Index Button</summary>
<img src="readme/documentation/features/index/discover_recipes.png">
</details>


### Recipes page
- On this page the user have option to use "search bar" to find specific posts or he can scroll down to search for post that he would like to get more information about it
- If input on search box is not empty the user will be redirected to the new page which will eaither displayed match post or display message to the user 
- Posts are displayed in 2 columns with 3 posts per row, each post contains of: image, author, date, indicator of likes and comments and title and brief description 
- Posts card are scaling up as the user hovers over them and clickable title and ecerpt are transforming to capitalize letter
- When clicked on title/excerpt user is redirected to another page which will give a user more information about the post

<details><summary>Recipe Categories</summary>
<img src="readme/documentation/features/all_recipes/categories1.png">
<img src="readme/documentation/features/all_recipes/categories2.png">
<img src="readme/documentation/features/all_recipes/categories3.png">
</details>
<details><summary>Recipe Categories Scrollbar</summary>
<img src="readme/documentation/features/all_recipes/scrollbar.png">
</details>

  
### Single recipe page
- On this page, the user can have a brief description of the certain post that he clicked on and get all relevant information about it
- Bellow post section register user can like/unlike post
- User can leave comment
- After the user posts his comment he will be prompted with the message that says "comment is waiting for approval"
- If user has already left comment he has option to either update his comment or delete it by simply clicking either of displayed buttons
- By clickin "Delete" button user will be asked to confirm his choice, if he do so success message will be displayed to the user and comment would be deleted
- By clicking "Update" the user will be redirected to the new page which will allow him to update his comment

<details><summary>Single Recipe Like and Comment Icons</summary>
<img src="readme/documentation/features/single_recipe/likes_comment_icons.png">
</details><details><summary>Single Recipe Comments</summary>
<img src="readme/documentation/features/single_recipe/comment_logged_out.png">
<img src="readme/documentation/features/single_recipe/comment_logged_in.png">
<img src="readme/documentation/features/single_recipe/comments.png">
<img src="readme/documentation/features/single_recipe/edit_delete_authorised.png">
<img src="readme/documentation/features/single_recipe/edit_delete_not_authorised.png">
</details>

### Edit comment page
- On this page one form field is displayed to the user with current comment that he wish to update
- Bellow the form there is submit button, which will confirm user new comment by providing success message to the user and redirecting to the previous page

<details><summary>Edit comment page</summary>
<img src="readme/documentation/features/comment_edit/original_comment.png">
<img src="readme/documentation/features/comment_edit/edit_box_original_comment.png">
<img src="readme/documentation/features/comment_edit/require_edit.png">
<img src="readme/documentation/features/comment_edit/edit_box_edited_comment.png">
<img src="readme/documentation/features/comment_edit/edited_comment.png">
</details>

### Delete comment page
- Profile page has 2 sections
- The first section on the left of the screen displays current information about the user which he provided upon registration
- The second section is a standard django form which allows the user to change information about him and to add "bio" and profile image if he wants to
- Bellow the form there is a link to reset/change his password. When a user clicks on it he will be directed to the page with further instructions.
- Bellow reset/change passwords there are 2 buttons to either "Update" or " Delete" the user account, if a user clicks on the delete button separate model will pop out for the user to confirm deleting his account. 
- If user click on update button, updated information would be shown on his profile card with success message

<details><summary>Delete comment page</summary>
<img src="readme/documentation/features/comment_delete/original_comment.png">
<img src="readme/documentation/features/comment_delete/delete_comment.png">
<img src="readme/documentation/features/comment_delete/comment_deleted.png">
</details>

### Create recipe page
- Use can only get to this page by inputing something on the search bar in the post page
- This page will either display a post that user has searched or it will provide a user with message that there is no post under that search
- Page behaves just like post page where user can open searched posts with click on the title of the post
- There is back link that will redirect user to the previous page

<details><summary>Create recipe page</summary>
<img src="readme/documentation/features/admin_recipe_create/create_recipe.png">
<img src="readme/documentation/features/admin_recipe_create/require_title.png">
<img src="readme/documentation/features/admin_recipe_create/require_author.png">
<img src="readme/documentation/features/admin_recipe_create/require_ingredients.png">
<img src="readme/documentation/features/admin_recipe_create/require_instructions.png">
<img src="readme/documentation/features/admin_recipe_create/require_image_alt.png">
<img src="readme/documentation/features/admin_recipe_create/require_category.png">
</details>

### Edit recipe page
- Use can only get to this page by inputing something on the search bar in the post page
- This page will either display a post that user has searched or it will provide a user with message that there is no post under that search
- Page behaves just like post page where user can open searched posts with click on the title of the post
- There is back link that will redirect user to the previous page

<details><summary>Edit recipe page</summary>
<img src="readme/documentation/features/admin_recipe_edit/edit_recipe.png">
<img src="readme/documentation/features/admin_recipe_edit/require_title.png">
<img src="readme/documentation/features/admin_recipe_edit/require_author.png">
<img src="readme/documentation/features/admin_recipe_edit/require_ingredients.png">
<img src="readme/documentation/features/admin_recipe_edit/require_instructions.png">
<img src="readme/documentation/features/admin_recipe_edit/require_image_alt.png">
<img src="readme/documentation/features/admin_recipe_edit/require_category.png"></details>

### Delete recipe page
- Use can only get to this page by inputing something on the search bar in the post page
- This page will either display a post that user has searched or it will provide a user with message that there is no post under that search
- Page behaves just like post page where user can open searched posts with click on the title of the post
- There is back link that will redirect user to the previous page

<details><summary>Delete recipe page</summary>
<img src="readme/documentation/features/admin_recipe_delete/test_recipe.png">
<img src="readme/documentation/features/admin_recipe_delete/delete_test_recipe.png">
<img src="readme/documentation/features/admin_recipe_delete/test_recipe_deleted.png">
</details>

### Login page
- Login page is a basic django allauth form that has 2 input fields for username and password with sign in the button below it
- A User also have description links to either signup for the website if he doesnt have an account or to reset his password which will redirect a user either to the "Password change page" or "Sign up" page

<details><summary>Login page</summary>
<img src="readme/documentation/features/login/login.png">
<img src="readme/documentation/features/login/no_username.png">
<img src="readme/documentation/features/login/no_password.png">
<img src="readme/documentation/features/login/wrong_username.png">
<img src="readme/documentation/features/login/wrong_password.png">
<img src="readme/documentation/features/login/sucessful_login.png">
</details>

### Logout page
- Login page is a basic django allauth form that has 2 input fields for username and password with sign in the button below it
- A User also have description links to either signup for the website if he doesnt have an account or to reset his password which will redirect a user either to the "Password change page" or "Sign up" page

<details><summary>Logout page</summary>
<img src="readme/documentation/features/logout/logout.png">
<img src="readme/documentation/features/logout/logged_out.png">
</details>

### Signup page
- The signup page is also a standard django form with all required fields for a user to input
- User must input all information (username, first name, last name, email and password) 
- After inputting all the fields and clicking sign-up button user will be automatically logged in and redirected to the home page.

<details><summary>Sign up page</summary>
<img src="readme/documentation/features/signup/signup.png">
<img src="readme/documentation/features/signup/require_username.png">
<img src="readme/documentation/features/signup/require_password.png">
<img src="readme/documentation/features/signup/require_password_again.png">
<img src="readme/documentation/features/signup/password_errors1.png">
<img src="readme/documentation/features/signup/password_errors2.png">
<img src="readme/documentation/features/signup/sucessful_signup.png">
</details>


## Future Features
<details><summary>Future features</summary>
<img src="readme_img/page_screen/future.png">
</details>

- There are 3 features that I would like to implement in the next iteration that would improve user experience and attract more traffic to my website
- Create a gallery page
- Allow users to create their posts (CRUD)
- Create a booking system for adventures


## Technologies Used
- [Balsamiq](https://en.wikipedia.org/wiki/Balsamiq) was used to create the wireframes.
- [LucidChart](https://www.lucidchart.com/pages/) was used to design the database schema.
- [HTML](https://en.wikipedia.org/wiki/HTML) was used for the mark up.
- [CSS](https://en.wikipedia.org/wiki/CSS)  was used to style the site.
- [Django](https://www.djangoproject.com/) was the framework that was used.
- [Python](https://en.wikipedia.org/wiki/Python_(programming_language)), django is a python framework.
- [JavaScript](https://en.wikipedia.org/wiki/JavaScript) was used for interactiveness with the messages.
- [Gitpod](https://www.gitpod.io/about) was used to create this site and then push everything to github.
- [Heroku](https://en.wikipedia.org/wiki/Heroku) is used to host this site.
- [Github](https://en.wikipedia.org/wiki/GitHub) was used to store the code.
- [Git](https://en.wikipedia.org/wiki/Git) was used for version control.
- [Cloudinary](https://cloudinary.com/) was used to store the images.
- [ElephantSQL](https://www.elephantsql.com/) was used to store the database.
- - -

## Libraries
- asgiref - A standard Python library to allow for asynchronous web apps and servers to communicate with each other.
- cloudinary - A Python package allowing integration between the application and Cloudinary.
- coverage - is a third-party package that helps developers measure code coverage in their Python codebase.
- dj-database-url - A Django utility to utilise the DATABASE_URL environment variable to configure the Django application. Used with PostgreSQL.
- dj3-cloudinary-storage - A Django package that facilitates integration with Cloudinary storage.
- Django - A python package for the Django framework.
- django-active-link - A Django package used to highlight an active link in the site navigation bars.
- django-allauth - An integrated set of Django applications addressing user authentication, registration and account management.
- django-summernote - is a third-party package that provides a rich text editor widget for Django web applications.
- django-crispy-forms - A Django package that provides tags and filters to control the rendering behaviour of Django forms. 
- gunicorn - A Python WSGI HTTP Server for UNIX.
- oauthlib - A generic, spec-compliant, thorough implementation of the OAuth request-signing logic for Python 3.6+.
- psycopg2 - A PostgreSQL database adapter for Python.
- PyJWT - A Python library that allows for encoding and decoding of JSON Web Tokens (JWT).
- python3-openid - A set of Python packages to support use of the OpenID decentralized identity system.
- pytz - A Python package for world timezone definitions, modern and historical.
- Pillow - A Python Imaging Library adds image processing capabilities
- requests-oauthlib - A Python package for OAuthlib authentication support for Requests.
- sqlparse - A non-validating SQL parser for Python.

## Testing
The testing section can be found [here](TESTING.md).

## Bugs
| **Bug** | **Fix** |
| ----------- | ----------- |
| On home page hero image was not rendering on deployed site| Created new file path directly to Cloudinary |
| Post page was not displaying| Change path in urls.py to post/ |
| Admin page have no style | Set DEBUG to True|
| Locally reset password email not working| Implemented if else statemEnt for DEVELOPMENT in settings.py for email part|
| No css style on Heroku | Before every deployment set debug to false and run "python3 manage.py collectstatic" |
| Deployment issue on Heroku multiple times error "etag" & error collectstatic | Deleted all Cloudinary files and pushed code again |
| Password reset & password confirm templates not rendering, displayed django templates | Renamed templates from django documentation |
| After signing up user was not logged in automatically | Changed registration function and added extra code to store data from user and use it to login automatically |
| Profile model information was not updating with the user model on the profile page| Combined 2 forms into 1 function |
| The user image was not uploading| Added code in the form = 'enctype="multipart/form-data"'|
| No css styles on heroku| Add ',' in settings.py 'STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static'),]'|
| No css styles on heroku| Deleted all static files in Cloduinary|
| No searched posts displayed on search page | replaced {% if post in posts %} with {% if posts %} statemant and placed it outside div |
| Profile picture/ form was not saving properly | Deleted 'username' from form fields in forms.py as I took it out from the template earlier so my form was not validating properly as it was searhing for that username |

### Unresolved bugs and issues
| **Bug** | **Fix** |
| ----------- | ----------- |
| Post image must be certain size in order to match other posts box sizes | X |
| Uploaded user picture can looked stretch depends on the upload height and width | X |
| Google map with hiking locations shows error message that "Page can't load Google maps correctly", the map and cluster locations are working though | X |
| In dev tools in console I'm getting 2 errors. First is for self clossing messages accross webstie, and second one is for dissapering text on the index page, both are workin as expected | X |

<details><summary>Console issues</summary>
<img src="readme_img/test/issues.png">
</details>

## Deployment
This website is deployed to Heroku from a GitHub repository, the following steps were taken:

#### Creating Repository on GitHub
- First make sure you are signed into [Github](https://github.com/) and go to the code institutes template, which can be found [here](https://github.com/Code-Institute-Org/gitpod-full-template).
- Then click on **use this template** and select **Create a new repository** from the drop-down. Enter the name for the repository and click **Create repository from template**.
- Once the repository was created, I clicked the green **gitpod** button to create a workspace in gitpod so that I could write the code for the site.

#### Creating an app on Heroku
- After creating the repository on GitHub, head over to [heroku](https://www.heroku.com/) and sign in.
- On the home page, click **New** and **Create new app** from the drop down.
- Give the app a name(this must be unique) and select a **region** I chose **Europe** as I am in Europe, Then click **Create app**.

#### Create a database On ElephantSQL
- Log into the [ElephantSQL](https://www.elephantsql.com/) website and click **Create new Instance**
- Enter a **Name** and keep the plan as **Tiny Turtle Free**, then **tags** field can be left blank, Select a region closest to you, I selected **EU-West-1(Ireland)** as I'm in Ireland. Then click **Review** and afterward click **create an instance**.
- On The Dashboard click on your database instance name.
- You will see the details for your database instance, in the URL section click on the copy icon to copy the database URL.
- Head over to gitpod and create a **Database URL** environment variable in your env.py file and set it equal to the copied URL.

#### Deploying to Heroku.
- Head back over to [heroku](https://www.heroku.com/) and click on your **app** and then go to the **Settings tab**
- On the **settings page** scroll down to the **config vars** section and enter the **DATABASE_URL** which you will set equal to the elephantSQL URL, create **Secret key** this can be anything,
**CLOUDINARY_URL** this will be set to your cloudinary url and finally **Port** which will be set to 8000.
- Then scroll to the top and go to the **deploy tab** and go down to the **Deployment method** section and select **Github** and then sign into your account.
- Below that in the **search for a repository to connect to** search box enter the name of your repository that you created on **GitHub** and click **connect**
- Once it has been connected scroll down to the **Manual Deploy** and click **Deploy branch** when it has deployed you will see a **view app** button below and this will bring you to your newly deployed app.
- Please note that when deploying manually you will have to deploy after each change you make to your repository.
- - -

## Credits
- [Stack Overflow](https://stackoverflow.com/) is probably a developer's best resource, this provided me with many answers to my questions.
  Examples of code I found on slack that helped me with coding:
    'def __init__(self, *args, **kwargs):
        super(FormUser, self).__init__(*args, **kwargs)
        for field in ["username", "email", "password1", "password2"]:
            self.fields[field].help_text = None'
  Also found similar solution on how to combine 2 forms into 1 (in my case User & Profile form)
- [W3schools](https://www.w3schools.com/) this was great for looking up forgotten **CSS** syntax and how to use it.
- [Unsplash](https://unsplash.com/) all images were taken from Unsplash.
- [CodeInstitute](https://learn.codeinstitute.net/) for their walkthrough project, which guided me with website build especially for publishing posts, comments and likes section which I code along with the video with few adjustments
- [AllTrails](https://www.alltrails.com/) for providing me some text and useful information for my posts
- [youtube](https://www.youtube.com/) videos from **codemy**, **netninja**, **veryacademy**, **djangolessons** and **ProgrammingWithJosh** channels for guidance and examples on how to create blog and improve website. I watch videos and tried to recreate some features accross my website such as 'search-box' & 'subscription', specific links could be found here
[codemy](https://www.youtube.com/watch?v=B40bteAMM_M&list=PLCC34OHNcOtr025c1kHSPrnP18YPB-NFi&ab_channel=Codemy.com)
[netninja](https://www.youtube.com/watch?v=n-FTlQ7Djqc&list=PL4cUxeGkcC9ib4HsrXEYpQnTOTZE1x0uc&ab_channel=TheNetNinja)
[veryacademy](https://www.youtube.com/watch?v=k_RY1og4Zj0&list=PLOLrQ9Pn6cawWd-5UZM6CIm0uqFXeBcTd&ab_channel=VeryAcademy)
[techwithtime](https://www.youtube.com/watch?v=Z4D3M-NSN58&list=PLzMcBGfZo4-kQkZp-j9PNyKq7Yw5VYjq9&ab_channel=TechWithTim)
[ProgrammingWithJosh](https://www.youtube.com/watch?v=rHux0gMZ3Eg&ab_channel=ProgrammingwithMosh)
- [Allauth](https://django-allauth.readthedocs.io/en/latest/) for their documentation which was helpfull in creating user authentication
- [Logoapp](https://logo.com/) for providing me with tools to easier generate my idea and create logo
- [Djangoforbeginners](https://djangoforbeginners.com/) for providing useful information abut basic concepts and setup for django
- [DEV community](https://dev.to/) for helping me to setup email with django
- [Traversy media](https://www.traversymedia.com/) for providing me with the code for dissapering hero text
- [Lucidchart](https://lucid.app/) for providing me with tools to create my database system
- [Balsamic](https://balsamiq.com/wireframes/) was used to create wireframes

## Acknowledgements:
- I would like to thank my mentor Narander Singh for all his help throughout the project and guidance in general
- I would like to thank Code Institutes Slack Community, and tutor support as this helped me so much when I got stuck on part of my project
- I would also like to thank our cohort facilitator Irene Neville, for answering any course-related questions I asked and for providing us with weekly guidance information about the project
- Last but not least I would like to thank fellow colleague Mark Fenton for helping me with debugging my code and general advices

[Back to the top](#take-a-hike)