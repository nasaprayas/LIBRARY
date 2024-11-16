const userIdInput = document.getElementById('email');
const passwordInput = document.getElementById('password');
const signInButton = document.getElementById('signInButton');

function toggleSignInButton() {
    if (userIdInput.value.trim() !== "" && passwordInput.value.trim() !== "") {
        signInButton.disabled = false;
        signInButton.classList.remove('secondary');
    } else {
        signInButton.disabled = true;
        signInButton.classList.add('secondary');
        }
}

userIdInput.addEventListener('input', toggleSignInButton);
passwordInput.addEventListener('input', toggleSignInButton);