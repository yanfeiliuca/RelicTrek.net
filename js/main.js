// RelicTrek — Main JavaScript
// Handles: language switch, ticker, mobile menu, search

document.addEventListener('DOMContentLoaded', function() {

  // ============================================
  // LANGUAGE SWITCHER
  // ============================================

  function applyLanguage(lang) {
    // Update all elements with data-en / data-zh attributes
    document.querySelectorAll('[data-en][data-zh]').forEach(el => {
      el.textContent = el.getAttribute('data-' + lang);
    });

    // Update placeholders
    document.querySelectorAll('[data-en-placeholder][data-zh-placeholder]').forEach(el => {
      el.placeholder = el.getAttribute('data-' + lang + '-placeholder');
    });

    // Update document lang attribute
    document.documentElement.lang = lang === 'zh' ? 'zh-CN' : 'en';
  }

  // Detect current page language: check body class first, then localStorage
  const bodyLang = document.body.classList.contains('lang-zh') ? 'zh' :
                    document.body.classList.contains('lang-en') ? 'en' : null;
  const savedLang = bodyLang || localStorage.getItem('relictrek-lang') || 'en';

  // Apply saved language on load
  applyLanguage(savedLang);
  // Only add lang class if body doesn't already have one
  if (!bodyLang) {
    document.body.classList.add('lang-' + savedLang);
  }

  // Set active button based on detected language
  document.querySelectorAll('.lang-switch button').forEach(btn => {
    if (btn.dataset.lang === savedLang) btn.classList.add('active');

    btn.addEventListener('click', function() {
      const lang = this.dataset.lang;
      const prevLang = document.body.classList.contains('lang-en') ? 'en' : 'zh';
      if (lang === prevLang) return;

      // Switch
      document.body.classList.remove('lang-en', 'lang-zh');
      document.body.classList.add('lang-' + lang);
      localStorage.setItem('relictrek-lang', lang);

      // Apply translations
      applyLanguage(lang);

      // Update active button
      document.querySelectorAll('.lang-switch button').forEach(b => b.classList.remove('active'));
      this.classList.add('active');
    });
  });

  // ============================================
  // TICKER — duplicate track for seamless loop
  // ============================================
  const tickerTrack = document.querySelector('.ticker-track');
  if (tickerTrack) {
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
        const currentLang = document.body.classList.contains('lang-zh') ? 'zh' : 'en';
        const msgEn = 'Item not found. Try: ankh shield, zenith, cell phone...';
        const msgZh = '\u672a\u627e\u5230\u7269\u54c1\u3002\u8bd5\u8bd5\uff1aankh shield, zenith, cell phone...';
        alert(currentLang === 'zh' ? msgZh : msgEn);
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
