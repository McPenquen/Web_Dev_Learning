// Execute in Node.js via: node.exe ../../Users/majda/MyCode/Web_Dev_Learning/docs/server.js

const { createServer } = require("http");

const PORT = process.env.PORT || 5000;

const server = createServer();

server.on("request", (request, response) => {
    response.end("ello");
    /*
    // REQUEST PAYLOAD
    if ( request.method === "POST") {
         let data = "";
            request.on("data", chunk => {
            data += chunk ;
         }) ;
        
         request.on("end", () => {
            try {
            const requestData = JSON.parse(data);
            requestData.ourMessage = "success";
            response.setHeader("Content-Type ", "application/json") ;
            response.end(JSON.stringify(requestData));
            } 
            catch (e) {
            response.statusCode = 400;
            response.end ("Invalid JSON");
            }
        }) ;
    } 
    else {
        response.statusCode = 400;
        response.end ("Please POST a JSON object") ;
    }


    // QUERY PARAMETERS
    const { query } = require("url").parse(request.url, true);
    if (query.name) {
        response.end(`You requested parameter name with value ${ query.name }`);
    }
    else {
        response.end("Hiya!");
    }
    
    // COOKIES
    response.setHeader("Set-Cookie", ["daka=dakadaka", "type=ninja", "name=santa"]);
    response.end(`Your cookies are: ${request.headers.cookie}`);
    
    // HTTP METHODS
    if ( request.method === "GET") {
        return response.end("Got a GET");
     }
     else if ( request.method === "POST") {
        return response.end("Got a POST");
     }
     else {
        resource.statusCode(400) ;
        return responsee.end("Method not supported");
     }

    
    // ROUTING
    switch(request.url) {
        case "/":
            response.end("HOMEPAGE");
            break;
        case "/about":
            response.end("ABOUT PAGE");
            break;
        default:
            response.statusCode = 404;
            response.end("PAGE NOT FOUND");
            break;
    }
    */
});

server.listen(PORT, () => {
    console.log(`Starting server at port ${PORT}`);
});
