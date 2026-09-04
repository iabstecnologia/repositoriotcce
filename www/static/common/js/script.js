// ===============================================
// MÓDULO 2: Funções de Eventos (Event Handlers e API)
// ===============================================

/**
 * Lógica de responsividade para navbar.
 */
function handleMobileResponsiveness() {
    const navbar = document.querySelector('.navbar');
    const heroTitle = document.querySelector('.hero-title');
    const navbarPositionClasses = ['position-absolute', 'w-100', 'start-0', 'navbar-mobile'];

    if (navbar && heroTitle) {
        if (window.innerWidth < 992) {
            navbar.classList.add(...navbarPositionClasses);
            // heroTitle.classList.add('alguma-classe-mobile'); // Se necessário
        } else {
            navbar.classList.remove(...navbarPositionClasses);
        }
    }
}


// ===============================================
// MÓDULO 3: Inicialização (DOMContentLoaded)
// ===============================================

// Script para funcionalidades da página
document.addEventListener('DOMContentLoaded', function() {
    // Responsividade para mobile
    const navbar = document.querySelector('.navbar');
    const navbarMenu = document.getElementById('navbarNav');
    const navbarToggler = document.querySelector('.navbar-toggler');
    if (navbar) {
        window.addEventListener('resize', function() {
            if (window.innerWidth < 992) {
                navbar.classList.add('navbar-mobile');
            } else {
                navbar.classList.remove('navbar-mobile');
            }
        });
    }

    if (navbarMenu && navbarToggler) {
        document.addEventListener('click', function(event) {
            if (
                window.innerWidth < 992 &&
                navbarMenu.classList.contains('show') &&
                !navbarMenu.contains(event.target) &&
                !navbarToggler.contains(event.target)
            ) {
                const navbarCollapse = bootstrap.Collapse.getInstance(navbarMenu);
                navbarCollapse?.hide();
            }
        });
    }

    // 1. Chamar a função Imediatamente
    handleMobileResponsiveness();

    // 2. Chamar a função no evento de redimensionamento da janela
    window.addEventListener('resize', handleMobileResponsiveness);
});


