var express=require('express');
var router=express.Router();

router.use(function(req, res, next) {
    res.header("Access-Control-Allow-Origin", "*");
    res.header("Access-Control-Allow-Headers", "Origin, X-Requested-With, Content-Type, Accept");
    next();
  });

router.get('/test',function(req,resp,next){
    var test = {
        name: 'test',
        other: 'xyz'
    };
    // resp.send('this is api data');
    resp.send(test);
});

module.exports=router;