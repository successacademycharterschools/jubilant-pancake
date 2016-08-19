import angular from 'angular';
import uiRouter from 'angular-ui-router';
// import todoFactory from 'factories/todo-factory';
import editController from 'templates/edit';

const app = angular.module('app', [uiRouter]);

app.config(($stateProvider, $urlRouterProvider, $locationProvider) => {
    $urlRouterProvider.otherwise('/');

    $stateProvider
        .state('index', {
            url: '/',
            template: require('templates/index.html'),
            controller: editController
        } );

    $locationProvider.html5Mode(true);
});

export default app;
