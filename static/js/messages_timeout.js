document.addEventListener('DOMContentLoaded', function() {
  setTimeout(function() {
    document.querySelectorAll('.alert').forEach(function(element) {
      element.style.display = 'none';
    });
  }, 3000); 
});