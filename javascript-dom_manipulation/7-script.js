// Fetch the list of Star Wars movies from the URL
fetch('https://swapi-api.hbtn.io/api/films/?format=json')
  .then(function(response) {
    // Check if the response is successful (status code 200)
    if (!response.ok) {
      throw new Error('Network response was not ok');
    }
    // Parse the JSON response
    return response.json();
  })
  .then(function(data) {
    // Select the HTML ul element with id "list_movies"
    var listMoviesElement = document.getElementById('list_movies');
    
    // Loop through the movie data and create list items
    data.results.forEach(function(movie) {
      var listItem = document.createElement('li');
      listItem.textContent = movie.title;
      listMoviesElement.appendChild(listItem);
    });
  })
  .catch(function(error) {
    // Handle errors
    console.error('There was a problem with the fetch operation:', error);
  });
