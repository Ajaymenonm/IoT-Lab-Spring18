// Node Red Flow to Turn LED On/Off

[  
  {  
    "id":"8e199d6b.b135",
    "type":"tab",
    "label":"Flow 1",
    "disabled":true,
    "info":"Turn LED On/Off"
  },
  {  
    "id":"7314e523.756edc",
    "type":"rpi-gpio out",
    "z":"8e199d6b.b135",
    "name":"LED",
    "pin":"12",
    "set":true,
    "level":"0",
    "freq":"",
    "out":"out",
    "x":510,
    "y":200,
    "wires":[  

    ]
  },
  {  
    "id":"4692f155.e2b36",
    "type":"inject",
    "z":"8e199d6b.b135",
    "name":"ON",
    "topic":"",
    "payload":"1",
    "payloadType":"str",
    "repeat":"",
    "crontab":"",
    "once":false,
    "onceDelay":0.1,
    "x":110,
    "y":120,
    "wires":[  
      [  
        "7314e523.756edc",
        "43300d71.3767d4"
      ]
    ]
  },
  {  
    "id":"a78ff070.1a043",
    "type":"inject",
    "z":"8e199d6b.b135",
    "name":"OFF",
    "topic":"",
    "payload":"0",
    "payloadType":"str",
    "repeat":"",
    "crontab":"",
    "once":false,
    "onceDelay":0.1,
    "x":110,
    "y":260,
    "wires":[  
      [  
        "7314e523.756edc",
        "f3569fb7.c546a"
      ]
    ]
  },
  {  
    "id":"f3569fb7.c546a",
    "type":"debug",
    "z":"8e199d6b.b135",
    "name":"",
    "active":true,
    "tosidebar":true,
    "console":false,
    "tostatus":false,
    "complete":"false",
    "x":400,
    "y":320,
    "wires":[  

    ]
  },
  {  
    "id":"43300d71.3767d4",
    "type":"debug",
    "z":"8e199d6b.b135",
    "name":"",
    "active":true,
    "tosidebar":true,
    "console":false,
    "tostatus":false,
    "complete":"false",
    "x":400,
    "y":80,
    "wires":[  

    ]
  }
]


//=============================================================================================================================


// Node Red Flow to Control LED by Push Button

[  
  {  
    "id":"f6c34028.093cc",
    "type":"tab",
    "label":"Flow 2",
    "disabled":true,
    "info":"Control LED by Push Button"
  },
  {  
    "id":"e1543d87.df913",
    "type":"rpi-gpio out",
    "z":"f6c34028.093cc",
    "name":"LED",
    "pin":"12",
    "set":true,
    "level":"0",
    "freq":"",
    "out":"out",
    "x":930,
    "y":280,
    "wires":[  

    ]
  },
  {  
    "id":"c1cef1e1.f8537",
    "type":"rpi-gpio in",
    "z":"f6c34028.093cc",
    "name":"Button",
    "pin":"16",
    "intype":"up",
    "debounce":"25",
    "read":false,
    "x":270,
    "y":220,
    "wires":[  
      [  
        "9ab8ba3e.940e78"
      ]
    ]
  },
  {  
    "id":"9ab8ba3e.940e78",
    "type":"switch",
    "z":"f6c34028.093cc",
    "name":"if input is 1",
    "property":"payload",
    "propertyType":"msg",
    "rules":[  
      {  
        "t":"eq",
        "v":"1",
        "vt":"str"
      },
      {  
        "t":"else"
      }
    ],
    "checkall":"true",
    "repair":false,
    "outputs":2,
    "x":470,
    "y":280,
    "wires":[  
      [  
        "20a6ebf8.8e8d34"
      ],
      [  
        "1226d9a9.573f76"
      ]
    ]
  },
  {  
    "id":"20a6ebf8.8e8d34",
    "type":"change",
    "z":"f6c34028.093cc",
    "name":"change to 0",
    "rules":[  
      {  
        "t":"set",
        "p":"payload",
        "pt":"msg",
        "to":"0",
        "tot":"str"
      }
    ],
    "action":"",
    "property":"",
    "from":"",
    "to":"",
    "reg":false,
    "x":710,
    "y":220,
    "wires":[  
      [  
        "e1543d87.df913"
      ]
    ]
  },
  {  
    "id":"1226d9a9.573f76",
    "type":"change",
    "z":"f6c34028.093cc",
    "name":"change to 1",
    "rules":[  
      {  
        "t":"set",
        "p":"payload",
        "pt":"msg",
        "to":"1",
        "tot":"str"
      }
    ],
    "action":"",
    "property":"",
    "from":"",
    "to":"",
    "reg":false,
    "x":710,
    "y":340,
    "wires":[  
      [  
        "e1543d87.df913"
      ]
    ]
  }
]


//=============================================================================================================================


// Node Red Flow to Log weather data to Evernote on click of a button

