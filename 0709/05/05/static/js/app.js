$(document).ready(function () {
    const ctx = document.getElementById("myChart").getContext("2d"); 

    var myChart = new Chart(ctx, {
        type: 'gauge',
        data: {
           
            datasets: [{
                label: 'Dynamic Chart Data',
                value: 20,
                minValue: 0,
                data: [10, 20, 30, 40],
                backgroundColor: ['green', 'yellow', 'orange', 'red'],
            }]
        },
        options: {
            responsive: true,
             title: {              
             display: true,
              text: 'MQTT Dashboard',        
      },

        layout: {
      padding: {
        bottom: 30
      }
    },
     needle: {
// Needle circle radius as the percentage of the chart area width
radiusPercentage: 2,
// Needle width as the percentage of the chart area width
widthPercentage: 3.2,
// Needle length as the percentage of the interval between inner radius (0%) and outer radius (100%) of the arc
lengthPercentage: 80,
// The color of the needle
color: 'rgba(0, 0, 0, 1)'
},
        valueLabel: {
          display: true,
formatter: (value) => {
return 'Temp:' + Math.round(value);
},
color: 'rgba(255, 255, 255, 1)',
backgroundColor: 'rgba(0, 0, 0, 1)',
borderRadius: 5,
padding: {
top: 10,
bottom: 10
}
}}
    });


    function addData(label, data) {
        console.log(myChart.data.datasets[0].value)
        myChart.data.datasets[0].value=label  
        myChart.update();
      }
           

    var socket = io.connect("http://127.0.0.1:5000/");    
    socket.on("updateSensorData", function (msg) {        
      console.log("Received sensorData :: " + msg.date );  
      addData(msg.date, msg.value);
    });
  });
  