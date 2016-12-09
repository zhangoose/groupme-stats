'use strict';

var stats = angular.module("Stats", ['720kb.datepicker', 'ngResource']);
var oauth = angular.module("Oauth", []);

angular.module('GroupmeStats', [
    'appRoutes',

    'Stats',
    'Oauth',
])

angular.module('GroupmeStats')
    .config(['$httpProvider', function($httpProvider) {
        $httpProvider.defaults.withCredentials = true;
    }]);
    
