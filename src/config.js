import angular from 'angular';
import uiRouter from 'angular-ui-router';
import editController from 'edit/edit';

const app = angular.module('app', [ uiRouter ]);

app.config(( $stateProvider, $urlRouterProvider, $locationProvider ) => {
    $urlRouterProvider.otherwise('/');

    $stateProvider
        .state( 'index', {
            url: '/',
            template: require( 'edit/index.html' ),
            controller: editController
        } );

    $locationProvider.html5Mode( true );
} );

export default app;
