function PostMessage(chatId) {
    var btnInput = $('#btn-input-'.concat(chatId))
    var message = btnInput.val();
    if (message){
        $.post({
            url: 'ajax/chat/',
            data: {
                'message': message,
                'user': document.getElementById("user").value,
                'channel': document.getElementById("currentChannel").value
            },
            success: function (data) {
                btnInput.val('');
            }
        });
    }
}

function PostMessageIfEnter(e, chatId) {
    if (e.keyCode == 13) {
        PostMessage(chatId)
    }
}

function ChangeChat(chatId, chatName) {
    var selectedChat = $('#chatroom-'.concat(chatId))
    if (selectedChat.hasClass('initialized') == false) {
        InitializePusher(chatId, chatName)
        selectedChat.addClass('initialized')
    }
    $('.chatroom').addClass('invisible')
    $('#chatroom-'.concat(chatId)).removeClass('invisible')
    $('#currentChannel').val(chatId.toString())
    selectedChat.removeClass('invisible')
}

function InitializePusher(chatId, chatName) {
    var pusher = new Pusher('e35aa2ec9d8ab3ac21ce', {cluster: 'eu', encrypted: true});
    var my_channel = pusher.subscribe(chatId.toString());
    my_channel.bind("my-event", function (data) {
            var new_message = `
                <li class="left clearfix"><span class="chat-img pull-left">
                    <img src="http://placehold.it/50/55C1E7/fff&text=`+data.name+`" alt="User Avatar" class="img-circle">
                </span>
                    <div class="chat-body clearfix">
                        </br>
                         <p style="margin-left: 100px">`+data.message+`
                        </p>
                    </div>
                </li>
            `;
        $('#chatroom-'.concat(chatId).concat('-chat')).append(new_message);
    });
}
