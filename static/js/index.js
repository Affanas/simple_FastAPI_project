const databaseKey = 'userDatabase';
const database = JSON.parse(localStorage.getItem(databaseKey)) || {};
url = "http://localhost:8000/users/new/";
function Login(){
    const namec = document.getElementById("name").value;
    const passwordc = document.getElementById("password").value;
    url = "http://localhost:8000/users/login/";
    fetch(url, {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({
          name: namec,
          password: passwordc,
        }),
      })
        .then((response) => response.text())
        .then((text) => JSON.parse(text))
        .then((json) => json.user_id)
        .then((user_id) => sessionStorage.setItem("user_id", user_id.toString()))
        .catch((error) => console.log(error));
  </body>
</html>
