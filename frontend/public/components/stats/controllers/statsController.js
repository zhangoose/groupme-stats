angular.module('Stats')
    .controller('StatsController', ['$scope', '$location', 'StatsManager', function($scope, $location, StatsManager) {
        var params = $location.search();
        var accessToken = params['access_token'] || null;

        var statsManager = StatsManager.init(accessToken);

        $scope.groupSelected = undefined;
        $scope.groupList = undefined;

        statsManager.loadGroups().then(function(result) {
            $scope.groupList = result;
        });

        $scope.refresh = function() {
            if ($scope.groupSelected != undefined && $scope.startDate != undefined && $scope.endDate != undefined) {
                statsManager.loadMessages(
                    $scope.groupSelected.group_id,
                    $scope.startDate,
                    $scope.endDate,
                    "user"
                ).then(function(result) {
                    $scope.countMessagesByUser = result;
                });
            }
        };

        $scope.selectGroup = function(group) {
            $scope.groupSelected = group;
        };


   }]);
