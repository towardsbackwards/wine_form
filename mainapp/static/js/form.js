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
                document.getElementById(field_id+1).innerHTML=this.response // or responseText
                // берём элемент, id которого равняется id выбранного + 1, и рендерим туда значения
            } else {
            // handle a non-successful response
                console.log('bad');
            }
        }
    };

    var data = new FormData(obj.form); // get_data(form.elements, {}); new FormData(obj.form)
    var field_id = parseInt(obj.id ); // id выбранного поля
    data.append('field_id', field_id);
    xhttp.open(obj.form.method, obj.getAttribute('data-url'), true);
    // xhttp.setRequestHeader('X-CSRFToken', data['csrfmiddlewaretoken']);
    xhttp.setRequestHeader('X-Requested-With','XMLHttpRequest');
    xhttp.send(data);
}