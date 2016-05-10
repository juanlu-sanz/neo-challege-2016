'use strict';

var MapHandler = function () {

    var mapHandler = {};
    var mapId = '';
    mapHandler.mapControl;
    var IMAGE_PATH = '../images/';
    var locationMarker;

    var latitudeInput = document.getElementById('latitude');
    var longitudeInput = document.getElementById('longitude');
    var Madrid = new L.LatLng(40.41677981974061, -3.703508377075195)

    //========PUBLIC METHODS=======
    mapHandler.init = function (inputMapId) {
        console.log('Starting mapHandler');
        mapId = inputMapId;
        initializeEmptyMap();
        createDateTime();
        return false;
    };

    //========PRIVATE METHODS=======
    var initializeEmptyMap = function () {
        console.log('initializing map');
        L.Icon.Default.imagePath = IMAGE_PATH;

        mapHandler.mapControl = L.map(mapId).setView(Madrid, 13);
        var CartoDB_Positron = L.tileLayer('http://{s}.basemaps.cartocdn.com/light_all/{z}/{x}/{y}.png', {
            attribution: '&copy; <a href="http://www.openstreetmap.org/copyright">OpenStreetMap</a> &copy; <a href="http://cartodb.com/attributions">CartoDB</a>',
            subdomains: 'abcd',
            maxZoom: 19
        }).addTo(mapHandler.mapControl);
        locationMarker = L.marker(Madrid, { draggable: 'true' }).addTo(mapHandler.mapControl)
        ondragend();
        locationMarker.on('dragend', ondragend);

        locateUser();
        turnLocationOff();
        return false;
    };
    var locateUser = function () {
        var lc = L.control.locate({ locateOptions: { maxZoom: 16 } }).addTo(mapHandler.mapControl);
        lc.start();

        mapHandler.mapControl.on('locationfound', onLocationFound);
        mapHandler.mapControl.invalidateSize();
    }
    function onLocationFound(e) {
        var radius = e.accuracy / 2;
        console.log('new marker')
        locationMarker.setLatLng(e.latlng).bindPopup("You are within " + radius + " meters from this point").openPopup();;
        L.circle(e.latlng, radius).addTo(mapHandler.mapControl);
        turnLocationOff();
    };
    function ondragend() {
        latLong = locationMarker.getLatLng();
        latitudeInput.value = latLong.lat;
        longitudeInput.value = latLong.lng;
    };
    function moveLocationMarker(lat, lng) {
        var newLatLng = new L.LatLng(lat, lng);
        locationMarker.setLatLng(newLatLng);
    }
    function turnLocationOff() {
        if (document.querySelector('.leaflet-control-locate.active a')) {
            var elem = document.querySelector('.fa-map-marker.fa').parentNode;
            var event = new Event('click');
            elem.dispatchEvent(event);
        }

    }
    function createDateTime() {
        console.log('asdf')
        $('.datepicker').datepicker({
            format: 'yyyy-mm-dd',
            setDate: new Date(),
            autoclose: true,
            startDate: '0',
            endDate: '+2m'
        }).datepicker('setDate', new Date());
    }
    return mapHandler;
}();