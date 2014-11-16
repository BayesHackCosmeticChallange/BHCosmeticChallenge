$(function() {
  var products = [
    {
    	value: "chanel-lift",
    	label: "Chanel - Lift",
      brandLabel: "Chanel",
      productLabel: "Lift",
      icon: "imgTest.jpg",
      score: { 
				"feature1" : 1,  
      	"feature2"  : 2,
    		"feature3"  : 3,
    		"feature4"  : 4,
    		"feature5"  : 5,
    		"feature6"  : 6
    		}
    },
    {
    	value: "chanel-lift-2",
    	label: "Chanel - Lift 2",
      brandLabel: "Chanel",
      productLabel: "Lift 2",
      icon: "imgTest.jpg",
      score: { 
				"feature1" : 4,  
      	"feature2"  : 5,
    		"feature3"  : 6,
    		"feature4"  : 7,
    		"feature5"  : 8,
    		"feature6"  : 9
    		}
    },
  ];

	function log( message ) {
	      $( "<div id='result'>" ).html( message ).prependTo( ".results" );
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
          "<div id='feature1' hidden>" + ui.item.score.feature1 + "</div>"+
          "<div id='feature2' hidden>" + ui.item.score.feature2 + "</div>"+
          "<div id='feature3' hidden>" + ui.item.score.feature3 + "</div>"+
          "<div id='feature4' hidden>" + ui.item.score.feature4 + "</div>"+
          "<div id='feature5' hidden>" + ui.item.score.feature5 + "</div>"+
          "<div id='feature6' hidden>" + ui.item.score.feature6 + "</div>"+
          "<img src='img/" + ui.item.icon + "'>" :
          "Nothing selected, input was " + this.label);
        return false;
      },
  })

	$( "div" ).on( 'click', '#result', function (e) {
		$("#main h1").hide();
		$("#main div").html(this);
		
		for (var i = 0; i < 6; i++) {
			var j = i  + 1;
			var curValue = $(this).find( "#feature" + j ).html();
		  d3.select('#handle' + i) 
			.attr("cx", width/2 + (rcenter + curValue * branch_len/10) * Math.cos(2 * Math.PI / n_branch * i - Math.PI / 2))            
			.attr("cy", height/2 + (rcenter + curValue * branch_len/10) * Math.sin(2 * Math.PI / n_branch * i - Math.PI / 2))
		};
		update_polygon();
		return false;
	});

});
