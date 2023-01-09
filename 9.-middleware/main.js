const btn = document.getElementById('btn');


btn.addEventListener('click', async () => {
    const objData = JSON.stringify({name:"Dante", age:45})

    const resp = await fetch(
        'http://localhost:8000',
        { 
            headers:{
                "content-type":"application/json"
            },
            mode:"cors",
            method:"POST",
            body:objData
        })
    const result = await resp.json()
    console.log(result['susu'])
    console.log(result)
})

