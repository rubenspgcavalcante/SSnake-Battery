App.Utils = {
    log: function(msg){
        App.droid.eventPost("log", "javascript: " + msg);
    }

}