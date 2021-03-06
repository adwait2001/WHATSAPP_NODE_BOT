const express = require('express');
const bodyParser = require('body-parser');
const app = express();
const port = process.env.PORT || 1500;
const {spawn} = require("child_process");
const{PythonShell}=require("python-shell")

app.use(bodyParser.json())
app.get('/',(req,res)=>{
  res.send('HEY')
})
app.post('/my_webhook_url', (req, res)=> {
    var inboundPayload = req.body;
    var event = inboundPayload.type; // get event type: user-event, message-event or message
    if(event == "user-event" && inboundPayload.payload.type == "sandbox-start")//To successfully set callback URL
    {
      // API documentation - https://www.gupshup.io/developer/docs/bot-platform/guide/whatsapp-api-documentation#events
      res.status(200).send();
    }else if(event == "message-event")//This event can be specifically used to get message notification,
    {
      // ------ Handle message-event types: enqueued, failed, sent, delivered, read, etc.
      // API documentation - https://www.gupshup.io/developer/docs/bot-platform/guide/whatsapp-api-documentation#events
    }else if(event == "message")// Get incoming message
    {
      // API documentation - https://www.gupshup.io/developer/docs/bot-platform/guide/whatsapp-api-documentation#InboundMessage
      var senderPhoneNumber = inboundPayload.payload.sender.phone
      var message = inboundPayload.payload.payload.text;
      if(!message =="" && message){
        //Get user message and reply same message back to user - echo bot
        // Using Send message API
      //   const pyProg = spawn('python',["./nlp_main/adwaitprblm.py",message]);
      //   pyProg.stdout.on('data', function(data) {
      //     console.log('inside')
      //     sendMessage(senderPhoneNumber,data.toString(), () =>{
      //       res.status(200).send();
      //     });
      // });

      let options = { 
        mode: 'text', 
        pythonOptions: ['-u'], // get print results in real-time 
        args: [message,senderPhoneNumber] //An argument which can be accessed in the script using sys.argv[1] 
    }; 
      
  
    PythonShell.run('./nlp_main/sender.py', options, function (err, result){ 
          if (err) throw err; 
          // result is an array consisting of messages collected  
          //during execution of script. 
          // console.log('result: ', result.toString()); 
          res.send() 
    }); 
       
      }
    }  
    
});

app.listen(port, ()=> {
    console.log("Server is up on port " + port)
})

function sendMessage(recepientNumber, message, callback){
  var request = require('request');
  var options = {
      'method': 'POST',
      'url': 'https://api.gupshup.io/sm/api/v1/msg',
      'headers': {
          'Content-Type': 'application/x-www-form-urlencoded',
          'apikey': '8w3nskoooe0rznmewrjlcec2eltfvfpx'
      },
      form: {
          'channel': 'whatsapp',
          'source': '917834811114', //This is the Sandbox number
          'destination': recepientNumber,
          'src.name': 'adwait2020',
          'message.payload': message
      }
  };
  request(options, function(error, response) {
      if (error) throw new Error(error);
      callback();
  });
}