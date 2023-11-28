# Let's Eat - Testing

[Return to the README](README.md)

## Table of Contents
- [Performance](#performance)
  - [Google's Lighthouse Performance](#googles-lighthouse-performance)
- [Browser Compatibility](#browser-compatibility)
- [Responsiveness](#responsiveness)
  - [Smaller screens](#smaller-screens)
  - [Medium screens](#medium-screens)
- [Code Validation](#code-validation)
  - [HTML Validation](#html-validation)
  - [CSS Validation](#css-validation)
  - [PEP8 Validation](#pep8-python)
  - [Javascript Validation](#javascript-validation)
- [Testing](#testing)
  - [Manual Testing](#manual-testing-bdd)
  - [Automated Testing](#automated-testing)
  - [Features Testing](#features-testing)

## Performance

### Google's Lighthouse Performance

[Google Lighthouse](https://developers.google.com/web/tools/lighthouse) was used to test the performance of the website.

#### Desktop Results:
<details><summary>Desktop</summary>
<img src="readme/documentation/performance/desktop/index.png">
<img src="readme/documentation/performance/desktop/all_recipes.png">
<img src="readme/documentation/performance/desktop/single_recipe.png">
<img src="readme/documentation/performance/desktop/comment_edit.png">
<img src="readme/documentation/performance/desktop/comment_delete.png">
<img src="readme/documentation/performance/desktop/admin_recipe_create.png">
<img src="readme/documentation/performance/desktop/admin_recipe_edit.png">
<img src="readme/documentation/performance/desktop/admin_recipe_delete.png">
<img src="readme/documentation/performance/desktop/signup.png">
<img src="readme/documentation/performance/desktop/login.png">
<img src="readme/documentation/performance/desktop/logout.png">
</details>


#### Mobile Results:
<details><summary>Mobile</summary>
<img src="readme/documentation/performance/mobile/index.png">
<img src="readme/documentation/performance/mobile/all_recipes.png">
<img src="readme/documentation/performance/mobile/single_recipe.png">
<img src="readme/documentation/performance/mobile/comment_edit.png">
<img src="readme/documentation/performance/mobile/comment_delete.png">
<img src="readme/documentation/performance/mobile/admin_recipe_create.png">
<img src="readme/documentation/performance/mobile/admin_recipe_edit.png">
<img src="readme/documentation/performance/mobile/admin_recipe_delete.png">
<img src="readme/documentation/performance/mobile/signup.png">
<img src="readme/documentation/performance/mobile/login.png">
<img src="readme/documentation/performance/mobile/logout.png">
</details>

## Browser Compatibility
|  Browser | Links  | Pages  | Responsivnes  | Form fields  |
| ------------ | ------------ | ------------ | ------------ | ------------ |
| Mozila  | Works as expected| Loading pages no issue  |  Responsivness works as expected |  Works as expected |
|  Chrome | Works as expected  |  Loading pages no issue | Responsivness works as expected  | Works as expected  |
|  Edge |  Works as expected | Loading pages no issue  | Responsivness works as expected  |  Works as expected |

## Responsiveness
|   | Iphone SE  | Galaxy A51   | iPhone12  | iPad mini  | desktop 1024px  |  desktop > 1200px | notes  |
| ------------ | ------------ | ------------ | ------------ | ------------ | ------------ | ------------ | ------------ |
|  site is responsive >= 700px |  n/a | n/a  |  n/a | Good  | Good  | Good  |   |
| site is responsive < 700px  |  Good | Good  | Good  |  n/a | n/a  |  n/a |   |
| Links/URLs work  | Yes  | Yes   | Yes   |  Yes  | Yes   | Yes   |   |
|  Images work |  Yes  |  Yes  |  Yes  | Yes   | Yes   | Yes   |   |
| Forms work  |  Yes  |  Yes  | Yes   | Yes   | Yes   | Yes   |   |

<details><summary>Smaller screens Index</summary>
<img src="readme/documentation/responsiveness/smaller_screen_index.png">
</details>
<details><summary>Smaller screens All Recipes</summary>
<img src="readme/documentation/responsiveness/smaller_screen_recipes.png">
</details>
<details><summary>Smaller screens Single Recipe</summary>
<img src="readme/documentation/responsiveness/smaller_screen_single_recipe.png">
</details>
<details><summary>Smaller screens Comments</summary>
<img src="readme/documentation/responsiveness/smaller_screen_comments.png">
</details>
<details><summary>Smaller screens Edit Comment</summary>
<img src="readme/documentation/responsiveness/smaller_screen_comment_edit.png">
</details>
<details><summary>Smaller screens Delete Comment</summary>
<img src="readme/documentation/responsiveness/smaller_screen_comment_delete.png">
</details>
<details><summary>Medium screens Create Recipe</summary>
<img src="readme/documentation/responsiveness/smaller_screen_recipe_create.png">
</details>
<details><summary>Smaller screens Edit Recipe</summary>
<img src="readme/documentation/responsiveness/smaller_screen_recipe_edit.png">
</details>
<details><summary>Smaller screens Delete Recipe</summary>
<img src="readme/documentation/responsiveness/smaller_screen_recipe_delete.png">
</details>
<details><summary>Smaller screens Signup</summary>
<img src="readme/documentation/responsiveness/signup.png">
</details>
<details><summary>Smaller screens Login</summary>
<img src="readme/documentation/responsiveness/login.png">
</details>
<details><summary>Smaller screens Logout</summary>
<img src="readme/documentation/responsiveness/logout.png">
</details>


## Code Validation

### HTML Validation
The [W3C Markup Validation Service](https://validator.w3.org/) was used to validate the HTML of the website.
Only profile page, I had to copy and paste code as I couldn't test as url page. Any error that is shown in validation test is cause of the Django templates. One particular that is shown accrosss website is **username** as username is displayed on navigation bar upon user login.
 <details><summary>Index page</summary>
<img src="readme/documentation/validation/html/index.png">
</details>

<details><summary>All Recipes page</summary>
<img src="readme/documentation/validation/html/all_recipes.png">
</details>

<details><summary>Single Recipe page</summary>
<img src="readme/documentation/validation/html/single_recipe.png">
</details>

<details><summary>Edit Comment page</summary>
<img src="readme/documentation/validation/html/comment_edit.png">
</details>

<details><summary>Delete Comment page</summary>
<img src="readme/documentation/validation/html/comment_delete.png">
</details>

<details><summary>Add Recipe page</summary>
<img src="readme/documentation/validation/html/admin_recipe_create.png">
</details>

<details><summary>Edit Recipe page</summary>
<img src="readme/documentation/validation/html/admin_recipe_edit.png">
</details>

<details><summary>Delete Recipe page</summary>
<img src="readme/documentation/validation/html/admin_recipe_delete.png">
</details>

<details><summary>Signup page</summary>
<img src="readme/documentation/validation/html/signup.png">
</details>

<details><summary>Login page</summary>
<img src="readme/documentation/validation/html/login.png">
</details>

<details><summary>Logout page</summary>
<img src="readme/documentation/validation/html/logout.png">
</details>


### CSS Validation 
[Jigsaw CSS validator](https://jigsaw.w3.org/css-validator/) was used for validating the CSS stylesheet. CSS file was tested by manually copying the CSS codes into the manual input option.

<details><summary>CSS Validation</summary>
<img src="readme/documentation/validation/css/style.png">
</details>


### PEP8 Python
[PEP8 CI Python Linter](https://pep8ci.herokuapp.com/) was used to check that the Python code meets PEP8 standards.

<details><summary>Admin</summary>
<img src="readme/documentation/validation/python/admin.png">
</details>

<details><summary>Forms</summary>
<img src="readme/documentation/validation/python/forms.png">
</details>

<details><summary>Views</summary>
<img src="readme/documentation/validation/python/views.png">
</details>

<details><summary>Urls</summary>
<img src="readme/documentation/validation/python/urls.png">
</details>

<details><summary>Models</summary>
<img src="readme/documentation/validation/python/models.png">
</details>

### JavaScript Validation

<details><summary>JS</summary>
<img src="readme/documentation/validation/javascript/script.png"></details>


## Manual Testing


User Story |  Test | Pass
--- | --- | :---:
As a first-time visitor, I want to understand the purpose of the website and easily navigate through | Upon landing on the index page, I can see a big hero navigation bar with 'home' and 'post' links, and below the navigation, there is big hero image displayed with hero text. Without scrolling further I can understand the purpose of this website | &check;
As a first-time visitor I want to be able to view the posts so that I would get quick access to relevant information and get a better understanding of the content|I can easily navigate to the post page which is shown different posts about different topics/hikes. If I wish to get more information about a certain post I just have to click on the title which will redirect me to the single_post page|&check;
As a first-time visitor I want to be able to see likes and comments for the posts to get some feedback from other users| I can either see the numbers of likes and comments that are located under each post on the post page if I wish to read comments all I have to do is click on the single post and comments will be displayed on the bottom of the page |&check;
As a first-time visitor I want to be able to register an account to have more access to the website | In the navigation bar there is a button 'sign up' which will lead me to the signup page on which I have to fill in all information to register for the website | &check;
As a first-time visitor I want to be able to search posts by title name so I could get quick access to the relevant one | On the post page, there is a search bar in the top right corner, in which I can input a title/word that I'm looking for. If there is a matching word in the current posts that post will be displayed on the new page, and if not message will be displayed indicating that I should search for another word | &check;
As a first-time visitor I want to be able to subscribe to the blog so I could get relevant information about future blog posts | On the bottom of the website in the left corner of the footer there is an input field with a label that allows me to input my email address and subscribe to newsletter |&check;
As a registered user I want to be able to leave comments for posts so that I can engage with other users and leave feedback about certain posts | I can click on any post I want to comment on, and that post will be displayed on a separate page. I have to scroll down after the post's description and there is a box in which I can write my comment and submit it |&check;
As a registered user I can update or delete my comments so that have more control over my content in case of errors, and to have better engagemant with other users | If my comment already exists update and delete button should be displayed under the comment! Clicking on the update new template is displayed to update comment and after confirmation updated comment is displayed. Clicking on delete button modal is shown to the user to confirm his actions. Once deleted that comment no longer exist in the post.  |&check;
As a registered user I want to be able to like/unlike posts so that I can support certain posts without providing comments | I can click on any post I want to like or unlike, and that post will be displayed on a separate page. I have to scroll down to the end of the description and the like button will be displayed, if I already like the post that button will be colored if not I can simply click on that button and like that post |&check;
As a registered user I want to be able to update my profile information so that I could change my first name, last name, email, and password and add a profile picture, and bio | After logging in to the website I can click on the profile page in the navbar which will lead me to a profile page. Page is divided into two sections, one is displaying current information for the user and the other gives the user the option to implement CRUD functionality | &check;
As a site owner, I want to be able to create, update and delete posts so that I can control my website content. |After logging in to the admin panel of the website I can navigate myself to Post model and perform CRUD functionality for the posts| &check;
As a site owner I want to be able to approve or delete comments so that I can filter out objectionable comments | After logging in to the admin panel of the website I can navigate myself to the Comments model and from there I can pick comments which I want to approve or delete| &check;
As a site owner I want to be able to access all subscribed emails so that I could send new information related to my website | After logging in to the admin panel of the website I can navigate myself to a Subscribed model which is displayed all subscribed emails | &check;
As a site owner, I want to be able to delete users so that I can receive several benefits such as: managing my data, reducing liability & resource optimization| After logging in to the admin panel of the website I can navigate myself to Users which is Django all auth model in which are displayed all registered users, from that model I can either update or delete specific users| &check;

## Automated Testing

I have performed some automated tests for views, models and forms. I found it challenging and time consuming to complete all tests although I do understand now concept of testing and why it is important to create test cases for code. Deadline of the project cought up to me to finish this section completly.

<details><summary>Number of tests</summary>s
<img src="readme_img/test/test.png">
</details>

<details><summary>Report</summary>
<img src="readme_img/test/report.png">
</details>

## Features Testing

In addition to the other tests, I have conducted a manual checklist for different features of the website to make sure that everything is working as intended.

| Status | **Navigation Bar - User Logged Out**
|:-------:|:--------|
| &check; | Clicking the navbar logo loads the home page
| &check; | Navbar shows the nav links for Home, Post, and buttons for Sign up and Sign In
| &check; | Current page is highlighted for the user
| &check; | Clicking the Home tab on the navbar loads the home page
| &check; | Clicking the Post tab on the navbar loads the post page
| &check; | Clicking the Sign in button on the navbar loads the Sign in page
| &check; | Clicking the Signup button on the navbar loads the Signup page

<details><summary>Logout navbar</summary>
<img src="readme_img/test/navbar_logged_out.png">
</details>


| Status | **Navigation Bar - User Logged In**
|:-------:|:--------|
| &check; | User name is displayed next to the logo
| &check; | Navbar shows additional link for Profile
| &check; | Clicking the Profile tab on the navbar loads the Profile page

<details><summary>Login navbar</summary>
<img src="readme_img/test/navbar_login.png">
</details>


| Status | **Footer - User Logged Out/In**
|:-------:|:--------|
| &check; | Clicking the footer logo loads the home page
| &check; | Clicking the LinkedIn, Facebook, Youtube, and Instagram icons directs the user to relevant pages
| &check; | Subscribe input field is displayed

<details><summary>Footer</summary>
<img src="readme_img/test/footer.png">
</details>

| Status | **Subscribe field**
|:-------:|:--------|
| &check; | No input not allowed
| &check; | Only standard email characters allowed
| &check; | After submitting confirmation message is displayed to the user
| &check; | User received subscription email to the email address he provided

<details><summary>Subscribe empty</summary>
<img src="readme_img/test/subscribe.png">
</details>

<details><summary>Subscribe wrong</summary>
<img src="readme_img/test/correct_subs.png">
</details>

<details><summary>Subscribe message</summary>
<img src="readme_img/test/subscr.png">
</details>

| Status | **Home Page**
|:-------:|:--------|
| &check; | Users receive basic knowledge about the website

<details><summary>Home page</summary>
<img src="readme_img/page_screen/home1.png">
</details>

<details><summary>Home page</summary>
<img src="readme_img/page_screen/home2.png">
</details>

| Status | **Post Page**
|:-------:|:--------|
| &check; | Shows the blog posts paginated by 6 posts
| &check; | Next and previous buttons at the bottom of the page works as expected and leads user to next or prevoius page 
| &check; | Hovering on the title colour change indicating user that is clickable
| &check; | Clicking on the title user gets redirected to the single post page
| &check; | Search input field is displayed to user

<details><summary>Post page</summary>
<img src="readme_img/test/post_pagination.png">
</details>

| Status | **Search field & page**
|:-------:|:--------|
| &check; | No input is not allowed
| &check; | Search not matched to the post - user is redirected to the search page with message indicating that there is no match to searched words
| &check; | Search matches the post - user is redirected to the search page with match post displayed to the user

<details><summary>Search - no input</summary>
<img src="readme_img/test/search_wrong.png">
</details>

<details><summary>Search page no match results</summary>
<img src="readme_img/test/no_match_posts.png">
</details>

<details><summary>Search page match result</summary>
<img src="readme_img/test/searched_post.png">
</details>

| Status | **Single post Page**
|:-------:|:--------|
| &check; | Shows the full content of the post
| &check; | Shows a list of comments posted so far
| &check; | Shows a numbers of likes
| &check; | If post not liked by user like button is not colored
| &check; | When clicked like button on the post that user hasn't liked yet button will change color
| &check; | If post was liked by the user like button is colored
| &check; | When clicked like button on the post that user has liked already like button will go back to previous state/not colored
| &check; | If post not liked by user like button is not coloured
| &check; | Shows a numbers of likes
| &check; | Comment box is only visible to registered users
| &check; | Only register user can like post
| &check; | Only register user can comment post
| &check; | When post is commented, confirmation message is displayed to the user
| &check; | Under current user comment two buttons are displayed "Update" &  "Delete"
| &check; | Clickin on "Delete" button modal is shown to the user to confirm his choice
| &check; | Confirming and deleting his comment message is displayed to the user and comment has been deleted
| &check; | Clicking on "Update" button new template is beeing shown to the user with box to update his comment
| &check; | Confirming his updated comment message is displayed to the user and his updated comment

<details><summary>Post page</summary>
<img src="readme_img/page_screen/post_pg.png">
</details>

<details><summary>Comments</summary>
<img src="readme_img/test/whole_cmnt.png">
</details>

<details><summary>Approve comments</summary>
<img src="readme_img/test/approval.png">
</details>

<details><summary>CRUD Comments</summary>
<img src="readme_img/test/comments_crud.png">
</details>

<details><summary>Update comments</summary>
<img src="readme_img/test/edit_comment.png">
</details>

<details><summary>Delete comments</summary>
<img src="readme_img/test/delete_comment.png">
</details>


| Status | **Profile page**
|:-------:|:--------|
| &check; | User information is displayed to the user
| &check; | Input fields are provided for the user to change his details
| &check; | Extra fields for Bio and Image are provided
| &check; | Two buttons for update and delete profile are displayed 

<details><summary>Profile page</summary>
<img src="readme_img/test/profile.png">
</details>

| Status | **Profile page Update**
|:-------:|:--------|
| &check; | Changing any fields, or adding a picture upon clicking on the 'Update' button new information is displayed to the user
| &check; | Confirmation message is shown to the user

<details><summary>Profile page update</summary>
<img src="readme_img/test/update_profile.png">
</details>

| Status | **Profile delete**
|:-------:|:--------|
| &check; | Clicking the 'Delete' button, the modal is displayed to the user to confirm his actions
| &check; | Clicking 'Cancel' in the modal the user is redirected to the Profile page
| &check; | Clicking 'Delete' in the modal the user is redirected to the Home page
| &check; | Confirmation message is shown to the user

<details><summary>Profile page delete</summary>
<img src="readme_img/test/modal_account.png">
</details>

<details><summary>Profile page delete</summary>
<img src="readme_img/test/deleted_acc.png">
</details>

| Status | **Login page**
|:-------:|:--------|
| &check; | No input not allowed
| &check; | Messages displayed to the user in case of the username or password is not matching the information in databese
| &check; | Clickin on 'Forgot password' link redirects user to password reset page

<details><summary>Incorrect password/username</summary>
<img src="readme_img/test/incorrect password.png">
</details>


| Status | **Password change route**
|:-------:|:--------|
| &check; | Input field is displayed on the password change page for the user to provide an email to recover the password
| &check; | No input is not allowed
| &check; | Allowed only standard email input 
| &check; | 'Send me instructions' button work as expected
| &check; | After submitting user is redirected to new conformation page
| &check; | If the email matches the registered username clickable link is provided in the inbox for the user
| &check; | If the email doesn't match the registered username message is displayed to ignore that email, if not registered with the Take a hike website
| &check; | Link redirects to input new password page
| &check; | New password must pass all standard criteria
| &check; | After submitting a new password new page with conformation is displayed to the user with a link to sign in to the website

<details><summary>Forgot password link</summary>
<img src="readme_img/test/forgot_password.png">
</details>

<details><summary>Forgot password</summary>
<img src="readme_img/test/highlight.png">
</details>

<details><summary>Check email</summary>
<img src="readme_img/test/check_email.png">
</details>

<details><summary>New password</summary>
<img src="readme_img/test/new_password.png">
</details>

<details><summary>Too short password</summary>
<img src="readme_img/test/too_short_pass.png">
</details>

<details><summary>Not matching password</summary>
<img src="readme_img/test/no_match_pass.png">
</details>

<details><summary>Confirmation news password</summary>
<img src="readme_img/test/reset_complete.png">
</details>

| Status | **Logout**
|:-------:|:--------|
| &check; | Clicking on logout user is redirected to a new page asking the user to confirm his choice
| &check; | Clicking 'Sign out' user is redirected to the home page with a confirmation message displayed to the user

<details><summary>Logout</summary>
<img src="readme_img/test/logout.png">
</details>

<details><summary>Logout message</summary>
<img src="readme_img/test/message-lgo.png">
</details>


| Status | **Sign up**
|:-------:|:--------|
| &check; | Clicking on Sign up in the navigation bar new page is displayed to the user with input fields
| &check; | All input fields must be put in for the user to sign in, standard criteria for email and passwords are present
| &check; | Relevant messages are displayed to the user if a certain field doesn't match the criteria
| &check; | Upon signing up, the user is directly logged into the website 
| &check; | Prompt message is displayed to the user indicating that he has successfully signed up

<details><summary>Signup</summary>
<img src="readme/documentation/">
</details>

<details><summary>Signup form validation</summary>
<img src="readme_img/test/signup_form_v.png">
</details>

<details><summary>Login message</summary>
<img src="readme_img/test/login_msg.png">
</details>

| Status | **Back link**
|:-------:|:--------|
| &check; | Link is displayed on 2 pages 'Search post' & 'Single post'
| &check; | Clicking the 'Back' link user is redirected to the previous page


*Go back to the [top](#table-of-contents)*