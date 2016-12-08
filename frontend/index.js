var express = require('express');
var app = express();

var gulp = require('gulp');
require('./gulpfile');
gulp.start('config'); 

app.use(express.static(__dirname));


app.listen(3000, function () {
    console.log('Example app listening on port 3000!')
})


exports = module.exports = app
