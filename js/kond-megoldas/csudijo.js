window.onload = legnepszerubb();

async function legnepszerubb() {
  let response = await fetch('/api/legnepszerubb', {
    method: 'GET',
    headers: {
      'Accept': 'application/json'
    }
  });
  let legnepszerubbEtel = await response.json();
  document.getElementById('legnepszerubb').innerHTML = legnepszerubbEtel.etelNev;
}

async function vendegkonyv() {
  const bejegyzes = document.getElementById('bejegyzes').value;
  let response = await fetch('/api/vendegkonyv', {
    method: 'POST',
    body: JSON.stringify({bejegyzes}),
    headers: {
      'Content-Type': 'application/json',
      'Accept': 'application/json'
    }
  });

  if (response.status == 200) {
    document.getElementById('bejegyzes').value = '';
    alert('Köszönjük a bejegyzését!');
  }
}