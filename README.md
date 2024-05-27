# **HealthifyZone - Portfolio Project 4**

HealthifyZone is a blog where people who would like to improve their lifestyle can come and find a lot of useful things. Some of them are articles about yoga and exercise. Users can sign up, leave comments, and like and dislike the comments of other users, as well as like and dislike articles. Users can also look for recipes, ingredients and preparation steps as well as see other users' profiles.

[Live link to website](https://healthifyzone-8c9a32d8f968.herokuapp.com/)

## **Contents**

- [HealthifyZone](#healthifyzone---portfolio-project-4)
  - [Contents](#contents)
  - [UX](#ux)
    - [Color Scheme](#colour-scheme)
    - [Typography](#typography)
  - [User Stories](#user-stories)
    - [Users](#users)
    - [Site Admin](#site-admin)
  - [Wireframes](#wireframes)
  - [Existing Features](#existing-features)
  - [Future Features](#future-features)
  - [Technologies Used](#technologies-used)
  - [Database Design](#database-design)
    - [Entity Relationship Diagram](#entity-relationship-diagram)
  - [Agile Development](#agile-development)
  - [Testing](#testing)
  - [Deployment](#deployment)
    - [ElephantSQL Database](#elephantsql-database)
    - [Cloudinary API](#cloudinary-api)
    - [Spoonacular API](#spoonacular-api)
    - [Deployment on Heroku](#deployment-on-heroku)
    - [Local Deployment](#local-deployment)
      - [How to Fork](#how-to-fork)
      - [How to Clone](#how-to-clone)
   - [Credits](#credits)
   - [Acknowledgements](#acknowledgements)

## **UX**

For the colors, I decided to keep it thematic and mainly stick with different shades of green, as green has been linked with growth, vitality, and overall well-being, as well as being soothing to the eyes, which in turn will help with the UX.

### **Colour Scheme**

I am using [Coolors.co](https://coolors.co/dff8df-1e4607-529929-76d176-6aad6a-333333-800080-fd5a5a-a89f9f) to showcase the color scheme of the website.

![Colour Scheme](https://github.com/devnickocodes/healthifyzone/blob/main/documentation/healthifyzone_color_scheme.png)

### **Typography**

I imported the font for the website from [Google Fonts](https://fonts.google.com/specimen/Inter) and I used the Inter font as the main font.

![Typography - Inter](https://github.com/devnickocodes/healthifyzone/blob/main/documentation/website_font.png)

## **User Stories**

### Users

- As a Site User I can click on the Categories tab in the navigation bar so that I can decide which one contains articles that might be relevant to me.
- As a Site User I can click on a category so that I can see what articles it contains.
- As a Site User I can view information about the categories so that I can see who created them and when they were created.
- As a Site User I can click on the category's author's username so that I can navigate to the author's profile page for more information about them.
- As a Registered Site User I can add a blog post so that I can contribute to the community.
- As a Site User I can see a paginated list of posts so that I can easily browse through them and access relevant content.
- As a Site User I can click on a blog post so that I can see the full article.
- As a Registered Site User I can click on the blog post's author's username so that I can navigate to the author's profile page for more information about them.
- As a Registered Site User I can comment on posts so that I can be a part of the conversation.
- As a Registered Site User I can I want to be able to Like or Unlike blog posts, so that I can express my appreciation for valuable content.
- As a Registered Site User I can Like or Unlike comments so that I can express my appreciation for valuable contributions.
- As a Registered Site User I can delete my own blog posts so that I can maintain control over my content and remove outdated or irrelevant posts.
- As a Registered Site User I can delete my own comments so that I can maintain control over my contributions and remove any inappropriate or outdated comments.
- As a Registered Site User I can update my comment so that I can fix any potential typos or change of mind.
- As a New Site User I can see a registration form so that I can create my account.
- As a New Site User I can verify my email address so that I can activate my account.
- As a Site User I can see appropriate error messages if my login attempt fails so that I can understand why the login failed and take corrective action if necessary.
- As a Site User I can choose the option to stay logged in after closing the browser so that I don't have to input my credentials everytime.
- As a Site User I can reset my password so that I don't have to create a new account.
- As a Site User I can log out of my account so that I can protect my privacy and secure my account when I'm done using the website.
- As a Site User I can choose to log in with my email instead of my username so that I can easily access my account using a method that I prefer.
- As a Site User I can see a paginated list of the already sorted articles by category so that I can navigate through the articles more easily
- As a Registered User I can click on My Profile tab so that I can view my profile information
- As a Registered User I can upload my own profile picture so that I can personalize my profile.
- As a Registered User I can edit my profile so that I can keep my profile information up-to-date and accurate.
- As a Site User I can search for recipes so that I can find healthy dishes.
- As a Site User I can click on the recipe so that I can see the necessary ingredients and the preparation instructions.
- As a Site User I can click on the About tab so that I can better understand the purpose of the website.
- As a Site User I can sign up to the website so that I can receive the full benefits of the website
- As a Registered User I can edit my comments so that I can ensure they accurately reflect the information I want to convey.
- 

### Site Admin

- As a Site Admin I can approve or disapprove comments so that I can monitor the comments' sections.
- As a Site Admin I can Delete Blog Posts so that I can monitor the blog's content.
- As a Site Admin I can delete comments on the website so that I can remove inappropriate or spam comments.
- As a Site Admin I can I can create, read, update and delete posts so that I can decide what content I can upload to the website.

## **Wireframes**

The wireframes were created with [Balsamiq's Website](https://balsamiq.com/).

- **Home Page Wireframe**

![Homepage wireframe](https://github.com/devnickocodes/healthifyzone/blob/main/documentation/homepage_wireframe.png)

- **Categories Wireframe**

![Category wireframe](https://github.com/devnickocodes/healthifyzone/blob/main/documentation/categories_wireframe.png)

- **Recipe Search Wireframe**

![Recipe Search wireframe](https://github.com/devnickocodes/healthifyzone/blob/main/documentation/recipe_search_wireframe.png)

- **Recipe Results Wireframe**

![Recipe Results wireframe](https://github.com/devnickocodes/healthifyzone/blob/main/documentation/recipe_results_wireframe.png)

- **View Recipe Details Wireframe**

![View Recipe Details wireframe](https://github.com/devnickocodes/healthifyzone/blob/main/documentation/view_recipe_wireframe.png)

- **View Recipe Details Wireframe**

![View Recipe Details wireframe](https://github.com/devnickocodes/healthifyzone/blob/main/documentation/view_recipe_wireframe.png)

- **View Article Wireframe**

![View Article wireframe](https://github.com/devnickocodes/healthifyzone/blob/main/documentation/view_article_wireframe.png)

- **View Article by Category Wireframe**

![Article by Category wireframe](https://github.com/devnickocodes/healthifyzone/blob/main/documentation/articles_by_category.png)

- **Create Article Wireframe**

![Create Article Wireframe](https://github.com/devnickocodes/healthifyzone/blob/main/documentation/create_article_wireframe.png)

- **Edit Article Wireframe**

![Edit Article Wireframe](https://github.com/devnickocodes/healthifyzone/blob/main/documentation/edit_article_wireframe.png)

- **Delete Article Wireframe**

![Delete Article Wireframe](https://github.com/devnickocodes/healthifyzone/blob/main/documentation/delete_article_wireframe.png)

- **Profile Wireframe**

![Profile wireframe](https://github.com/devnickocodes/healthifyzone/blob/main/documentation/profile_wireframe.png)

- **Sign Up Wireframe**

![Sign Up wireframe](https://github.com/devnickocodes/healthifyzone/blob/main/documentation/sign_up_wireframe.png)

- **Log In Wireframe**

![Log In wireframe](https://github.com/devnickocodes/healthifyzone/blob/main/documentation/login_wireframe.png)


- **Log Out Wireframe**

![Log Out wireframe](https://github.com/devnickocodes/healthifyzone/blob/main/documentation/logout_wireframe.png)

### Existing Features

- **Navbar**

    - The navbar can be seen on every page of the website it includes links to the main pages of the site.

![Navbar](https://github.com/devnickocodes/healthifyzone/blob/main/documentation/navbar.png)

- **Footer**

    - The footer can also be found on each page of the website and it contains information about me as the developer as well as a link to my GitHub page.

![Footer](https://github.com/devnickocodes/healthifyzone/blob/main/documentation/footer.png)

- **Homepage**

    - The landing page contains previews for each article of the blog and pagination buttons for "NEXT" and "PREV".

![Homepage](https://github.com/devnickocodes/healthifyzone/blob/main/documentation/landing_page.png)

- **Article Preview (logged out user)**

    - Each preview consits of the article's title, subtitle, date of creation and link to the author's profile page as well as "View Article" button.

![Article Preview (logged out user)](https://github.com/devnickocodes/healthifyzone/blob/main/documentation/article_preview.png)

- **Article Preview (logged in user that is owner of the article)**

    - Along with the rest of the features the logged in owner of the article can see two additional options. A "Delete Article" button and an "Edit Article" button.

![Article Preview (logged in user that is owner of the article)](https://github.com/devnickocodes/healthifyzone/blob/main/documentation/article_preview_logged_in_owner_of_article.png)

- **Delete Article Button**

    - The "Delete Article" button will take the user to a page where they would need to confirm the deletion of the article.

![Delete Article Button](https://github.com/devnickocodes/healthifyzone/blob/main/documentation/article_delete_button.png)

- **Delete Article Page**

    - When the owner of the article clicks on the "Delete Article" button the user will be taken to a page where they would need to confirm the deletion of the article.

![Delete Article Page](https://github.com/devnickocodes/healthifyzone/blob/main/documentation/delete_article_page.png)


- **Edit Article Button**

    - The "Edit Article" button will take the user to a page where they will be able to edit/update their article.

![Edit Article Button](https://github.com/devnickocodes/healthifyzone/blob/main/documentation/article_edit_button.png)

- **Edit Article Page**

    - When the owner of the article clicks on the "Edit Article" button the user will be taken to a page with a form for updating the article with prefilled input fields.

![Edit Article Page](https://github.com/devnickocodes/healthifyzone/blob/main/documentation/edit_article_page.png)

- **Article Author Profile Link**

    - The link to the article's author's profile page will only work for logged in users, if they are not logged in they will be taken to the log in page.

![Article Author Profile Link](https://github.com/devnickocodes/healthifyzone/blob/main/documentation/article_author_link.png)

- **View Article Button**

    - The "View Article" button will take the user to the full page for that article.

![View Article Button](https://github.com/devnickocodes/healthifyzone/blob/main/documentation/view_article_button.png)

- **Pagination Button (NEXT)**

    - The "NEXT" pagination button will take the user to the next page.

![Pagination Button (NEXT)](https://github.com/devnickocodes/healthifyzone/blob/main/documentation/pagination_button_next.png)

- **Pagination Button (PREV)**

    - The "PREV" pagination button will bring back the user to the previous page.

![Pagination Button (PREV)](https://github.com/devnickocodes/healthifyzone/blob/main/documentation/pagination_button_prev.png)

- **View Article (complete article page)**

    - When the user clicks the "View Article" button they will be taken to this page where they will be able to read the whole article as well as comment, like other users' comments, visit their profiles, visit the article's owner's profile from the lni and like the article itself.

![View Article (complete article page)](https://github.com/devnickocodes/healthifyzone/blob/main/documentation/view_article_page.png)

- **Article Author Profile Link (Individual Article Page)**

    - The functionality is the same for this link as with the one on the landing page.

![View Article (complete article page)](https://github.com/devnickocodes/healthifyzone/blob/main/documentation/article_author_link.png)

- **Article/Comment Like Button (that's not active)**

    - The user can like the article as long as they are logged in, if they are not they will be shown a messaged that will let them know that they have to be logged in.

![Article/Comment Like Button (that's not active)](https://github.com/devnickocodes/healthifyzone/blob/main/documentation/like_button_not_active.png)

- **Article/Comment Like Button (active)**

    - When the user clicks the like button the heart will turn purple indicating that the user's like for this article or comment is active.

![Article/Comment Like Button (that's not active)](https://github.com/devnickocodes/healthifyzone/blob/main/documentation/active_like_button_by_logged_in_user.png)

- **Comment Section (not logged in user or user not owner of comment)**

    - The comment section shows the username of the comment's author, date of creation and the comment itself.

![Comment Section (not logged in user or user not owner of comment)](https://github.com/devnickocodes/healthifyzone/blob/main/documentation/comment_section_not_logged_in_logged_out.png)

- **Comment Section (logged in owner of comment)**

    - For the logged in user that is the author of the comment, they can see two additional options. "Edit" and "Delete", which will allow them to edit/update their comment or delete it respectively.

![Comment Section (logged in owner of comment)](https://github.com/devnickocodes/healthifyzone/blob/main/documentation/delete_comment_confirm.png)

- **Leave Comment Button (not logged in user)**

    - If a non logged in user tries to leave a comment they will be shown a message letting them know that they will need to sign up or log in in order to leave a comment, with links to the necessary pages.

![Leave Comment Button (not logged in user)](https://github.com/devnickocodes/healthifyzone/blob/main/documentation/leave_comment_button_not_logged_in_user.png)

- **Leave Comment Button (logged in user)**

    - If a logged in user tries to leave a comment they will be provided with a form that they will need to fill in order for their comment to be send out for approval. The same form will be used when a user wants to edit their comment.

![Leave Comment Button (logged in user)](https://github.com/devnickocodes/healthifyzone/blob/main/documentation/leave_comment_button_logged_in_user.png)

- **Comment Awaiting Approval**

    - When the user submits a comment, until it is approved only the logged in owner of the comment will be able to see the comment and that it is waiting for approval.

![Comment Awaiting Approval](https://github.com/devnickocodes/healthifyzone/blob/main/documentation/comment_awaiting_approval.png)

- **Categories Page**

    - When the user lands on the page they can find what categories the articles are grouped in.

![Categories Page](https://github.com/devnickocodes/healthifyzone/blob/main/documentation/category_page.png)

- **Categories Preview**

    - For each of the categories there is a preview with title, subtitle, date of creation as well as a link to the author's profile page and a "View Category" button.

![Categories Preview](https://github.com/devnickocodes/healthifyzone/blob/main/documentation/category_preview.png)

- **View Category Button**

    - When the user clicks the "View Category" button they will be take to a page consisting of all the articles related to this category.

![View Category Button](https://github.com/devnickocodes/healthifyzone/blob/main/documentation/view_category_button.png)

- **View Articles Related to a Category**

    - On this page the user can see all articles related to the category that they have clicked on.

![View Category Button](https://github.com/devnickocodes/healthifyzone/blob/main/documentation/articles_related_to_a_category.png)

- **Recipe Search Page**

    - On this page the user can search for recipes based on a keyword of their choosing.

![View Category Button](https://github.com/devnickocodes/healthifyzone/blob/main/documentation/search_recipes_page.png)

- **Recipe Results Page**

    - On this page depending on what the user has searched for, nine recipes will be displayed that the user can choose from.

![Recipe Results Page](https://github.com/devnickocodes/healthifyzone/blob/main/documentation/search_recipes_results_page.png)

- **View Recipe Button**

    - For each one of the recipes there will be a "View Recipe" button that when clicked the user will be taken to a page that will contain more information about the recipe.

![View Recipe Button](https://github.com/devnickocodes/healthifyzone/blob/main/documentation/view_recipe_button.png)

- **View Recipe Button**

    - For each one of the recipes there will be a "View Recipe" button that when clicked the user will be taken to a page that will contain more information about the recipe.

![View Recipe Button](https://github.com/devnickocodes/healthifyzone/blob/main/documentation/view_recipe_button.png)

- **Recipe Card Page**

    - Upon clicking on the "View Recipe" button the user will be taken to this page where they will find all the information about the recipe.

![Recipe Card Page](https://github.com/devnickocodes/healthifyzone/blob/main/documentation/recipe_card_page.png)

- **Recipe Prep Time and Servings**

    - The first thing that the user will see is the feature image for the recipe as well as the preparation time and the servings size.

![Recipe Card Page](https://github.com/devnickocodes/healthifyzone/blob/main/documentation/recipe_prep_time_servings_and_image.png)


- **Recipe Ingredients**

    - Followed by the ingredients necessary for this recipe.

![Recipe Ingredients](https://github.com/devnickocodes/healthifyzone/blob/main/documentation/recipe_ingredients.png)

- **Recipe Instructions**

    - Finally the user will see a dropdown "View Instructions" button that when clicked they will be provided with the instructions and steps for the preparation of the recipe.

![Recipe Instructions](https://github.com/devnickocodes/healthifyzone/blob/main/documentation/recipe_instructions.png)

- **Profile Page (own profile page)**

    - When the user navigates to their own profile page, they will see their profile picture (it will be a placeholder image if they haven't changed it), username, status, bio, first and last names if they have provided these details upon signing up, their email as well as a "Create Article" and "Settings" buttons.

![Profile Page (own profile page)](https://github.com/devnickocodes/healthifyzone/blob/main/documentation/logged_in_user_own_profile_page.png)

- **Create Article Button**

    - When the user clicks the "Create Article" button they will be taken to a page where they can create an article so it is sent for approval.

![Create Article Button](https://github.com/devnickocodes/healthifyzone/blob/main/documentation/create_article_button.png)

- **Settings Button**

    - When the user clicks the "Settings" dropdown button a profile update form will be shown so they can edit their profile information.

![Settings Button](https://github.com/devnickocodes/healthifyzone/blob/main/documentation/profile_settings_button.png)

- **Profile Update Form**

![Profile Update Form](https://github.com/devnickocodes/healthifyzone/blob/main/documentation/profile_update_form.png)

- **Profile Page (another user's profile page)**

    - This is the page where the user will be taken if they have clicked on the author's profile link from the article, categories or the comments. The page displays the other user's profile picture, username, status, first and last name if it was provided upond signing up.

![Profile Page (another user's profile page)](https://github.com/devnickocodes/healthifyzone/blob/main/documentation/logged_in_user_not_own_profile_page.png)

- **Sign Up Page**

    - Here the user can create their account by typing in their first name, last name, username, email, and two times the password for confirmation. Their fitness proficiency status will be assigned as 'Beginner' innitially, which they can easily change from the profile page. 

![Sign Up Page](https://github.com/devnickocodes/healthifyzone/blob/main/documentation/sign_up_page.png)

- **Already Have an Account Link**

    - If the user has entered this page on accident and they have an account they can click on sign in next to Already have an account? and log in easily.

![Already Have an Account Link](https://github.com/devnickocodes/healthifyzone/blob/main/documentation/already_have_an_account_link.png)

- **Log In Page**

    - On this page the user can log in into their account by providing a username and a password 

![Log In Page](https://github.com/devnickocodes/healthifyzone/blob/main/documentation/log_in_page.png)

- **Remember Me Checkbox**

    - If the user would like to remain signed in they can check the "Remember Me" Checkbox.

![Remember Me Checkbox](https://github.com/devnickocodes/healthifyzone/blob/main/documentation/remember_me_checkbox.png)

- **Password Reset Link**

    - If the user has forgotten their password they can easily click on the forgot my password link, after which they would have to provide the email with which they have signed up and if it matches they will receive a password reset link.

![Password Reset Link](https://github.com/devnickocodes/healthifyzone/blob/main/documentation/forgotten_password_link.png)

- **Log In Page Sign Up Link**

    - If the user has entered this page on accident and they don't have an account they can click on the sign up link and create an account.

![Log In Page Sign Up Link](https://github.com/devnickocodes/healthifyzone/blob/main/documentation/log_in_page_sign_up_link.png)

- **Error Pages**

    - If a user lands on a page that they don't have access to or doesn't exist they will be taken to an error page with the option to go back to the homepage.

## **Future Features**

- The following are things that I would like to add in the future:

    - Sign Up with email verification.
    - Add an 'About Me' page.
    - Add the option for the user to log in with an email.
    - Add a follow/unfollow functionality.
    - Add personal messages between users.

## **Technologies Used**

- [HTML5](https://developer.mozilla.org/en-US/docs/Glossary/HTML)
- The structure of the website was created with HTML5.
- [CSS3](https://developer.mozilla.org/en-US/docs/Web/CSS)
- The styling of the website was created with CSS3.
- [Bootstrap](https://getbootstrap.com/)
- Used as fron-end CSS framework for pre-built components.
- [JavaScript](https://developer.mozilla.org/en-US/docs/Web/JavaScript)
- Used for AJAX functions for the likes of articles and comments, checking of user uploaded image sizes and notifying the user if they have uploaded an image that is too large, messages timeout as well as the update and delete of comments.
- [Python](https://www.python.org) 
- Used as the back-end programming language.
- [Font Awesome](https://fontawesome.com/)
- The icons of the website were imported from Font Awesome.
- [Google Fonts](https://fonts.google.com/)
- The Inter font was imported from Google Fonts.
- [Github](https://github.com/)
- For storage of the website's code as well as deployment, Github was used.
- [Git](https://git-scm.com/)
- Git commands were used in the IDE for version control.
- [Balsamiq](https://balsamiq.com/)
- The wireframe designs for the website were created with Balsamiq.
- [Django](https://www.djangoproject.com) 
- Used as the Python framework for the site.
- [PostgreSQL](https://www.postgresql.org) 
- Used as the relational database management.
- [ElephantSQL](https://www.elephantsql.com) 
- Used as the Postgres database management.
- [Heroku](https://www.heroku.com) 
- Used for hosting the deployed website.
- [Cloudinary](https://cloudinary.com) 
- Used for online image file storage.
- [Spoonacular](https://spoonacular.com/food-api) 
- An API used for fetching recipes.
- [Gmail](https://www.google.com/gmail/about/) 
- Used for sending out password reset links.
- [CodeAnywhere](https://codeanywhere.com/signin)
- Used as an IDE to write the code for this project.
- [W3C HTML Validator](https://validator.w3.org/) 
- Used to validate the HTML code of the website.
- [W3C CSS Validator](https://jigsaw.w3.org/css-validator/) 
- Used to validate the CSS code of the website.
- [JSHint Validator](https://jshint.com/) 
- Used to validate the JavaScript code of the website.
- [CI Python Linter](https://pep8ci.herokuapp.com/) 
- Used to validate the Python code for the website

## **Database Design**

 - I created the entity relationship diagram using [draw.io](https://app.diagrams.net/). 

### Entity Relationship Diagram

![ERD](https://github.com/devnickocodes/healthifyzone/blob/main/documentation/erd_database_models.png)

## **Agile Development**

I used [GitHub Projects](https://github.com/users/devnickocodes/projects/6/views/1) as one of the Agile tools for this project. The development progress was tracked using the Kanban board.

![Project Board](https://github.com/devnickocodes/healthifyzone/blob/main/documentation/project_board.png)

Another Agile tool that was used is GitHub Issues. There I used a User Story Template to create all of my user stories.

- **Closed Issues**

![Closed Issues 1](https://github.com/devnickocodes/healthifyzone/blob/main/documentation/closed_issues_1.png)

![Closed Issues 2](https://github.com/devnickocodes/healthifyzone/blob/main/documentation/closed_issues_2.png)

- **Open Issues**

![Open Issues](https://github.com/devnickocodes/healthifyzone/blob/main/documentation/open_issues.png)

## **Testing**

You can find the testing and validation [here](TESTING.md).

## **Deployment**

### ElephantSQL Database

- To obtain your ElephantSQL database, create an accound and follow the steps below.

    - Click on "Create New Instance".
    - Pick a name of your choosing.
    - Choose the "Free" plan.
    - You can skip the tags part.
    - Select the "Region" that is closest to you.
    - Click on the name of the database where you can find your database URL.

### Cloudinary API

- To obtain your Cloudinary API key, API secret and name, create an accound and follow the steps below.

    - Navigate to the "Programmable Media" tab.
    - Navigate to the "Dashboard".
    - This is where you can find the necessary API key, secret and name.

### Spoonacular API

- To obtain your Spoonacular API key, create an accound and follow the steps below.

    - Click on "My Console".
    - Navigate to "Profile".
    - Copy your Spoonacular API.

### Deployment on Heroku

- Heroku is used for the deployment of the project, here are the steps after you create your account:

    - Click on 'New' at the top-right corner of your Dashboard, then select 'Create new app'
    - Choose a distinct app name (as no two projects can have the same name on Heroku) and choose your region
    - Click on 'Create App'
    - Navigate to 'Settings'
    - Click on 'Reveal Config Vars' to set up your environment variables.

        - The key/ value pairs are as follows.

            - CLOUDINARY_API_KEY - insert your Claudinary API key here.
            - CLOUDINARY_API_SECRET - insert your Claudinary API secret here.
            - CLOUDINARY_CLOUD_NAME - insert your Claudinary name here.
            - DATABASE_URL - inster your ElephantSQL database URL here.
            - EMAIL_HOST_PASSWORD - insert your email host password (for password reset emails)
            - GMAIL_EMAIL_ADDRESS - insert your gmail email address (for password reset emails)
            - SECRET_KEY - insert your secret key, which can by any random secret key
            - SPOONACULAR_API_KEY - insert your Spoonacular API key here.
    
    - Navigate to the 'Deploy' tab, which is on the left side of the 'Settings' tab, in the deployment method section click on GitHub
    - To connect your GitHub code to Heroku, type in the name of your repository and then click on 'Search'. Once you see your repository show up click on 'Connect'
    - Choose a branch from which you wish to deploy.
    - You can choose to deploy your app manualy in the 'Manual Deploy' section click on 'Deploy Branch'
    - If you prefer you can also choose automatic deploys, in that case navigate to the 'Automatic Deploys' section and click on 'Enable Automatic Deploys', this method keeps the project up to date with your repository.

    - Heroku requires two additional files for deployments
        
        - requirements.txt 
        - Profile

    - To install the list of dependancies used for this project which will go in your requirements.txt file you can use the following command:

        - `pip3 freeze > requirements.txt` 

    - To create the Procfile you can use the following command:

        - `echo web: node index.js > Procfile`  
    
    - Your project should now be deployed on Heroku.

### Local Deployment

- In order to run the project locally, you will need to install all the dependancies and packages from the requirements.txt file.

    - `pip3 freeze > requirements.txt` 

- You will also need to create an env.py at the root-level of the project and set up the environment v

- You can find a sample env.py file bellow:

import os

os.environ.setdefault("CLOUDINARY_API_KEY", "insert your Claudinary API key here")

os.environ.setdefault("CLOUDINARY_API_SECRET", "insert your Claudinary API secret here")

os.environ.setdefault("CLOUDINARY_CLOUD_NAME", "insert your Claudinary name here")

os.environ.setdefault("DATABASE_URL", "inster your ElephantSQL database URL here")

os.environ.setdefault("EMAIL_HOST_PASSWORD", "insert your email host password which is for password reset emails")

os.environ.setdefault("GMAIL_EMAIL_ADDRESS", "insert your gmail email address which is for password reset emails")

os.environ.setdefault("SECRET_KEY", "insert your secret key, which can by any random secret key")

os.environ.setdefault("SPOONACULAR_API_KEY", "insert your Spoonacular API key here")

- Once the project is Cloned or Forked, follow the steps below 

    - Start your Django app by typing  `python3 manage.py runserver` in the terminal.
    - Stop the already running project by doing "CTRL+C".
    - Make migrations by typing `python3 manage.py makemigrations` in the terminal.
    - Migrate to the database: `python3 manage.py migrate` in the terminal.
    - Create a superuser which will be the admin of the project by typing `python3 manage.py createsuperuser` in the terminal.
    - Start your Django app again by typing `python3 manage.py runserver` in the terminal.

#### How to Fork

- You can fork the repository, follow the steps below.

    - Sign Up or Log In if you have an account to Github.
    - Go to the repository for the HealthifyZone project - [devnickocodes/HealthifyZone Project](https://github.com/devnickocodes/healthifyzone/)
    - Click on the Fork button that is on the right side of the repository name.

#### How to Clone

- You can make a local copy of The Elements Game project by writing the following command in your IDE terminal.

    - `git clone https://github.com/devnickocodes/healthifyzone.git` 

## **Credits**

- Some of the code is inspired by [Code Institute's](https://codeinstitute.net/) I Think Therefore I Blog walkthrough project with some adjustments made.
- I learned how to impement ajax functionality and liking of comments with [this](https://www.youtube.com/watch?v=Lsxc5ok4qdU&t=1240s) video.
- I learned how to create a custom register view and user registration form with some adjustments made for the form, with [this](https://www.youtube.com/watch?v=lHYzmlx2Vso&list=PLbMO9c_jUD44i7AkA4gj1VSKvCFIf59fb&index=7&ab_channel=PythonLessons) video.
- I learned how to build the profile view function [here](https://www.youtube.com/watch?v=q5oO9XB6Vrs&list=PLbMO9c_jUD44i7AkA4gj1VSKvCFIf59fb&index=12&ab_channel=PythonLessons)
- I learned how I could use model_to_dict to convert the user model instance saved by the form into a dictionary [here](https://stackoverflow.com/questions/21925671/convert-django-model-object-to-dict-with-all-of-the-fields-intact)
- The user profile card is inspired by [this](https://bbbootstrap.com/snippets/user-profile-font-awesome-icons-43178317) Bootstrap 4 User profile with font awesome icons.
- The placeholder for the profile photo is from [pixabay](https://pixabay.com/vectors/avatar-icon-placeholder-facebook-1577909/)
- The article and category photos are from [pexels](https://www.pexels.com/).
- To tackle the 'Missing timeout argument for method 'requests.get' can cause your program to hang indefinitely' I looked into the timeout parameter and its implementation [here](https://requests.readthedocs.io/en/latest/user/quickstart/#timeouts).
- [This](https://www.youtube.com/watch?v=yVdvR7fZ0A0&ab_channel=AlinaChudnova) video helped me get started on the code for the recipes.
- I used [jQuery's](https://api.jquery.com/) API documentantion.
- I used [this](https://imageresizer.com/) image resizer and [TinyPNG](https://tinypng.com/).
- The content for the blog was gathered from the following links:
    - [helpguide](https://www.helpguide.org/articles/depression/depression-symptoms-and-warning-signs.htm)
    - [helpguide](https://www.helpguide.org/articles/healthy-living/the-mental-health-benefits-of-exercise.htm)
    - [health.harvard](https://www.health.harvard.edu/staying-healthy/yoga-benefits-beyond-the-mat)
- The favicon is from [this](https://www.flaticon.com/free-icon/leaf_257611?term=leaf&page=1&position=21&origin=search&related_id=257611) website.
- The [Spoonacular](https://spoonacular.com/food-api/docs) documentation helped me with all the veiws reagrding the recipe section.
- The logic for the user uploaded image sizes errors is from [this](https://www.youtube.com/watch?v=Af4Kc3NQ8z4&ab_channel=OpenJavaScript) video.
- The README and TESTING files' markdown is inspired by [adamgilroy22](https://github.com/adamgilroy22)

## **Acknowledgements**

- I would like to acknowledge and thank the following people.

    - Jubril Akolade - My Code Institute Mentor.
    - The Code Institute Tutor Support - For their awesome and quick technical help.
    - Thank you to everyone who took the time to use the app and give feedback.