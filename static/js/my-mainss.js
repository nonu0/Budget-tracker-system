

// Sidebar Toggler
$('.toggle').click(function () {
    console.log('working')
    $('.sidebar, .content').toggleClass("open");
    return false;
});

// Calender
    $('#calender').datetimepicker({
        inline: true,
        format: 'L'
    });


// Worldwide Sales Chart
var ctx1 = $("#worldwide-sales").get(0).getContext("2d");
var data1 = JSON.parse(document.getElementById('income').textContent)
var data1a = JSON.parse(document.getElementById('debt').textContent)
var data1b = JSON.parse(document.getElementById('expense').textContent)
var myChart1 = new Chart(ctx1, {
    
    type: "bar",
    data: {
        labels: ["JANUARY", "FEBRUARY", "MARCH", "APRIL", "MAY", "JUNE", "JUNE","July","August","September","October","November","December"],
        datasets: [{
                label: "INCOME",
                data: data1,
                backgroundColor: "rgba(235, 22, 22, .7)"
            },
            {
                label: "DEBT",
                data: data1a,
                backgroundColor: "rgba(235, 22, 22, .5)"
            },
            {
                label: "EXPENSES",
                data: data1b,
                backgroundColor: "rgba(235, 22, 22, .3)"
            }
        ]
        },
    options: {
        responsive: true
    },
});


// Salse & Revenue Chart
var ctx2 = $("#sales-revenue").get(0).getContext("2d");
var data2 = JSON.parse(document.getElementById('expense').textContent)
var data1 = JSON.parse(document.getElementById('income').textContent)
var datamonths = JSON.parse(document.getElementById('months').textContent)
console.log('months',datamonths)
var label = ["JANUARY", "FEBRUARY", "MARCH", "APRIL", "MAY", "JUNE", "JUNE","July","August","September","October","November","December"]
var myChart2 = new Chart(ctx2, {
    type: "line",

    data: {
    labels: datamonths,
        datasets: [{
                label: "INCOME",
                data: data1,
                backgroundColor: "rgba(235, 22, 22, .7)",
                fill: true
            },
            {
                label: "EXPENSES",
                data: data2,
                backgroundColor: "rgba(235, 22, 22, .5)",
                fill: true
            }
        ]
        },
    options: {
        responsive: true
        
    }
});

// // Spinner
// var spinner = function () {
//     setTimeout(function () {
//         if ($('#spinner').length > 0) {
//             $('#spinner').removeClass('show');
//         }
//     }, 1);
// };
// spinner();