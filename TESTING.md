# Testing

## **HTML Validation**

As there is jinja syntax in my HTML code, simply pasting the code directly in the validator wouldn't work.
The way I have done the validation is by using the URIs from the deployed pages from Heroku.

Since some of the pages require the user to be logged in, this way of validation wouldn't work as the HTML validator doesn't have access to authentication.

For these pages I have extracted the code by right-clicking on the pages that need validation and selecting "View Page Source" and pasting the code directly in the validator.

