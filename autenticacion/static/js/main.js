// Obtener el botón de menú y el menú de navegación
const menuToggle = document.getElementById('menu-toggle');
const navLinks = document.getElementById('nav-links');

// Agregar un evento de clic al botón de menú
menuToggle.addEventListener('click', () => {
    navLinks.classList.toggle('active'); // Alternar la clase 'active' para mostrar/ocultar el menú
});
