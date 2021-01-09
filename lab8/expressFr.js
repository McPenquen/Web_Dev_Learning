var express = require('express');
var app = express();

app.get('/', function (req, res) {
    res.set('Content-Type', 'text/html');
    res.send(new Buffer('<h1> The root </h1>'));
});

app.get('/hello', function (req, res) {
    res.set('Content-Type', 'text/html');
    res.send(new Buffer('<h2> HIIIII! </h2>'));
});

app.get('/bye', function (req, res) {
    res.set('Content-Type', 'text/html');
    res.send(new Buffer('<p> BYE </p>'));
});

/*
// ROUTING
app.get('/', function (req, res) {
    res.send('A GET request to root');
});

app.post('/', function (req, res) {
    res.send('A POST request to root');
});

app.head('/', function (req, res) {
    res.send('A HEAD request to root');
});
*/
var server = app.listen(5000, "127.0.0.1", function () {
    var host = server.address().address;
    var port = server.address().port;

    console.log("Listening on http://%s:%s", host, port);
});