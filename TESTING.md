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
