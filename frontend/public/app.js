'use strict';

var stats = angular.module("Stats", []);
var oauth = angular.module("Oauth", []);

angular.module('GroupmeStats', [
    'appRoutes',

    'Stats',
    'Oauth',
    'StatsService'
])

angular.module('GroupmeStats')
    .config(['$httpProvider', function($httpProvider) {
        $httpProvider.defaults.withCredentials = true;
    }]);
    
