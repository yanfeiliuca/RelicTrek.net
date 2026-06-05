// RelicTrek — Main JavaScript
// Handles: language switch (page navigation), ticker, mobile menu, search

document.addEventListener('DOMContentLoaded', function() {

  // ============================================
  // LANGUAGE SWITCHER — Page Navigation Mode
  // ============================================
  // IMPORTANT: RelicTrek uses SEPARATE HTML pages for EN/ZH.
  // Clicking a language button NAVIGATES to the other language page.
  // This is NOT a JS text-swap system.

  // Set active button based on body class (set server-side in HTML)
  const isZhPage = document.body.classList.contains('lang-zh');

  document.querySelectorAll('.lang-switch button').forEach(btn => {
    const btnLang = btn.dataset.lang;

    // Set active class based on current page language
    if ((btnLang === 'zh' && isZhPage) || (btnLang === 'en' && !isZhPage)) {
      btn.classList.add('active');
    } else {
      btn.classList.remove('active');
    }

    // Language buttons use onclick in HTML for navigation.
    // This JS only handles the visual active state.
    // NO event listeners added — onclick in HTML handles the actual navigation.
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
