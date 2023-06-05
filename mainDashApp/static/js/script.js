const navBurger = document.querySelector('.nav-burger');
const navOptions = document.querySelector('.nav-options');

navBurger.addEventListener('click', () => {
    navBurger.classList.toggle('open');
    navOptions.classList.toggle('show');
});
  