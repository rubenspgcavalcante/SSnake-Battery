if(typeof(Android) == "undefined"){
    Android = function(){};
}

var App = {
    
    droid: new Android(),

    updateBatteryWarning: function(value){
        if(value <= 20){
                $(document).trigger("interface:batteryLow");
        }
        else{
            $(document).trigger("interface:batteryOk");
        }
    },
     
    updateBattery: function(value){
        if(typeof(value) != "number" && value < 0 || value > 100){
            return false;
        }
        
        $("#battery-bar").animate({
            "width": value,
        }, 10000);

        this.updateBatteryLabel(value);
        return true;
    },

    updateBatteryLabel: function(value){

        if(typeof(value) != "number" && value < 0 || value > 100){
            return false;
        }

        var that = this;
        var state = parseInt($("#batteryValue").html());

        var id  = setInterval(function(){
            
            if(state == value){
                clearInterval(id);
            }
            
            else if(state > value){
                state -= 1;
            }
            
            else if(state < value){
                state += 1;
            }

            that.updateBatteryWarning(state);

            $("#batteryValue").html(state);

        }, 100);
        
        return true;
    }


}