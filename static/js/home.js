
var inputBox = document.getElementById("urlinput");

inputBox.addEventListener("change", () => {
        document.getElementById("urlsubmit").disabled = true;
        var x = document.getElementById("urlinput").value;
        var regex = new RegExp("\\s", "g");
        var replace = "";
        var res = x.replace(regex, replace);
    
        if(res.length < 1){
                document.getElementById("urlinput").style.borderColor = "#ed4956"; 
                return false;
        }
        else{
                document.getElementById("urlinput").style.borderColor = "#18db18";
                document.getElementById("urlsubmit").disabled = false;
                return false;
        }
    
});

inputBox.addEventListener("blur", () => {

        document.getElementById("urlsubmit").disabled = true;
        var x = document.getElementById("urlinput").value;
        var regex = new RegExp("\\s", "g");
        var replace = "";
        var res = x.replace(regex, replace);
    
        if(res.length < 1){
                document.getElementById("urlinput").style.borderColor = "#ed4956"; 
                return false;
        }
        else{
                document.getElementById("urlinput").style.borderColor = "#18db18";
                document.getElementById("urlsubmit").disabled = false;
                return false;
        }
    
});