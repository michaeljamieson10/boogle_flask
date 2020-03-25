async function getData(){   
    const response = await axios.get('https://swapi.co/api/planets/');
    console.log(response.data);
    console.log("Line of axios.get")
}