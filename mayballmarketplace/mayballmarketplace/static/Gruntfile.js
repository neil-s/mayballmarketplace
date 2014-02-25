/* global module */
module.exports = function(Grunt) {
	// Load external tasks
	Grunt.loadNpmTasks('grunt-contrib-less');
	Grunt.loadNpmTasks('grunt-contrib-requirejs');

	// Configure Grunt tasks, etc..
	Grunt.initConfig({
		// LESS task for processing our stylesheets
		// https://github.com/gruntjs/grunt-contrib-less
		// Two targets: dev, production
		less: {
			options: {
				paths: ['style', 'lib']
			},
			dev: {
				options: {
					sourceMap: true,
				},
				files: {
					"dist/styles.dev.css": "style/styles.less"
				}
			},
			production: {
				options: {
					compress: true,
					cleancss: true
				},
				files: {
					"dist/styles.css": "style/styles.less"
				}
			}
		},
		// Require.js task for compiling javascript
		// https://github.com/gruntjs/grunt-contrib-requirejs
		// More info: https://github.com/jrburke/r.js/blob/master/build/example.build.js
		// This is for production only
		requirejs: {
			compile: {
				baseUrl: "js",
				mainConfigFile: "js/main.js",
				optimize: "uglify",
				out: 'dist/main.js',
				
			}
		}
	});
}