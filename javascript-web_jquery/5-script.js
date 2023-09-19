// Utiliza jQuery para seleccionar el elemento con el ID "add_item" y agrega un evento de clic
$('#add_item').click(function() {
	// Crea un nuevo elemento <li>
	var newItem = $('<li>Item</li>');
  
	// Agrega el nuevo elemento a la lista <ul class="my_list">
	$('.my_list').append(newItem);
  });
  