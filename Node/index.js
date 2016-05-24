"use strict"

var 	express = require('express'),
		http = require('http'),
		PORT = 3000,
		bodyParser = require('body-parser'),
		Settings = require('./settings'),
		app = express();

app.use(bodyParser.json());
app.use(bodyParser.urlencoded({extended: true}));

require('./routes/Utils')(app);

var httpServer = http.Server(app).listen(Settings.httpPort, function() {console.log('Server running on port: '+Settings.httpPort)});

module.exports = app;