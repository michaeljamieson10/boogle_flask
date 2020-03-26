const $guessForm = $("#guess-form");
const $displayGuess = $("#displayGuess");

$guessForm.on("submit", async function(evt) {
    evt.preventDefault(); // no page-refresh on submit

    const userGuessText = $("#user-guess-text").val()
    console.log(userGuessText)
    // const guessText =
    const isGuess = await getData(userGuessText)
    console.log(isGuess,"isGuess")
    $displayGuess.text(isGuess.result)
//We need a ajax request to the server with our $userGuessText  
//const userInstance = await User.login(userGuessT);
  
});
