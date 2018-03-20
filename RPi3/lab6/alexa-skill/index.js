'use strict';
module.change_code = 1;

// requiring alexa-app and aws-sdk module
var alexa = require('alexa-app');
var app = new alexa.app('iot');
var AWS = require('aws-sdk');

// Constructing an IotData object
var iotdata = new AWS.IotData({
  region: 'us-east-1',
  endpoint: 'xxxxxxxxxxxxxxxxxxxxxxxxxxxx',
  apiVersion: '2015-05-28'
});


// launch request
app.launch(function(req, res) {
  res.say("Hi there! I can help you turn on or turn off your light. What would you like me to do?").shouldEndSession(false);
});


// intent request to turn led On
app.intent('switchOnIntent',
  function(req, res) {
    var prompt;

    let promise = new Promise((resolve, reject) => {
      var params = {
        topic: 'alexa-rpi',
        payload: "On",
        qos: 0
      };
      // publish payload to the topic
      iotdata.publish(params, function(err, data) {
        if (err) {
          console.log(err, err.stack);
        } else {
          console.log(data);
          res.say('Done! Your light is on')
          resolve()
        }
      });
    });
    return promise.then((successMessage) => {});
  }
);


// intent request to turn led On
app.intent('switchOffIntent',
  function(req, res) {
    var prompt;

    let promise = new Promise((resolve, reject) => {
      var params = {
        topic: 'alexa-rpi',
        payload: "Off",
        qos: 0
      };
      // publish payload to the topic
      iotdata.publish(params, function(err, data) {
        if (err) {
          console.log(err, err.stack);
        } else {
          console.log(data);
          res.say('Okay. I just did!')
          resolve()
        }
      });
    });
    return promise.then((successMessage) => {});
  }
);


module.exports = app;