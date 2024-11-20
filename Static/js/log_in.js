const userMailInput = document.getElementById('email');
const passwordInput = document.getElementById('password');
const userType = document.getElementById('user_type')
const signInButton = document.getElementById('logInButton');

function toggleLogInButton() {
    if (userMailInput.value.trim() !== "" && passwordInput.value.trim() !== "" && userType.value.trim() !== "") {
        signInButton.classList.remove('secondary');
    } else {
        signInButton.classList.add('secondary');
        }
}

userMailInput.addEventListener('input', toggleLogInButton);
passwordInput.addEventListener('input', toggleLogInButton);
userType.addEventListener('input', toggleLogInButton);