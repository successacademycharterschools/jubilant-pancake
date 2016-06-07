angular.module('MinimumEditDistance', [])
    .directive('medForm', function() {
        return {
            restrict: 'E',
            templateUrl: '/static/js/minimum-edit-distance/partials/med-form.html',
            controller: ['$scope', function($scope) {
                // Set our initial values
                this.str1 = '';
                this.str2 = '';

                this.submit_form = function() {
                    this.show_str1 = this.str1;
                    this.show_str2 = this.str2;
                    this.step_count = 10;
                };
            }],
            controllerAs: 'medCtrl'
        };
    });
