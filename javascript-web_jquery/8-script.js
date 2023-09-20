// Utiliza jQuery para hacer una solicitud GET a la URL
$.get('https://swapi-api.hbtn.io/api/films/?format=json', function(data) {
  // Obtiene la lista de películas desde los datos obtenidos
  var movies = data.results;

  // Selecciona el elemento <ul id="list_movies">
  var ulElement = $('#list_movies');

  // Recorre la lista de películas y agrega los títulos a la lista
  $.each(movies, function(index, movie) {
    ulElement.append('<li>' + movie.title + '</li>');
  });
});
