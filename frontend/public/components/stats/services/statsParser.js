angular.module('Stats')
    .service('StatsParser', function() {
        return {
            countMessagesByUser: function(messagesByUser) {
                /**
                 * Returns in the form of:
                 * [
                 *   {
                 *     "name": (str),
                 *     "count": (int)
                 *   },
                 *   ....
                 * ]
                 */
                var countMessagesByUser = [];

                for (var userId in messagesByUser) {
                    var name = messagesByUser[userId][0]['name'];
                    var count = messagesByUser[userId].length;
                    countMessagesByUser.push({"name": name, "count": count});
                }
                return countMessagesByUser;
            },
            
            countMessagesByUserDay: function(messagesByUserDay, userId) {
                /**
                 * Returns in the form of:
                 * {
                 *   "YYYY-MM-DD": (int),
                 *   ...
                 * }
                 */
                var countMessagesByUserDay = {};

                var messagesByDay = messagesByUserDay[userId];
                for (var day in messagesByDay) {
                    countMessagesByUserDay[day] = messagesByDay[day].length;
                }
                return countMessagesByUserDay;
            }
            
        };

    });
