/* Mortgages by Dennis Eng — Shared JS */

// FAQ Accordion
document.addEventListener('DOMContentLoaded', function() {
  const faqItems = document.querySelectorAll('.faq-item');
  faqItems.forEach(function(item) {
    const question = item.querySelector('.faq-question');
    if (!question) return;
    question.addEventListener('click', function() {
      const isOpen = item.classList.contains('active');
      // Close all
      faqItems.forEach(function(i) { i.classList.remove('active'); });
      faqItems.forEach(function(i) {
        const q = i.querySelector('.faq-question');
        if (q) q.setAttribute('aria-expanded', 'false');
      });
      // Open clicked
      if (!isOpen) {
        item.classList.add('active');
        question.setAttribute('aria-expanded', 'true');
      }
    });
  });
});
