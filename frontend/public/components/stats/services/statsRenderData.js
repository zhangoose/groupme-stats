angular.module('Stats')
    .service('StatsRenderData', function() {
        var color = "#cfe1fd";
        return {
            messagesByUser: function(messages) {
                var data = [
                    {
                        "key": "Posts by person",
                        "color": color,
                        "values": []
                    }
                ];
                
                for (var user in messages) {
                    data[0]['values'].push({"label": user, "value": messages[user]});
                }
                return data;

            },

            messagesByUserDay: function(messages, start, end) {
                var data = [
                    {
                        "key": "Posts by day",
                        "color": color,
                        "values": []
                    }
                ];
                var endDate = new Date(end);
                var currentDate = new Date(start);

                while (currentDate.getTime() <= endDate.getTime()) {
                    var formattedDate = "".concat(currentDate.getFullYear() + "-" + (currentDate.getMonth() + 1) + "-" + ("0" + currentDate.getDate()).slice(-2));
                    data[0]['values'].push({
                        "label": formattedDate,
                        "value": (messages[formattedDate] != undefined ? messages[formattedDate] : 0)
                    });
                    currentDate = new Date(currentDate.getTime() + 86400000);
                }
                return data;
            }

        };

    });
