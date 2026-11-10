// Mobile menu
document.querySelectorAll('.menu-toggle').forEach(function (btn) {
  btn.addEventListener('click', function () {
    var nav = document.getElementById('site-nav');
    var open = nav.classList.toggle('open');
    btn.setAttribute('aria-expanded', open ? 'true' : 'false');
  });
});

// Forms: posts to the endpoint in the form's action (e.g. Formspree).
document.querySelectorAll('form.signup').forEach(function (form) {
  form.addEventListener('submit', function (e) {
    var action = form.getAttribute('action') || '';
    if (action.indexOf('YOUR_FORM_ID') !== -1) return; // not wired yet: let the browser handle it
    e.preventDefault();
    var status = form.querySelector('.form-status');
    var button = form.querySelector('button[type="submit"]');
    button.disabled = true;
    fetch(action, { method: 'POST', body: new FormData(form), headers: { 'Accept': 'application/json' } })
      .then(function (r) {
        if (!r.ok) throw new Error();
        form.reset();
        status.textContent = form.dataset.success || 'Sent. Andrew will be in touch within one business day.';
      })
      .catch(function () {
        status.textContent = 'That didn’t send. Check your connection and try again, or email hello@localaibootcamp.com.';
      })
      .finally(function () { button.disabled = false; });
  });
});
