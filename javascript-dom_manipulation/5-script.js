// Select the element with id "update_header"
var updateHeaderElement = document.getElementById('update_header');

// Add a click event listener to the element
updateHeaderElement.addEventListener('click', function() {
  // Select the header element
  var headerElement = document.querySelector('header');
  
  // Update the text of the header element
  headerElement.textContent = 'New Header!!!';
});
