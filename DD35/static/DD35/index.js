function PostMessage(e) {
    if (e.keyCode == 13) {
        var message = $('#btn-input').val();
        if (message){
            $.post({
                url: 'ajax/chat/',
                data: {
                'message': message,
                'user': document.getElementById("user").value
                },
                success: function (data) {

                    $('#btn-input').val('');

                }
            });
        }
        return false;
    }
}

function DisplayChatRoom(chatId) {


}
//initiate pusher with your application key
var pusher = new Pusher('e35aa2ec9d8ab3ac21ce', {cluster: 'eu', encrypted: true});
//subscribe to the channel you want to listen to
var my_channel = pusher.subscribe('my-channel');
//wait for an event to be triggered in that channel
my_channel.bind("my-event", function (data) {
    // declare a variable new_message to hold the new chat messages
    var new_message = `<li class="left clearfix"><span class="chat-img pull-left">
                        <img src="http://placehold.it/50/55C1E7/fff&text=`+data.name+`" alt="User Avatar" class="img-circle">
                    </span>
                        <div class="chat-body clearfix">
                            </br>
                             <p style="margin-left: 100px"><strong>`+data.name+` </strong> : `+data.message+`
                            </p>
                        </div>
                    </li>`;
 //append the new message to the ul holding the chat messages
$('#chat').append(new_message);
});
//wait until the DOM is fully ready
$(document).ready(function(){
//add event listener to the chat button click
    $("#btn-chat").click(function(){
//get the currently typed message
        var message = $('#btn-input').val();
        <!--Ajouter une fonction qui introduit des balises br pour couper le message sur plusieurs lignes lorsqu'il est trop long-->
        if (message){
            $.post({
                url: 'ajax/chat/',
                data: {
                'message': message,
                'user': document.getElementById("user").value
                },
                success: function (data) {

                    $('#btn-input').val('');

                }
            });
        }
    })
})
