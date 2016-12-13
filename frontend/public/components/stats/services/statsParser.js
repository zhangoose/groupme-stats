angular.module('Stats')
    .service('StatsParser', function() {
        return {
            countMessagesByUser: function(messagesByUser) {
                var countMessagesByUser = {};

                for (var userId in messagesByUser) {
                    var name = messagesByUser[userId][0]['name'];
                    var count = messagesByUser[userId].length;
                    countMessagesByUser[name] = count;
                }
                return countMessagesByUser;
            },
            
            countMessagesByUserDay: function(messagesByUserDay, userId) {
                var countMessagesByUserDay = {};

                var messagesByDay = messagesByUserDay[userId];
                for (var day in messagesByDay) {
                    countMessagesByUserDay[day] = messagesByDay[day].length;
                }
                return countMessagesByUserDay;
            }
            
        };

    });
