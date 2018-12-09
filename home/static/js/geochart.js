$(document).ready(function () {
    google.charts.load('current', {
    'packages': ['geochart']
    });
    $("form").submit(event => {
        $(".se-pre-con").fadeIn("slow");

        const rr = [];
        if (document.getElementById('defaultCheck1').checked){
            rr.push($('#defaultCheck1').val())
        }
        if (document.getElementById('defaultCheck2').checked){
            rr.push($('#defaultCheck2').val())
        }
        if (document.getElementById('defaultCheck3').checked){
            rr.push($('#defaultCheck3').val())
        }
        if (document.getElementById('defaultCheck4').checked){
            rr.push($('#defaultCheck4').val())
        }
        if (document.getElementById('defaultCheck5').checked){
            rr.push($('#defaultCheck5').val())
        }
        if (document.getElementById('defaultCheck6').checked){
            rr.push($('#defaultCheck6').val())
        }
        if (document.getElementById('defaultCheck7').checked){
            rr.push($('#defaultCheck7').val())
        }
        if (document.getElementById('defaultCheck8').checked){
            rr.push($('#defaultCheck8').val())
        }
        // console.log(rr);
        // const r = $("#tanaman").val().split("_")
        // console.log(r);
        // const sliced = r.slice(1);
        // console.log(sliced);
        const plants = ["padi", "jagung", "tebu", "kopi",
                        "teh", "kelapa sawit", "cengkeh", "tembakau"]
        
        for (var i = 0; i < rr.length; i++){
            if (!(plants.includes(rr[i].toLowerCase()))){
                console.log(rr[i].toLowerCase())
                event.preventDefault();
                alert("Tanaman tidak bisa dimasukkan.")
                break;
            }
        }

        if (rr.length < 3 || rr.length > 6) {
            event.preventDefault();
            alert("Jumlah tidak sesuai (3 sampai 6)");
        }
        // else if rr.length != r[0]) {
        //     event.preventDefault();
        //     alert("Berikan jumlah tanaman yang tepat sesuai input")
        // }
        
        // else {
        //     for (var i; i < sliced.length; i++) {
        //         console.log(tanamans);
                
        //         if (sliced[i] in tanamans) {
        //             event.preventDefault()
        //             alert("Ada tanaman yang sama")
        //         }else {
        //             tanamans.push(sliced[i])
        //         }
        //     }
        // }
    });
    var namaDaerah = $(".data").text();
    var newND = namaDaerah.split(";");
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
    ]);

    var options = {
        region: 'ID',
        legend: 'none',
        displayMode: 'regions',
        resolution: 'provinces',
        colorAxis: {
            colors: ['#724C9F', '#FFC60B', '#F58A4B', '#0EB99E', '#EF426D', '#AEA1A4'],
            values: [1, 2, 3, 4, 5, 6]
        },
        backgroundColor: {
            fill: '#FFFFFF'
        },
        keepAspectRatio: true,
    };

    var chart = new google.visualization.GeoChart(document.getElementById('geochart'));

    chart.draw(data, options);
    }
}
)

