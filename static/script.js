var map = L.map('map', {
  scrollWheelZoom: false,
  center: [37.753972, -122.431297],
  zoom: 12
});

L.tileLayer("http://{s}.tile.stamen.com/toner-lite/{z}/{x}/{y}.png", 
  {
    attribution: '&copy; Map tiles by <a href="http://stamen.com">Stamen Design</a>, under <a href="http://creativecommons.org/licenses/by/3.0">CC BY 3.0</a>. Data by <a href="http://openstreetmap.org">OpenStreetMap</a>, under <a href="http://www.openstreetmap.org/copyright">ODbL</a>.',
    maxZoom: 18
}).addTo(map);
