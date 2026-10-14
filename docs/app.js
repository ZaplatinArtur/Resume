const menuButton = document.querySelector('.menu-toggle');
const navigation = document.querySelector('.nav');
const motionQuery = window.matchMedia('(prefers-reduced-motion: reduce)');
const reducedMotion = motionQuery.matches;

function closeMenu() {
  navigation?.classList.remove('open');
  menuButton?.setAttribute('aria-expanded', 'false');
}
menuButton?.addEventListener('click', () => {
  menuButton.setAttribute('aria-expanded', String(navigation.classList.toggle('open')));
});
navigation?.querySelectorAll('a').forEach(link => link.addEventListener('click', closeMenu));
document.addEventListener('keydown', event => { if (event.key === 'Escape') closeMenu(); });

const revealItems = document.querySelectorAll('.reveal');
if (!reducedMotion && 'IntersectionObserver' in window) {
  document.documentElement.classList.add('motion-enabled');
  const observer = new IntersectionObserver(entries => entries.forEach(entry => {
    if (entry.isIntersecting) {
      entry.target.classList.add('visible');
      observer.unobserve(entry.target);
    }
  }), {threshold: .04});
  revealItems.forEach(item => observer.observe(item));
} else {
  revealItems.forEach(item => item.classList.add('visible'));
}

const grid = document.querySelector('.project-grid');
const cards = [...document.querySelectorAll('.project-card')];
const filterButtons = [...document.querySelectorAll('[data-filter]')];
const countLabel = document.querySelector('.project-count');
function filterProjects(filter) {
  let count = 0;
  cards.forEach(card => {
    card.hidden = filter !== 'all' && !card.dataset.domains.split(' ').includes(filter);
    if (!card.hidden) count++;
  });
  filterButtons.forEach(button => button.setAttribute('aria-pressed', String(button.dataset.filter === filter)));
  grid.classList.toggle('is-filtered', filter !== 'all');
  countLabel.textContent = `${String(count).padStart(2, '0')} ${count === 1 ? 'проект' : count < 5 ? 'проекта' : 'проектов'}`;
  updateProgress();
}
filterButtons.forEach(button => button.addEventListener('click', () => filterProjects(button.dataset.filter)));
document.querySelector('.project-filters').hidden = false;

const dialog = document.querySelector('#project-dialog');
const dialogContent = dialog.querySelector('.dialog-content');
const projectLinks = [...document.querySelectorAll('.project-card-link[data-project]')];
let activeProject = null;
let lastTrigger = null;
let preserveHashOnClose = false;

function renderProject(id) {
  const template = document.getElementById(`project-${id}`);
  if (!template) return false;
  dialogContent.replaceChildren(template.content.cloneNode(true));
  window.initProjectFolders(dialogContent);
  dialogContent.querySelectorAll('.reveal').forEach(item => item.classList.add('visible'));
  dialogContent.querySelectorAll('.detail-art,.case-scene,.project-hero-scene').forEach(item => item.classList.add('scene-running'));
  activeProject = id;
  const position = projectLinks.findIndex(link => link.dataset.project === id);
  document.querySelector('#dialog-label').textContent = `Папка проекта / ${String(position + 1).padStart(2, '0')}`;
  dialog.scrollTop = 0;
  return true;
}

function openProject(id, trigger, updateHash = true) {
  if (typeof dialog.showModal !== 'function' || !renderProject(id)) return;
  lastTrigger = trigger || null;
  closeMenu();
  document.body.classList.add('dialog-open');
  if (!dialog.open) dialog.showModal();
  if (updateHash) history.pushState(null, '', `#project/${id}`);
}

if (typeof dialog.showModal === 'function') {
  document.querySelectorAll('a[data-project]').forEach(link => link.addEventListener('click', event => {
    if (event.ctrlKey || event.metaKey || event.shiftKey || event.altKey) return;
    event.preventDefault();
    openProject(link.dataset.project, link);
  }));
}
document.querySelector('#close-project').addEventListener('click', () => dialog.close());
dialog.addEventListener('click', event => { if (event.target === dialog) dialog.close(); });
dialog.addEventListener('close', () => {
  document.body.classList.remove('dialog-open');
  if (!preserveHashOnClose) history.replaceState(null, '', '#projects');
  preserveHashOnClose = false;
  lastTrigger?.focus({preventScroll: true});
  activeProject = null;
});

