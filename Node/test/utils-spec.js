var expect = require('chai').expect;
//var rewire = require('rewire');
var Utils = require('../library/utils');

describe('Utils Library Unit Tests', function(){
	
	describe('minimumEditDistance()', function(){
		
		it ('should return 0 when both inputs are null', function(done){
			var minimumEditDistance = Utils.minimumEditDistance(null,null);
			expect(minimumEditDistance).to.equal(0);
			done();
		});

		it ('should return the length of the first string while the second is empty', function(done){
			var string1 = '12345';
			var string2 = '';
			var minimumEditDistance = Utils.minimumEditDistance(string1,string2);
			expect(minimumEditDistance).to.equal(string1.length);
			done();
		});

		it ('should return the length of the second string while the first is empty', function(done){
			var string1 = '';
			var string2 = '12345';
			var minimumEditDistance = Utils.minimumEditDistance(string1,string2);
			expect(minimumEditDistance).to.equal(string2.length);
			done();
		});

		it ('should return 1 for a single deletion', function(done){
			var string1 = 'ABCDE';
			var string2 = 'ABDE';
			var minimumEditDistance = Utils.minimumEditDistance(string1,string2);
			expect(minimumEditDistance).to.equal(1);
			done();
		});

		it ('should return 1 for a single insertion', function(done){
			var string1 = 'ABDE';
			var string2 = 'ABCDE';
			var minimumEditDistance = Utils.minimumEditDistance(string1,string2);
			expect(minimumEditDistance).to.equal(1);
			done();
		});

		it ('should return 1 for a single insertion', function(done){
			var string1 = 'ABDE';
			var string2 = 'ABCDE';
			var minimumEditDistance = Utils.minimumEditDistance(string1,string2);
			expect(minimumEditDistance).to.equal(1);
			done();
		});

		it ('should return the length of the string for case toggled entry in case-sensitive mode', function(done){
			var string1 = 'abcde';
			var string2 = 'ABCDE';
			var minimumEditDistance = Utils.minimumEditDistance(string1,string2);
			expect(minimumEditDistance).to.equal(string1.length);
			done();
		});

		it ('should return 0 for case toggled entry in case-insensitive mode', function(done){
			var string1 = 'abcde';
			var string2 = 'ABCDE';
			var minimumEditDistance = Utils.minimumEditDistance(string1,string2, { caseSensitive: false });
			expect(minimumEditDistance).to.equal(0);
			done();
		});

	});

});