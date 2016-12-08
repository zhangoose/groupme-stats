angular.module('Stats')
    .controller('StatsController', ['$scope', '$location', 'Groups', 'Messages', function($scope, $location, Groups, Messages) {
        var params = $location.search();
        var accessToken = params['access_token'] || null;

        $scope.groupSelected = "";
        $scope.groupList = [];

        Groups.query(accessToken).$promise.then(function(result) {
            $scope.groupList = result.data;
        });

        $scope.loadMessages = function(groupId, startDate, endDate){
            Messages.query(accessToken, groupId, startDate, endDate, "user").$promise.then(function(result) {
                var messagesByUser = result.data;
                var countMessagesByUser = {};

                for (var userId in messagesByUser) {
                    var name = messagesByUser[userId][0]['name'];
                    var count = messagesByUser[userId].length;
                    countMessagesByUser[name] = count;

                }

                $scope.countMessagesByUser = countMessagesByUser;

            });
        };


   }]);
