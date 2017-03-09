//initiate these on load
window.onload = function() {
	console.log("fired");
	// get butons
    var buttons = document.getElementsByClassName("selection");
	var objs = new Array();
	//make then an array
	for(var i = 0; i < buttons.length; i++){
		objs.push( document.getElementById(buttons[i].id));
	}
	//set checkboxes to be checked
	forEach(objs,function(obj){
		obj.checked = true;
	});
	//run through array and asign on click function
    forEach(objs, function(obj){
		obj.onclick = function() {
			if(obj.checked ==false){
				forEach(obj.dataset.cls,function(obj){
					hide(obj);
				});
			}else{
				forEach(obj.dataset.cls,function(obj){
					show(obj);
				});
			}
        }
	});
}

//hide an element
function hide(elm){
	if(elm.style.display != "none"){
		elm.style.display = "none";
	}
}
//show an element
function show(elm){
	if(elm.style.display != "block"){
		elm.style.display = "block";
	}
}
//for each class or array element
function forEach(obj, fun) {
    if (typeof(obj) == "string") {
        var arr = document.getElementsByClassName(obj);
        for (var i = 0; i < arr.length; i++) {
            fun(arr[i]);
        }
    } else {
        for (var i = 0; i < obj.length; i++) {
            fun(obj[i]);
        }
    }
}
