"""Generate the portfolio homepage and individual project pages."""
import json
from hashlib import sha256
from html import escape
from pathlib import Path
if __package__:
    from .project_art import scene_body
    from .desk_art import TOOLS, BLUEPRINT, NOTES, FOLDER_LABELS, specimen
    from .project_sheets import folder_body
else:
    from project_art import scene_body
    from desk_art import TOOLS, BLUEPRINT, NOTES, FOLDER_LABELS, specimen
    from project_sheets import folder_body

REPO = Path(__file__).resolve().parent
DOCS = REPO / 'docs'
DATA = json.loads((DOCS / 'resume-data.json').read_text(encoding='utf-8'))

FEATURED = [
    dict(id='vlm-agent', number='01', title='VLM-агент с RAG по турецким учебникам', short='Агент, который умеет искать', category='LLM / VLM / AGENTIC RAG', context='ML-академия Яндекса · 2026', lead='Школьные задания по изображениям, поиск по учебникам и контроль найденного контекста.', metrics=[['91,6%', 'accuracy · 274 задания']], domains='llm retrieval', art='agent'),
    dict(id='ural-rag', number='02', title='RAG-система по истории Урала', short='История Урала. Поиск с источниками.', category='RETRIEVAL / RAG', context='Учебный проект · 2026', lead='1 433 PDF-страницы, пять методов поиска и единая оценка качества retrieval.', metrics=[['0,82', 'Recall@5 · Hybrid RRF']], domains='retrieval', art='archive'),
]
META = {
    'semantic-ids': ('retrieval', 'tokens', 'Семантика вместо обычного ID'),
    'smart-scales': ('vision retrieval', 'scales', 'Весы, которые видят продукт'),
    'product-search': ('vision retrieval', 'search', 'Найти товар по фотографии'),
    'wine-recognition': ('vision', 'wine', 'Прочитать этикетку. Найти вино.'),
    'deer-detection': ('vision', 'detection', 'Подсчитать оленей с высоты'),
    'nlp-service': ('llm', 'text', 'Меньше текста. Больше смысла.'),
    'trading-agent': ('llm', 'market', 'Агент в торговой среде'),
}


def artwork(kind):
    start = '<svg viewBox="0 0 600 300" fill="none" aria-hidden="true" focusable="false"><defs><pattern id="dots-' + kind + '" width="20" height="20" patternUnits="userSpaceOnUse"><circle cx="1" cy="1" r=".65" fill="currentColor" opacity=".25"/></pattern></defs><rect width="600" height="300" fill="url(#dots-' + kind + ')"/>'
    groups = {}
    if kind == 'agent':
        groups[kind] = '''<g stroke="currentColor" stroke-width="1.5">
          <g class="phone-device"><rect x="85" y="23" width="153" height="254" rx="23"/><rect x="98" y="53" width="127" height="184" rx="3"/><path d="M143 37h38m-36 220h34"/><circle cx="197" cy="37" r="3"/>
          <g opacity=".6"><path d="M113 77h73m-73 11h94m-94 11h82"/><path d="M120 192l31-64 44 64Z"/><path d="M151 128v64m-31-32h75"/><path d="M113 215h70m-70 10h93"/></g>
          <path class="phone-scan" d="M104 104h116" stroke-width="2"/><path d="M108 65h10m-10 0v10m107-10h-10m10 0v10m-107 151h10m-10 0v-10m107 10h-10m10 0v-10"/><rect class="phone-flash" x="99" y="54" width="125" height="182" fill="currentColor" stroke="none"/>
          </g><path class="signal-path" d="M255 150h68m88 0h57"/><circle cx="368" cy="150" r="45"/><circle class="vlm-ring" cx="368" cy="150" r="59" stroke-dasharray="2 8"/><rect x="469" y="107" width="55" height="74"/><path d="M478 96h55v75m-43-49h21m-21 13h21m-21 13h16"/></g>
          <g fill="currentColor"><text x="348" y="155">VLM</text><text x="93" y="296">PHONE / PHOTO</text><text x="322" y="246">AGENT → SEARCH</text></g>'''
    elif kind == 'archive':
        groups[kind] = '''<g class="industrial-sky" stroke="currentColor" stroke-width=".8" opacity=".22"><path d="M0 93h600M0 116h600M0 139h600"/><circle cx="485" cy="69" r="34"/><path d="M448 32l74 74m-74 0 74-74"/></g>
          <g class="factory-layer" stroke="currentColor" opacity=".44"><path d="M0 216V146l48-24v24l48-24v24l48-24v94M145 216v-63h120v63m-85-63V55h16v98m25 0V35h16v118M269 216V127l56-26v26l56-26v26l56-26v115M436 216v-58h163v58m-45-58V72h18v86"/><path d="M24 166v19m26-19v19m28-19v19m30-19v19m205-30v30m26-30v30m26-30v30m26-30v30m67-14v25m30-25v25m30-25v25"/></g>
          <g stroke="currentColor"><path d="M0 244h600M0 253h600" stroke-width="2"/><path class="rail-ties" d="M0 261h600" stroke-width="7" stroke-dasharray="2 20"/></g>
          <g class="steam-train" stroke="currentColor" stroke-width="1.7">
          <g class="train-smoke" opacity=".5"><circle class="smoke-one" cx="161" cy="111" r="12"/><circle class="smoke-two" cx="184" cy="87" r="18"/><circle class="smoke-three" cx="215" cy="60" r="24"/></g>
          <path class="train-body" d="M106 201v-21c0-24 18-32 36-32h105v-39h60v92H106Z" fill="var(--scene-paper)"/><path d="M247 109l-10-10h81l-11 10M160 148v-27h21v27M153 119h34M121 163h109m-107 12h107m-107 12h107M264 124h26v33h-26Zm-12 48h38m-140 29h110m-135-23-13 37h33m-1-33h-15m162 19h23"/>
          <path d="M330 147h111v63H330Zm-7-6h126m-111 20h18v32h-18m28-32h18v32h-18m28-32h18v32h-18M309 209h20m112 0h13" fill="var(--scene-paper)"/>
          <g class="train-wheel" transform="translate(153 221)"><g class="wheel-rotor"><circle r="20" fill="var(--scene-paper)"/><circle r="5"/><path d="M-15 0h30M0-15v30M-11-11l22 22M-11 11l22-22"/></g></g>
          <g class="train-wheel" transform="translate(205 221)"><g class="wheel-rotor"><circle r="20" fill="var(--scene-paper)"/><circle r="5"/><path d="M-15 0h30M0-15v30M-11-11l22 22M-11 11l22-22"/></g></g>
          <g class="train-wheel" transform="translate(276 223)"><g class="wheel-rotor"><circle r="17" fill="var(--scene-paper)"/><circle r="4"/><path d="M-13 0h26M0-13v26"/></g></g>
          <g class="train-wheel" transform="translate(348 223)"><g class="wheel-rotor"><circle r="17" fill="var(--scene-paper)"/><path d="M-13 0h26M0-13v26"/></g></g>
          <g class="train-wheel" transform="translate(423 223)"><g class="wheel-rotor"><circle r="17" fill="var(--scene-paper)"/><path d="M-13 0h26M0-13v26"/></g></g><path class="piston" d="M153 221h52" stroke-width="3"/>
          </g><g fill="currentColor"><text x="24" y="32">URAL / INDUSTRIAL ARCHIVE</text><text x="25" y="287">DOCUMENTS → RETRIEVAL → SOURCES</text></g>'''
    else:
        groups[kind] = scene_body(kind)
    return start + groups[kind] + '</svg>'


