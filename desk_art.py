"""Drafting-table graphics and project annotations, rendered as native HTML/SVG."""

if __package__:
    from .drafting_tools import TOOLS
else:
    from drafting_tools import TOOLS

BLUEPRINT = '''<div class="drawing-board">
  <div class="board-caption"><span>АЗ / ЛИСТ 001</span><span>РАБОЧАЯ СХЕМА · 2026</span></div>
  <h2>От данных<br />к решению.</h2>
  <div class="blueprint-map" aria-label="Данные, модель и проверка результата">
    <div class="blueprint-input"><span class="draft-label">01 / ВХОД</span><div>Текст<br />Изображение<br />Контекст</div></div>
    <span class="blueprint-arrow" aria-hidden="true">→</span>
    <div class="blueprint-model"><span>ML</span><i>+</i><span>LLM</span></div>
    <span class="blueprint-arrow" aria-hidden="true">→</span>
    <div class="blueprint-output"><span class="draft-label">02 / ПРОВЕРКА</span><div>Гипотеза<br />Эксперимент<br />Результат</div></div>
  </div>
  <div class="blueprint-links"><a href="./cases/vlm-agent.html" data-project="vlm-agent">Агенты <span>↗</span></a><a href="./cases/smart-scales.html" data-project="smart-scales">Зрение <span>↗</span></a><a href="./cases/ural-rag.html" data-project="ural-rag">Поиск <span>↗</span></a></div>
  <div class="blueprint-titleblock"><span>ПРОЕКТИРОВАНИЕ ML-СИСТЕМ</span><span>А. ЗАПЛАТИН</span><span>МАСШТАБ 1:1</span></div>
</div>'''

NOTES = {
    'vlm-agent': ('Изображение задания', 'Ответ + проверенный контекст', 'Собрал агентный цикл, фильтрацию контекста и MMR.', 'Слабый источник не должен менять верный ответ.', 'LangGraph · Qwen · FAISS', 'task'),
    'ural-rag': ('Исторические PDF', 'Ответ со ссылками', 'Подготовил корпус и сравнил пять методов поиска.', 'Точные даты и фамилии делают BM25 полезным даже рядом с embeddings.', 'BM25 · FAISS · RRF', 'archive'),
    'semantic-ids': ('Вектор объекта', 'Последовательность SID', 'Исследовал кодбуки, коллизии и покрытие каталога.', 'Идентификатор может хранить семантику объекта.', 'PyTorch · FAISS · HNSW', 'sid'),
    'smart-scales': ('Изображение + масса', 'Продукт → стоимость', 'Связал visual embeddings, каталог и FastAPI.', 'Новый товар можно добавить в каталог без переобучения классификатора.', 'DINOv2 · pgvector · FastAPI', 'scale'),
    'product-search': ('Фотография этикетки', 'Ранжированный каталог', 'Объединил визуальный и текстовый поиск через RRF.', 'Если товара нет в каталоге, системе нужен надёжный отказ.', 'YOLO · SigLIP2 · RRF', 'catalog'),
    'wine-recognition': ('Бутылка в кадре', 'OCR → сопоставление', 'Собрал модульный pipeline детекции, OCR и поиска.', 'Сложная этикетка требует fallback и дополнительной проверки.', 'YOLO · PaddleOCR · OpenCV', 'wine'),
    'deer-detection': ('Аэрофотоснимок', 'Детекция → подсчёт', 'Готовил разметку и разбирал ошибки на малых объектах.', 'Качество данных и пропущенные объекты важнее красивого кадра.', 'YOLO · OpenCV · PyTorch', 'aerial'),
    'nlp-service': ('Статья или комментарий', 'Краткий текст + тональность', 'Подготовил данные и обработку длинных документов.', 'Сокращение полезно, пока сохраняется ключевая информация.', 'Transformers · LangChain · Docker', 'text'),
    'trading-agent': ('Рыночная информация', 'Сигнал → действие → проверка', 'Исследовал агентные решения и управление состоянием.', 'Прогноз, действие и его последствия нужно оценивать вместе.', 'LLM · State · Risk control', 'market'),
}

FOLDER_LABELS = {
    'vlm-agent': 'VLM / АГЕНТ', 'ural-rag': 'RAG / УРАЛ',
    'semantic-ids': 'SID / ПОИСК', 'smart-scales': 'CV / ВЕСЫ',
    'product-search': 'CV / КАТАЛОГ', 'wine-recognition': 'OCR / ВИНО',
    'deer-detection': 'CV / БПЛА', 'nlp-service': 'NLP / ТЕКСТ',
    'trading-agent': 'AI / MOEX',
}


