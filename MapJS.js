
function initMap() {
    var options = {
        zoom: 6,
        center: { lat: 31.5086, lng: -98.2117 },//need to adjust, localize to Texas' center
        restriction: {
            latLngBounds: {
                north: 37.4985,
                south: 24.8474,
                east: -91.5351,
                west: -108.6444,
            }
        }//end restriction
    }
    var map = new google.maps.Map(document.getElementById('map'), options);
}//end initMap