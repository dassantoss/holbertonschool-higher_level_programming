// Fetch the character data from the URL
fetch('https://swapi-api.hbtn.io/api/people/5/?format=json')
  .then(function(response) {
    // Check if the response is successful (status code 200)
    if (!response.ok) {
      throw new Error('Network response was not ok');
    }
    // Parse the JSON response
    return response.json();
  })
  .then(function(data) {
    // Select the HTML element with id "character"
    var characterElement = document.getElementById('character');
    
    // Display the character name in the selected element
    characterElement.textContent = data.name;
  })
  .catch(function(error) {
    // Handle errors
    console.error('There was a problem with the fetch operation:', error);
  });
