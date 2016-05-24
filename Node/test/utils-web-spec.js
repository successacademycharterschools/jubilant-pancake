var expect = require('chai').expect;
var app = require('../index.js');
var request = require('supertest').agent(app.listen());


describe('Utils Web API Integration Tests', function(){
	
	describe('/api/1/Utils/minimumEditDistance', function(){
		
		it ('should return 0 when both inputs are null', function(done){
			var res = request.get('/api/1/Utils/minimumEditDistance?string1=&string2=')
			res.expect(200, {minimumEditDistance:0}, done);
		});

		it ('should return the length of the first string while the second is empty', function(done){
			var string1='12345';
			var string2='';
			var res = request.get(`/api/1/Utils/minimumEditDistance?string1=${string1}&string2=${string2}`)
			res.expect(200, {minimumEditDistance:string1.length}, done);
		});

		it ('should return the length of the second string while the first is empty', function(done){
			var string1='';
			var string2='12345';
			var res = request.get(`/api/1/Utils/minimumEditDistance?string1=${string1}&string2=${string2}`)
			res.expect(200, {minimumEditDistance:string2.length}, done);
		});

		it ('should return 1 for a single deletion', function(done){
			var string1='ABCDE';
			var string2='ABDE';
			var res = request.get(`/api/1/Utils/minimumEditDistance?string1=${string1}&string2=${string2}`)
			res.expect(200, {minimumEditDistance:1}, done);
		});

		it ('should return 1 for a single insertion', function(done){
			var string1='ABDE';
			var string2='ABCDE';
			var res = request.get(`/api/1/Utils/minimumEditDistance?string1=${string1}&string2=${string2}`)
			res.expect(200, {minimumEditDistance:1}, done);
		});

		it ('should return the length of the string for case toggled entry in case-sensitive mode', function(done){
			var string1 = 'abcde';
			var string2 = 'ABCDE';
			var res = request.get(`/api/1/Utils/minimumEditDistance?string1=${string1}&string2=${string2}`)
			res.expect(200, {minimumEditDistance:string1.length}, done);
		});

		it ('should return 0 for case toggled entry in case-insensitive mode', function(done){
			var string1 = 'abcde';
			var string2 = 'ABCDE';
			var res = request.get(`/api/1/Utils/minimumEditDistance?string1=${string1}&string2=${string2}&&caseSensitive=false`)
			res.expect(200, {minimumEditDistance:0}, done);
		});

	});

});