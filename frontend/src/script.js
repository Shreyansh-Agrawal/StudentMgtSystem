
const baseUrl = "http://127.0.0.1:5000/v1"

function toggleVisibility() {
    let passwordInput = document.getElementById('password');

    passwordInput.type = passwordInput.type === "password"? "text": "password";
}

let loginForm = document.getElementById("loginForm");


loginForm.addEventListener("submit", (e) => {
    e.preventDefault();
    login()
    getAllCourses()


    // fetch(`${baseUrl}/login`, requestOptions)
    //     .then(response => response.json())
    //     .then(res => console.log(res))
    //     .catch(e => console.log(e))
})
const data = {
    "username": "admin",
    "password": "123456",
    "role": "admin"
}
console.log(JSON.stringify(data));
const requestOptions = {
    method: 'POST',
    headers: {
        'Content-Type': 'application/json',
        // 'Access-Control-Allow-Origin': '*'
    },
    // mode: 'no-cors',
    body: JSON.stringify(data),
};
async function login() {
    let resp = await fetch(`${baseUrl}/login`, requestOptions);
    let res = await resp.json();
    console.log(res);
}
async function getAllCourses() {
    let resp = await fetch(`${baseUrl}/courses`);
    let res = await resp.json();
    console.log(res);
}

// var a = 10

// function func() {
//     let b = 2
//     console.log("hello");
// }

// func()