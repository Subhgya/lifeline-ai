function sendSOS() {
    navigator.geolocation.getCurrentPosition(function(position) {
        fetch('http://127.0.0.1:5000/sos', {
            method: 'POST',
            headers: {'Content-Type': 'application/json'},
            body: JSON.stringify({
                latitude: position.coords.latitude,
                longitude: position.coords.longitude
            })
        })
        .then(response => response.json())
        .then(data => {
            document.getElementById("sosStatus").innerText = data.message;
        });
    });
}

function findHospitals() {
    navigator.geolocation.getCurrentPosition(function(position) {
        let lat = position.coords.latitude;
        let lon = position.coords.longitude;
        window.open(`https://www.google.com/maps/search/hospitals/@${lat},${lon},15z`);
    });
}

function sendMessage() {
    let input = document.getElementById("userInput").value;

    fetch('http://127.0.0.1:5000/chat', {
        method: 'POST',
        headers: {'Content-Type': 'application/json'},
        body: JSON.stringify({message: input})
    })
    .then(response => response.json())
    .then(data => {
        let chatbox = document.getElementById("chatbox");
        chatbox.innerHTML += "<p><b>You:</b> " + input + "</p>";
        chatbox.innerHTML += "<p><b>AI:</b> " + data.reply + "</p>";
    });

    document.getElementById("userInput").value = "";
}

function startVoice() {
    let recognition = new webkitSpeechRecognition();
    recognition.onresult = function(event) {
        document.getElementById("userInput").value =
            event.results[0][0].transcript;
    }
    recognition.start();
}

function loadUser(username){
    fetch('http://127.0.0.1:5000/user/' + username)
    .then(res => res.json())
    .then(data => {
        document.getElementById("blood").innerText = data.blood_group;
        document.getElementById("contact").innerText = data.emergency_contact;
    })
    .catch(error => {
        console.error("Error loading user data:", error);
    });
}

function logout() {
    localStorage.removeItem("username");
    window.location.href = "login.html";
}