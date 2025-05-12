async function requestAPI(path, data) {
  const res = await fetch(path, {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify(data)
  });
  return res.json();
}

// Login
document.getElementById('loginForm')?.addEventListener('submit', async e => {
  e.preventDefault();
  const email = e.target.email.value;
  const password = e.target.password.value;
  const result = await requestAPI('/api/login', { email, password });
  if (result.success) {
    window.location.href = 'dashboard.html';
  } else {
    alert(result.message);
  }
});

// Signup
document.getElementById('signupForm')?.addEventListener('submit', async e => {
  e.preventDefault();
  const name = e.target.name.value;
  const email = e.target.email.value;
  const password = e.target.password.value;
  const result = await requestAPI('/api/signup', { name, email, password });
  if (result.success) {
    window.location.href = 'dashboard.html';
  } else {
    alert(result.message);
  }
});

// Forgot password
document.getElementById('forgotForm')?.addEventListener('submit', async e => {
  e.preventDefault();
  const email = e.target.email.value;
  const result = await requestAPI('/api/forgot', { email });
  alert(result.message);
});
