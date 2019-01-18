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
let codesymbol = "table-codes";
let codesymbolColumns = [
    {
        "field" : "number",
        "title" : '<span class="lang ru">Номер</span>'
    },
    {
        "field" : "code",
        "title" : '<span class="lang ru">Код</span'
    },
    {
        "field" : "symbol",
        "title" : '<span class="lang ru">Символ</span>'
    }
];
let symbolsTable = table(codesymbol,codesymbolColumns);
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
        console.log(data);
        $('.size-basic-alphabet').html(data.length);
        symbolsTable.bootstrapTable('load', data);
      });
}
$(document).ready(function() {
    update_alphabet_table();
    $('#generate').click(function(){
        $('#result-link').removeClass('disabled')
    });
    $('#my-tab a').on('click', function (e) {
        e.preventDefault();
        $('a.active').removeClass('active')
        $(this).addClass('active');
        $(this).tab('show');
      });
    $('input[type="checkbox"]').click(update_alphabet_table);
})