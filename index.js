var express = require('express');
var app = express();
var port = 3005;
var spawn = require('child_process').spawn;


app.listen(port, () => {
    console.log("server started in port " + port)
})

app.get('/test', (req,res) => {
    var process = spawn('python', ['./pyscripts/main.py'])
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
        res.send(data.toString());
    });
})