function myFunction() {
	document.getElementById("myDropdown").classlist.toggle("show");

}

window.onclick = function(event){
	if(!event.targetmatches('.dropbtn')){

		var dropdowns = document.getElementByClassName("dropdown-content");
		var x;
		for(x=0; x<dropdowns.length;x++)
			var opendropdown = dropdowns[x]{
			if(opendropdown.classlist.contains('show')){
				opendropdown.classlist.remove('show');
			}
		}
	}
}