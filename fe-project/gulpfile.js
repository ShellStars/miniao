const gulp = require('gulp');
const uglify = require('gulp-uglify');
const sass = require('gulp-sass');
const autoprefixer = require('gulp-autoprefixer');
const minifyCSS = require('gulp-minify-css');
const imagemin = require('gulp-imagemin');
const ejs = require('gulp-ejs');
const gutil = require('gulp-util');
const clean = require('gulp-clean');
const data = require('gulp-data');
const nunjucks = require('gulp-nunjucks');
const rename = require('gulp-rename');

gulp.task('js', function () {
  gulp.src('./src/js/*.js')
      .pipe(uglify())
      .pipe(gulp.dest('../static/js'));
});

gulp.task('css', function () {
  gulp.src('./src/css/*.*')
      .pipe(sass().on('error', sass.logError))
      .pipe(autoprefixer({
        browsers: [
          "> 1%",
          "last 3 versions",
          "ie 9"
        ],
        cascade: false
      }))
      .pipe(minifyCSS())
      .pipe(rename({
        extname: '.css'
      }))
      .pipe(gulp.dest('../static/css'));
});

gulp.task('image', function () {
  gulp.src('./src/images/*.*')
      // .pipe(imagemin({
      //   progressive: true
      // }))
      .pipe(gulp.dest('../static/images'));
});

gulp.task('html', function () {
  gulp.src('./src/html/*.njk')
      .pipe(data(() => ({name: 'd'})))
      .pipe(nunjucks.compile())
      .pipe(rename({
        extname: '.html'
      }))
      .pipe(gulp.dest('../templates'));
});

gulp.task('clean', function () {
  gulp.src('../static', { read: false} )
      .pipe(clean({ force: true }))
      .pipe(gulp.dest('../static'));
});

gulp.task('all', ['html', 'js', 'image', 'css']);

gulp.task('default', ['all'], function () {
  gulp.watch('./src/js/*.js', function(){
    gulp.run('js');
  });
  gulp.watch('./src/html/**/*.njk', function(){
    gulp.run('html');
  });
  gulp.watch('./src/css/**/*.*', function(){
    gulp.run('css');
  });
  gulp.watch('./src/images/*.*', function(){
    gulp.run('image');
  });
});