function changeProject(direction) {
  let links = projectLinks.filter(link => !link.closest('.project-card').hidden);
  if (!links.some(link => link.dataset.project === activeProject)) links = projectLinks;
  const index = links.findIndex(link => link.dataset.project === activeProject);
  const next = links[(index + direction + links.length) % links.length];
  renderProject(next.dataset.project);
  history.replaceState(null, '', `#project/${next.dataset.project}`);
}
document.querySelector('#previous-project').addEventListener('click', () => changeProject(-1));
document.querySelector('#next-project').addEventListener('click', () => changeProject(1));

function applyHash() {
  const hash = location.hash.slice(1);
  const id = hash.startsWith('project/') ? hash.slice(8) : hash;
  if (document.getElementById(`project-${id}`)) {
    openProject(id, null, false);
  } else if (dialog.open) {
    preserveHashOnClose = true;
    dialog.close();
  }
}
window.addEventListener('popstate', applyHash);
window.addEventListener('hashchange', applyHash);
applyHash();

const tabs = [...document.querySelectorAll('.toolbox-tabs [role="tab"]')];
const panels = [...document.querySelectorAll('.toolbox-panel')];
function selectTab(tab) {
  tabs.forEach(item => {
    const selected = item === tab;
    item.setAttribute('aria-selected', String(selected));
    item.tabIndex = selected ? 0 : -1;
  });
  panels.forEach(panel => {
    panel.hidden = panel.id !== tab.getAttribute('aria-controls');
    panel.setAttribute('role', 'tabpanel');
  });
}
tabs.forEach((tab, index) => {
  tab.addEventListener('click', () => selectTab(tab));
  tab.addEventListener('keydown', event => {
    const directions = {ArrowRight: 1, ArrowLeft: -1};
    let next;
    if (event.key in directions) next = (index + directions[event.key] + tabs.length) % tabs.length;
    else if (event.key === 'Home') next = 0;
    else if (event.key === 'End') next = tabs.length - 1;
    else return;
    event.preventDefault();
    selectTab(tabs[next]);
    tabs[next].focus();
  });
});
document.querySelector('.toolbox-tabs').hidden = false;
selectTab(tabs[0]);

const baselines = {
  page: {label: 'Page-RAG', accuracy: 51.5, correct: 141},
  visual: {label: 'Визуальный RAG', accuracy: 62.4, correct: 171},
  agent: {label: 'Без инструментов', accuracy: 69.7, correct: 191},
};
const formatAccuracy = value => value.toLocaleString('ru-RU', {minimumFractionDigits: 1, maximumFractionDigits: 1});
document.querySelectorAll('input[name="baseline"]').forEach(input => input.addEventListener('change', () => {
  const baseline = baselines[input.value];
  document.querySelector('#baseline-label').textContent = baseline.label;
  document.querySelector('#baseline-value').textContent = `${formatAccuracy(baseline.accuracy)}%`;
  document.querySelector('#baseline-bar').style.setProperty('--bar', `${baseline.accuracy}%`);
  document.querySelector('#baseline-answers').textContent = `${baseline.correct} из 274`;
  document.querySelector('#delta-value').replaceChildren(document.createTextNode(`+${formatAccuracy(91.6 - baseline.accuracy)} `), Object.assign(document.createElement('span'), {textContent: 'п.п.'}));
  document.querySelector('#delta-caption').textContent = `${251 - baseline.correct} дополнительных верных ответов`;
  document.querySelector('.comparison-chart').setAttribute('aria-label', `${baseline.label}: ${formatAccuracy(baseline.accuracy)}%. Итоговый агент: 91,6%.`);
}));

const copyEmail = document.querySelector('.copy-email');
if (navigator.clipboard?.writeText) {
  copyEmail.hidden = false;
  copyEmail.addEventListener('click', async () => {
    try {
      await navigator.clipboard.writeText('arturzaplatin@gmail.com');
      copyEmail.textContent = 'Скопировано ✓';
      document.querySelector('#copy-status').textContent = 'Email скопирован';
    } catch {
      document.querySelector('#copy-status').textContent = 'Не удалось скопировать email. Адрес указан рядом.';
    }
  });
}

