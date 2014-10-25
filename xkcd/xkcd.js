var fs = require("fs");
var request = require("request");
var cheerio = require("cheerio");

function downloadComic(id, max)
{
    request("http://xkcd.com/" + id + "/", function(error, response, body) {
        if (!error && response.statusCode == 200) {
            var $ = cheerio.load(body);
            var img = $("div#comic img");

            var alt = $(img).attr("alt");
            var title = $(img).attr("title");
            var url = $(img).attr("src");

            console.log(id + ": " + alt + ": " + title + " @ " + url);
            if (url) {
                var path = "img/" + Array(max.length - id.length + 1).join("0") + id;
                request(url).pipe(fs.createWriteStream(path));
            }
        }
    });
}

function withMaxId(cb)
{
    request("http://xkcd.com/", function(error, response, body) {
        if (!error) {
            var $ = cheerio.load(body);
            var res = /xkcd.com\/([0-9]+)\//.exec($("div#middleContainer.box").text());
            if (res)
                cb(res[1]);
            else
                console.error("Could not determine last comic");
        }
    });
}

withMaxId(function(id) {
    for (var i = 1; i <= id; i++)
    {
        downloadComic('' + i, id);
    }
});
