(function () {

    'use strict';

    var JubilantPancake = angular.module('JubilantPancakeApp', []);


    JubilantPancake.controller('PancakeForm', ['$scope', '$http', function ($scope, $http) {

        var api_url = '/edit_distance';

        $scope.calculateEditDistance = function () {
            var form_data = JSON.stringify({
                a: $scope.input1,
                b: $scope.input2,
            });
            $http.post(api_url, form_data).then(function successCallback(response) {
                $scope.result = response.data.result;
            }, function errorCallback(response) {
                $scope.result = response.data.error;
            });
        };
    }]);


}());