/* ─────────────────────────────────────────────
   Pandey Eatery — script.js
   ───────────────────────────────────────────── */

// ── CHAT PANEL TOGGLE ──────────────────────────

function initChatUi() {
  const chatFab     = document.getElementById('chat-fab');
  const chatPanel   = document.getElementById('chat-panel');
  const chatClose   = document.getElementById('chat-close');
  const heroChatBtn = document.getElementById('hero-order-btn');
  const navChatBtn  = document.getElementById('open-chat-btn');
  const contactBtn  = document.getElementById('contact-chat-btn');

  if (!chatFab || !chatPanel || !chatClose) return;

  function openChat() {
    chatPanel.classList.add('open');
    chatPanel.style.opacity = '1';
    chatPanel.style.transform = 'scale(1) translateY(0)';
    chatFab.style.transform = 'scale(0.92)';
  }

  function closeChat() {
    chatPanel.classList.remove('open');
    chatPanel.style.opacity = '';
    chatPanel.style.transform = '';
    chatFab.style.transform = '';
  }

  function isChatTrigger(target) {
    return Boolean(target.closest('#hero-order-btn, #open-chat-btn, #contact-chat-btn, .add-to-chat, #chat-fab'));
  }

  chatFab.addEventListener('click', (e) => {
    e.stopPropagation();
    chatPanel.classList.contains('open') ? closeChat() : openChat();
  });

  chatClose.addEventListener('click', (e) => {
    e.stopPropagation();
    closeChat();
  });

  heroChatBtn?.addEventListener('click', (e) => {
    e.preventDefault();
    e.stopPropagation();
    openChat();
  });

  navChatBtn?.addEventListener('click', (e) => {
    e.preventDefault();
    e.stopPropagation();
    openChat();
  });

  contactBtn?.addEventListener('click', (e) => {
    e.preventDefault();
    e.stopPropagation();
    openChat();
  });

  document.addEventListener('click', (e) => {
    if (
      chatPanel.classList.contains('open') &&
      !chatPanel.contains(e.target) &&
      !isChatTrigger(e.target)
    ) {
      closeChat();
    }
  });
}

if (document.readyState === 'loading') {
  document.addEventListener('DOMContentLoaded', initChatUi);
} else {
  initChatUi();
}


// ── TOAST ──────────────────────────────────────

function showToast(msg, duration = 3000) {
  const toast = document.getElementById('toast');
  toast.textContent = msg;
  toast.classList.add('show');
  setTimeout(() => toast.classList.remove('show'), duration);
}


// ── QUANTITY CONTROLS ──────────────────────────

document.querySelectorAll('.menu-card').forEach(card => {
  const minusBtn  = card.querySelector('.qty-btn.minus');
  const plusBtn   = card.querySelector('.qty-btn.plus');
  const qtyValue  = card.querySelector('.qty-value');
  const addBtn    = card.querySelector('.add-to-chat');
  const itemName  = card.dataset.item;

  minusBtn.addEventListener('click', () => {
    const current = parseInt(qtyValue.textContent);
    if (current > 1) qtyValue.textContent = current - 1;
  });

  plusBtn.addEventListener('click', () => {
    const current = parseInt(qtyValue.textContent);
    if (current < 20) qtyValue.textContent = current + 1;
  });

  addBtn.addEventListener('click', () => {
    const qty = parseInt(qtyValue.textContent);
    const label = qty === 1 ? itemName : `${qty} ${itemName}`;

    // Copy suggestion text to clipboard for easy pasting into chatbot
    const suggestion = qty === 1
      ? `I want 1 ${itemName}`
      : `I want ${qty} ${itemName}`;

    navigator.clipboard.writeText(suggestion).catch(() => {});

    showToast(`💬 "${suggestion}" copied — paste it into Quicky!`);
    openChat();

    // Reset qty to 1 after adding
    qtyValue.textContent = 1;
  });
});


// ── NAVBAR SCROLL EFFECT ──────────────────────

window.addEventListener('scroll', () => {
  const navbar = document.querySelector('.navbar');
  if (window.scrollY > 60) {
    navbar.style.boxShadow = '0 2px 20px rgba(0,0,0,0.3)';
  } else {
    navbar.style.boxShadow = 'none';
  }
});


// ── SCROLL REVEAL (lightweight) ──────────────

const revealTargets = document.querySelectorAll(
  '.menu-card, .about-inner, .contact-card, .contact-cta'
);

const observer = new IntersectionObserver((entries) => {
  entries.forEach(entry => {
    if (entry.isIntersecting) {
      entry.target.style.opacity    = '1';
      entry.target.style.transform  = 'translateY(0)';
      observer.unobserve(entry.target);
    }
  });
}, { threshold: 0.1 });

revealTargets.forEach(el => {
  el.style.opacity   = '0';
  el.style.transform = 'translateY(24px)';
  el.style.transition = 'opacity 0.5s ease, transform 0.5s ease';
  observer.observe(el);
});