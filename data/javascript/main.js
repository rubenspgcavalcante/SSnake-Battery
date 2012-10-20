function init(){

    // Init events
    $.each(App.Events, function(index, eventRegister){
        new eventRegister();
    });
}

$(document).ready(function(){
    
    App.droid.eventPost("documentReady", null);

    try{
        init();
    }

    catch(e){
        alert(e);
        App.Utils.log("Caught exception" + e);
    }

});