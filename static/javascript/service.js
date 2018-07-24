// define angular module/app
var formApp = angular.module('formApp', [])
	.config(function($interpolateProvider) {
		$interpolateProvider.startSymbol('//').endSymbol('//');
	});

// create angular controller and pass in $scope and $http
function formController($scope, $http) {

	// create a blank object to hold our form information
	$scope.formData = {};

	// process the form
	$scope.submitForm = function() {
		$http.post('http://127.0.0.1:5002/test_string', $scope.formData)
			.success(function(data) {
				$scope.result = data.moves;
			}
		);
	};

}