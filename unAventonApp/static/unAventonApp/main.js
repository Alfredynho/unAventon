function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = jQuery.trim(cookies[i]);
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

function getJson(url, data, successCallback, errorCallback, completeCallback) {
    $.ajax({
        dataType: "json",
        method: 'get',
        url: url,
        data: data,
        success: successCallback,
        error: errorCallback,
        complete: completeCallback
    });
}

function postJson(url, data, successCallback, errorCallback, completeCallback) {
    data['csrfmiddlewaretoken']=getCookie('csrftoken');
    $.ajax({
        dataType: "json",
        method: 'post',
        url: url,
        data: data,
        success: successCallback,
        error: errorCallback,
        complete: completeCallback
    });
}

function validate_passwords_match() {
    return $('#id_confirmPassword').val() === $('#id_password').val();
}

function getFormData($form){
    /* retorna la data del form en json*/
    var unindexed_array = $form.serializeArray();
    var indexed_array = {};
    $.map(unindexed_array, function(n, i){
        indexed_array[n['name']] = n['value'];
    });
    return indexed_array;
}

function toTimeUnix( date, hour) {
    /*los parametros son los values de los inputs !!! */
    date = new Date(date);
    hora = hour.split(":");
    date.setHours(hora[0], hora[1]);
    return date.getTime() / 1000;
}
