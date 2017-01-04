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

                var sortedMessages = _.sortBy(messages, function(item) {
                    return -item.count; // descending order
                });
                
                for (var i in sortedMessages) {
                    var item = sortedMessages[i]
                    data[0]['values'].push({"label": item['name'], "value": item['count']});
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
                    var formattedDate = "".concat(currentDate.getFullYear() + "-" + ("0" + (currentDate.getMonth() + 1)).slice(-2) + "-" + ("0" + currentDate.getDate()).slice(-2));
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
