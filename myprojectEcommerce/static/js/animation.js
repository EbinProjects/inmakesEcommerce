// script.js
document.addEventListener('DOMContentLoaded', function() {
    const content = document.querySelector('.slide-up-content');

    // Check if the content should be visible
    function checkVisibility() {
        if (window.scrollY > 0 || sessionStorage.getItem('hasScrolled')) {
            content.classList.add('visible');
            sessionStorage.setItem('hasScrolled', 'true');
        }
    }

    // Initialize visibility check
    checkVisibility();

    // Check visibility on scroll
    window.addEventListener('scroll', checkVisibility);
});
