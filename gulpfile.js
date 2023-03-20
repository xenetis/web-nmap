const gulp = require('gulp');
const uglify = require('gulp-uglify');
const sass = require('gulp-sass')(require('sass'));
const del = require('del');
const rename = require('gulp-rename');
const cleanCss = require('gulp-clean-css');


// Gulp task minify CSS files
gulp.task('styles', function () {
    return gulp.src('./apps/static/assets/sass/style.scss')
        .pipe(sass().on('error', sass.logError))
        .pipe(gulp.dest('./apps/static/assets/css/'))
        .pipe(cleanCss())
        .pipe(rename({ suffix: ".min" }))
        .pipe(gulp.dest('./apps/static/assets/css/'))
});

// Gulp task minify JavaScript files
gulp.task('scripts', function() {
    return gulp.src('./apps/static/assets/js/script.js')
        .pipe(uglify())
        .pipe(rename({ suffix: ".min" }))
        .pipe(gulp.dest('./apps/static/assets/js'))
});

// Gulp task to minify HTML files
// gulp.task('pages', function() {
//   return gulp.src(['./src/**/*.html'])
//     .pipe(htmlmin({
//       collapseWhitespace: true,
//       removeComments: true
//     }))
//     .pipe(gulp.dest('./dist'));
// });

// Clean output directory
gulp.task('clean', () => {
    return del([
        './apps/static/assets/css/style.css',
        './apps/static/assets/css/style.min.css',
        './apps/static/assets/js/script.min.js',
    ]);
});

// Default task
gulp.task('default', gulp.series(['clean', 'styles', 'scripts']));

gulp.task('watch', () => {
    gulp.watch('./apps/static/assets/sass/*.scss', (done) => {
        gulp.series(['clean', 'styles', 'scripts'])(done);
    });
    gulp.watch('./apps/static/assets/js/script.js', (done) => {
        gulp.series(['clean', 'styles', 'scripts'])(done);
    });
});