// Select the element with id "red_header"
var redHeaderElement = document.getElementById('red_header');

// Add a click event listener to the element
redHeaderElement.addEventListener('click', function() {
  // Change the text color to red
  var headerElement = document.querySelector('header');
  headerElement.style.color = '#FF0000';
});