def project_body(item):
    original = None
    if item['id'] in ('vlm-agent', 'ural-rag'):
        original = (DOCS / 'project-content' / (item['id'] + '.html')).read_text(encoding='utf-8')
    return folder_body(item, artwork(item['art']), NOTES[item['id']], original)


def build_site():
    css_version = sha256((DOCS / 'styles.css').read_bytes()).hexdigest()[:12]
    desk_version = sha256((DOCS / 'desk.css').read_bytes()).hexdigest()[:12]
    script_version = sha256((DOCS / 'app.js').read_bytes()).hexdigest()[:12]
    folder_style_version = sha256((DOCS / 'folders.css').read_bytes()).hexdigest()[:12]
    folder_script_version = sha256((DOCS / 'folders.js').read_bytes()).hexdigest()[:12]
    projects = FEATURED + [dict(p, domains=META[p['id']][0], art=META[p['id']][1], display_title=META[p['id']][2]) for p in DATA['projects']]
    cards, templates = [], []
    cases = DOCS / 'cases'
    cases.mkdir(exist_ok=True)
    for i, item in enumerate(projects):
        value, label = item['metrics'][0] if item['metrics'] else ('AI', 'автономный агент')
        title = item.get('display_title', item['short'])
        featured = ' project-card-featured' if i < 2 else ''
        incoming, outgoing, contribution, observation, stack, sample = NOTES[item['id']]
        lead = item['lead'] if i < 2 else contribution
        score_sheet = ''
        if item['id'] == 'smart-scales':
            scores = ''.join(f'<div><span>{escape(k)}</span><strong>{escape(v)}</strong><i style="--score:{v.replace(",", ".")}" aria-hidden="true"></i></div>' for v, k in item['metrics'])
            score_sheet = f'<figure class="card-score-sheet"><figcaption>ПРОВЕРОЧНЫЙ ЛИСТ / ПОИСК ПО КАТАЛОГУ</figcaption><div>{scores}</div></figure>'
        cards.append(f'''<article class="project-card reveal{featured}" id="{item['id']}" data-domains="{item['domains']}">
          <a class="project-card-link" href="./cases/{item['id']}.html" data-project="{item['id']}" data-title="{escape(item['title'])}">
            <span class="folder-tab" aria-hidden="true"><span>ДЕЛО {item['number']}</span><b>{FOLDER_LABELS[item['id']]}</b></span>
            <div class="card-topline"><span>ЛИСТ {item['number']} / {escape(item['category'])}</span><span class="card-arrow" aria-hidden="true">↗</span></div>
            <div class="card-visual"><div class="card-art scene-{item['art']}">{artwork(item['art'])}</div>{specimen(sample)}<div class="visual-register"><span>ВХОД → МЕТОД → РЕЗУЛЬТАТ</span><span>{item['number']} / 09</span></div></div>
            <div class="card-info"><p>{escape(item['context'])}</p><h3>{escape(title)}</h3><p class="card-lead">{escape(lead)}</p><dl class="card-io"><div><dt>Вход</dt><dd>{escape(incoming)}</dd></div><div><dt>Выход</dt><dd>{escape(outgoing)}</dd></div></dl><div class="card-result"><strong>{escape(value)}</strong><span>{escape(label)}</span></div><p class="card-stack">{escape(stack)}</p><span class="card-action">Открыть папку · 4 листа <i aria-hidden="true">↗</i></span></div>
          </a><aside class="card-margin"><span>НА ПОЛЯХ / {item['number']}</span><p>{escape(observation)}</p></aside>{score_sheet}</article>''')
        body = project_body(item)
        # Prefix SVG pattern IDs so cloned dialog content cannot conflict with card graphics.
        dialog_body = body.replace('dots-', 'detail-dots-')
        templates.append(f'<template id="project-{item["id"]}">{dialog_body}</template>')
        page = f'''<!doctype html><html lang="ru"><head><meta charset="UTF-8"/><meta name="viewport" content="width=device-width,initial-scale=1"/><title>{escape(item['title'])} — Артур Заплатин</title><meta name="description" content="{escape(item['lead'])}"/><link rel="stylesheet" href="../styles.css?v={css_version}"/><link rel="stylesheet" href="../desk.css?v={desk_version}"/><link rel="stylesheet" href="../folders.css?v={folder_style_version}"/><link rel="icon" href="../assets/artur-engraving.png"/></head><body class="case-page drafting-table"><nav class="case-page-nav"><a href="../index.html#projects">← Все проекты</a><a href="../Artur_Zaplatin_Resume.pdf">Резюме PDF ↗</a></nav><main>{dialog_body}</main><footer class="case-page-nav"><a href="../index.html#projects">← Вернуться к портфолио</a><a href="mailto:arturzaplatin@gmail.com">Обсудить проект ↗</a></footer><script src="../folders.js?v={folder_script_version}"></script></body></html>'''
        (cases / (item['id'] + '.html')).write_text(page, encoding='utf-8', newline='\n')

    groups = [
        ('llm', 'LLM / NLP', 'Модели с контекстом и инструментами.', 'Обучение языковых моделей, работа с контекстом и агентные циклы.', [0, 3]),
        ('vision', 'Computer Vision', 'От изображения — к пониманию.', 'Детекция, визуальные представления, OCR и поиск по каталогу.', [2]),
        ('retrieval', 'Retrieval / RecSys', 'Найти то, что действительно нужно.', 'Гибридный поиск, семантические идентификаторы и оценка выдачи.', [1]),
        ('ml', 'ML / Data', 'Качество начинается с данных.', 'Подготовка данных, классические модели и корректные эксперименты.', [4, 7]),
        ('engineering', 'Engineering', 'Довести модель до сервиса.', 'API, воспроизводимые окружения, обработка данных и контроль качества.', [5, 6]),
    ]
    tabs, panels = [], []
    for i, (gid, label, title, description, indices) in enumerate(groups):
        tabs.append(f'<button role="tab" id="tab-{gid}" type="button" aria-controls="panel-{gid}" aria-selected="{str(i==0).lower()}" tabindex="{0 if i==0 else -1}">{label}</button>')
        pills = ''.join(f'<span>{escape(tech.strip())}</span>' for n in indices for tech in DATA['skills'][n][1].split('·'))
        panels.append(f'<section class="toolbox-panel" id="panel-{gid}" data-tab="{gid}" aria-labelledby="tab-{gid}"><div><span class="toolbox-number">0{i+1}</span><h3>{title}</h3><p>{description}</p></div><div class="tech-cloud">{pills}</div></section>')
    practice = ''.join(f'<article><span>0{i+1}</span><h3>{escape(title)}</h3><p>{escape(body)}</p></article>' for i,(title,body) in enumerate(DATA['practice']))
    source = (REPO / 'templates' / 'index.html').read_text(encoding='utf-8')
    for token, value in [('PROJECT_CARDS', '\n'.join(cards)), ('PROJECT_TEMPLATES', '\n'.join(templates)), ('SKILL_TABS', ''.join(tabs)), ('SKILL_PANELS', ''.join(panels)), ('PRACTICE', practice), ('STYLE_VERSION', css_version), ('DESK_VERSION', desk_version), ('SCRIPT_VERSION', script_version), ('FOLDER_STYLE_VERSION', folder_style_version), ('FOLDER_SCRIPT_VERSION', folder_script_version), ('DRAFTING_TOOLS', TOOLS), ('BLUEPRINT', BLUEPRINT)]:
        source = source.replace('{{' + token + '}}', value)
    (DOCS / 'index.html').write_text(source, encoding='utf-8', newline='\n')


if __name__ == '__main__':
    build_site()
