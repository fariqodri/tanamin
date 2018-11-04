google.charts.load('current', {
  'packages': ['geochart']
});
google.charts.setOnLoadCallback(drawRegionsMap);

function drawRegionsMap() {

  var data = google.visualization.arrayToDataTable([
      ['Provinsi', 'Value', {
          role: 'tooltip',
          p: {
              html: true
          }
      }],
      ['Banten', 1, "Padi"],
      ['Sumatera Utara', 2, "Jagung"],
      ['Aceh', 3, "Teh"],
      ['Riau', 4, "Kopi"],
      ['Sumatera Barat', 1, "Padi"],
      ['Jambi', 2, "Jagung"],
      ['Bengkulu', 3, "Teh"],
      ['Sumatera Selatan', 4, "Kopi"],
      ['Lampung', 1, "Padi"],
      ['Jakarta', 4, "Kopi"],
      ['Jawa Barat', 2, "Jagung"],
      ['Jawa Tengah', 3, "Teh"],
      ['Yogyakarta', 1, "Padi"],
      ['Jawa Timur', 2, "Jagung"],
      ['Bali', 3, "Teh"],
      ['Nusa Tenggara Barat', 4, "Kopi"],
      ['Nusa Tenggara Timur', 1, "Padi"],
      ['Bangka Belitung', 2, "Jagung"],
      ['Kalimantan Barat', 3, "Teh"],
      ['Kalimantan Tengah', 4, "Kopi"],
      ['Kalimantan Selatan', 1, "Padi"],
      ['Kalimantan Timur', 2, "Jagung"],
      ['Kalimantan Utara', 3, "Teh"],
      ['Sulawesi Selatan', 4, "Kopi"],
      ['Sulawesi Tenggara', 1, "Padi"],
      ['Sulawesi Barat', 2, "Jagung"],
      ['Sulawesi Tengah', 3, "Teh"],
      ['Sulawesi Utara', 4, "Kopi"],
      ['Gorontalo', 1, "Padi"],
      ['ID-MA', 2, "Jagung"], // Harus ID-MA, ID-PB     => Kalo mau muncul maluku,
      //                           harus diformat semuanya.
      ['ID-PB', 3, "Teh"], //                           https://developers.google.com/chart/interactive/docs/reference#patternformatter
      ['Papua', 4, "Kopi"],
      ['Maluku Utara', 1, "Padi"],
  ]);

  var options = {
      region: 'ID',
      displayMode: 'regions',
      resolution: 'provinces',
      colorAxis: {
          colors: ['#a6cee3', '#1f78b4', '#b2df8a', '#33a02c'],
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