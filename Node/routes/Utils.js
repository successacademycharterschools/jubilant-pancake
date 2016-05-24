const 	Utils = require('../library/utils.js'),
		cors = require("cors");

module.exports = function(app){
	
	app.get('/api/1/Utils/minimumEditDistance', cors(), function(req, res){
		res.json({ minimumEditDistance: Utils.minimumEditDistance(req.query.string1, req.query.string2, { caseSensitive: req.query.caseSensitive!=='false' }) });
	});

}