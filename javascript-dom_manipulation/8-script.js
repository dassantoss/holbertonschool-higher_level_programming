// Fetch the translation of "hello" from the URL
fetch('https://hellosalut.stefanbohacek.dev/?lang=fr')
  .then(function(response) {
    // Check if the response is successful (status code 200)
    if (!response.ok) {
      throw new Error('Network response was not ok');
    }
    // Parse the text response
    return response.text();
  })
  .then(function(translation) {
    // Select the HTML element with id "hello"
    var helloElement = document.getElementById('hello');
    
    // Display the translation in the selected element
    helloElement.textContent = translation;
  })
  .catch(function(error) {
    // Handle errors
    console.error('There was a problem with the fetch operation:', error);
  });
