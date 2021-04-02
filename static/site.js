
function post_chat(textArr){
    var imgURL = imgURLArr[Math.floor(Math.random() * imgURLArr.length)];
    var chatHistory = $("<div></div>");
    chatHistory.load(chatHistoryPartial, function() {
        this.innerHTML = this.innerHTML.replace("{{imgURL}}", imgURL);
        for(var i = 0; i < textArr.length; i++){
            if (i == 0) {
                this.innerHTML = this.innerHTML.replace("{{chatText}}", textArr[i]);
            } else {
                var msgHTML = '<br><div style="margin-top: 4px;" class="mf-content">' + textArr[i] + '</div>';
                this.children[0].children[1].innerHTML = this.children[0].children[1].innerHTML + msgHTML;
            }
        }
        $("#historyWindow").append(chatHistory);
        $("#historyWindow").scrollTop($("#historyWindow")[0].scrollHeight);
    });
}

function post_reply(textArr){
    var replyHistory = $("<div></div>"); 
    replyHistory.load(replyHistoryPartial, function() {
        for(var i = 0; i < textArr.length; i++){
            if (i == 0) {
                this.innerHTML = this.innerHTML.replace("{{replyText}}", textArr[i]);
            } else {
                var msgHTML = '<br><div style="margin-top: 4px;" class="mf-content">' + textArr[i] + '</div>';
                this.children[0].children[0].innerHTML = this.children[0].children[0].innerHTML + msgHTML;
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
                this.innerHTML = this.innerHTML.replace("{{number}}", i + 1);
                this.innerHTML = this.innerHTML.replace(/{{replyText}}/g, textArr[i]);
            } else {
                this.innerHTML = this.innerHTML + ('<div class="reply-btn" onclick="reply_click(\''+ cleanText +'\')">' +
                    '<i style=" font-size: x-large;" class="bi bi-caret-right-fill"></i>' + 
                    ' <button type="button"> <b>' + (i + 1).toString() + '.</b> ' + textArr[i] + '</button> </div>')
            }
        }
    });
    $("#replyWindow").html('') 
    $("#replyWindow").append(replyButtons);
    setTimeout(function(){
        $("#replyWindow").height('auto');
    }, 100);
}

function reply_click(text){
    post_reply([text]);
    $("#replyWindow").height($("#replyWindow").height()); 
    $("#replyWindow").html('<span style="color:black;font-size: x-large;">...</span>');
    setTimeout(function(){
        post_chat(['...']);
        post_reply_buttons(['new','sdf', 'sdf']);
    }, 400);

}