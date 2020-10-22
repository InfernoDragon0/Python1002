var express = require('express');
var app = express();
var port = 5000;
var spawn = require('child_process').spawn;


app.listen(port, () => {
    console.log("server started in port " + port)
})

app.get('/test', (req,res) => {
    console.log("something connected")
    var process = spawn('python', ['./main.py'])
    var finalData = "start: "
    process.stdout.on('data', function (data) {
        // var options = {
        //     chart: {
        //       type: 'line'
        //     },
        //     series: [{
        //       name: 'sales',
        //       data: data
        //     }],
        //     xaxis: {
        //       categories: [1991,1992,1993,1994,1995,1996,1997, 1998,1999]
        //     }
        //   }
          
        //   var chart = new ApexCharts(document.querySelector("#chart"), options);
          
        //   chart.render();
        console.log(data.toString())
        finalData += data.toString()
    });
    process.stderr.on('data', function (data) {
      console.log(data.toString());
      finalData += data.toString()
  });
    process.stdout.on('end', function () {
      res.send(finalData)
  });
  process.on('end', function (data) {
    console.log(finalData)
    res.send(finalData)
  })
})