var persistent = false,
    has_websocket = 'WebSocket' in this,
    session = null,
    counter = 0,
    clients = [];

onconnect = function (e) {
   var port = e.ports[0];
   clients.push(port);
   port.onmessage = function (e) {

      if(e.data === "setPersistent") {
         persistent = true;
         if(session === null) {
            session = new WebSocket("ws://127.0.0.1:8000/echo");
         }
         session.onmessage = function(msg) { port.postMessage(msg.data); };
      } else if(e.data === "readPersistent") {
        port.postMessage(persistent);
        session.onmessage = function(msg) { port.postMessage(msg.data); };
      } else {
          session.send(JSON.stringify(e.data));
          session.onmessage = function(msg) {
              clients.forEach(function(client){
                  console.log(msg)
                  client.postMessage(msg.data);
              });
          };
      }
   };
};

