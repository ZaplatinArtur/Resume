const menuButton = document.querySelector('.menu-toggle');
const navigation = document.querySelector('.nav');

if (menuButton && navigation) {
  menuButton.addEventListener('click', () => {
    const isOpen = navigation.classList.toggle('open');
    menuButton.setAttribute('aria-expanded', String(isOpen));
  });

  navigation.querySelectorAll('a').forEach((link) => {
    link.addEventListener('click', () => {
      navigation.classList.remove('open');
      menuButton.setAttribute('aria-expanded', 'false');
    });
  });
}

const reducedMotion = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
const revealItems = document.querySelectorAll('.reveal');

if (reducedMotion || !('IntersectionObserver' in window)) {
  revealItems.forEach((item) => item.classList.add('visible'));
} else {
  const observer = new IntersectionObserver((entries) => {
    entries.forEach((entry) => {
      if (entry.isIntersecting) {
        entry.target.classList.add('visible');
        observer.unobserve(entry.target);
      }
    });
  }, { threshold: 0.08, rootMargin: '0px 0px -40px' });

  revealItems.forEach((item) => observer.observe(item));
}

const year = document.querySelector('#year');
if (year) year.textContent = String(new Date().getFullYear());

const scrollIndex = document.querySelector('.scroll-index');
const scrollCurrent = document.querySelector('#scroll-current');
const scrollLabel = document.querySelector('#scroll-label');
const trackedSections = [
  { element: document.querySelector('#about'), number: '01', label: 'ОБО МНЕ' },
  { element: document.querySelector('#expertise'), number: '02', label: 'СТЕК' },
  { element: document.querySelector('#projects'), number: '03', label: 'ПРОЕКТЫ' },
  { element: document.querySelector('#education'), number: '04', label: 'ОБРАЗОВАНИЕ' },
].filter((section) => section.element);

if (scrollIndex && scrollCurrent && scrollLabel && trackedSections.length) {
  let scrollTicking = false;

  const updateScrollIndex = () => {
    const readingLine = window.scrollY + window.innerHeight * 0.45;
    let activeSection = trackedSections[0];

    trackedSections.forEach((section) => {
      if (section.element.offsetTop <= readingLine) activeSection = section;
    });

    scrollCurrent.textContent = activeSection.number;
    scrollLabel.textContent = activeSection.label;
    scrollIndex.setAttribute('aria-label', `Текущий раздел: ${activeSection.label}, ${activeSection.number} из 04`);
    scrollTicking = false;
  };

  window.addEventListener('scroll', () => {
    if (!scrollTicking) {
      window.requestAnimationFrame(updateScrollIndex);
      scrollTicking = true;
    }
  }, { passive: true });

  window.addEventListener('resize', updateScrollIndex);
  updateScrollIndex();
}
