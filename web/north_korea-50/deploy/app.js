var express = require('express');
var app = express();
var http = require('http');

app.get('/', function(req, res) {
	res.sendFile('index.html', { root : __dirname});
});

app.get('/code', function(req, res) {
	var ip = getClientIp(req); 
	if(typeof ip === 'string' || ip instanceof String) {
		var options = {
			host: 'www.freegeoip.net',
			path: '/json/' + ip
		};
		http.get(options, function(geo) {
			var bodyChunks = [];
			geo.on('data', function(chunk) {
				bodyChunks.push(chunk);
			}).on('end', function() {
				var body = Buffer.concat(bodyChunks);
				var loc = JSON.parse(body.toString()).country_code;
				if(loc === 'KP') {
					res.send('ctf(jk_we_aint_got_n0_nuk35)');
				} else {
					res.send('Nice try kiddo');
				}
			});
		});
		return;
	}
	res.send('Nice try kiddo');
});

app.listen(3000, function() {
	console.log('North korean security measures are now in place!');
});

function getClientIp(req) {
	var ipAddress;
	var forwardedIpsStr = req.header('x-forwarded-for');
	if (forwardedIpsStr) {
		var forwardedIps = forwardedIpsStr.split(',');
		ipAddress = forwardedIps[0];
	}
	if (!ipAddress) {
		ipAddress = req.connection.remoteAddress;
	}
	return ipAddress;
}
