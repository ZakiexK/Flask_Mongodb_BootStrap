document.getElementById('formData').addEventListener('submit' , retrievename)


function retrievename(e) 
{
    e.preventDefault()

    let name = document.getElementById('name').value


    fetch(`http://localhost:5000/${name}`)
    .then((res)=> res.json())
    .then((data)=> {document.getElementById('output').innerHTML = `Name : ${data.name} Genre : ${data.genre} Game : ${data.game}`})

}

document.getElementById('postData').addEventListener('submit',postData)

function postData(e)
{
    e.preventDefault()

    let name =document.getElementById('postName').value
    let genre =document.getElementById('postGenre').value
    let game =document.getElementById('postGame').value

    fetch('http://localhost:5000/postData',{
        method : 'POST',
        headers :{
            'Content-Type' : 'application/json'
        },
        body : JSON.stringify({
            'name' : name,
            'favGame' : game,
            'favGenre' : genre
        })
    })
    .then((response) => response.json())
    .then((data) => console.log(data))

}