[  
  {  
    "id":"2f3719c8.080526",
    "type":"tab",
    "label":"Flow 3",
    "disabled":true,
    "info":"Log weather data to Evernote on click of a button"
  },
  {  
    "id":"a9ce2ef8.8f0f9",
    "type":"rpi-gpio in",
    "z":"2f3719c8.080526",
    "name":"Button",
    "pin":"7",
    "intype":"up",
    "debounce":"25",
    "read":false,
    "x":70,
    "y":200,
    "wires":[  
      [  
        "d12f2bd8.d29b08"
      ]
    ]
  },
  {  
    "id":"d12f2bd8.d29b08",
    "type":"switch",
    "z":"2f3719c8.080526",
    "name":"if input is 1",
    "property":"payload",
    "propertyType":"msg",
    "rules":[  
      {  
        "t":"eq",
        "v":"1",
        "vt":"str"
      }
    ],
    "checkall":"true",
    "repair":false,
    "outputs":1,
    "x":170,
    "y":260,
    "wires":[  
      [  
        "f38006ae.ed4f18"
      ]
    ]
  },
  {  
    "id":"f38006ae.ed4f18",
    "type":"change",
    "z":"2f3719c8.080526",
    "name":"change to 0",
    "rules":[  
      {  
        "t":"set",
        "p":"payload",
        "pt":"msg",
        "to":"0",
        "tot":"str"
      }
    ],
    "action":"",
    "property":"",
    "from":"",
    "to":"",
    "reg":false,
    "x":270,
    "y":320,
    "wires":[  
      [  
        "810f0567.9a3b48"
      ]
    ]
  },
  {  
    "id":"810f0567.9a3b48",
    "type":"openweathermap",
    "z":"2f3719c8.080526",
    "name":"",
    "wtype":"current",
    "lon":"",
    "lat":"",
    "city":"New York City",
    "country":"USA",
    "language":"en",
    "x":390,
    "y":380,
    "wires":[  
      [  
        "21ab889e.f3f538"
      ]
    ]
  },
  {  
    "id":"21ab889e.f3f538",
    "type":"function",
    "z":"2f3719c8.080526",
    "name":"Format Payload",
    "func":"msg.payload = {\n\"value1\":msg.payload.tempc+\" C\",\n\"value2\":msg.payload.tempk+\" K\",\n\"value3\":msg.payload.location\n}\nreturn msg;",
    "outputs":1,
    "noerr":0,
    "x":530,
    "y":440,
    "wires":[  
      [  
        "ef9b5fe6.c5def"
      ]
    ]
  },
  {  
    "id":"ef9b5fe6.c5def",
    "type":"http request",
    "z":"2f3719c8.080526",
    "name":"IFTTT Endpoint",
    "method":"POST",
    "ret":"txt",
    "url":"https://maker.ifttt.com/trigger/{Event}/with/key/{SecretKey}",
    "tls":"",
    "x":620,
    "y":500,
    "wires":[  
      [  
        "64fc53d4.30cd4c"
      ]
    ]
  },
  {  
    "id":"64fc53d4.30cd4c",
    "type":"debug",
    "z":"2f3719c8.080526",
    "name":"",
    "active":true,
    "tosidebar":true,
    "console":false,
    "tostatus":false,
    "complete":"false",
    "x":700,
    "y":560,
    "wires":[  

    ]
  }
]


//=============================================================================================================================


// Node Red Flow to Send distance measured by Ultrasonic Sensor as a mobile SMS

[  
  {  
    "id":"38d582b5.896bee",
    "type":"tab",
    "label":"Flow 4",
    "disabled":true,
    "info":"Send distance measured by Ultrasonic Sensor as a mobile SMS"
  },
  {  
    "id":"b143d55e.95aa78",
    "type":"inject",
    "z":"38d582b5.896bee",
    "name":"Trigger",
    "topic":"",
    "payload":"",
    "payloadType":"date",
    "repeat":"",
    "crontab":"",
    "once":false,
    "onceDelay":0.1,
    "x":270,
    "y":180,
    "wires":[  
      [  
        "bfc167fa.dc9c68"
      ]
    ]
  },
  {  
    "id":"bfc167fa.dc9c68",
    "type":"exec",
    "z":"38d582b5.896bee",
    "command":"python3 workspace/a.py",
    "addpay":true,
    "append":"",
    "useSpawn":"false",
    "timer":"",
    "oldrc":false,
    "name":"Ultrasonic Sensor",
    "x":370,
    "y":260,
    "wires":[  
      [  
        "ac9e94cc.7e2928"
      ],
      [  

      ],
      [  

      ]
    ]
  },
  {  
    "id":"ac9e94cc.7e2928",
    "type":"rbe",
    "z":"38d582b5.896bee",
    "name":"",
    "func":"rbe",
    "gap":"",
    "start":"",
    "inout":"out",
    "property":"payload",
    "x":490,
    "y":360,
    "wires":[  
      [  
        "4452c53d.f1271c",
        "241f68ff.dc4408"
      ]
    ]
  },
  {  
    "id":"4452c53d.f1271c",
    "type":"debug",
    "z":"38d582b5.896bee",
    "name":"",
    "active":true,
    "tosidebar":true,
    "console":false,
    "tostatus":false,
    "complete":"false",
    "x":720,
    "y":260,
    "wires":[  

    ]
  },
  {  
    "id":"241f68ff.dc4408",
    "type":"twilio out",
    "z":"38d582b5.896bee",
    "twilio":"59425d80.e10a44",
    "twilioType":"sms",
    "url":"",
    "number":"203631xxxx",
    "name":"Send SMS",
    "x":710,
    "y":440,
    "wires":[  

    ]
  },
  {  
    "id":"59425d80.e10a44",
    "type":"twilio-api",
    "z":"",
    "name":"Axxx",
    "sid":"AC0346d16d9e8xxxxxxxx461869b405",
    "from":"+1203654xxxx"
  }
]