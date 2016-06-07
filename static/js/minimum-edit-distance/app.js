angular.module('MinimumEditDistance', [])
    .factory('medService', ['$http', function($http) {
        return {
            calculate: function(str1, str2) {
                return $http({
                    method: 'POST',
                    url: '/api/edit-distance/',
                    data: JSON.stringify({
                        str1: str1,
                        str2: str2
                    })
                })
            }
        }
    }])
    .directive('medForm', function() {
        return {
            restrict: 'E',
            templateUrl: '/static/js/minimum-edit-distance/partials/med-form.html',
            controller: ['medService', function(medService) {
                // Alias our this value so we can use it in nested scopes
                ctrl = this;

                // Set our initial values
                ctrl.str1 = '';
                ctrl.str2 = '';

                ctrl.submit_form = function() {
                    medService.calculate(ctrl.str1, ctrl.str2).then(function onSuccess(response) {
                        ctrl.show_results = true;
                        ctrl.show_str1 = ctrl.str1;
                        ctrl.show_str2 = ctrl.str2;
                        ctrl.step_count = response.data.steps;
                    });
                };
            }],
            controllerAs: 'medCtrl'
        };
    });
