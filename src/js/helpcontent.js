/**
* template for pop-up help
*/
'use strict';

module.exports = [
    '<md-dialog aria-label="Help" ng-cloak>',
    '<md-toolbar><div class="md-toolbar-tools">',
        '<h2>Levenshtein distance</h2>',
        '<span flex></span>',
        '<md-button class="md-icon-button" ng-click="help.cancel()">',
        '<md-icon class="material-icons" aria-label="Close dialog">close</md-icon>',
        '</md-button>',
    '</div></md-toolbar>',
    '<md-dialog-content>',
        '<div class="md-dialog-content">',
        '<h4>From Wikipedia:</h4>',
        '<p>',
        'Informally, the Levenshtein distance between two words is the minimum number of single-character edits ',
        '(i.e. insertions, deletions or substitutions) required to change one word into the other.',
        '</p>',
        '<h4>To run:</h4>',
        '<p>',
        'Enter two strings into two text fields, click "Calculate"',
        '</p>',
        '</div>',
    '</md-dialog-content>',
    '<md-dialog-actions layout="row">',
        '<md-button href="http://en.wikipedia.org/wiki/Levenshtein_distance" target="_blank">More on Wikipedia</md-button>',
        '<span flex></span>',
        '</md-button>',
        '<md-button ng-click="help.cancel()" md-autofocus>Got it!</md-button>',
    '</md-dialog-actions>',
    '</md-dialog>'
].join('')
;
