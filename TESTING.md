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
| main app / admin.py   | ![main app / admin.py ](https://github.com/devnickocodes/healthifyzone/blob/main/documentation/pep8-validator-main-admin.py.png) | PASS |
| main app / forms.py   | ![main app / forms.py ](https://github.com/devnickocodes/healthifyzone/blob/main/documentation/pep8-validator-main-forms.py.png) | PASS |
| main app / models.py   | ![main app / models.py ](https://github.com/devnickocodes/healthifyzone/blob/main/documentation/pep8-validator-main-models.py.png) | PASS |
| main app / urls.py   | ![main app / urls.py ](https://github.com/devnickocodes/healthifyzone/blob/main/documentation/pep8-validator-main-urls.py.png) | PASS |
| main app / views.py   | ![main app / views.py ](https://github.com/devnickocodes/healthifyzone/blob/main/documentation/pep8-validator-main-views.py.png) | PASS |
| recipe app / urls.py   | ![recipe app / urls.py ](https://github.com/devnickocodes/healthifyzone/blob/main/documentation/pep8-validator-recipe-urls.py.png) | PASS |
| recipe app / views.py   | ![recipe app / views.py ](https://github.com/devnickocodes/healthifyzone/blob/main/documentation/pep8-validator-recipe-views.py.png) | PASS |
| healthifyzone / urls.py   | ![healthifyzone / urls.py ](https://github.com/devnickocodes/healthifyzone/blob/main/documentation/pep8-validator-project-urls.py.png) | PASS |
| healthifyzone / settings.py   | ![healthifyzone / settings.py ](https://github.com/devnickocodes/healthifyzone/blob/main/documentation/pep8-validator-project-settings.py.png) | PASS |
| users app / admin.py   | ![users app / admin.py ](https://github.com/devnickocodes/healthifyzone/blob/main/documentation/pep8-validator-users-admin.py.png) | PASS |
| users app / forms.py   | ![users app / forms.py ](https://github.com/devnickocodes/healthifyzone/blob/main/documentation/pep8-validator-users-forms.py.png) | PASS |
| users app / models.py   | ![users app / models.py ](https://github.com/devnickocodes/healthifyzone/blob/main/documentation/pep8-validator-users-models.py.png) | PASS |
| users app / urls.py   | ![users app / urls.py ](https://github.com/devnickocodes/healthifyzone/blob/main/documentation/pep8-validator-users-urls.py.png) | PASS |
| users app / views.py   | ![users app / views.py ](https://github.com/devnickocodes/healthifyzone/blob/main/documentation/pep8-validator-users-views.py.png) | PASS |
