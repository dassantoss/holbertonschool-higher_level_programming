// Utiliza jQuery para hacer una solicitud GET a la URL
$.get('https://hellosalut.stefanbohacek.dev/?lang=fr', function(data) {
  // Obtiene el valor de "hello" desde los datos obtenidos
  var helloValue = data.hello;

  // Muestra la traducción de "hello" en el elemento <div id="hello">
  $('#hello').text(helloValue);
});
