function login() {
    const username = prompt("Enter your username:");
    if (username) {
    document.getElementById("username").textContent = "Hello, " + username + "!";
    }
}

function signup() {
    alert("Redirecting to signup page...");
}
