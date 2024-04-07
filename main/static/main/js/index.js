$(document).ready(function() {
    $('form').submit(function(event) {
        event.preventDefault();
        var form = $(this);
        $.ajax({
            type: form.attr('method'),
            url: form.attr('action'),
            data: form.serialize(),
            success: function(data) {
                window.location.reload(); // Перезагружаем страницу после успешного удаления
            }
        });
    });
});