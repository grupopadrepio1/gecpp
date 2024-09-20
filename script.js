const toggleMenuButton = document.getElementById('toggle-menu');
const navMenu = document.querySelector('nav ul');

// Alterna o menu ao clicar no botão
toggleMenuButton.addEventListener('click', function() {
    navMenu.classList.toggle('show-menu');
});

// Fecha o menu ao clicar fora dele, se o menu estiver aberto
document.addEventListener('click', function(event) {
    if (!navMenu.contains(event.target) && event.target !== toggleMenuButton) {
        navMenu.classList.remove('show-menu');
    }
});

// Fecha o menu automaticamente ao redimensionar a tela para mais de 768px
window.addEventListener('resize', function() {
    if (window.innerWidth > 768) {
        navMenu.classList.remove('show-menu'); // Fecha o menu em telas grandes
    }
});






// Carrossel //

let currentIndex = 0;
const items = document.querySelectorAll('.carousel-item');
const totalItems = items.length;

function showItem(index) {
    items.forEach((item, i) => {
        item.classList.remove('active');
        if (i === index) {
            item.classList.add('active');
        }
    });
}

function nextItem() {
    currentIndex = (currentIndex + 1) % totalItems;
    showItem(currentIndex);
}

function prevItem() {
    currentIndex = (currentIndex - 1 + totalItems) % totalItems;
    showItem(currentIndex);
}

document.querySelector('.next').addEventListener('click', nextItem);
document.querySelector('.prev').addEventListener('click', prevItem);

// Opcional: Iniciar o carrossel automaticamente
setInterval(nextItem, 5000); // Altera a cada 5 segundos

