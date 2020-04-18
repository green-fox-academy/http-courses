var http = require('http');

var server = http.createServer(function (req, res) {
  console.log('Nezd mar, egy http keres');
  res.end();
});

server.listen(8003);

