// not working.. why?

var http = require("http") , fs = require("fs");

http.createServer(function (request, response) {
    request.on("end", function () {
        fs.readFile("test.txt", 'utf-8', function (error, data) {
            response.writeHead(200 , {
                'Content-Type' : 'text/plain'
            }) ;
            data = parseInt(data) + 1;
            fs.writeFile('test.txt', data);
            response.end('This page was refreshed ' + data + ' times!');
        }) ;
    }) ;
}).listen(5000);