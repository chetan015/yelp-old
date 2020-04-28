async function createHeatMap(businessId){
    // access data
    let dataset = await d3.json("/../tempeCheckinNew.json");
    var checkIns = dataset.filter( (data) => data.business_id === businessId).map(data => data.checkin)[0];
    var checkInList = []
    Object.keys(checkIns).forEach(i =>Object.values(checkIns[i]).forEach(j=>checkInList.push(j)));
    
    // set margins, width
    var margin = { top: 50, right: 0, bottom: 60, left: 120 },
    offsetWidth = parseInt(d3.select("#heatMapArea").style("width").slice(0,-2))
    //offsetWidth = 800
    width = 0.8*offsetWidth - margin.left - margin.right
    height = 0.45*width - margin.top - margin.bottom
    boxSize = Math.floor(width / 24),
    legendBoxWidth = boxSize*1.5,
    dayLabelList = ["M", "T", "W", "TH", "F", "SA", "SU"],
    timeLabelList = ["1a", "2a", "3a", "4a", "5a", "6a", "7a", "8a", "9a", "10a", "11a", "12p", "1p", "2p", "3p", "4p", "5p", "6p", "7p", "8p", "9p", "10p", "11p"];
    var svg = d3.select("#heatMapArea").append("svg")
        .attr("width", width + margin.left + margin.right)
        .attr("height", height + margin.top + margin.bottom)
        .append("g")
        .attr("transform", "translate(" + margin.left + "," + margin.top + ")");
    svg.selectAll(".daylabel")
          .data(dayLabelList)
          .enter().append("text")
          .text(function (d) { return d; })
          .attr("x", 0)
          .attr("y", function (d, i) { return i * boxSize; })
          .style("text-anchor", "end")
          .style("font-size","10px")
          .attr("fill","#081D58")
          .style("font-weight","bold")
          .attr("transform", "translate(-10," + boxSize / 1.5 + ")");
          
    svg.selectAll(".timelabel")
          .data(timeLabelList)
          .enter().append("text")
          .text(function(d,i){return d;})
          .attr("x",function(d,i){return i*boxSize;})
          .attr("y",0)
          .attr("transform", "translate(" + boxSize/1.5+ ", -10)")
          .style("font-size","10px")
          .style("font-weight","bold")
          .attr("fill","#081D58");
    var thresholds = [2,5,10,20,35,50,75,100];
                      
    var colorScale = d3.scaleThreshold()
        .domain(thresholds)
        .range(d3.schemeYlGnBu[9])
        ;
    var boxes = svg.selectAll(".box")
        .data(checkInList);  
        boxes.enter().append("rect")
              .attr("x", function(d,i) { return i%24 * boxSize; })
              .attr("y", function(d,i) { return Math.floor(i/24) * boxSize; })
              .attr("rx", 5)
              .attr("ry", 5)
              .attr("class", "box")
              .attr("width", boxSize-2)
              .attr("height", boxSize-2)
              .style("fill", "#FEFEFE")
              .style("stroke","#00000040")
              .style("stroke-width","1px")
              .transition().duration(function(d,i){return 100+(i%24)*50+Math.floor(i/24)*50;})
              .style("fill", function(d) { return colorScale(d); });
                        
    boxes.exit().remove();    
    var legend = svg.selectAll(".legend").attr("class","legendMark")
    // legend.append("g");
    // var legendBox = legend.selectAll("g");
    legend.data([0].concat(thresholds)).enter().append("rect")
        .attr("x",function(d,i){return 150+legendBoxWidth*i})
        .attr("y",height)
        .attr("width",legendBoxWidth)
        .attr("height",legendBoxWidth/2)
        .style("fill","white")
        .attr("class","legendBox")
        .transition().duration(function(d,i){return 300 + i*170;})
        .style("fill",function(d){return colorScale(d);});

    legend.data(["<2"].concat(thresholds.slice(1)).concat(">=100")).enter().append('text')
    .attr("x",function(d,i){val = 140+legendBoxWidth*(i+1);if(i==7)val-=5; else if(i==8) val-=20;return val})
    .attr("y",height+40)
    .text(function(d){return d;})
    .style("font-size","10px")
    .style("font-weight","bold")
    .attr("fill","#081D58");;
   
}