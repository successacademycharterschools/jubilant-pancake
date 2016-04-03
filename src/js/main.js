/**
 * main application controller
 */
'use strict';

module.exports = function ($scope, $mdDialog, $mdToast, $log, engine) {
    /**
     * @engine: service that communicates to the backend
     */
    var vm = this;
    vm.fabOpen = false;  // controls the visibility of the help fab
    vm.calculate = calculate;
    vm.showHelp = showHelp;
    vm.textInput1 = 'Alabama';
    vm.textInput2 = 'West Virginia';

    function calculate () {
        /**
         * calls a service to get the calculated distance from the backend
         */
        vm.distance = null;
        engine
            .calculate(vm.textInput1, vm.textInput2)
            .then(
                function ondone (response) {
                    vm.distance = response.data.distance;
                    showResult(vm.distance);
                },
                function onfail (response) {
                    toastError('Error ' + response.status + ': ' + response.statusText);
                }
            )
        ;
    }

    function showHelp () {
        /**
         * pop-over for page help
         */
        $mdDialog.show({
            controller: helpController,
            controllerAs: 'help',
            template: require('./helpcontent'),
            clickOutsideToClose: true,
            fullscreen: false,
            locals: {
                cancel: function () { $mdDialog.cancel(); }
            },
        });
    }

    function showResult (distance) {
        /**
         * dialog showing the result of server-side calculations
         */
        var distanceFmt = distance || '0 (your inputs are identical)';

        $mdDialog.show(
            $mdDialog
                .alert()
                .clickOutsideToClose(true)
                .ok('Got it!')
                .title('The Levenshtein edit distance between your inputs is:')
                .textContent(distanceFmt)
        );
    }

    function toastError (errorText) {
        /**
         * pop-up for server-side errors
         */
        $mdToast.show({
            template: '<md-toast class="md-capsule"><span flex>' + errorText + '</span></md-toast>',
            hideDelay: 3000,
            position: 'top right',
        });
    }

    function helpController($mdDialog) {
        /**
         * mini-controller for help pop-up
         */
        this.cancel = function() {
            $mdDialog.cancel();
        };
    }
}