let scrollFrame = 0;
function updateProgress() {
  const available = document.documentElement.scrollHeight - innerHeight;
  document.querySelector('.site-header').style.setProperty('--scroll', available > 0 ? Math.min(1,scrollY / available) : 0);
}
window.addEventListener('scroll', () => {
  if (scrollFrame) return;
  scrollFrame = requestAnimationFrame(() => { updateProgress(); scrollFrame = 0; });
}, {passive: true});
window.addEventListener('resize', updateProgress);
updateProgress();
const year = document.querySelector('#year');
if (year) year.textContent = String(new Date().getFullYear());

if ('IntersectionObserver' in window) {
  const sceneObserver = new IntersectionObserver(entries => entries.forEach(entry => {
    entry.target.classList.toggle('scene-running', entry.isIntersecting);
  }), {threshold: .1});
  document.querySelectorAll('.card-art').forEach(scene => sceneObserver.observe(scene));
}

const motionToggle = document.querySelector('.motion-toggle');
motionToggle.hidden = motionQuery.matches;
motionToggle.addEventListener('click', () => {
  const paused = document.body.classList.toggle('motion-paused');
  motionToggle.textContent = paused ? 'Включить анимацию ▶' : 'Пауза анимации Ⅱ';
});
motionQuery.addEventListener('change', () => { motionToggle.hidden = motionQuery.matches; });

// Three small workbench views: measured retrieval, illustrative vision and text.
const labTabs = [...document.querySelectorAll('.lab-tabs [role="tab"]')];
const labPanels = [...document.querySelectorAll('.lab-panel')];
function selectLab(tab) {
  labTabs.forEach(button => {
    const selected = button === tab;
    button.setAttribute('aria-selected', String(selected));
    button.tabIndex = selected ? 0 : -1;
  });
  labPanels.forEach(panel => {
    panel.hidden = panel.id !== tab.getAttribute('aria-controls');
    panel.setAttribute('role', 'tabpanel');
  });
}
labTabs.forEach((tab, index) => {
  tab.addEventListener('click', () => selectLab(tab));
  tab.addEventListener('keydown', event => {
    let next;
    if (event.key === 'ArrowRight') next = (index + 1) % labTabs.length;
    else if (event.key === 'ArrowLeft') next = (index - 1 + labTabs.length) % labTabs.length;
    else if (event.key === 'Home') next = 0;
    else if (event.key === 'End') next = labTabs.length - 1;
    else return;
    event.preventDefault();
    selectLab(labTabs[next]);
    labTabs[next].focus();
  });
});
if (labTabs.length) {
  document.querySelector('.lab-tabs').hidden = false;
  selectLab(labTabs[0]);
}

const retrievalResults = {
  bm25: {name: 'Точные слова и сущности', description: 'Лексический поиск хорошо находит даты, имена и редкие исторические термины.', recall: .7933, mrr: .7333},
  faiss: {name: 'Смысловые совпадения', description: 'Векторный поиск находит близкий смысл и переформулировки, но отдельно уступает BM25.', recall: .7467, mrr: .6280},
  rrf: {name: 'Лексика + смысл', description: 'RRF объединяет точные совпадения BM25 и смысловые совпадения FAISS.', recall: .82, mrr: .7867},
};
const retrievalButtons = [...document.querySelectorAll('[data-retrieval]')];
retrievalButtons.forEach(button => button.addEventListener('click', () => {
  const result = retrievalResults[button.dataset.retrieval];
  if (!result) return;
  retrievalButtons.forEach(item => item.setAttribute('aria-pressed', String(item === button)));
  document.querySelector('#retrieval-name').textContent = result.name;
  document.querySelector('#retrieval-description').textContent = result.description;
  document.querySelector('#retrieval-recall').textContent = result.recall.toLocaleString('ru-RU', {minimumFractionDigits: 4, maximumFractionDigits: 4});
  document.querySelector('#retrieval-mrr').textContent = result.mrr.toLocaleString('ru-RU', {minimumFractionDigits: 4, maximumFractionDigits: 4});
  document.querySelector('.retrieval-meter>span').style.setProperty('--recall', `${result.recall * 100}%`);
}));

