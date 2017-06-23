/**
 * This has experimental improvements to the generate_markdown.js script. Still not complete, but better at handling
 * referenced schemas and types.
 */
var parse = require('json-schema-to-markdown');
var fs = require('fs');

function writeMarkdownToFile(filename, markdown){
	fs.writeFile(filename, markdown, function(err) {
	    if(err) {
	        return console.log(err);
	    }
	}); 
}


var schemas = [
  '../cert_schema/schema/2.0/issuerSchema.json'
];

for (var i = 0; i < schemas.length; i++) {
	var schema = schemas[i];

	// build 'out' file name
	var parts = schema.split('/');
	var lastPart = parts[parts.length - 1];
  var secondToLastPart = '';
	if (parts.length > 2) {
    secondToLastPart = parts[parts.length - 2] + '_';
  }
	var fileName = lastPart.substring(0, lastPart.length - 5);

	// convert
	var certschema = require(schema);
	var certmarkdown = parse(certschema);

	console.log('Writing markdown to ' + secondToLastPart + fileName);

	writeMarkdownToFile(secondToLastPart + fileName + '.md', certmarkdown)
}
