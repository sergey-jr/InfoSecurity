function table(id,columns){
    var $table = $('#'+id);
    $('#toolbar'+id).find('select').change(function () {
        $table.bootstrapTable('refreshOptions', {
        exportDataType: $(this).val()
        });
    });
    $table.bootstrapTable({
    columns: columns
    }); 
    return $table;
    }
let codesymbol = 'table-codes';
let codesymbolColumns = [
    {
        'field' : 'number',
        'title' : '<span class="lang ru">Номер</span>'
    },
    {
        'field' : 'code',
        'title' : '<span class="lang ru">Код</span'
    },
    {
        'field' : 'symbol',
        'title' : '<span class="lang ru">Символ</span>'
    }
];
let tableStrength = 'table-strength';
let tableStrengthColumns = [
    {
        'field' : 'length',
        'title' : '<span class="lang ru">Длина</span>'
    },{
        'field' : 'number',
        'title' : '<span class="lang ru">Полное число</span>'
    },{
        'field' : 'average',
        'title' : '<span class="lang ru">Средное число</span>'
    },{
        'field' : 'time',
        'title' : '<span class="lang ru">Средное время</span>'
    }
];
let $symbolsTable = table(codesymbol,codesymbolColumns);
let $complexityTable = table(tableStrength, tableStrengthColumns);
function update_alphabet_table(){
    $.get('http://127.0.0.1:5000/get/alphabet', {
        ll: $('#check-ll').prop('checked'),
        lu: $('#check-lu').prop('checked'),
        rl: $('#check-rl').prop('checked'),
        ru: $('#check-ru').prop('checked'),
        yo: $('#check-yo').prop('checked'),
        you: $('#check-you').prop('checked'),
        numbers: $('#check-n').prop('checked'),
        special: $('#check-sp').prop('checked')
    }).done(function( data ) {
        $('.size-basic-alphabet').html(data.length);
        $symbolsTable.bootstrapTable('load', data);
      });
}
function update_complexity_table(){
    $.get('http://127.0.0.1:5000/get/password_strength', {
        ll: $('#check-ll').prop('checked'),
        lu: $('#check-lu').prop('checked'),
        rl: $('#check-rl').prop('checked'),
        ru: $('#check-ru').prop('checked'),
        yo: $('#check-yo').prop('checked'),
        you: $('#check-you').prop('checked'),
        numbers: $('#check-n').prop('checked'),
        special: $('#check-sp').prop('checked'),
        n_max: $('#maxlength').val() ? $('#maxlength').val() : $('#maxlength').prop('placeholder'),
        v: $('#hackspeed').val() ? $('#hackspeed').val() : $('#hackspeed').prop('placeholder'),
        k: $('#strength').val() ? $('#strength').val() : $('#strength').prop('placeholder'),
    }).done(function( data ) {
        $complexityTable.bootstrapTable('load', data);
      });  
}
function get_password() {
    $.get('http://127.0.0.1:5000/get/password', {
        ll: $('#check-ll').prop('checked'),
        lu: $('#check-lu').prop('checked'),
        rl: $('#check-rl').prop('checked'),
        ru: $('#check-ru').prop('checked'),
        yo: $('#check-yo').prop('checked'),
        you: $('#check-you').prop('checked'),
        numbers: $('#check-n').prop('checked'),
        special: $('#check-sp').prop('checked'),
        n_max: $('#maxlength').val() ? $('#maxlength').val() : $('#maxlength').prop('placeholder'),
        v: $('#hackspeed').val() ? $('#hackspeed').val() : $('#hackspeed').prop('placeholder'),
        k: $('#strength').val() ? $('#strength').val() : $('#strength').prop('placeholder'),
        method: $('#method').val() ? $('#method').val(): '1',
        n: $('#length').val() ? $('#length').val(): $('#length').prop('placeholder'),
    }).done(function( data ) {
        $("#password-result").html(data)
      }); 
}
$(document).ready(function() {
    $('#generate').click(function(){
        $('#result-link').removeClass('disabled');
        get_password();
    });
    $('#my-tab a').on('click', function (e) {
        e.preventDefault();
        $('a.active').removeClass('active')
        $(this).addClass('active');
        $(this).tab('show');
      });
    $('input[type="checkbox"]').click(update_alphabet_table);
    $('.calculate-complexity').click(update_complexity_table);
})