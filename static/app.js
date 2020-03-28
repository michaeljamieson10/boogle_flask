class User{
    constructor(brand){
        this.user = "you are";
    }

    async getData(userGuess){   
        const response = await axios.post('http://127.0.0.1:5000/guess',{
            userGuess
        });
        return response.data
    }
    async getScore(userScore){   
        const response = await axios.post('http://127.0.0.1:5000/score',{
            userScore
        });
        console.log(response.data.result,"inside app")
        return response.data
        
        // return response.data
    }
}
