var express = require('express');
var app = express();
var port = 3005;
var path = require('path');
var port = 5005;
var spawn = require('child_process').spawn;
var hbs = require('express-handlebars');
var helper = hbs.create({});

app.listen(port, () => {
    console.log("server started in port " + port)
})
app.set('view engine', 'hbs');

app.engine( 'hbs', hbs( {
  extname: 'hbs',
  defaultView: 'default',
  layoutsDir: __dirname + '/views/layouts/',
  partialsDir: __dirname + '/views/partials/'
}));

helper.handlebars.registerHelper('json', function (content) {
  return JSON.stringify(content);
})

app.use(express.static(__dirname + '/public'))

app.get('/test', (req,res) => {
    var process = spawn('python', ['./main.py'])
    var finalData = ""
    process.stdout.on('data', function (data) {
        //console.log(data.toString())
        finalData += data.toString()
    });
    process.stderr.on('data', function (data) {
      //console.log(data.toString());
      finalData += data.toString()
  });
    process.stdout.on('end', function () {
      res.render('index', {layout: 'default', chartData: finalData})
  });
  process.on('end', function () {
    ///console.log(finalData)
    //res.send(finalData)
  })
})


