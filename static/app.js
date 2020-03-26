async function getData(userGuess){   
    const response = await axios.post('http://127.0.0.1:5000/guess',{
        userGuess
    });
    console.log(response)
    console.log(response.config.data, "my response.config")
    console.log("Line of axios.get")
    console.log(response.data, "my flask data")
    return response.data
}