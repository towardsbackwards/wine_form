function get_csrf(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = cookies[i].trim();
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

function addForm(obj){
    var xhttp = new XMLHttpRequest();
    xhttp.responseType = 'json';
    xhttp.timeout = 5000;
    xhttp.ontimeout = function (e) {
            console.log('bad timeout');
        };
    xhttp.onreadystatechange = function() {
        if (this.readyState === 4){
            if (this.status && this.status === 200) {
                console.log('good');
                console.log(this.response);
                console.log(obj)
                // document.getElementById('city_form').elements.fieldset.innerHTML = this.response.form;
                document.getElementById('city_form').innerHTML = this.response.form;
            } else {
                console.log('bad');
            }
        }
    };
    var data = new FormData(obj.form);

    xhttp.open(obj.form.method, obj.getAttribute('data-url'), true);
    xhttp.setRequestHeader('X-Requested-With','XMLHttpRequest');
    var csrftoken = get_csrf('csrftoken');
    var field_id = parseInt(obj.id ); // id выбранного поля
    data.append('field_id', field_id);
    data.append('csrfmiddlewaretoken', csrftoken)
    xhttp.send(data);
}