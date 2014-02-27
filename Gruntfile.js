/* global module */
module.exports = function(Grunt) {
	'use strict';

	// Load external tasks
	Grunt.loadNpmTasks('grunt-contrib-less');
	Grunt.loadNpmTasks('grunt-contrib-requirejs');
	Grunt.loadNpmTasks('grunt-contrib-watch');

	// Configure Grunt tasks, etc..
	Grunt.initConfig({
		// LESS task for processing our stylesheets
		// https://github.com/gruntjs/grunt-contrib-less
		// Two targets: dev, production
		less: {
			options: {
				paths: ['mayballmarketplace/static/less', 'mayballmarketplace/static/lib']
			},
			dev: {
				options: {
					sourceMap: true,
					compress: false,
					cleancss: false
				},
				files: {
					'mayballmarketplace/static/dist/styles.dev.css': 'mayballmarketplace/static/less/styles.less'
				}
			},
			production: {
				options: {
					compress: true,
					cleancss: true
				},
				files: {
					'mayballmarketplace/static/dist/styles.css': 'mayballmarketplace/static/less/styles.less'
				}
			}
		},
		// Require.js task for compiling javascript
		// https://github.com/gruntjs/grunt-contrib-requirejs
		// More info: https://github.com/jrburke/r.js/blob/master/build/example.build.js
		// This is for production only
		requirejs: {
			compile: {
				options: {
					baseUrl: 'mayballmarketplace/static/js',
					mainConfigFile: 'mayballmarketplace/static/js/main.js',
					optimize: 'uglify',
					keepBuildDir: true,
					name: 'main',
					out: 'mayballmarketplace/static/dist/main.js'
				}
			}
		},
		// Watch task for watching files to build out
		// https://github.com/gruntjs/grunt-contrib-watch
		watch: {
			options: {
				livereload: true
			},
			styles: {
				files: ['mayballmarketplace/static/less/*.less', 'mayballmarketplace/static/less/**/*.less'],
				tasks: ['less:dev']
			},
			scripts: {
				files: ['mayballmarketplace/static/js/*.js', 'mayballmarketplace/static/js/**/*.js']
				// probably should add some jshint tasks in here at some point
			}
		}
	});
};