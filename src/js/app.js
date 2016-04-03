/**
 * Angular entry point
 */
'use strict';

require('angular');
require('angular-cookies');
require('angular-material');
require('angular-animate');
require('angular-aria');
require('angular-messages');
require('angular-sanitize');

// ngSanitize: handles the html content of the help popover
angular
    .module('app', ['ngMaterial', 'ngCookies', 'ngSanitize'])
    .controller('main', ['$scope', '$mdDialog', '$mdToast', '$log', 'engine', require('./main.js')])
    .factory('engine', ['$http', '$q', '$log', require('./engine.js')])  // service for backend communications
;
