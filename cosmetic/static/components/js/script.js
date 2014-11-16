$(function() {

//    var products;
//    $.ajax({
//        type: "GET",
//        url: "/chart",
//        success: function(result){
//            products = result;
//        }
//    });

	function log( message ) {
	      $( "<div id='result'>" ).html( message ).prependTo( ".results" );
	      $( ".results" ).scrollTop( 0 );
	    }

  $( "#product" ).autocomplete({
    minLength: 0,
    source: function(request, response){
            $.ajax({
            type: "GET",
            url: "/chart",
            success: function(result){
                response(result);
            }
       });
    },
    focus: function( event, ui ) {
      $( "#product" ).val( ui.item.label );
      return false;
    },
    select: function( event, ui ) {
        log( ui.item ?
          "<h3>" + ui.item.label + "</h3>" +
          "<div id='feature1' hidden>" + ui.item.score.efficancy_long + "</div>"+
          "<div id='feature2' hidden>" + ui.item.score.smell + "</div>"+
          "<div id='feature3' hidden>" + ui.item.score.texture + "</div>"+
          "<div id='feature4' hidden>" + ui.item.score.toxicity + "</div>"+
          "<div id='feature5' hidden>" + ui.item.score.lavant + "</div>"+
          "<div id='feature6' hidden>" + ui.item.score.rincable + "</div>"+
          "<img src='../static/image/productAvatar.png'>" :
          "Nothing selected, input was " + this.label);
        return false;
      },
  })

	$( "#left" ).on( 'click', '#result', function (e) {
		$("#main h1").hide();
		$("#main div").html(this);
		
		for (var i = 0; i < 6; i++) {
			var j = i  + 1;
			var curValue = $(this).find( "#feature" + j ).html();
		  d3.select('#handle' + i) 
			.attr("cx", width/2 + (rcenter + curValue * branch_len/10) * Math.cos(2 * Math.PI / n_branch * i - Math.PI / 2))            
			.attr("cy", height/2 + (rcenter + curValue * branch_len/10) * Math.sin(2 * Math.PI / n_branch * i - Math.PI / 2))
			update_value( i, curValue);
			update_polygon();
		};
		return false;
	});

});
