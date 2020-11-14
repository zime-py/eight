$(document).ready(function(){
    $("#button").click(function(){
      var nid = $('#id_nid').val();
      var api_url = 'http://localhost:8000/nid/check/'+nid
      $.ajax({
              url: api_url,
              method: 'get',
              success: function(data){
                  var status_msg = $('#status');
                  // if api return True
                  if (data.status){
                      status_msg.text("Status: Valid");
                      status_msg.css('color','green');
                  }
                  else // if api return False
                  {
                      status_msg.text("Status: Invalid");
                      status_msg.css('color','red');
                  }
              },

              error: function(err){
                  console.log("error",err);
              }
          });
    });
  });