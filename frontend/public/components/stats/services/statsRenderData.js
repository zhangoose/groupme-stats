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

            messagesByUserDay: function(messages, startDate, endDate) {
                var data = [
                    {
                        "key": "Posts by day",
                        "color": color,
                        "values": []
                    }
                ];
                for (var day in messages) {
                    data[0]['values'].push({"label": day, "value": messages[day]});
                }

                return data;
            }

        };

    });
