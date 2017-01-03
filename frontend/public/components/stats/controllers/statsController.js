angular.module('Stats')
    .controller('StatsController', ['$scope', '$location', 'StatsManager', 'StatsParser', 'StatsRenderData', function($scope, $location, StatsManager, StatsParser, StatsRenderData) {
        var params = $location.search();
        var accessToken = params['access_token'] || null;

        var statsManager = StatsManager.init(accessToken);

        $scope.groupSelected = undefined;
        $scope.groupList = undefined;

        $scope.init = function() {
            statsManager.loadGroups().then(function(result) {
                $scope.groupList = result;
            });
        };

        $scope.refresh = function() {
            if ($scope.groupSelected != undefined && $scope.startDate != undefined && $scope.endDate != undefined) {
                if ($scope.memberSelected == undefined) {
                    statsManager.loadMessages(
                        $scope.groupSelected.group_id,
                        $scope.startDate,
                        $scope.endDate,
                        "user"
                    ).then(function(result) {
                        var messagesData = StatsRenderData.messagesByUser(
                            StatsParser.countMessagesByUser(result)
                        );
                        $scope.refreshD3(messagesData);
                    });
                }
                else {
                    statsManager.loadMessages(
                        $scope.groupSelected.group_id,
                        $scope.startDate,
                        $scope.endDate,
                        "user_day"
                    ).then(function(result) {
                        var messagesData = StatsRenderData.messagesByUserDay(
                            StatsParser.countMessagesByUserDay(result, $scope.memberSelected.user_id),
                            $scope.startDate,
                            $scope.endDate
                        );
                        $scope.refreshD3(messagesData);
                    });
                }
            }
        };

        $scope.selectMember = function(member) {
            if ($scope.memberSelected == member) {
                $scope.memberSelected = undefined;
            }
            else {
                $scope.memberSelected = member;
            }
        };


        $scope.selectGroup = function(group) {
            $scope.memberSelected = undefined;
            $scope.groupSelected = group;
        };

        $scope.refreshD3 = function (messagesData) {
            $scope.d3options = {
                chart: {
                    type: 'multiBarHorizontalChart',
                    height: 450,
                    width: 700,
                    margin: {
                        left: 150
                    },
                    x: function(d) {
                       return d.label;
                    },
                    y: function(d) {
                        return d.value;
                    },
                    showControls: true,
                    showValues: true,
                    valueFormat: d3.format('d'),
                    duration: 500,
                    xAxis: {
                        showMaxMin: false
                    },
                    yAxis: {
                        axisLabel: 'Values',
                        tickFormat: function(d) {
                            return d;
                        }
                    }
                }
            };
            $scope.data = messagesData;
        };

   }]);
