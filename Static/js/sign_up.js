const nameInput = document.getElementById('full_name');
const userMailInput = document.getElementById('email');
const dobInput = document.getElementById('dob');
const passwordInput = document.getElementById('password');
const signInButton = document.getElementById('signUpButton');

function toggleSignUpButton() {
    if (userMailInput.value.trim() !== "" && passwordInput.value.trim() !== "" && nameInput.value.trim() !== "" && dobInput.value.trim() !== "") {4
        signInButton.classList.remove('secondary');
    } else {
        signInButton.classList.add('secondary');
        }
}

dobInput.addEventListener('input', toggleSignUpButton);
nameInput.addEventListener('input', toggleSignUpButton);
userMailInput.addEventListener('input', toggleSignUpButton);
passwordInput.addEventListener('input', toggleSignUpButton);