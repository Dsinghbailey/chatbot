function post_wait(callback){
    var imgURL = imgURLArr[Math.floor(Math.random() * imgURLArr.length)]; 
    var chatHistory = $("<div id='chatWait'></div>");
    chatHistory.load(chatHistoryPartial, function() {
        this.innerHTML = this.innerHTML.replace("{{imgURL}}", imgURL);
        var ID = $('.message-feed').length
        this.innerHTML = this.innerHTML.replace("{{chatText}}", '...');
        this.innerHTML = this.innerHTML.replace("{{ID}}", ID); 
        $("#historyWindow").append(chatHistory);
        $("#historyWindow").scrollTop($("#historyWindow")[0].scrollHeight);
        if (typeof callback == "function") {
            setTimeout( function(){
                callback();
            }, 500);
        }
    });
}
function post_chat(textArr, callback){
    var imgURL = imgURLArr[Math.floor(Math.random() * imgURLArr.length)];
    var chatHistory = $("<div></div>");
    chatHistory.load(chatHistoryPartial, function() {
        this.innerHTML = this.innerHTML.replace("{{imgURL}}", imgURL);
        for(let j = 0; j < textArr.length; j++){
            if (j == 0) {
                var ID = $('.message-feed').length
                this.innerHTML = this.innerHTML.replace("{{chatText}}", textArr[j]);
                this.innerHTML = this.innerHTML.replace("{{ID}}", ID); 
                //Clear goose "..." 
                $('#chatWait').remove()
                $("#historyWindow").append(chatHistory);
                $("#historyWindow").scrollTop($("#historyWindow")[0].scrollHeight);
                if ((j == textArr.length - 1) && (typeof callback == "function")) {
                    callback(); 
                }
            } else {
                setTimeout( function(){
                    var msgHTML = '<br><div style="margin-top: 4px;" class="mf-content">' + textArr[j] + '</div>';
                    $("#chatMsg_" + ID).append(msgHTML);
                    $("#historyWindow").scrollTop($("#historyWindow")[0].scrollHeight);
                    if ((j == textArr.length - 1) && (typeof callback == "function")){
                        setTimeout( function(){
                            callback();
                        }, 500);
                    }
                }, j * 500); 
            }
        }
    });
}

function post_reply(textArr, callback){
    var replyHistory = $("<div></div>"); 
    replyHistory.load(replyHistoryPartial, function() {
        for(var i = 0; i < textArr.length; i++){
            if (i == 0) {
                this.innerHTML = this.innerHTML.replace("{{replyText}}", textArr[i]);
            } else {
                var msgHTML = '<br><div style="margin-top: 4px;" class="mf-content">' + textArr[i] + '</div>';
                this.children[0].children[0].innerHTML = this.children[0].children[0].innerHTML + msgHTML;
            }
            if ((i == textArr.length - 1) && (typeof callback == "function")){
                setTimeout( function(){
                    callback();
                }, 500);
            }
        }
        $("#historyWindow").append(replyHistory);
        $("#historyWindow").scrollTop($("#historyWindow")[0].scrollHeight);
    });
}

function post_reply_buttons(textArr){
    var replyButtons = $("<div></div>"); 
    replyButtons.load(replyButtonPartial, function() {
        for(var i = 0; i < textArr.length; i++){
            var cleanText = textArr[i].replace(/'/g, "\\'") 
            if (i == 0) {
                this.innerHTML = this.innerHTML.replace(/{{number}}/g, (i + 1));
                this.innerHTML = this.innerHTML.replace(/{{replyText}}/g, textArr[i]);
            } else {
                this.innerHTML = this.innerHTML + ('<div class="reply-btn" onclick="reply_click(' + (i + 1) + ',\''+ cleanText +'\')">' +
                    '<i style=" font-size: x-large;" class="bi bi-caret-right-fill"></i>' + 
                    ' <button type="button"> <b>' + (i + 1).toString() + '.</b> ' + textArr[i] + '</button> </div>')
            }
        }
    });
    $("#replyWindow").html('') 
    $("#replyWindow").append(replyButtons);
}

function post_text_box(){
    $("#replyWindow").html('<div class="form-group">' +
        '<input type="text" class="form-control" id="text_box" placeholder="Type here">' +
        '<button type="button" class="btn btn-primary pull-right" onclick="reply_click(' + 0 + ',\'get_text\')">Done</button>'+
        '</div>');
}

function reply_click(number, text){
    var http = new XMLHttpRequest();
    if (number == 0){
        text = $('#text_box').val(); 
    }
    var params = "num=" + number + '&text=' + text
    http.open("POST", '/reply', true);
    http.setRequestHeader("Content-type", "application/x-www-form-urlencoded");

    http.onreadystatechange = function() {
		if (http.readyState == 4){
			if (http.status == 200) {
                data = JSON.parse(http.response)
                post_chat(data['chat'], function() {
                    if (data['replies'][0] == 'text_box'){
                        post_text_box();
                    } else{
                        post_reply_buttons(data['replies']);
                    }
                });
			} else {
                alert('Honk. There was an error');
			}
		}
	}

    post_reply([text], function(){
        post_wait();
        http.send(params)
    });
    $("#replyWindow").html('<span id="replyWait">...</span>');
}