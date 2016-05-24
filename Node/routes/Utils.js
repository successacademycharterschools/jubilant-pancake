const 	express = require('express'),
		router = express.Router(),
		Utils = require('../library/utils.js'),
		cors = require("cors");

router.get('/minimumEditDistance', cors(), function(req, res){
	res.json({ minimumEditDistance: Utils.minimumEditDistance(req.query.string1, req.query.string2, { caseSensitive: req.query.caseSensitive!=='false' }) });
});

module.exports = router;
