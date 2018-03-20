'use strict';
var alexa = require('alexa-app'); //require alexa app

module.change_code = 1; // Allow this module to be reloaded by hotswap when changed
var app = new alexa.app('temp-hty');
var DatabaseHelper = require('./database_helper');
var databaseHelper = new DatabaseHelper();


// Launch Intent
app.launch(function(req, res) {
  var prompt = "Hi there! I can check the temperature and humidity. What would you like to know?"
  res.say(prompt).reprompt(prompt).shouldEndSession(false);
});


// Temperature Intent
app.intent('temperatureIntent', function(req, res) {

  var reading = databaseHelper.readSensorValue();
  return reading.then(function(result) {
    res.say('Current temperature is ' + result[0] + ' celcius.');
  });
});


// Temperature Intent
app.intent('humidityIntent', function(req, res) {

  var reading = databaseHelper.readSensorValue();
  return reading.then(function(result) {
    res.say('Current humidity is ' + result[1] + ' percent.');
  });
});


// AMAZON YES Intent
app.intent('AMAZON.YesIntent',
  function(req, res) {
    var prompt = "Okay.";
    res.say(prompt);
  }
);


// AMAZON NO Intent
app.intent('AMAZON.NoIntent',
  function(req, res) {
    var response = "Okay.";
    res.say(response);
  }
);


// Help Intent
app.intent('AMAZON.HelpIntent',
  function(req, res) {
    var help = "You can ask me to check the temperature or humidity. If not, you can say stop to exit from the skill.";
    res.say(help).shouldEndSession(false);
  }
);


// Stop Intent
app.intent('AMAZON.StopIntent',
  function(req, res) {
    var goodbye = "Had a nice time talking to you. Goodbye.";
    res.say(goodbye);
  }
);


module.exports = app;