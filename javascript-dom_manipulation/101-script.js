document.addEventListener('DOMContentLoaded', function() {
  // Function to fetch and display the translation
  function translateHello() {
    // Get the selected language code from the dropdown
    var languageCode = document.getElementById('language_code').value;
    
    // Check if a language is selected
    if (languageCode === '') {
      alert('Please choose a language.');
      return;
    }

    // Fetch the translation from the API based on the selected language code
    fetch(`https://hellosalut.stefanbohacek.dev/?lang=${languageCode}`)
      .then(function(response) {
        // Check if the response is successful (status code 200)
        if (!response.ok) {
          throw new Error('Network response was not ok');
        }
        // Parse the JSON response
        return response.json();
      })
      .then(function(data) {
        // Display only the translation, not the JSON code
        document.getElementById('hello').textContent = data.hello;
      })
      .catch(function(error) {
        // Handle errors
        console.error('There was a problem with the fetch operation:', error);
      });
  }

  // Add click event to the "Translate" button
  var translateButton = document.getElementById('btn_translate');
  translateButton.addEventListener('click', translateHello);
});
