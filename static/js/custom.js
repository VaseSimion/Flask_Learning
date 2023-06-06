function toggleNav() {
    var navLinks = document.querySelector('.nav-links');
    navLinks.classList.toggle('nav-open');
}

window.addEventListener('DOMContentLoaded', function() {
  var hero = document.querySelector('.hero');
  hero.style.height = (window.innerHeight * 0.8) + 'px';
});

window.addEventListener('resize', function() {
  var hero = document.querySelector('.hero');
  hero.style.height = (window.innerHeight * 0.8) + 'px';
});