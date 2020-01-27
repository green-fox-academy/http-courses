async function legnepszerubbEtel() {
  const valasz = await fetch('/api/legnepszerubb');
  const legnepszerubb = await valasz.json();
  const etelNev = legnepszerubb.etelNev;
  document.getElementById('legnepszerubb').innerHTML = etelNev;
}

async function vendegkonyv() {
  const bejegyzes = document.getElementById('bejegyzes').value;
  const valasz = await fetch('api/vendegkonyv', {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
      'Accept': 'application/json',
    },
    body: JSON.stringify({ bejegyzes }),
  });

  if (valasz.status == 200) {
    document.getElementById('bejegyzes').value = '';
    alert('Köszönjük a bejegyzését!');
  }
}

window.onload = legnepszerubbEtel();