let paragraphs = document.getElementsByClassName('bekezdes');
for (let p of paragraphs) {
  p.innerHTML = parseInt(p.innerHTML) + 1;
}

const cim = document.getElementById('cim').innerHTML;
console.log(cim);
