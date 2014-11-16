function selectedResult(selected) {
	console.log(selected);
	$("#main h1").hide();
	$("#main div").html(selected);
}


$(function() {
  var products = [
    {
    	value: "chanel-lift",
    	label: "Chanel - Lift",
      brandLabel: "Chanel",
      productLabel: "Lift",
      icon: "imgTest.jpg"
    },
    {
    	value: "chanel-lift-2",
    	label: "Chanel - Lift 2",
      brandLabel: "Chanel",
      productLabel: "Lift 2",
      icon: "imgTest.jpg"
    },
  ];

	function log( message ) {
	      $( "<div onclick='selectedResult(this)'>" ).html( message ).prependTo( ".results" );
	      $( ".results" ).scrollTop( 0 );
	    }

  $( "#product" ).autocomplete({
    minLength: 0,
    source: products,
    focus: function( event, ui ) {
      $( "#product" ).val( ui.item.label );
      return false;
    },
    select: function( event, ui ) {
        log( ui.item ?
          "<h3>" + ui.item.label + "</h3>" +
          "<img src='img/" + ui.item.icon + "'>" :
          "Nothing selected, input was " + this.label);
        return false;
      },
  })
});