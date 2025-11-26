document.addEventListener('DOMContentLoaded', () => {
    const counters = document.querySelectorAll('.counter-value');
    const duration = 2000; // Duração da animação em milissegundos (2 segundos)

    const startCounter = (counter) => {
        const target = +counter.getAttribute('data-target');
        const format = counter.getAttribute('data-format') || '';
        const step = target / (duration / 10); // Calcula o passo para que a contagem dure 'duration' milissegundos
        let current = 0;

        const updateCounter = () => {
            if (current < target) {
                current += step;
                // Arredonda para o número inteiro mais próximo, formatando números grandes com vírgula
                let displayValue = Math.ceil(current).toLocaleString('pt-BR'); 

                // Adiciona o sufixo (km) para o item de Kilometragem
                if (format === 'km') {
                    displayValue += ' km';
                }

                counter.textContent = displayValue;
                requestAnimationFrame(updateCounter);
            } else {
                // Garante que o valor final seja exatamente o alvo
                let finalValue = target.toLocaleString('pt-BR');
                if (format === 'km') {
                    finalValue += ' km';
                }
                counter.textContent = finalValue;
            }
        };

        updateCounter();
    };

    // Usando Intersection Observer para iniciar a animação quando o elemento for visível
    const observer = new IntersectionObserver((entries, observer) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                startCounter(entry.target);
                // Para de observar depois de iniciar a contagem
                observer.unobserve(entry.target);
            }
        });
    }, {
        // Opções do Observer: A animação começa quando 50% do elemento estiver visível
        threshold: 0.5 
    });

    // Observa todos os elementos com a classe .counter-value
    counters.forEach(counter => {
        observer.observe(counter);
    });
});
