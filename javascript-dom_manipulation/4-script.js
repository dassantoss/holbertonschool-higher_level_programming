// Select the element with ID "add_item" and the <ul> element with class "my_list"
var addItemButton = document.getElementById('add_item');
var myList = document.querySelector('.my_list');

// Add a click event listener to the "add_item" element
addItemButton.addEventListener('click', function() {
  // Create a new <li> element
  var newItem = document.createElement('li');
  
  // Set the text content of the new <li> element
  newItem.textContent = 'Item';

  // Append the new <li> element to the <ul> element
  myList.appendChild(newItem);
});
