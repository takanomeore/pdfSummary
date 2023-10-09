$("#keySend").on("click",function(event) {
    let question = $("#question").val();
    $("#return").append("<p id=waitM>回答生成中...<p>");
    $.ajax({
        type: "POST",
        url: "./notSyncphp.php",
        data: { "data" : question },
    }).done(function(data){
        $("#waitM").remove();

        $("#return").append('<p>'+data+'</p>');
    }).fail(function(XMLHttpRequest,status,e) {
        alert(e);
    });
});

$('#pdfSubmit').on('click', function() {
    let fd = new FormData();
    let $upfile = $('input[name="pdfFile"]');
    fd.append("pdfFile",$upfile.prop('files')[0]);
    $('#pdfreturn').append("<p id=pdfWait>回答生成中...</p>");
    $.ajax({
        url:'./pdfSummary.php',
        type: 'POST',
        data: fd,
        processData: false,
        contentType: false,
        cache: false,
    }).done(function(data) {
        $('#pdfWait').remove();
        $('#pdfreturn').append('<p>'+data+'</p>');
        let pdfquest = document.getElementById("pdfQuestion");
        if(pdfquest.style.display == "none")
            pdfquest.style.display = "block";
    }).fail(function() {
        alert('failed');
    });
});

$('#pdfQuestionSubmit').on('click',function() {
    $('#pdfQuestion').append('<p>unti</p>');
    alert('untingStyle');
});