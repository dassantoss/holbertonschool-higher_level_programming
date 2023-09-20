// Espera a que se cargue completamente el DOM antes de ejecutar el script
$(document).ready(function() {
  // Cuando se hace clic en el elemento con ID "add_item"
  $('#add_item').click(function() {
    // Crea un nuevo elemento <li>
    var newItem = $('<li>Item</li>');
    
    // Agrega el nuevo elemento a la lista <ul class="my_list">
    $('.my_list').append(newItem);
  });

  // Cuando se hace clic en el elemento con ID "remove_item"
  $('#remove_item').click(function() {
    // Elimina el último elemento <li> de la lista <ul class="my_list">
    $('.my_list li:last-child').remove();
  });

  // Cuando se hace clic en el elemento con ID "clear_list"
  $('#clear_list').click(function() {
    // Elimina todos los elementos <li> de la lista <ul class="my_list">
    $('.my_list').empty();
  });
});
