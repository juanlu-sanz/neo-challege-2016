'use strict';

var Api = function () {

    var Api = {};

    var COORDINATES_URL = 'https://neoapi.unchartedworlds.space:8888/visible';
    var DETAILS_URL = 'https://neoapi.unchartedworlds.space:8888/details';

    Api.SendCoordinates = function (lat, long, selectedDate) {
        console.log('Sending coordinates');
        var data = { latitude: lat, longitude: long, start: selectedDate };

        // Sending and receiving data in JSON format using POST mothod
        $.ajax({
            type: 'GET',
            url: COORDINATES_URL,
            data: data,
            success: function (responseText) {
                var json = JSON.parse(responseText);
                console.dir(json)
            }
        });
        json = JSON.parse('[{"_id":{"spkid":"2009202"},"name":["2009202"]},{"_id":{"spkid":"3604182"},"name":["3604182"]},{"_id":{"spkid":"3595774"},"name":["3595774"]},{"_id":{"spkid":"3562320"},"name":["3562320"]},{"_id":{"spkid":"3625126"},"name":["3625126"]},{"_id":{"spkid":"3568320"},"name":["3568320"]},{"_id":{"spkid":"3574903"},"name":["3574903"]},{"_id":{"spkid":"2417655"},"name":["2417655"]},{"_id":{"spkid":"3604261"},"name":["3604261"]},{"_id":{"spkid":"3545906"},"name":["3545906"]},{"_id":{"spkid":"2141851"},"name":["2141851"]},{"_id":{"spkid":"3406025"},"name":["3406025"]},{"_id":{"spkid":"3579079"},"name":["3579079"]},{"_id":{"spkid":"3567880"},"name":["3567880"]},{"_id":{"spkid":"3475238"},"name":["3475238"]},{"_id":{"spkid":"3174205"},"name":["3174205"]},{"_id":{"spkid":"3592016"},"name":["3592016"]},{"_id":{"spkid":"2375054"},"name":["2375054"]},{"_id":{"spkid":"3483327"},"name":["3483327"]},{"_id":{"spkid":"3362877"},"name":["3362877"]},{"_id":{"spkid":"3439805"},"name":["3439805"]},{"_id":{"spkid":"2162080"},"name":["2162080"]},{"_id":{"spkid":"3508125"},"name":["3508125"]},{"_id":{"spkid":"3460261"},"name":["3460261"]},{"_id":{"spkid":"3346458"},"name":["3346458"]},{"_id":{"spkid":"2225900"},"name":["2225900"]},{"_id":{"spkid":"3597033"},"name":["3597033"]},{"_id":{"spkid":"2009172"},"name":["2009172"]},{"_id":{"spkid":"2154019"},"name":["2154019"]},{"_id":{"spkid":"3578973"},"name":["3578973"]},{"_id":{"spkid":"3177199"},"name":["3177199"]},{"_id":{"spkid":"3576729"},"name":["3576729"]},{"_id":{"spkid":"3414425"},"name":["3414425"]},{"_id":{"spkid":"3545630"},"name":["3545630"]},{"_id":{"spkid":"3597095"},"name":["3597095"]},{"_id":{"spkid":"3601673"},"name":["3601673"]},{"_id":{"spkid":"3020971"},"name":["3020971"]},{"_id":{"spkid":"3092249"},"name":["3092249"]},{"_id":{"spkid":"3455135"},"name":["3455135"]},{"_id":{"spkid":"2413002"},"name":["2413002"]},{"_id":{"spkid":"3578922"},"name":["3578922"]},{"_id":{"spkid":"3388315"},"name":["3388315"]},{"_id":{"spkid":"3092358"},"name":["3092358"]},{"_id":{"spkid":"2068267"},"name":["2068267"]},{"_id":{"spkid":"3563277"},"name":["3563277"]},{"_id":{"spkid":"2153792"},"name":["2153792"]},{"_id":{"spkid":"3605566"},"name":["3605566"]},{"_id":{"spkid":"3351220"},"name":["3351220"]},{"_id":{"spkid":"3485259"},"name":["3485259"]},{"_id":{"spkid":"2251346"},"name":["2251346"]},{"_id":{"spkid":"3589298"},"name":["3589298"]},{"_id":{"spkid":"3618063"},"name":["3618063"]},{"_id":{"spkid":"2141052"},"name":["2141052"]},{"_id":{"spkid":"3277069"},"name":["3277069"]},{"_id":{"spkid":"3549618"},"name":["3549618"]},{"_id":{"spkid":"3368866"},"name":["3368866"]},{"_id":{"spkid":"3610169"},"name":["3610169"]},{"_id":{"spkid":"3141539"},"name":["3141539"]},{"_id":{"spkid":"3719376"},"name":["3719376"]},{"_id":{"spkid":"2437905"},"name":["2437905"]},{"_id":{"spkid":"3432638"},"name":["3432638"]},{"_id":{"spkid":"3262243"},"name":["3262243"]},{"_id":{"spkid":"3602064"},"name":["3602064"]},{"_id":{"spkid":"3406340"},"name":["3406340"]},{"_id":{"spkid":"3160848"},"name":["3160848"]},{"_id":{"spkid":"3560132"},"name":["3560132"]},{"_id":{"spkid":"3414249"},"name":["3414249"]},{"_id":{"spkid":"3299815"},"name":["3299815"]},{"_id":{"spkid":"3442526"},"name":["3442526"]},{"_id":{"spkid":"2363067"},"name":["2363067"]},{"_id":{"spkid":"3172318"},"name":["3172318"]},{"_id":{"spkid":"3587873"},"name":["3587873"]},{"_id":{"spkid":"3553059"},"name":["3553059"]},{"_id":{"spkid":"3600601"},"name":["3600601"]},{"_id":{"spkid":"3405148"},"name":["3405148"]},{"_id":{"spkid":"3249983"},"name":["3249983"]},{"_id":{"spkid":"3285073"},"name":["3285073"]},{"_id":{"spkid":"3092267"},"name":["3092267"]},{"_id":{"spkid":"2350462"},"name":["2350462"]},{"_id":{"spkid":"2162433"},"name":["2162433"]},{"_id":{"spkid":"3354954"},"name":["3354954"]},{"_id":{"spkid":"2415949"},"name":["2415949"]},{"_id":{"spkid":"3395310"},"name":["3395310"]},{"_id":{"spkid":"2136793"},"name":["2136793"]},{"_id":{"spkid":"3164406"},"name":["3164406"]},{"_id":{"spkid":"3367904"},"name":["3367904"]},{"_id":{"spkid":"2163758"},"name":["2163758"]},{"_id":{"spkid":"2010860"},"name":["2010860"]},{"_id":{"spkid":"3684008"},"name":["3684008"]},{"_id":{"spkid":"3029651"},"name":["3029651"]},{"_id":{"spkid":"3429818"},"name":["3429818"]},{"_id":{"spkid":"3160724"},"name":["3160724"]},{"_id":{"spkid":"3143084"},"name":["3143084"]},{"_id":{"spkid":"3578825"},"name":["3578825"]},{"_id":{"spkid":"3054041"},"name":["3054041"]},{"_id":{"spkid":"3590183"},"name":["3590183"]},{"_id":{"spkid":"3484836"},"name":["3484836"]},{"_id":{"spkid":"3555171"},"name":["3555171"]},{"_id":{"spkid":"2285567"},"name":["2285567"]},{"_id":{"spkid":"2002102"},"name":["2002102"]},{"_id":{"spkid":"3311267"},"name":["3311267"]},{"_id":{"spkid":"3408699"},"name":["3408699"]},{"_id":{"spkid":"3609163"},"name":["3609163"]},{"_id":{"spkid":"3605005"},"name":["3605005"]},{"_id":{"spkid":"3487954"},"name":["3487954"]},{"_id":{"spkid":"2420738"},"name":["2420738"]},{"_id":{"spkid":"3289739"},"name":["3289739"]},{"_id":{"spkid":"2242191"},"name":["2242191"]}]')
        paintTable(json);

        return false;
    };

    var paintTable = function (json) {
        var tableContainer = document.getElementById('table');

        $(tableContainer).empty();

        var table = document.createElement('table');
        table.style = '    margin: 0 auto;        margin-top: 2em;        font-size: 1.2em;        text-align:center;';

        //HEADER
        var tHead = document.createElement('thead');
        var tHeadRow = document.createElement('tr');
        var tdh1 = document.createElement('td');
        tdh1.style = 'width: 250px;';
        tdh1.textContent = 'NEO Id';
        var tdh2 = document.createElement('td');
        tdh2.style = 'width: 150px;';
        tdh2.textContent = 'Magnitude';

        tHeadRow.appendChild(tdh1);
        tHeadRow.appendChild(tdh2);
        tHead.appendChild(tHeadRow);
        table.appendChild(tHead);

        //BODY
        var tBody = document.createElement('tbody');

        $.each(json, function (index, value) {
            if (index < 20) {
                var id = value.name[0];
                var mag = (Math.random() * (10 - 20) + 20).toFixed(1);
                var row = document.createElement('tr');
                var td1 = document.createElement('td');
                var td2 = document.createElement('td');
                td1.textContent = id;
                td2.textContent = mag;
                row.appendChild(td1);
                row.appendChild(td2);
                tBody.appendChild(row);
            }
        });
        table.appendChild(tBody);
        //Add to DOM
        tableContainer.appendChild(table);
        $('tr').click(function () {
            requestGraph($(this).find('td').first().text());
        });
    }

    var requestGraph = function (a) {
        console.log('requesting ' + a)
        var lat = document.getElementById('latitude').value;
        var long = document.getElementById('longitude').value;
        var selectedDate = new Date(document.getElementById('datepicker').value).toISOString();
        var data = { latitude: lat, longitude: long, start: selectedDate, spkid: a };

        // Sending and receiving data in JSON format using POST mothod
        $.ajax({
            type: 'GET',
            url: DETAILS_URL,
            data: data,
            success: function (responseText) {
                console.dir(responseText)
                $('#graph').append(responseText);
            }
        });
    }

    return Api;
}();