function postit() {
    postObj = {
        action: "move-forward",
        increment: 10
    }

    let post = JSON.stringify(postObj)
    const url = "/move-forward"
    let xhr = new XMLHttpRequest()
    xhr.open('POST', url, true)
    xhr.setRequestHeader('Content-type', 'application/json; charset=UTF-8')
    xhr.send(post);
    xhr.onload = function () {
        if(xhr.status === 201) {
            console.log("Post successfully created!") 
        }
    }
}

document.addEventListener("keypress", function onPress(event) {
    if (event.key === "w") {
        postObj = {
            action: "move-forward",
            increment: 10
        }
    
        let post = JSON.stringify(postObj)
        const url = "/move-forward"
        let xhr = new XMLHttpRequest()
        xhr.open('POST', url, true)
        xhr.setRequestHeader('Content-type', 'application/json; charset=UTF-8')
        xhr.send(post);
        xhr.onload = function () {
            if(xhr.status === 201) {
                console.log("Post successfully created!") 
            }
        }
    }
});
