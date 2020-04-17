function addForm(obj){
    var xhttp = new XMLHttpRequest();
    xhttp.responseType = 'json';
    xhttp.timeout = 5000; // time in milliseconds
    xhttp.ontimeout = function (e) {
            // XMLHttpRequest timed out. Do something here.
            console.log('bad timeout');
        };
    xhttp.onreadystatechange = function() {
        if (this.readyState === 4){
            if (this.status && this.status === 200) {
            // handle a successful response
                console.log('good');
                alert(JSON.stringify(this.response));
                // filler(this.response);
                document.getElementById('id_region').innerHTML=this.response // or responseText
            } else {
            // handle a non-successful response
                console.log('bad');
            }
        }
    };

    var data = new FormData(obj.form); // get_data(form.elements, {}); new FormData(obj.form)
    xhttp.open(obj.form.method, obj.getAttribute('data-url'), true);
    // xhttp.setRequestHeader('X-CSRFToken', data['csrfmiddlewaretoken']);
    xhttp.setRequestHeader('X-Requested-With','XMLHttpRequest');
    xhttp.send(data);
}