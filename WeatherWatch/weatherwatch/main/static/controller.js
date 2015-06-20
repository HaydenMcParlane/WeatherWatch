$(document).ready(function(){		
	$('#get_weather_button').click(fetchTemperature);
});

var BASE_URL = "http://127.0.0.1:5000/api/";

function fetchTemperature(){
	var city = $('#city').val();
	var state = $('#state').val();	
	var curUrl = BASE_URL + "temperature/" + city + "/" + state;		

	$.ajax({
	    type: "GET",
	    url: curUrl,	    
	    dataType:"json",
	    accepts: "application/json",
	    success: function(data){	    	
	    	$("#temperature_display").text(data.temperature);
	    	return;
	    },
	    error: function(){
	    	alert("REST Error!");
	    	return;
	    }
	});
}

//jQuery.ajax({
//    type: "GET|POST|DELETE|PUT",
//    url: url,
//    data: data,
//    dataType:"text|html|json|jsonp|script|xml"
//    success: success_callback,
//    error: error_callback
//});

