// Wait for the document to be fully loaded
$(document).ready(function() {
  // Function to fetch and display translation
  function fetchTranslation() {
    // Get the language code entered by the user
    var languageCode = $('#language_code').val();

    // Make a GET request to the API with the entered language code
    $.get(`https://www.fourtonfish.com/hellosalut/hello/?lang=${languageCode}`, function(data) {
      // Extract the translation of "Hello" from the response data
      var translation = data.hello;

      // Display the translation in the HTML tag DIV#hello
      $('#hello').text(translation);
    });
  }

  // When the "Translate" button is clicked
  $('#btn_translate').click(fetchTranslation);

  // When ENTER key is pressed in the input field
  $('#language_code').keypress(function(event) {
    // Check if the pressed key is ENTER (key code 13)
    if (event.which == 13) {
      // Prevent the default form submission behavior
      event.preventDefault();

      // Call the function to fetch and display translation
      fetchTranslation();
    }
  });
});
