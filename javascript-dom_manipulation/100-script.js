document.addEventListener('DOMContentLoaded', function() {
  // Function to add a new <li> element to the list
  function addItem() {
    var myList = document.querySelector('.my_list');
    var newItem = document.createElement('li');
    newItem.textContent = 'Item';
    myList.appendChild(newItem);
  }

  // Function to remove the last <li> element from the list
  function removeItem() {
    var myList = document.querySelector('.my_list');
    var lastItem = myList.lastElementChild;
    if (lastItem) {
      myList.removeChild(lastItem);
    }
  }

  // Function to clear all <li> elements from the list
  function clearList() {
    var myList = document.querySelector('.my_list');
    myList.innerHTML = '';
  }

  // Add click event to add a new item
  var addItemButton = document.getElementById('add_item');
  addItemButton.addEventListener('click', addItem);

  // Add click event to remove the last item
  var removeItemButton = document.getElementById('remove_item');
  removeItemButton.addEventListener('click', removeItem);

  // Add click event to clear the entire list
  var clearListButton = document.getElementById('clear_list');
  clearListButton.addEventListener('click', clearList);
});
