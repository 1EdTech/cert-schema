var parse = require('json-schema-to-markdown')
var fs = require('fs')

function writeMarkdownToFile(filename, markdown){
	fs.writeFile(filename, markdown, function(err) {
	    if(err) {
	        return console.log(err);
	    }
	}); 
}

var certschema = require('../schema/certificate-schema-v2.json')
var certmarkdown = parse(certschema)
writeMarkdownToFile('../docs/certificate-schema-v2.md', certmarkdown)

var issuerschema = require('../schema/issuer-schema-v2.json')
var issuermarkdown = parse(issuerschema)
writeMarkdownToFile('../docs/issuer-schema-v2.md', issuermarkdown)
