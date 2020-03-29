const $guessForm = $("#guess-form");
const $displayGuess = $("#displayGuess");
const $score = $("#score");
$guessForm.show()
let score = 0
let newUser = new User("cat")

setTimeout(async function(){ 
    $guessForm.hide()
    const isHighestS = await newUser.getScore(score)
    }, 10000);
$guessForm.on("submit", async function(evt) {
    evt.preventDefault(); // no page-refresh on submit
    const $userGuessText = $("#user-guess-text").val()
    const isGuess = await newUser.getData($userGuessText)
    if(isGuess.result == "ok"){
        score  = isGuess.finalNum
        $score.text(score)  
    }
  

    $displayGuess.text(isGuess.result)
//We need a ajax request to the server with our $userGuessText  
//const userInstance = await User.login(userGuessT);
  
});
