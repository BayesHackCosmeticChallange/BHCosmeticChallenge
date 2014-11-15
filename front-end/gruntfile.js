module.exports = function(grunt) {
	grunt.loadNpmTasks('grunt-contrib-watch');
	grunt.loadNpmTasks('grunt-contrib-compass');
	grunt.initConfig({
		compass: {
			dev: {
				options: {
					config: 'config.rb'
				}
			}
		},
		watch: {
			options: {
				livereload: true
			},
			sass: {
				files: ['./components/scss/*.scss'],
				tasks: ['compass:dev']
			},
			html: {
				files: ['*.html']
			}
		}
	})
	grunt.registerTask('default', 'watch');
}