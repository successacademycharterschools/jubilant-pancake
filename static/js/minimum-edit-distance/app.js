angular.module('MinimumEditDistance', [])
    .controller('MinimumEditDistanceController', function() {
        console.log('loaded controller');
    })
    .directive('medForm', function() {
        return {
            restrict: 'E',
            templateUrl: '/static/js/minimum-edit-distance/partials/med-form.html',
            controller: ['$scope', function($scope) {
                this.click_me = function() { alert('clicked me!'); };
            }],
            controllerAs: 'medCtrl'
        };
    });
