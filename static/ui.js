const $guessForm = $("#guess-form");
const $displayGuess = $("#displayGuess");
const $score = $("#score");
$guessForm.show()
let score = 0

setTimeout(function(){ $guessForm.hide() }, 60000);
$guessForm.on("submit", async function(evt) {
    evt.preventDefault(); // no page-refresh on submit

    const $userGuessText = $("#user-guess-text").val()
    console.log($userGuessText)
    const isGuess = await getData($userGuessText)
    console.log(isGuess,"isGuess")
    console.log($userGuessText.length, "is Guess lengths")
    if(isGuess.result == "ok"){
        score  += $userGuessText.length
        console.log(score, "score score score")
        $score.text(score)  
    }
  

    $displayGuess.text(isGuess.result)
//We need a ajax request to the server with our $userGuessText  
//const userInstance = await User.login(userGuessT);
  
});
