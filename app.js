(function() {
  var app = angular.module('jubilantPancake', []);
  
  app.controller('GetdistanceController', function(){
    var request = {
      "string1": "",
      "string2": ""
    },
    result = {
      "answer" : ""
    };

  });

  app.directive("getdistanceRequest", function() {
      return {
        restrict: 'E',
        templateUrl: "getdistance-form.html",
        controller: ['$http', function($http) {
          var endpoint = "supply-distance.php",
            result = {},
            submitted = false,
            error = false,
            errorMsg = "",
            formCtrl = this;
          this.inputFocus = function() {
            formCtrl.inputFocused = true;
          };
          this.inputBlur = function() {
            formCtrl.inputFocused = false;
          }
          this.getResult = function(data) {
            formCtrl.submitted = true;
            console.log(data.string1.length);
            console.log(data.string2.length);
            if (data.string1.length !== data.string2.length) {
              formCtrl.errorMsg = ": String1 and String2 must have matching lengths.";
              formCtrl.error = true;
            } else {
              formCtrl.error = false;
              $http.post('supply-distance.php', JSON.stringify(data)).success(function(data){
                formCtrl.result = data;
              }).error(function(data){
                formCtrl.errorMsg = ": " + data.error;
                formCtrl.error = true;
              }); 
            };
          };
        }],
        controllerAs: 'formCtrl'
      };
    }); 

})();
