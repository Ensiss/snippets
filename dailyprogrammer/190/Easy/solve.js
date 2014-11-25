var fs = require("fs");
var request = require("request");
var cheerio = require("cheerio");

var happy_list = ['love','loved','like','liked','awesome','amazing','good','great','excellent']
var sad_list = ['hate','hated','dislike','disliked','awful','terrible','bad','painful','worst']

function count(text, list) {
    var c = 0;
    for (var i in list) {
        var res = text.match(RegExp("[^a-zA-Z0-9]" + list[i] + "[^a-zA-Z0-9]"), 'ig');
        c += res ? res.length : 0;
    }
    return (c);
}

function parse(url, cb) {
    request("https://plus.googleapis.com/u/0/_/widget/render/comments?first_party_property=YOUTUBE&href=" + url, function(error, response, body) {
        if (!error && response.statusCode == 200) {
            var $ = cheerio.load(body);
            var happy = 0;
            var sad = 0;
            var ncomms = 0;
            $("div.Ct").each(function() {
                var text = $(this).text();
                happy += count(text, happy_list);
                sad += count(text, sad_list);
                ncomms++;
            });
            cb(ncomms, happy, sad);
        }
    });
}

parse("https://www.youtube.com/watch?v=dQw4w9WgXcQ", function(ncomms, happy, sad) {
    console.log("From a sample size of " + ncomms + " comments.");
    console.log("The comments contained " + happy + " amount of Happy keywords and " + sad + " amount of sad keywords.");
    console.log("The general feelings towards this video were " + (happy > sad ? "happy" : "sad"));
});
