function modifyValue(data) {
  data += 1;
  return data;
}

function modifyValues(data) {
  // for (let element of data) {
  //   element += 1;
  // }
  for (let i = 0; i < data.length; i++) {
    data[i] += 1;
  }
}

var number = 1;
number = modifyValue(number);
// console.log(number);

let array = [1, 2, 3];
modifyValues(array);
// console.log(array);

let alma = 'alma';
let korte = new String('korte');
korte = modifyValue(korte);
// console.log(korte);

// spread operator
// console.log(...array);

let user = {
  name: 'Jozsi',
  age: 20,
  gender: 'male',
  'szeme szine': 'kek',
}

// console.log(user);
// console.log(user.name);
// console.log(user['szeme szine']);

const field = 'age';
// console.log(user[field]);

// for (let key in user) {
//   console.log(key);
// }

// for (let key of Object.keys(user)) {
//   console.log(key);
// }

// for (let value of Object.values(user)) {
//   console.log(value);
// }

// for (let entry of Object.entries(user)) {
//   console.log(entry);
// }

// user['iskola'] = 'Green Fox';
// console.log(user);


// let [key, value] = ['name', 'Pisti'];
// console.log(key);
// console.log(value);

// object destructioring, objektum felbontas
// let {name, gender} = user;
// console.log(name);
// console.log(gender);

// console.log('van-e benne name mezo? ', Object.keys(user).includes('nev'));
let tomb = {};
tomb['alma'] = 'piros';
console.log(tomb);