const catalogExamples = {
  apple: {title: 'Яблоко', candidates: ['Яблоко Голден', 'Яблоко Гала', 'Груша Конференция'], note: 'Похожие товары находятся по визуальному представлению. Дальше — ранжирование и проверка.'},
  pear: {title: 'Груша', candidates: ['Груша Конференция', 'Груша Вильямс', 'Яблоко Голден'], note: 'Один каталог, разные визуальные признаки. Первый кандидат меняется вместе с образцом.'},
  unknown: {title: 'Товар вне каталога', candidates: [], note: 'Совпадение не подтверждено. Система должна отказаться от ответа и предложить проверку.'},
};
const productButtons = [...document.querySelectorAll('[data-product]')];
productButtons.forEach(button => button.addEventListener('click', () => {
  const key = button.dataset.product;
  const example = catalogExamples[key];
  if (!example) return;
  productButtons.forEach(item => item.setAttribute('aria-pressed', String(item === button)));
  document.querySelectorAll('[data-fruit]').forEach(item => { item.toggleAttribute('hidden', item.dataset.fruit !== key); });
  document.querySelector('.sample-camera svg').setAttribute('aria-label', `Иллюстрация: ${example.title}`);
  const candidates = document.querySelector('.sample-candidates');
  candidates.replaceChildren();
  const rows = example.candidates.length ? example.candidates : ['Нет подтверждённого совпадения'];
  rows.forEach((name, index) => {
    const row = document.createElement('li');
    const number = document.createElement('b');
    const title = document.createElement('span');
    const status = document.createElement('em');
    number.textContent = example.candidates.length ? String(index + 1).padStart(2, '0') : '—';
    title.textContent = name;
    status.textContent = !example.candidates.length ? 'проверить' : index ? 'кандидат' : 'выбран';
    row.append(number, title, status);
    candidates.append(row);
  });
  document.querySelector('#catalog-observation').textContent = example.note;
}));

const textExamples = {
  request: {
    title: 'Что важно в обращении?',
    source: 'Вчера я оформил заказ в приложении и выбрал доставку на утро. Оплата прошла, подтверждение пришло, но курьер так и не приехал. В поддержке сначала попросили подождать, а затем перестали отвечать. Мне нужно узнать, когда привезут заказ, или вернуть деньги, если доставка уже невозможна.',
    summary: 'Заказ оплачен, доставка не состоялась. Клиент просит сообщить срок доставки или вернуть деньги.',
    sentiment: 'негативная',
  },
  article: {
    title: 'Что важно в статье?',
    source: 'Команда тестирует прототип умных весов. Камера снимает продукт на платформе, а визуальная модель превращает изображение в вектор. Затем система ищет похожие объекты в каталоге и предлагает несколько кандидатов. После выбора товара сервис получает цену за килограмм и рассчитывает стоимость по массе. Чтобы расширить ассортимент, в каталог добавляют фотографии и описания новых продуктов.',
    summary: 'Умные весы ищут продукт по изображению и рассчитывают стоимость по массе. Ассортимент расширяется через каталог.',
    sentiment: 'нейтральная',
  },
};
let activeText = 'request';
let summaryVisible = false;
const textButtons = [...document.querySelectorAll('[data-text]')];
const summaryButton = document.querySelector('#summarize-example');
function renderTextExample() {
  const example = textExamples[activeText];
  document.querySelector('#text-source-title').textContent = example.title;
  document.querySelector('#text-source').textContent = example.source;
  document.querySelector('#text-summary').textContent = example.summary;
  document.querySelector('#text-source-count').textContent = `${example.source.length} символов`;
  const reduction = Math.round((1 - example.summary.length / example.source.length) * 100);
  document.querySelector('#text-summary-count').textContent = `${example.summary.length} символов / −${reduction}%`;
  document.querySelector('#text-sentiment').textContent = `Тональность: ${example.sentiment}`;
  document.querySelector('.summary-output').hidden = !summaryVisible;
  document.querySelector('.text-sample').classList.toggle('has-summary', summaryVisible);
  summaryButton.setAttribute('aria-pressed', String(summaryVisible));
  summaryButton.replaceChildren(document.createTextNode(summaryVisible ? 'Скрыть краткую версию ' : 'Показать краткую версию '), Object.assign(document.createElement('span'), {textContent: summaryVisible ? '↗' : '↘'}));
  textButtons.forEach(button => button.setAttribute('aria-pressed', String(button.dataset.text === activeText)));
}
textButtons.forEach(button => button.addEventListener('click', () => {
  activeText = button.dataset.text;
  summaryVisible = false;
  renderTextExample();
}));
summaryButton?.addEventListener('click', () => {
  summaryVisible = !summaryVisible;
  renderTextExample();
});
if (summaryButton) renderTextExample();
