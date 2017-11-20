var express=require('express');
var router=express.Router();

router.use(function(req, res, next) {
    res.header("Access-Control-Allow-Origin", "*");
    res.header("Access-Control-Allow-Headers", "Origin, X-Requested-With, Content-Type, Accept");
    next();
  });



/*
Test Api: Begin
/api/test
*/
router.get('/test',function(req,resp,next){
    var test = {
        name: 'test',
        other: 'xyz'
    };
    // resp.send('this is api data');
    resp.send(test);
});
/*
Test Api: End
*/


/*
Compute Distance Api: Begin
/api/compute
*/
router.post('/compute', function(req, res, next) {
    var textsObj = req.body;
    var text1CharArray = textsObj.text1.split('');
    var text2CharArray = textsObj.text2.split('');

    //Creating 2D Array: Begin
    var iMax = text1CharArray.length + 1;
    var jMax = text2CharArray.length + 1;
    var temp = [];
    for (i = 0; i < iMax; i++) {
        temp[i] = [];
        for (j = 0; j < jMax; j++) {
            temp[i][j] = 0;
        }
    }
    //Creating 2D Array: End

    //Calculating Edit Distance: Begin
    for (var i = 0; i < temp[0].length; i++) {
    temp[0][i] = i;
    }
    for (var i = 0; i < temp.length; i++) {
        temp[i][0] = i;
    }

    for (var i = 1; i <= text1CharArray.length; i++) {
        for(var j = 1; j <= text2CharArray.length; j++) {
            if (text1CharArray[i-1] == text2CharArray[j-1]) {
                temp[i][j] = temp[i-1][j-1];
            } else {
                temp[i][j] = 1 + Math.min(temp[i-1][j-1], temp[i-1][j], temp[i][j-1]);
            }
        }
    }
    //Calculating Edit Distance: End

    res.send({
        distOper: temp[text1CharArray.length][text2CharArray.length],
        matrix: temp,
        text1CharsArray: text1CharArray,
        text2CharsArray: text2CharArray
    });
    
});
/*
Compute Distance Api: End
*/

module.exports=router;