angular.module('Stats')
    .factory('Groups', function($resource) {
        return {
            query: function(accessToken) {
                return $resource(
                    "http://localhost:5000/".concat('groups'),
                    {},
                    {
                        "query": {
                            method: "GET",
                            headers: {
                                "Content-Type": "application/json",
                                "Access-Control-Allow-Credentials": true,
                                "Authorization": accessToken
                            }

                        }
                    }
                ).query();
            }
        }
    })

    .factory('Messages', function($resource) {
        return {
            query: function(accessToken, groupId, startDate, endDate, bucketBy) {
                return $resource(
                    "http://localhost:5000/".concat('groups/', groupId, '/messages'),
                    {},
                    {
                        "query": {

                            method: "GET",
                            headers: {
                                "Content-Type": "application/json",
                                "Access-Control-Allow-Credentials": true,
                                "Authorization": accessToken
                            },
                            params: {
                                "bucket_by": bucketBy,
                                "start_date": startDate,
                                "end_date": endDate
                            }
                        }

                    }
                ).query()

           }
        }


    });



