angular.module('Stats')
    .service('StatsManager', function(Groups, Messages) {
        var accessToken;
        return {
            init: function(accessToken) {
                this.accessToken = accessToken;
                return this;
            },

            loadMessages: function(groupId, startDate, endDate, bucketBy) {
                var startEpoch = new Date(startDate).getTime() / 1000;
                var endEpoch = new Date(endDate).getTime() / 1000;
                var countMessagesByUser = {};

                return Messages.query(this.accessToken, groupId, startEpoch, endEpoch, bucketBy).$promise.then(function(result) {
                    return result.data;
                });

            },

            loadGroups: function() {
                return Groups.query(this.accessToken).$promise.then(function(result) {
                    return result.data;
                });

            }

        };

    });

