$(document).ready(function (event) {

    $("#event-create-form").submit(function(e) {

        //prevent Default functionality
        e.preventDefault();

        const data={
            platformcode:$("input[name='platformcode']").val() ,
            citycode:$("input[name='citycode']").val(),
            daycode:$("input[name='daycode']").val(),
            dbcode:$("input[name='dbcode']").val(),
            ip_address:$("input[name='ip_address']").val(),
            login_id: $("input[name='login_id']").val(),
            session_id:$("input[name='session_id']").val(),
            processcode:$("input[name='processcode']").val(),
            regional_time:$("input[name='regional_time']").val(),
            dowell_time:$("input[name='dowell_time']").val(),
            location:$("input[name='location']").val(),
            objectcode:$("input[name='objectcode']").val(),
            instancecode:$("input[name='instancecode']").val(),
            context:$("input[name='context']").val(),
            document_id:$("input[name='document_id']").val(),
            rules:$("input[name='rules']").val(),
            status:$("input[name='status']").val(),
            data_type: $("input[name='data_type']").val(),
            purpose_of_usage: $("input[name='purpose_of_usage']").val(),
            bookmarks: $("input[name='bookmarks']").val(),
        }

        $("#output-section").html("<h2>loading....</h2>");

        //do your own request an handle the results
        $.ajax({
                url: "/event_creation",
                type: 'post',
                contentType: "application/json; charset=utf-8",
                data:  JSON.stringify(data),
                success: function(data) {
                  $("#output-section").html(data);
                },

                error: function (request, status, error) {

                    $("#output-section").html(error);

                }
        });

    });
});
