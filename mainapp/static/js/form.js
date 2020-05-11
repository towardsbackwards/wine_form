// function addForm(obj){
//     var xhttp = new XMLHttpRequest();
//     xhttp.responseType = 'json';
//     xhttp.timeout = 5000;
//     xhttp.ontimeout = function (e) {
//             console.log('bad timeout');
//         };
//     xhttp.onreadystatechange = function() { // это событие которое случится когда нам придет ответ от сервера
//         if (this.readyState === 4){
//             if (this.status && this.status === 200) {
//                 console.log('good');
//                 document.getElementById('city_form').elements.fieldset.innerHTML = this.response.form;
//             } else {
//                 console.log('bad');
//             }
//         }
//     };
//     var data = new FormData(obj.form);
//     data.append('field_name', obj.name);
//     data.append('num', obj.getAttribute('num'));
//     xhttp.open(obj.form.method, obj.getAttribute('data-url'), true);
//     xhttp.setRequestHeader('X-Requested-With','XMLHttpRequest');
//     xhttp.send(data);
// }