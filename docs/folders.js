/* Shared by standalone case pages and folder contents cloned into the dialog. */
(() => {
  const rememberedSheets = new Map();
  const rememberedNodes = new Map();

  function keyboardCycle(event, buttons, select) {
    if (!['ArrowRight', 'ArrowLeft', 'Home', 'End'].includes(event.key)) return;
    event.preventDefault();
    const index = buttons.indexOf(event.currentTarget);
    const next = event.key === 'Home' ? 0 : event.key === 'End' ? buttons.length - 1
      : (index + (event.key === 'ArrowRight' ? 1 : -1) + buttons.length) % buttons.length;
    select(buttons[next]);
    buttons[next].focus();
  }

  window.initProjectFolders = (root = document) => {
    root.querySelectorAll('.project-folder').forEach(folder => {
      if (folder.dataset.initialized) return;
      folder.dataset.initialized = 'true';
      const id = folder.dataset.folder;
      const tabs = [...folder.querySelectorAll('[data-sheet]')];
      const panels = [...folder.querySelectorAll('[data-sheet-panel]')];
      const selectSheet = (button, scroll = false) => {
        tabs.forEach(tab => {
          const selected = tab === button;
          tab.setAttribute('aria-selected', String(selected));
          tab.tabIndex = selected ? 0 : -1;
        });
        panels.forEach(panel => { panel.hidden = panel.dataset.sheetPanel !== button.dataset.sheet; });
        rememberedSheets.set(id, button.dataset.sheet);
        if (scroll) {
          const selectedPanel = panels.find(panel => panel.dataset.sheetPanel === button.dataset.sheet);
          const barHeight = folder.closest('dialog')?.querySelector('.dialog-topbar')?.offsetHeight || 0;
          selectedPanel.style.scrollMarginTop = `${barHeight + folder.querySelector('.folder-sheet-tabs').offsetHeight + 10}px`;
          selectedPanel.scrollIntoView({block: 'start', behavior: 'instant'});
        }
      };
      tabs.forEach(tab => {
        tab.addEventListener('click', () => selectSheet(tab, true));
        tab.addEventListener('keydown', event => keyboardCycle(event, tabs, button => selectSheet(button, true)));
      });
      selectSheet(tabs.find(tab => tab.dataset.sheet === rememberedSheets.get(id)) || tabs[0]);

      const nodes = [...folder.querySelectorAll('[data-node]')];
      const notes = [...folder.querySelectorAll('[data-node-note]')];
      const selectNode = button => {
        nodes.forEach(node => node.setAttribute('aria-pressed', String(node === button)));
        notes.forEach(note => { note.hidden = note.dataset.nodeNote !== button.dataset.node; });
        rememberedNodes.set(id, button.dataset.node);
      };
      nodes.forEach(button => {
        button.addEventListener('click', () => selectNode(button));
        button.addEventListener('keydown', event => keyboardCycle(event, nodes, selectNode));
      });
      selectNode(nodes.find(node => node.dataset.node === rememberedNodes.get(id)) || nodes[0]);
      folder.classList.add('folder-interactive');
    });
  };

  const projectDialog = document.querySelector('#project-dialog');
  if (projectDialog && 'ResizeObserver' in window) {
    new ResizeObserver(entries => {
      projectDialog.style.setProperty('--folder-topbar', `${entries[0].target.offsetHeight}px`);
    }).observe(projectDialog.querySelector('.dialog-topbar'));
  }

  window.initProjectFolders();
})();
