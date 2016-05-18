$(document).ready(function() {

    $('#login_form').submit(function() {

        $.ajax({
            type: "POST",
            url: '/api-auth/login/',
            data: {
                username: $("#username").val(),
                password: $("#password").val()
            },
            success: function(data)
            {
                if (data === 'Correct') {
                    console.log("WOOOT")
                }

                else {
                    alert(data);
                }
            }
        });

    });

});
