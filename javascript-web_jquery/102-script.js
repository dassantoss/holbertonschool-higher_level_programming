// Wait for the document to be fully loaded
$(document).ready(function() {
  // When the "Translate" button is clicked
  $('#btn_translate').click(function() {
    // Get the language code entered by the user
    var languageCode = $('#language_code').val();
    
    // Make a GET request to the API with the entered language code
    $.get(`https://www.fourtonfish.com/hellosalut/hello/?lang=${languageCode}`, function(data) {
      // Extract the translation of "Hello" from the response data
      var translation = data.hello;

      // Display the translation in the HTML tag DIV#hello
      $('#hello').text(translation);
    });
  });
});
