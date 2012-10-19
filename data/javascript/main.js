function init(){

    // Init events
    $.each(App.Events, function(index, eventRegister){
        new eventRegister();
    });
}

$(document).ready(function(){
    
    try{
        init();
        App.updateBattery(0);
    }

    catch(e){
        alert(e);
        App.Utils.log("Caught exception" + e);
    }

});