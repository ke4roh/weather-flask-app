
    var socket = io.connect('http://' + document.domain + ':' + location.port);
    socket.on('connect', function() {
        socket.emit('client_connected', {data: 'New client!'});
    });

    socket.on('message', function (data) {
        console.log('message form backend ' + data);
        document.body.style.backgroundColor = 'rgb(165,0,0)';
        document.body.style.color = '#fff';
        //window.document.getElementById('tornado').style.display = 'none';
        window.document.getElementById('tornado').style.display = 'block';
        window.document.getElementById('message').innerHTML = data;
    });

    socket.on('alert', function (data) {
        window.document.getElementById('message').innerHTML = data;
        alert('Alert Message!! ' + data);
    });

    function json_button() {
        socket.send('{"message": "test"}');
    }

    function alert_button() {
        socket.emit('alert_button', 'Message from client!')
    }

