'use strict';

var stats = angular.module("Stats", ['720kb.datepicker', 'ngResource', 'nvd3']);
var oauth = angular.module("Oauth", []);

angular.module('GroupmeStats', [
    'appRoutes',
    'nvd3',

    'Stats',
    'Oauth',
])

angular.module('GroupmeStats')
    .config(['$httpProvider', function($httpProvider) {
        $httpProvider.defaults.withCredentials = true;
    }]);
    
