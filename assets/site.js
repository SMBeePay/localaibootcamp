// Mobile menu
document.querySelectorAll('.menu-toggle').forEach(function (btn) {
  btn.addEventListener('click', function () {
    var nav = document.getElementById('site-nav');
    var open = nav.classList.toggle('open');
    btn.setAttribute('aria-expanded', open ? 'true' : 'false');
  });
});

// Forms: posts to FormSubmit, which emails each submission to the inbox in the form's action.
document.querySelectorAll('form.signup').forEach(function (form) {
  form.addEventListener('submit', function (e) {
    var action = form.getAttribute('action') || '';
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
        status.textContent = 'That didn’t send. Check your connection and try again, or email andrew@localaibootcamp.com.';
      })
      .finally(function () { button.disabled = false; });
  });
});
