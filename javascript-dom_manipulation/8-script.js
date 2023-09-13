// Fetch the translation of "hello" from the URL
fetch('https://hellosalut.stefanbohacek.dev/?lang=fr')
  .then(function(response) {
    // Check if the response is successful (status code 200)
    if (!response.ok) {
      throw new Error('Network response was not ok');
    }
    // Parse the JSON response
    return response.json();
  })
  .then(function(data) {
    // Select the HTML element with id "hello"
    var helloElement = document.getElementById('hello');
    
    // Display only the translation "Salut"
    helloElement.textContent = data.hello;
  })
  .catch(function(error) {
    // Handle errors
    console.error('There was a problem with the fetch operation:', error);
  });
