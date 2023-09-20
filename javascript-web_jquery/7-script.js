// Utiliza jQuery para hacer una solicitud GET a la URL
$.get('https://swapi-api.hbtn.io/api/people/5/?format=json', function(data) {
  // Extrae el nombre del personaje de los datos obtenidos
  var characterName = data.name;

  // Muestra el nombre del personaje en el elemento <div id="character">
  $('#character').text(characterName);
});
