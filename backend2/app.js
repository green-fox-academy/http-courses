var express = require('express');

var app = express();

app.get('/', function(req, res) {
    res.send('Csao ez a <strong>fooldal</strong>');
});

app.get('/alma', function(req, res) {
    res.send('Szia itt egy alma');
});

app.listen(8003);
