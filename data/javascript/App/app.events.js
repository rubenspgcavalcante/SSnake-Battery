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
    };

App.Events.System = function(){
    var batteryLevel = function(){
        var result = App.droid.eventWaitFor("batteryLevel").result;
        App.droid.eventWait()
        App.updateBattery(parseInt(result["data"]));
    };

    batteryLevel();
};