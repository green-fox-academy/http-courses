async function legnepszerubbEtel() {
  const valasz = await fetch('/api/legnepszerubb');
  const legnepszerubb = await valasz.json();
  const etelNev = legnepszerubb.etelNev;
  document.getElementById('legnepszerubb').innerHTML = etelNev;
}

window.onload = legnepszerubbEtel();