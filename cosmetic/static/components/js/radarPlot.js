// svg part
var n_branch = 5;
var height= 450;
var width = 450;
var viewBox = "0 40 450 450";
var rcenter = 0;
var rhandle = 3;
var rtext = 60;
var base_color = "#fff";
var color = base_color;

var feature1 = 'Efficacy - Long run';
var feature2 = 'Efficacy - Short run';
var feature3 = 'Price/Quality';
var feature4 = 'Texture';
var feature5 = 'Smell';

var branch_len = height / 2 - 2*rtext;

var handles = [];

var names = [feature1, feature2,feature3, feature4, feature5];

var svgContainer = d3.select("#main").append("svg")
    .attr({
        "width": '100%',
        "height": '100%'
    })
    .attr("viewBox", viewBox)
    .attr("preserveAspectRatio", "xMidYMin")

var polygon = svgContainer.append("polygon")
    .attr("stroke", color)
    .attr("fill", color)
    .attr("fill-opacity", "0.2")
    .attr("stroke-width","1");

for (i=0 ; i<n_branch ; i++) {

    svgContainer.append("line")        
        .attr("stroke",color)
        .attr("stroke-width","1")
        .attr("stroke-linecap", "round")
        .attr("x1",width/2)
        .attr("y1",height/2)
        .attr("x2",width/2 + (branch_len + rcenter) * Math.cos(2 * Math.PI / n_branch * i - Math.PI / 2))
        .attr("y2",height/2 + (branch_len + rcenter) * Math.sin(2 * Math.PI / n_branch * i - Math.PI / 2));

    svgContainer.append("text")
        .text(names[i])
        .attr('id', names[i])
        .attr("fill",color)
        .attr("font-size", "1rem")
        .attr('text-anchor', 'middle')
        .attr('font-weight', 'light')
        .attr("font-family","Lato")
        .attr("x",width/2 + (branch_len + rtext + rcenter) * Math.cos(2 * Math.PI / n_branch * i - Math.PI / 2))
        .attr("y",height/2 + (branch_len + rtext + rcenter) * Math.sin(2 * Math.PI / n_branch * i - Math.PI / 2));

    svgContainer.append("text")
        .text('5')
        .attr('id', 'value' + i)
        .attr("fill",color)
        .attr("font-size", "1.5rem")
        .attr('text-anchor', 'middle')
        .attr('font-weight', 'light')
        .attr("font-family","Lato")
        .attr("x",width/2 + (branch_len + rtext + rcenter) * Math.cos(2 * Math.PI / n_branch * i - Math.PI / 2))
        .attr("y",height/2 + (branch_len + rtext + rcenter) * Math.sin(2 * Math.PI / n_branch * i - Math.PI / 2) + 40);

    var handle = svgContainer.append("circle")
        .attr("fill",color)
        .attr("cx",width/2 + (rcenter + branch_len/2) * Math.cos(2 * Math.PI / n_branch * i - Math.PI / 2))
        .attr("cy",height/2 + (rcenter + branch_len/2) * Math.sin(2 * Math.PI / n_branch * i - Math.PI / 2))
        .attr("r", rhandle)
        .attr("id", "handle" + i)
    handles.push(handle);
}

function update_polygon() {
    var handle_pol = "";
    for (i=0 ; i<n_branch ; i++) {
        handle_pol += handles[i].attr("cx")+","+handles[i].attr("cy")+" ";
    }
    polygon.attr("points", handle_pol);
}

function update_value(selected, r) {
    d3.select("#value" + selected)
        .text(r);
}

update_polygon();



