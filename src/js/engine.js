/**
* interface to the backend, as a service
*/
'use strict';

module.exports = function ($http, $q, $log) {
    var service = {
        calculate: calculate,
    };

    return service;

    function calculate (input1, input2) {
        var deferred = $q.defer();  // the promise that this function returns
        $http.post(
            '/calculate',
            {
                v1: input1,
                v2: input2,
            }
        ).then(
            function ondone (response) {
                deferred.resolve(response);
            },
            function onfail (response) {
                deferred.reject(response);
            }
        );
        return deferred.promise;
    }
}
