// Utiliza jQuery para seleccionar el elemento con el ID "toggle_header" y agrega un evento de clic
$('#toggle_header').click(function() {
	// Selecciona el elemento <header>
	var headerElement = $('header');
  
	// Verifica si ya tiene la clase ".red"
	if (headerElement.hasClass('red')) {
	  // Si tiene la clase ".red", la elimina y agrega la clase ".green"
	  headerElement.removeClass('red').addClass('green');
	} else {
	  // Si no tiene la clase ".red", la elimina y agrega la clase ".red"
	  headerElement.removeClass('green').addClass('red');
	}
});
