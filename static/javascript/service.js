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

		// if no variables are entered or the formData is empty, then we do not make a service call
		if (Object.keys($scope.formData).length == 0 || ($scope.formData.str1 == '' && $scope.formData.str2 == '')) {
			$scope.result = 'You have to enter two strings to calculate the edit distance';
			return false;
		}

		$http.post('http://127.0.0.1:5002/test_string', $scope.formData)
			.success(function(data) {
				$scope.result = data.moves + ' moves would be needed';
			}
		);
	};

}