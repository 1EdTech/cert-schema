var parse = require('json-schema-to-markdown');
var fs = require('fs');

function writeMarkdownToFile(filename, markdown){
	fs.writeFile(filename, markdown, function(err) {
	    if(err) {
	        return console.log(err);
	    }
	}); 
}

/*
var certschema = require('../cert_schema/schema/certificate/1.1/certificate-schema-v1-1.json');
var certmarkdown = parse(certschema);
writeMarkdownToFile('docs/certificate-schema-v1-1.md', certmarkdown);
*/

var schemas = ['../cert_schema/schema/certificate/1.2/assertion-1.2.json',
				'../cert_schema/schema/certificate/1.2/blockchain-certificate-1.2.json',
				'../cert_schema/schema/certificate/1.2/blockchain-receipt-1.2.json',
				'../cert_schema/schema/certificate/1.2/certificate-1.2.json',
				'../cert_schema/schema/certificate/1.2/certificate-document-1.2.json',
				'../cert_schema/schema/certificate/1.2/issuer-1.2.json'];

for (var i = 0; i < schemas.length; i++) {
	var schema = schemas[i];

	// build 'out' file name
	var parts = schema.split('/');
	var lastPart = parts[parts.length - 1];
	var fileName = lastPart.substring(0, lastPart.length - 5);

	// convert
	var certschema = require(schema);
	var certmarkdown = parse(certschema);

	console.log('Writing markdown to ' + fileName);

	writeMarkdownToFile('docs/' + fileName + '.md', certmarkdown)
}


/*
var issuerschema = require('../cert_schema/schema/issuer-keys/1.1/issuer-schema-v1-1.json')
var issuermarkdown = parse(issuerschema)
writeMarkdownToFile('../docs/issuer-schema-v1-1.md', issuermarkdown)*/
