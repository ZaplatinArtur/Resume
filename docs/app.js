document.documentElement.classList.add("js");

const header = document.querySelector(".site-header");
const themeToggle = document.querySelector(".theme-toggle");
const menuToggle = document.querySelector(".menu-toggle");
const nav = document.querySelector(".nav");

const storedTheme = localStorage.getItem("resume-theme");
if (storedTheme === "dark" || storedTheme === "light") {
  document.documentElement.dataset.theme = storedTheme;
}

const currentTheme = () =>
  document.documentElement.dataset.theme === "dark" ? "dark" : "light";

const updateThemeLabel = () => {
  if (!themeToggle) return;
  const next = currentTheme() === "dark" ? "светлую" : "тёмную";
  themeToggle.setAttribute("aria-label", `Включить ${next} тему`);
  themeToggle.setAttribute("title", `Включить ${next} тему`);
};

themeToggle?.addEventListener("click", () => {
  const next = currentTheme() === "dark" ? "light" : "dark";
  document.documentElement.dataset.theme = next;
  localStorage.setItem("resume-theme", next);
  updateThemeLabel();
});

updateThemeLabel();

const updateHeader = () => {
  header?.classList.toggle("is-scrolled", window.scrollY > 12);
};

updateHeader();
window.addEventListener("scroll", updateHeader, { passive: true });

const setMenu = (open) => {
  nav?.classList.toggle("is-open", open);
  menuToggle?.setAttribute("aria-expanded", String(open));
};

menuToggle?.addEventListener("click", () => {
  setMenu(menuToggle.getAttribute("aria-expanded") !== "true");
});

nav?.querySelectorAll("a").forEach((link) => {
  link.addEventListener("click", () => setMenu(false));
});

window.addEventListener("keydown", (event) => {
  if (event.key === "Escape") setMenu(false);
});

const revealItems = document.querySelectorAll(".reveal");
if ("IntersectionObserver" in window) {
  const observer = new IntersectionObserver(
    (entries) => {
      entries.forEach((entry) => {
        if (!entry.isIntersecting) return;
        entry.target.classList.add("is-visible");
        observer.unobserve(entry.target);
      });
    },
    { rootMargin: "0px 0px -8%", threshold: 0.08 },
  );
  revealItems.forEach((item) => observer.observe(item));
} else {
  revealItems.forEach((item) => item.classList.add("is-visible"));
}
