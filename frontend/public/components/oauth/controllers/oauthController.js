angular.module('Oauth')
    .controller('OauthController', function($scope, CLIENT_ID) {
        $scope.clientId = CLIENT_ID
    });
