'use strict';

var gulp = require('gulp');
var gulpNgConfig = require('gulp-ng-config');

var configureSetup  = {
    createModule: false,
    constants: {
        myNodeEnvVariable: process.env.MY_NODE_ENV_VARIABLE,
    }
};

gulp.task('config', function() {
    gulp.src('config.json')
    .pipe(gulpNgConfig('GroupmeStats', configureSetup))
    .pipe(gulp.dest('config')); 
});
