// RelicTrek — Main JavaScript (Pure C Edition)
// Handles: language switch, ticker, mobile menu, search

document.addEventListener('DOMContentLoaded', function() {

  // ============================================
  // LANGUAGE SWITCHER
  // ============================================
  const savedLang = localStorage.getItem('relictrek-lang') || 'en';
  document.body.classList.add('lang-' + savedLang);

  document.querySelectorAll('.lang-switch button').forEach(btn => {
    if (btn.dataset.lang === savedLang) btn.classList.add('active');

    btn.addEventListener('click', function() {
      const lang = this.dataset.lang;
      document.body.classList.remove('lang-en', 'lang-zh');
      document.body.classList.add('lang-' + lang);
      localStorage.setItem('relictrek-lang', lang);

      document.querySelectorAll('.lang-switch button').forEach(b => b.classList.remove('active'));
      this.classList.add('active');
    });
  });

  // ============================================
  // TICKER — duplicate track for seamless loop
  // ============================================
  const tickerTrack = document.querySelector('.ticker-track');
  if (tickerTrack) {
    // Clone all children and append for infinite scroll
    const items = Array.from(tickerTrack.children);
    items.forEach(item => {
      const clone = item.cloneNode(true);
      tickerTrack.appendChild(clone);
    });
  }

  // ============================================
  // MOBILE MENU
  // ============================================
  const menuToggle = document.querySelector('.menu-toggle');
  const leftSidebar = document.querySelector('.left-sidebar');

  if (menuToggle) {
    menuToggle.addEventListener('click', () => {
      leftSidebar.classList.toggle('open');
    });
  }

  // Close sidebar when clicking outside on mobile
  document.addEventListener('click', (e) => {
    if (window.innerWidth <= 768 && leftSidebar && leftSidebar.classList.contains('open')) {
      if (!leftSidebar.contains(e.target) && e.target !== menuToggle) {
        leftSidebar.classList.remove('open');
      }
    }
  });

  // ============================================
  // SEARCH
  // ============================================
  const searchInput = document.querySelector('input[type="search"]');
  if (searchInput) {
    searchInput.addEventListener('keydown', (e) => {
      if (e.key === 'Enter') {
        const term = searchInput.value.toLowerCase().trim();
        if (!term) return;

        const links = document.querySelectorAll('.quick-nav a, .item-card');
        for (const link of links) {
          const text = (link.textContent || link.querySelector('h3')?.textContent || '').toLowerCase();
          if (text.includes(term)) {
            const href = link.getAttribute('href');
            if (href) { window.location.href = href; return; }
          }
        }
        const msgEn = 'Item not found. Try: ankh shield, zenith, cell phone...';
        const msgZh = '未找到物品。试试：ankh shield, zenith, cell phone...';
        alert(savedLang === 'zh' ? msgZh : msgEn);
      }
    });
  }

  // ============================================
  // HIGHLIGHT CURRENT PAGE IN QUICK NAV
  // ============================================
  const currentFile = window.location.pathname.split('/').pop();
  document.querySelectorAll('.quick-nav a').forEach(link => {
    const href = link.getAttribute('href');
    if (href === currentFile || href === './' + currentFile || href === currentFile + '.html') {
      link.style.color = 'var(--accent)';
      link.style.fontWeight = '600';
    }
  });
});