def specimen(kind):
    """Illustrative specimens are labelled; they are not claimed model outputs."""
    start = '<div class="specimen specimen-' + kind + '" aria-hidden="true"><span class="specimen-label">'
    if kind == 'task':
        return start + '''ЭСКИЗ ЗАДАНИЯ</span><svg viewBox="0 0 180 150" fill="none"><g stroke="currentColor" stroke-width="1.3"><path d="M29 116V30l120 86H29Z"/><path d="M29 102h14v14"/><path d="M14 28v89m-4-89h8m-8 89h8M29 134h120m-120-4v8m120-8v8"/></g><g fill="currentColor"><text x="3" y="77">6</text><text x="84" y="147">8</text><text x="102" y="63">?</text></g></svg><span class="specimen-foot">IMAGE → CONTEXT → ANSWER</span></div>'''
    if kind == 'archive':
        return ''
    if kind == 'sid':
        return start + '''СХЕМА ИДЕНТИФИКАТОРА</span><div class="specimen-vector">[ v₁ · v₂ · … · vₙ ]</div><div class="specimen-down">↓</div><div class="sid-tokens"><b>SID₁</b><b>SID₂</b><b>SID₃</b></div><span class="specimen-foot">SEMANTIC CODEBOOK</span></div>'''
    if kind == 'scale':
        return start + '''КАРТОЧКА КАТАЛОГА</span><svg viewBox="0 0 180 135" fill="none"><g stroke="currentColor" stroke-width="1.4"><path d="M92 38c-35-27-57 4-41 43 9 27 28 30 42 22 19 13 43-5 45-35 4-24-22-42-46-30Z"/><path d="M91 40c-2-16 5-24 13-28m-10 10c17-17 35-8 35-8-7 16-25 14-35 8Z"/><path d="M25 113h130v13H25Z"/></g></svg><span class="specimen-foot">64 СОРТА / IMAGE + WEIGHT</span></div>'''
    if kind in ('catalog', 'wine'):
        return start + ('ЭСКИЗ ЭТИКЕТКИ' if kind == 'wine' else 'ЭСКИЗ ТОВАРА') + '''</span><svg viewBox="0 0 180 150" fill="none"><g stroke="currentColor" stroke-width="1.2"><path d="M73 14h34v39l17 23v63H56V76l17-23Z"/><path d="M71 20h38m-34 12h30"/><rect x="64" y="90" width="52" height="33"/><path d="M70 103h40m-40 7h28m-28 7h35"/><path d="M47 66h13m-13 0v13m86-13h-13m13 0v13m-86 66h13m-13 0v-13m86 13h-13m13 0v-13" stroke="var(--accent)"/></g></svg><span class="specimen-foot">DETECT → READ → MATCH</span></div>'''
    if kind == 'aerial':
        return start + '''СХЕМА ДЕТЕКЦИИ</span><svg viewBox="0 0 180 145" fill="none"><g stroke="currentColor" opacity=".25"><path d="M0 28c65 50 105-35 180 9M0 48c65 50 105-35 180 9M0 68c65 50 105-35 180 9M0 88c65 50 105-35 180 9M0 108c65 50 105-35 180 9"/></g><g fill="currentColor"><ellipse cx="56" cy="63" rx="10" ry="4" transform="rotate(-20 56 63)"/><ellipse cx="127" cy="103" rx="10" ry="4" transform="rotate(-20 127 103)"/></g><g stroke="var(--accent)"><rect x="37" y="46" width="38" height="32"/><rect x="108" y="86" width="38" height="32"/></g></svg><span class="specimen-foot">МАЛЫЕ ОБЪЕКТЫ / UAV</span></div>'''
    if kind == 'text':
        return start + '''СХЕМА СУММАРИЗАЦИИ</span><div class="specimen-lines"><i></i><i></i><i></i><i></i><i></i><i></i></div><div class="specimen-down">↓</div><p>Главная мысль.<br />Коротко и по делу.</p><span class="specimen-foot">TEXT → SUMMARY</span></div>'''
    return start + '''ЦИКЛ АГЕНТА</span><div class="agent-loop"><span>Состояние</span><i>↓</i><span>Действие</span><i>↓</i><span>Проверка ↺</span></div><span class="specimen-foot">ТЕСТОВАЯ ТОРГОВАЯ СРЕДА</span></div>'''
