function caesar_code() {
    let message = $('#caesar_message').val();
    let key = Number($('#caesar_key').val());
    let method = $('#caesar_method').val();
    if(key && method && message.length)
    {
        $.get('http://127.0.0.1:5000/caesar', {
            message: message,
            key: key,
            method: method
        }).done(function(data){
            data = JSON.parse(data);
            $('#caesar_result').html(data);
        }); 
    }   
}
function viginer_code(){
    let message = $('#viginer_message').val();
    let key = $('#viginer_key').val();
    let method = $('#viginer_method').val();
    let language = $('#viginer_language').val();
    if(key.length && method && message.length && language)
    {
        $.get('http://127.0.0.1:5000/viginer', {
            message: message,
            key: key,
            method: method,
            lang: language
        }).done(function(data){
            data = JSON.parse(data);
            $('#viginer_result').html(data);
        }); 
    } 
}
function matrix_code(){
    let message = $('#matrix_message').val();
    let key_n = $('#matrix_key_n').val();
    let key_m = $('#matrix_key_m').val();
    let method = $('#matrix_method').val();
    if(key_n.length && method && message.length && key_m.length)
    {
        $.get('http://127.0.0.1:5000/matrix', {
            message: message,
            key_n: key_n,
            key_m: key_m,
            method: method
        }).done(function(data){
            data = JSON.parse(data);
            $('#matrix_result').html(data);
        }); 
    }
}
function adfgx_code(){
    let message = $('#adfgx_message').val();
    let key = $('#adfgx_key').val();
    let method = $('#adfgx_method').val();
    let alphabet = $('#adfgx_alphabet').val();
    if(key.length && method && message.length)
    {
        if(method == 'encode' || (method=='decode' && alphabet.length)){            
            $.get('http://127.0.0.1:5000/adfgx', {
                message: message,
                key: key,
                method: method,
                alphabet: alphabet
            }).done(function(data){
                data = JSON.parse(data);
                if(typeof(data) == 'object' && data.length == 3){
                    let a = 'Алфавит: ' + data[0].join('') + '<br>';
                    let code = 'adfgx'.toUpperCase();
                    let m = '<table class="table"><thead><td>#</td><td>A</td><td>D</td><td>F</td><td>G</td><td>X</td></thead>';
                    for(let i = 0; i<data[1].length; i++){
                        m += '<tr><td>' + code[i] + '</td>';
                        for(let j = 0; j<data[1][i].length; j++){
                            m += '<td>' + data[1][i][j] + '</td>';
                        }
                        m += '</tr>';
                    }
                    m += '</table><br>';
                    let encoded = 'Закодировано: ' + data[2];
                    $('#adfgx_result').html([a, m, encoded].join(' '));    
                }
                else{
                    $('#adfgx_result').html(data);
                }
            }); 
        }
    }
}
function pair_method_change(method){
    if(method == 'encode'){
        $('#pair_language-container').show();
        $('#pair_alphabet-container').hide();
    }else{
        $('#pair_language-container').hide();
        $('#pair_alphabet-container').show();
    }
}
function pair_code(){
    let message = $('#pair_message').val();
    let method = $('#pair_method').val();
    let alphabet = $('#pair_alphabet').val();
    let language = $('#pair_language').val();
    if(message.length && method){
        if((method == 'encode' && language) || (method == 'decode' && alphabet)){
            $.get('http://127.0.0.1:5000/pair', {
                message: message,
                method: method,
                lang: language,
                alphabet: alphabet
            }).done(function(data){
                data = JSON.parse(data);
                if(method == 'encode'){
                    let a = 'Алфавит: ' + data[0].join('') + '<br>';
                    let encoded = 'Закодировано: ' + data[1];
                    $('#pair_result').html([a, encoded].join(''));
                }else{
                    $('#pair_result').html(data);
                }
            }); 
        }
    }
}
function rsa_code(){
    let message = $('#rsa_message').val();
    let p = Number($('#rsa_key_p').val());
    let q = Number($('#rsa_key_q').val());
    let e = Number($('#rsa_key_e').val());
    let method = $('#rsa_method').val();
    let language = $('#rsa_language').val();
    if((language && p && q &&message.length) && ( method == 'encode' || (method == 'decode' && e))){
        $.get('http://127.0.0.1:5000/rsa', {
            message: message,
            method: method,
            lang: language,
            p: p,
            q: q,
            e: e
        }).done(function(data){
            data = JSON.parse(data);
            if(method == 'encode'){
                let encoded = 'Закодировано: ' + data['c'].join(' ') + '<br>';
                let e = 'e = ' + data['e'];
                $('#rsa_result').html([encoded, e].join(''));
            }else{
                $('#rsa_result').html(data);
            }
        }); 
    }
}
$(document).ready(function() {
    $('#caesar_go').click(caesar_code);
    $('#viginer_go').click(viginer_code);
    $('#matrix_go').click(matrix_code);
    $('#adfgx_go').click(adfgx_code);
    $('#pair_go').click(pair_code);
    $('#rsa_go').click(rsa_code);
    $('#my-tab a').first().click();
    $('#pair_method').change(function(e, n){
        e.preventDefault();
        let method = $(this).val();
        pair_method_change(method);
    });
    pair_method_change('encode');
    $('#adfgx_method').change(function(e, n){
        e.preventDefault();
        let method = $(this).val();
        if(method=='decode'){
            $('#adfgx_alphabet-container').show();
        }
        else{
            $('#adfgx_alphabet-container').hide();
        }
    });
    $('#rsa_method').change(function(e, n){
        e.preventDefault();
        let method = $(this).val();
        if(method=='decode'){
            $('#rsa_key_e-container').show();
            $('#rsa_message-label').parent().removeClass('col-md-3');
            $('#rsa_message-label').parent().addClass('col-md-6');
            $('#rsa_message-label').html('Закодированное сообщение(цифры через пробел):');
        }
        else{
            $('#rsa_key_e-container').hide();
            $('#rsa_message-label').parent().removeClass('col-md-6');
            $('#rsa_message-label').parent().addClass('col-md-3');
            $('#rsa_message-label').html('Сообщение:');
        }
    });
    $('#my-tab a').on('click', function (e) {
        e.preventDefault();
        $('a.active').addClass('disabled');
        $('a.active').removeClass('active');
        $(this).addClass('active');
        $(this).removeClass('disabled');
        $(this).tab('show');
      });
})