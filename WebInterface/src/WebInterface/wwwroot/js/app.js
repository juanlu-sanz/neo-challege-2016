'use strict';

var App = function () {

    var App = {};
    var coordinatesButton = document.getElementById('coordinates-button');
    var mainSection = document.getElementById('main');
    var wrapperSection = document.getElementById('wrapper');
    var map = null;

    App.init = function () {
        console.log('Starting Neofit');
        map = MapHandler;
        map.init('mapid');
        eventListeners();
        return false;
    };

    var eventListeners = function () {
        coordinatesButton.addEventListener('click', requestCoordinatesInfo);
    }

    function requestCoordinatesInfo() {
        var apiHandler = Api;
        var latitude = document.getElementById('latitude').value;
        var longitude = document.getElementById('longitude').value;
        var selectedDate = new Date(document.getElementById('datepicker').value).toISOString();
        apiHandler.SendCoordinates(latitude, longitude, selectedDate);
        activateAnalysisMode();
        map.mapControl.invalidateSize();

        map.mapControl.setView(new L.LatLng(latitude, longitude, 13));
    }

    function activateAnalysisMode() {
        var className = 'analysis';
        if (mainSection.classList)
            mainSection.classList.add(className);
        else
            mainSection.className += ' ' + className;

        if (wrapperSection.classList)
            wrapperSection.classList.add(className);
        else
            wrapperSection.className += ' ' + className;
    }

    return App;
}();