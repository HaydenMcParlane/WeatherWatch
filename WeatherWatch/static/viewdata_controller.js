$(document).ready(function(){		
});

setInterval(fetchData, 5000);

var BASE_URL = "http://weathertrack.mybluemix.net";
//var BASE_URL = "http://localhost:8000";

function fetchData(){		
	curUrl = BASE_URL + "/get-data"
	$.ajax({
	    type: "GET",
	    url: curUrl,	    
	    dataType:"json",
	    accepts: "application/json",
	    success: function(data){	    	
	    	var r = new Array(), j = -1;
	    	for (var key=0, size=data.length; key<size; key++){
	    	     r[++j] ='<tr><td>';
	    	     r[++j] = data[key]['city'];
	    	     r[++j] = '</td><td>';
	    	     r[++j] = data[key]['state'];
	    	     r[++j] = '</td><td>';
	    	     r[++j] = data[key]['temperature'];
	    	     r[++j] = '</td><td>';
	    	     r[++j] = data[key]['date-time']
	    	     r[++j] = '</td></tr>';
	    	 }
	    	 $('#data_table').html(r.join(''));			    	
	    	return;
	    },
	    error: function(){
	    	alert("REST Error!");
	    	return;
	    }
	});
}