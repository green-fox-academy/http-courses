window.onload = domManipulation();

function domManipulation() {
  let paragraphs = document.getElementsByClassName('bekezdes');
  let paragraphs2 = document.querySelectorAll('.bekezdes, .masik');

  for (let p of paragraphs2) {
    p.innerHTML = parseInt(p.innerHTML) + 1;
    p.onclick = () => alert(p.innerHTML);
  }

  paragraphs2[paragraphs2.length - 1].innerHTML += '<a href="#">link</a>';

  const link = document.createElement('a');
  link.innerHTML = 'link2';
  link.href = 'http://index.hu';
  paragraphs2[paragraphs2.length - 1].appendChild(link);

  const cim = document.getElementById('cim').innerHTML;
}

function printHello() {
  console.log('hello');
}
