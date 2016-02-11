var parse = require('json-schema-to-markdown')
var fs = require('fs')

function writeMarkdownToFile(filename, markdown){
	fs.writeFile(filename, markdown, function(err) {
	    if(err) {
	        return console.log(err);
	    }
	}); 
}

var certschema = require('../schema/certificate-schema-v1-1.json')
var certmarkdown = parse(certschema)
writeMarkdownToFile('../docs/certificate-schema-v1-1.md', certmarkdown)

var issuerschema = require('../schema/issuer-schema-v1-1.json')
var issuermarkdown = parse(issuerschema)
writeMarkdownToFile('../docs/issuer-schema-v1-1.md', issuermarkdown)
