$(function() {

   var products = $.ajax({
       type: "GET",
       url: "/chart",
       async: false,
       success: function(result){
           products = result;
       }
   }).responseText;
   var cache = $.parseJSON(products);
	function log( message ) {
	      $( "<div id='result'>" ).html( message ).prependTo( ".results" );
	      $( ".results" ).scrollTop( 0 );
	    }

  function toxReport (message) {
        console.log(message);
        $( "#result" ).append( message );
      }

  $( "#product" ).autocomplete({
    minLength: 0,
    source: cache,
    focus: function( event, ui ) {
      $( "#product" ).val( ui.item.label );
      return false;
    },
    select: function( event, ui ) {
        log( ui.item ?
          "<h3>" + ui.item.label + "</h3>" +
          "<div id='feature1' hidden>" + ui.item.score.efficancy_short + "</div>"+
          "<div id='feature2' hidden>" + ui.item.score.efficancy_long + "</div>"+
          "<div id='feature3' hidden>" + ui.item.score['quality on price'] + "</div>"+
          "<div id='feature4' hidden>" + ui.item.score.texture + "</div>"+
          "<div id='feature5' hidden>" + ui.item.score.smell + "</div>"+
          "<img src='../static/image/productAvatar.png'>" :
          "Nothing selected, input was " + this.label);
        console.log(ui.item.score.toxicity);
        if (ui.item.score.toxicity.male_reproductive == 1){
        toxReport ( 
          "<div id='toxicity' hidden>Reported as toxic for male reproduction</div>"
          );
        }
        else if (ui.item.score.toxicity.female_reproductive == 1){
        toxReport ( 
          "<div id='toxicity' hidden>Reported as toxic for female reproduction</div>"
          );
        }
        else if (ui.item.score.toxicity.cancer == 1){
        toxReport ( 
          "<div id='toxicity' hidden>Reported as cancerogene</div>"
          );
        }
        else if (ui.item.score.toxicity.developmental == 1){
        toxReport ( 
          "<div id='toxicity' hidden>Reported as potential teratogene</div>"
          );
        }
        else {
        toxReport ( 
          "<div id='toxicity' hidden>Not reported as toxic</div>"
          );  
        }
        return false;
      },
  })

	$( "#left" ).on( 'click', '#result', function (e) {
    
    $("#main h1").hide();
		$("#main div").html(this);
    $("#main #toxicity").hide();

    $("#right #toxicReport").html(this.lastElementChild);
    $("#right #toxicity").show();


    // $("#right #toxicity").show();
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

  $("input").on('click', function() {
    if ($(this).val() != ""){
      $(this).val("");
    }
    return false;
  });
});