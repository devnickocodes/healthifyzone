# Testing

## **HTML Validation**

As there is jinja syntax in my HTML code, simply pasting the code directly in the validator wouldn't work.
The way I have done the validation is by using the URIs from the deployed pages from Heroku.

Since some of the pages require the user to be logged in, this way of validation wouldn't work as the HTML validator doesn't have access to authentication.

For these pages I have extracted the code by right-clicking on the pages that need validation and selecting "View Page Source" and pasting the code directly in the validator.

| Page | Screenshot | PASS/FAIL |
| --- | --- | --- |
| Homepage (first validation) | ![Homepage (first validation)](https://github.com/devnickocodes/healthifyzone/blob/main/documentation/first-validation-homepage.png) | FAIL: The first validation returned a couple of errors about the button elements being descendants of the anchor tags elements |
| Homepage (second validation) | ![Homepage (second validation)](https://github.com/devnickocodes/healthifyzone/blob/main/documentation/second-validation-homepage.png) | PASS |
| Category Page | ![Category Page](https://github.com/devnickocodes/healthifyzone/blob/main/documentation/category-page-validation.png) | PASS |
| View Article Page | ![View Article Page](https://github.com/devnickocodes/healthifyzone/blob/main/documentation/view_article_page_validation.png) | PASS |
| Sign Up Page | ![Sign Up Page](https://github.com/devnickocodes/healthifyzone/blob/main/documentation/sign-up-page-validation.png) | PASS |
| Log In Page | ![Log In Page](https://github.com/devnickocodes/healthifyzone/blob/main/documentation/log_in_page_validation.png) | PASS |
| Log Out Page | ![Log Out Page](https://github.com/devnickocodes/healthifyzone/blob/main/documentation/log_out_page_validation.png) | PASS |
| Log Out Page | ![Log Out Page](https://github.com/devnickocodes/healthifyzone/blob/main/documentation/log_out_page_validation.png) | PASS |
| Recipe Search Page | ![Recipe Search Page](https://github.com/devnickocodes/healthifyzone/blob/main/documentation/recipe_search_page_validation.png) | PASS |
| Recipe Results Page | ![Recipe Results Page](https://github.com/devnickocodes/healthifyzone/blob/main/documentation/recipe_results_page_validation.png) | PASS |
| View Recipe Page | ![View Recipe Page](https://github.com/devnickocodes/healthifyzone/blob/main/documentation/recipe_details_page_validation.png) | PASS |
| Own Profile Page | ![Own Profile Page](https://github.com/devnickocodes/healthifyzone/blob/main/documentation/own_profile_page_validation.png) | PASS |
| Another User's Profile Page | ![Another User's Profile Page](https://github.com/devnickocodes/healthifyzone/blob/main/documentation/another_user_profile_page_validation.png) | PASS |
| Password Reset Page | ![Password Reset Page](https://github.com/devnickocodes/healthifyzone/blob/main/documentation/password_reset_page_validation.png) | PASS |
| Password Reset Email Sent Page | ![Password Reset Page](https://github.com/devnickocodes/healthifyzone/blob/main/documentation/password_reset_email_sent_page_validation.png) | PASS |
| Password Reset Email Link Opened Page | ![Password Reset Email Link Opened Page](https://github.com/devnickocodes/healthifyzone/blob/main/documentation/password_reset_email_opened_page_validation.png) | PASS |
| Password Reset Done Page | ![Password Reset Done Page](https://github.com/devnickocodes/healthifyzone/blob/main/documentation/password_reset_done_page_validation.png) | PASS |
| Create Article Page | ![Create Article Page](https://github.com/devnickocodes/healthifyzone/blob/main/documentation/create_article_page_validation.png) | PASS |
| Edit Article Page | ![Edit Article Page](https://github.com/devnickocodes/healthifyzone/blob/main/documentation/edit_article_page_validation.png) | PASS |
| Delete Article Page | ![Delete Article Page](https://github.com/devnickocodes/healthifyzone/blob/main/documentation/delete_article_page_validation.png) | PASS |

## **CSS Validation**



## **JavaScript Validation**

| JS File | Screenshot | PASS/FAIL |
| --- | --- | --- |
| ajax_article_likes.js | ![ajax_article_likes.js](https://github.com/devnickocodes/healthifyzone/blob/main/documentation/ajax_article_likes.js-validation.png) | PASS |
| ajax_comment_likes.js | ![ajax_comment_likes.js](https://github.com/devnickocodes/healthifyzone/blob/main/documentation/ajax_comment_likes.js-validation.png) | PASS |
| check_image_size_create_article.js | ![check_image_size_create_article.js](https://github.com/devnickocodes/healthifyzone/blob/main/documentation/check_image_size_create_article.js_validation.png) | PASS |
| check_image_size_edit_article.js | ![check_image_size_edit_article.js](https://github.com/devnickocodes/healthifyzone/blob/main/documentation/check_image_size_edit_article.js_validation.png) | PASS |
| check_image_size_profile_update.js | ![check_image_size_profile_update.js](https://github.com/devnickocodes/healthifyzone/blob/main/documentation/check_image_size_profile_update.js_validation.png) | PASS |
| comments.js | ![comments.js](https://github.com/devnickocodes/healthifyzone/blob/main/documentation/comments.js-validation.png) | PASS |
| messages_timeout.js | ![messages_timeout.js](https://github.com/devnickocodes/healthifyzone/blob/main/documentation/messages_timeout.js-validation.png) | PASS |

## **Python Validation**

| Python App/File | Screenshot | PASS/FAIL |
| --- | --- | --- |
| main app / admin.py | ![main app / admin.py](https://github.com/devnickocodes/healthifyzone/blob/main/documentation/pep8-validator-main-admin.py.png) | PASS |
| main app / forms.py | ![main app / forms.py](https://github.com/devnickocodes/healthifyzone/blob/main/documentation/pep8-validator-main-forms.py.png) | PASS |
| main app / models.py | ![main app / models.py](https://github.com/devnickocodes/healthifyzone/blob/main/documentation/pep8-validator-main-models.py.png) | PASS |
| main app / urls.py | ![main app / urls.py](https://github.com/devnickocodes/healthifyzone/blob/main/documentation/pep8-validator-main-urls.py.png) | PASS |
| main app / views.py | ![main app / views.py](https://github.com/devnickocodes/healthifyzone/blob/main/documentation/pep8-validator-main-views.py.png) | PASS |
| recipe app / urls.py | ![recipe app / urls.py](https://github.com/devnickocodes/healthifyzone/blob/main/documentation/pep8-validator-recipe-urls.py.png) | PASS |
| recipe app / views.py | ![recipe app / views.py](https://github.com/devnickocodes/healthifyzone/blob/main/documentation/pep8-validator-recipe-views.py.png) | PASS |
| healthifyzone / urls.py | ![healthifyzone / urls.py](https://github.com/devnickocodes/healthifyzone/blob/main/documentation/pep8-validator-project-urls.py.png) | PASS |
| healthifyzone / settings.py | ![healthifyzone / settings.py](https://github.com/devnickocodes/healthifyzone/blob/main/documentation/pep8-validator-project-settings.py.png) | PASS | 
| users app / admin.py | ![users app / admin.py](https://github.com/devnickocodes/healthifyzone/blob/main/documentation/pep8-validator-users-admin.py.png) | PASS |
| users app / forms.py | ![users app / forms.py ](https://github.com/devnickocodes/healthifyzone/blob/main/documentation/pep8-validator-users-forms.py.png) | PASS |
| users app / models.py | ![users app / models.py](https://github.com/devnickocodes/healthifyzone/blob/main/documentation/pep8-validator-users-models.py.png) | PASS |
| users app / urls.py | ![users app / urls.py](https://github.com/devnickocodes/healthifyzone/blob/main/documentation/pep8-validator-users-urls.py.png) | PASS |
| users app / views.py | ![users app / views.py](https://github.com/devnickocodes/healthifyzone/blob/main/documentation/pep8-validator-users-views.py.png) | PASS |

## **Browser Compatibility**

| Browser | Screenshot | PASS/FAIL |
| --- | --- | --- |
| Google Chrome | ![Google Chrome](https://github.com/devnickocodes/healthifyzone/blob/main/documentation/google_chrome.png) | PASS |
| Mozilla Firefox | ![Mozilla Firefox](https://github.com/devnickocodes/healthifyzone/blob/main/documentation/mozilla.png) | PASS |
| Microsoft Edge | ![Microsoft Edge](https://github.com/devnickocodes/healthifyzone/blob/main/documentation/microsoft_edge.jpeg) | PASS |


## **Responsiveness**

| Device | Screenshot | PASS/FAIL |
| --- | --- | --- |
| Desktop | ![Desktop](https://github.com/devnickocodes/healthifyzone/blob/main/documentation/desktop_responsiveness.png) | PASS |
| Laptop | ![Laptop](https://github.com/devnickocodes/healthifyzone/blob/main/documentation/laptop_responsiveness.png) | PASS |
| Tablet (Google DevTools) | ![Tablet](https://github.com/devnickocodes/healthifyzone/blob/main/documentation/tablet_responsiveness.png) | PASS |
| Mobile (Google DevTools) | ![Mobile](https://github.com/devnickocodes/healthifyzone/blob/main/documentation/mobile_responsiveness.png) | PASS |

## **Lighthouse Validation**

| Page | Screenshot | PASS/FAIL |
| --- | --- | --- |
| Homepage | ![Homepage](https://github.com/devnickocodes/healthifyzone/blob/main/documentation/homepage_lighthouse.png) | PASS: Some minor warnings |
| Category Page | ![Category Page](https://github.com/devnickocodes/healthifyzone/blob/main/documentation/category_lighthouse.png) | PASS |
| Sign Up Page | ![Sign Up Page](https://github.com/devnickocodes/healthifyzone/blob/main/documentation/sign_up_lighthouse.png) | PASS |
| Log In Page | ![Log In Page](https://github.com/devnickocodes/healthifyzone/blob/main/documentation/login_lighthouse.png) | PASS |
| Log Out Page | ![Log Out Page](https://github.com/devnickocodes/healthifyzone/blob/main/documentation/logout_lighthouse.png) | PASS |
| Recipe Search Page | ![Recipe Search Page](https://github.com/devnickocodes/healthifyzone/blob/main/documentation/recipe_search_lighthouse.png) | PASS |
| Recipe Results Page | ![Recipe Results Page](https://github.com/devnickocodes/healthifyzone/blob/main/documentation/recipe_results_lighthouse.png) | PASS |
| Recipe Details Page | ![Recipe Details Page](https://github.com/devnickocodes/healthifyzone/blob/main/documentation/recipe_details_lighthouse.png) | PASS |
| Profile Page | ![Profile Page](https://github.com/devnickocodes/healthifyzone/blob/main/documentation/profile_lighthouse.png) | PASS |
| Create Article Page | ![Create Article Page](https://github.com/devnickocodes/healthifyzone/blob/main/documentation/create_article_lighthouse.png) | PASS |
| Edit Article Page | ![Edit Article Page](https://github.com/devnickocodes/healthifyzone/blob/main/documentation/edit_article_lighthouse.png) | PASS |
| Delete Article Page | ![Delete Article Page](https://github.com/devnickocodes/healthifyzone/blob/main/documentation/delete_article_lighthouse.png) | PASS |
| Password Reset Page | ![Password Reset Page](https://github.com/devnickocodes/healthifyzone/blob/main/documentation/password_reset_lighthouse.png) | PASS |
| Password Reset Email Sent Page | ![Password Reset Email Sent Page](https://github.com/devnickocodes/healthifyzone/blob/main/documentation/password_reset_email_sent_lighthouse.png) | PASS |
| Password Reset Email Opened Page | ![Password Reset Email Opened Page](https://github.com/devnickocodes/healthifyzone/blob/main/documentation/password_reset_email_opened_lighthouse.png) | PASS |
| Password Reset Done Page | ![Password Reset Done Page](https://github.com/devnickocodes/healthifyzone/blob/main/documentation/password_reset_done_lighthouse.png) | PASS |

## **Manual Testing**

There was ongoing testing throughout the whole development of the website. I was using the Google Developer Tools to troubleshoot issues as well as performing early deployments to see if everything on the website was functioning the way it was expected.

| Page | Feature | Expected Outcome | PASS/FAIL |
| --- | --- | --- | --- |
| Homepage | Logo | When the user clicks on the logo they are redirected to the homepage | PASS |
| Homepage | Home tab | When the user clicks on the Home tab they are redirected to the homepage | PASS |
| Homepage | Category tab | When the user clicks on the Category tab they are redirected to the Category page | PASS |
| Homepage | Recipes tab | When the user clicks on the Recipes tab they are redirected to the Recipes page where they can search for a recipe | PASS |
| Homepage | Sign Up tab | When the user clicks on the Sign Up tab they are redirected to the Sign Up page where they can create an account | PASS |
| Homepage | Log In tab | When the user clicks on the Log In tab they are redirected to the Log In page where they can log in to their account | PASS |
| Homepage | Footer | When the user clicks on the GitHub icon they are redirected to the GitHub page of the developer | PASS |
| Homepage | Article Author Profile Link | When a user that is not logged in clicks on the author profile link in the article card they will be redirected to the log in page | PASS |
| Homepage | Article Author Profile Link | When a user that is logged in and clicks on the author profile link in the article card they will be redirected to the profile page of the author | PASS |
| Homepage | View Article Button | When a user clicks on the "View Article" button they will be redirected to the individual page for the article | PASS |
| Homepage | Delete Article Button | When a user is logged in and is the author of an article they will see a "Delete Article" button which when clicked will take the user to a delete confirmation page | PASS |
| Homepage | Edit Article Button | When a user is logged in and is the author of an article they will see an "Edit Article" button which when clicked will take the user to a  page where the user can update/ edit the article | PASS |
| Homepage | Pagination Buttons | When the user clicks on the "NEXT" button they will be taken to the next page | PASS |
| Homepage | Pagination Buttons | When the user clicks on the "PREV" button they will be taken to the previous page | PASS |



