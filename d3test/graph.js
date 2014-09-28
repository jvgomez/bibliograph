// General config variables.
var w = 200;
var h = 200;

// Setting SVG blob
var vis = d3.select("#graph")
            .append("svg")
            .attr("width", w)
            .attr("height", h);

vis.text("My BiblioGraph")
   .select("#graph");

// Nodes and connections data
var nodes = [{x: 40, y: 50},
             {x: 50, y: 80},
             {x: 90, y: 120}]

var links = [{source: nodes[0], target: nodes[1]},
             {source: nodes[2], target: nodes[1]}]

// Plotting nodes
vis.selectAll("circle")
   .data(nodes)
   .enter()
   .append("circle")
   .attr("cx", function(d) {return d.x})
   .attr("cy", function(d) {return d.y})
   .attr("r", "10px")

// Plotting connections
vis.selectAll("line")
   .data(links)
   .enter()
   .append("line")
   .attr("x1", function(d) {return d.source.x})
   .attr("y1", function(d) {return d.source.y})
   .attr("x2", function(d) {return d.target.x})
   .attr("y2", function(d) {return d.target.y})