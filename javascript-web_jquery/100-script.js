// Espera a que se cargue completamente el DOM antes de ejecutar el script
document.addEventListener('DOMContentLoaded', function() {
  // Selecciona el elemento <header>
  var headerElement = document.querySelector('header');

  // Actualiza el color del texto a rojo (#FF0000)
  headerElement.style.color = '#FF0000';
});
