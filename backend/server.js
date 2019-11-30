var http = require('http');

var server = http.createServer(function(req, res) {
  console.log('na nezd valami tortent');
  res.end();
});

server.listen(8003);