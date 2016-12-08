angular
    .module('appRoutes', ["ui.router"])
    .config(['$stateProvider', '$urlRouterProvider', function($stateProvider, $urlRouterProvider) {

    $stateProvider.state({
        name: 'stats',
        url: '/stats',
        templateUrl: 'public/components/stats/templates/stats.template',
        controller: 'StatsController'
    });

    $stateProvider.state({
        name: 'oauth',
        url: '/',
        templateUrl: 'public/components/oauth/templates/oauth.template',
        controller: 'OauthController'
    });

    $urlRouterProvider.otherwise('/');
}]);
