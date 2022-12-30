const uri = 'http://jsonplaceholder.typicode.com/users';

let h =new Headers();
h.append('Cookie','application=json');

let req = new Request(uri, {
    method: 'GET',
    headers: h,

});

fetch(req, {
    method: 'GET',
    credentials: 'include'
  })
    .then((response) => response.json())
    .then((json) => {
      console.log(" document.cookie = 'key=value';");
    }).catch((err) => {
      console.log(err);
  });