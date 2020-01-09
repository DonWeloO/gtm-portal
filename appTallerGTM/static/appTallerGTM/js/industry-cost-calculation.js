 //Set up an associative array
 //The keys represent the size of the cake
 //The values represent the cost of the cake i.e A 10" cake cost's $35
 var cake_prices = new Array();
 cake_prices["Round6"]=20;
 cake_prices["Round8"]=25;
 cake_prices["Round10"]=35;
 cake_prices["Round12"]=75;
 
 //wall_service_prices 
 var wall_service_prices= new Array();
 wall_service_prices["None"]=0;
 wall_service_prices["Painting"]=40;
 wall_service_prices["Painting_repair"]=60;


 //floor_service_prices 
 var floor_service_prices= new Array();
 floor_service_prices["None"]=0;
 floor_service_prices["Tiles"]=20;
 floor_service_prices["Carpet"]=15;
 floor_service_prices["Wood"]=10;
 
	 

//This function finds the filling price based on the 
//drop down selection
function WallServicePrice()
{
    var wallServicePrice=0;
    //Get a reference to the form id="cakeform"
    var theForm = document.forms["cakeform"];
    //Get a reference to the select id="wall-service"
     var selectedFilling = theForm.elements["wall-service"];
     
    //set cakeFilling Price equal to value user chose
    //For example wall_service_prices["Lemon".value] would be equal to 5
    wallServicePrice = wall_service_prices[selectedFilling.value];

    //finally we return cakeFillingPrice
    return wallServicePrice;
}

//This function finds the filling price based on the 
//drop down selection
function FloorServicePrice()
{
    var floorServicePrice=0;
    //Get a reference to the form id="cakeform"
    var theForm = document.forms["cakeform"];
    //Get a reference to the select id="wall-service"
     var selectedFilling = theForm.elements["floor-service"];
     
    //set cakeFilling Price equal to value user chose
    //For example wall_service_prices["Lemon".value] would be equal to 5
    floorServicePrice = floor_service_prices[selectedFilling.value];

    //finally we return cakeFillingPrice
    return floorServicePrice;
}

function calculateTotal()
{
    //Here we get the total price by calling our function
    //Each function returns a number so by calling them we add the values they return together
    var cakePrice = WallServicePrice() + FloorServicePrice();
    
    //display the result
    var divobj = document.getElementById('totalPrice');
    divobj.style.display='block';
    divobj.innerHTML = "Total Cost $"+cakePrice;

}

function hideTotal()
{
    var divobj = document.getElementById('totalPrice');
    divobj.style.display='none';
}