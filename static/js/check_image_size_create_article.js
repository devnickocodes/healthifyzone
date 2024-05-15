document.addEventListener("DOMContentLoaded", function() {
  var form = document.getElementById('articleForm');
  var errorMessage = document.getElementById('errorCreateArticleMessage');

  form.addEventListener('submit', function(event) {
    var fileInput = document.getElementById('id_featured_article_image');
    var file = fileInput.files[0];
    var maxSize = 900 * 1024;

    if (file && file.size > maxSize) {
      event.preventDefault();
      errorMessage.textContent = "The selected image file is too large. Please select an image file less than 900KB.";
    } else {
      errorMessage.textContent = "";
    }
  });
});