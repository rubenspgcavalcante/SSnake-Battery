App.Events = {};

App.Events.Interface = function(){
    /**
    * Shows the warning sign when battery
    * hits the low meter
    */
    var batteryLow =
        $(document).bind("interface:batteryLow", function(event, data) {
            $("#battery-low").show();
        });

    /**
    * Hides the battery sign when battery
    * hits a non-low state
    */
    var batteryOk =
        $(document).bind("interface:batteryOk", function(event, data) {
            $("#battery-low").hide();
        });

    /**
    * Speaks the percentage level of the
    * battery
    */
    var speak = 
        $("#speakButton").click(function(){
            App.droid.eventPost("say", null);
        });

    /**
    * Exits the application
    */
    var quit =
        $("#quitButton").click(function(){
           App.droid.eventPost("app-quit", null); 
        })

    };

App.Events.System = function(){
    var batteryLevel = function(){
        var result = App.droid.eventWaitFor("batteryLevel").result;
        App.droid.eventWait()
        App.updateBattery(parseInt(result["data"]));
    };

    batteryLevel();
};