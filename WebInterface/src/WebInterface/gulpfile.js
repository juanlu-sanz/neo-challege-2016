/// <binding BeforeBuild='sass-compile, min' Clean='clean' ProjectOpened='watch-sass' />
'use strict';

var gulp = require('gulp'),
    rimraf = require('rimraf'),
    concat = require('gulp-concat'),
    cssmin = require('gulp-cssmin'),
    uglify = require('gulp-uglify'),
    sassCompile = require('gulp-sass');


var paths = {
    webroot: './wwwroot/'
};

paths.jsFolder = paths.webroot + 'js/';
paths.js = paths.webroot + 'js/**/*.js';
paths.minJs = paths.webroot + 'js/**/*.min.js';
paths.css = paths.webroot + 'css/**/*.css';
paths.sass = paths.webroot + 'sass/**/*.scss';
paths.minCss = paths.webroot + 'css/**/*.min.css';
paths.concatJsDest = paths.webroot + 'js/site.min.js';
paths.concatCssDest = paths.webroot + 'css/site.min.css';
paths.jsLibs = paths.webroot + 'lib/**/*.js';
paths.cssLibs = paths.webroot + 'lib/**/*.css';

gulp.task('clean:js', function (cb) {
    rimraf(paths.concatJsDest, cb);
});

gulp.task('clean:css', function (cb) {
    rimraf(paths.concatCssDest, cb);
});

gulp.task('clean', ['clean:js', 'clean:css']);

gulp.task('min:js', function () {
    console.log('++++++MIN JS++++++++')

    return gulp.src([
        paths.jsLibs,
        paths.jsFolder + 'leaflet.js',
        paths.jsFolder + 'bootstrap-datepicker.js',
        paths.jsFolder + 'map.js',
        paths.jsFolder + 'api.js',
        paths.jsFolder + 'app.js',
        '!' + paths.minJs
    ], { base: '.' })
        .pipe(concat(paths.concatJsDest))
        //.pipe(uglify())
        .pipe(gulp.dest('.'));
});

gulp.task('min:css', function () {
    console.log('++++++MIN CSS++++++++')

    return gulp.src([paths.cssLibs, paths.css, '!' + paths.minCss])
        .pipe(concat(paths.concatCssDest))
        .pipe(cssmin())
        .pipe(gulp.dest('.'));
});

gulp.task('min', ['min:js', 'min:css']);

gulp.task('sass-compile', function () {
    console.log('++++++COMPILE SASS++++++++')
    console.log(paths.webroot + 'css/')
    gulp.src(paths.sass)
        .pipe(sassCompile())
        .pipe(gulp.dest(paths.webroot + 'css/.'));
});

gulp.task('watch-sass', function () {
    gulp.watch([paths.sass, paths.js], ['sass-compile', 'min']);
});