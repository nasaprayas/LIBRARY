const userMailInput = document.getElementById('email');
const passwordInput = document.getElementById('password');
const signInButton = document.getElementById('logInButton');

function toggleLogInButton() {
    if (userMailInput.value.trim() !== "" && passwordInput.value.trim() !== "") {
        signInButton.disabled = false;
        signInButton.classList.remove('secondary');
    } else {
        signInButton.disabled = true;
        signInButton.classList.add('secondary');
        }
}

userMailInput.addEventListener('input', toggleLogInButton);
passwordInput.addEventListener('input', toggleLogInButton);