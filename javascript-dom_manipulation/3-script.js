// Select the <header> element and the element with ID "toggle_header"
var headerElement = document.querySelector('header');
var toggleButton = document.getElementById('toggle_header');

// Add a click event listener to the element with ID "toggle_header"
toggleButton.addEventListener('click', function() {
  // Check the current class of the <header> element
  if (headerElement.classList.contains('red')) {
    // If the current class is "red," switch to "green"
    headerElement.classList.remove('red');
    headerElement.classList.add('green');
  } else {
    // If the current class is "green," switch to "red"
    headerElement.classList.remove('green');
    headerElement.classList.add('red');
  }
});
