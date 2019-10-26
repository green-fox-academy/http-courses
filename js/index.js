let paragraphs = document.getElementsByClassName('bekezdes');
let paragraphs2 = document.querySelectorAll('.bekezdes');

for (let p of paragraphs2) {
  p.innerHTML = parseInt(p.innerHTML) + 1;
}

const cim = document.getElementById('cim').innerHTML;
console.log(cim);
