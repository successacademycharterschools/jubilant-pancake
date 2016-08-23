var test = require('tape');
var editCtrl = require( '../edit/edit.js' );

test( 'timing test', function ( t ) {
    t.plan( 1 );

    t.equal( typeof Date.now, 'function' );
    var start = Date.now();
} );

test( 'Edit Function', function ( t ) {
  var actual = getEditDistance( 'cat', 'dog' );
  var expected = 3;

  t.equal( actual, expected, "should both equal 3" );

  t.end();
} );
