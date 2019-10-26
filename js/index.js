window.onload = callbackExample();

function callbackExample() {
  let xhr = new XMLHttpRequest();
  xhr.open('GET', 'https://jsonplaceholder.typicode.com/users', true);
  xhr.send();

  xhr.onload = () => {
    console.log('aaa');
  
    if (xhr.status == 200) {
      console.log('most erkezett meg az adat');
    
      let users = JSON.parse(xhr.responseText);
      let ul = document.getElementById('users');

      for (let user of users) {
        const li = document.createElement('li');
        li.innerText = user.name;
        ul.appendChild(li);
      }
    }
  };
  console.log('most kuldtuk el a requestet');
}

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
