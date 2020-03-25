const $guessForm = $("#guess-form");
const $userGuessText = $("#user-guess-text");


$guessForm.on("submit", async function(evt) {
    evt.preventDefault(); // no page-refresh on submit

    $userGuessText = $("#user-guess-text").val()
    console.log($userGuessText)
   
//We need a ajax request to the server with our $userGuessText  
//const userInstance = await User.login(userGuessT);
  
});
