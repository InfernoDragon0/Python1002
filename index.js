var express = require('express');
var app = express();
var path = require('path');
var port = 5000;
var spawn = require('child_process').spawn;
var hbs = require('express-handlebars');

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


app.use(express.static('public'))

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