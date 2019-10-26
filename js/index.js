let paragraphs = document.getElementsByClassName('bekezdes');
for (let p of paragraphs) {
  // console.log(p.innerHTML);
  console.log(p.textContent);
  
  p.innerHTML = parseInt(p.innerHTML) + 1;
}
console.log(paragraphs);
