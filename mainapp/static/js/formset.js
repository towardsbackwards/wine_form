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
                document.getElementById(obj.parentNode.id).innerHTML = this.response.form;
                // console.log(obj.getElementsByTagName('option')[obj.id-1].text);
                // alert(obj.value);
                // alert(JSON.stringify(this.response));
                // var jsonResult = JSON.stringify(this.response);
                // var tableResult = jsonResult[0];
                // document.getElementById(obj.id).innerHTML = this.response.region;
            } else {
                console.log('bad');
            }
        }
    };

    var data = new FormData(obj.form);
    xhttp.open(obj.form.method, obj.getAttribute('data-url'), true);
    xhttp.setRequestHeader('X-Requested-With','XMLHttpRequest');
    xhttp.send(data);
}

