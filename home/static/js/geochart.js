$(document).ready(function () {
    google.charts.load('current', {
    'packages': ['geochart']
    });
    
    var namaDaerah = $(".data").text();
    var newND = namaDaerah.split(";");
    console.log($(".jumlah").val());
    
    var hasil = []
    for (var i = 0; i < newND.length-1;i++){
        var tmp = newND[i].split(",");
        var angka = parseInt(tmp[1]);
        tmp[1] = angka;        

        if(tmp[0] == "DKI JAKARTA"){
            tmp[0] = "JAKARTA RAYA";
        }

        else if(tmp[0] == "MALUKU"){
            tmp[0] = "ID-MA";
        }

        else if(tmp[0] == "PAPUA BARAT"){
            tmp[0] = "ID-PB";
        }

        else if(tmp[0] == "DI YOGYAKARTA"){
            tmp[0] = "YOGYAKARTA";
        }

        else if(tmp[0] == "KEP. RIAU"){
            tmp[0] = "ID-KR";
        }

        else if(tmp[0] == "KEP. BANGKA BELITUNG"){
            tmp[0] = "BANGKA BELITUNG";
        }
    
        hasil.push(tmp)
    }
    
    google.charts.setOnLoadCallback(drawRegionsMap);

    function drawRegionsMap() {
    
    console.log(hasil)

    var data = google.visualization.arrayToDataTable([
        ['Provinsi', 'Value', {
            role: 'tooltip',
            p: {
                html: true
            }
        }],
        hasil[0],
        hasil[1],
        hasil[2],
        hasil[3],
        hasil[4],
        hasil[5],
        hasil[6],
        hasil[7],
        hasil[8],
        hasil[9],
        hasil[10],
        hasil[11],
        hasil[12],
        hasil[13],
        hasil[14],
        hasil[15],
        hasil[16],
        hasil[17],
        hasil[18],
        hasil[19],
        hasil[20],
        hasil[21],
        hasil[21],
        hasil[22],
        hasil[23],
        hasil[24],
        hasil[25],
        hasil[26],
        hasil[27],
        hasil[28],
        hasil[29],
        hasil[30],
        hasil[31],
        hasil[32],
        hasil[33],
        
    ]);

    var options = {
        region: 'ID',
        displayMode: 'regions',
        resolution: 'provinces',
        colorAxis: {
            colors: ['#107895', '#EBC844', '#F58A4B', '#92A660'],
            values: [1, 2, 3, 4]
        },
        backgroundColor: {
            fill: '#FFFFFF'
        },
        keepAspectRatio: false,
    };

    var chart = new google.visualization.GeoChart(document.getElementById('geochart'));

    chart.draw(data, options);
    }
}
)