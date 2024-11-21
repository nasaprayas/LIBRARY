//* Loop through all dropdown buttons to toggle between hiding and showing its dropdown content - This allows the user to have multiple dropdowns without any conflict */
var menu_button = document.getElementById('menu_button');
var menu_dots = document.getElementById('dots');
var sidenav = document.getElementById('side_nav');
var main = document.getElementById('main');

menu_button.addEventListener('click', function () {
    menu_dots.classList.toggle("menu_dots");
    sidenav.classList.toggle('disappear');
    main.classList.toggle('main');
})