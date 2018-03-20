'use strict';
module.change_code = 1;
var SENSOR_DATA_TABLE_NAME = 'alexa_dht22'; // Table name

// connect to dynamo db
var credentials = {
  accessKeyId: '',
  secretAccessKey: ''
};
var dynasty = require('dynasty')(credentials);
// connect to dynamo db

function SensorDataHelper() {}

var DataTable = function() {
  return dynasty.table(SENSOR_DATA_TABLE_NAME);
};

// Read data from Dynamo
SensorDataHelper.prototype.readSensorValue = function() {
  return DataTable().findAll('01')
    .then(function(result) {
      var a = result.length;
      console.log(result[a - 1].data.state.reported)
      var temperature = result[a - 1].data.state.reported.temperature;
      var humidity = result[a - 1].data.state.reported.humidity;
      return [temperature, humidity];
    })
    .catch(function(error) {
      console.log('error from dynamo', error);
    });
};

module.exports = SensorDataHelper;