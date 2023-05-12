// Load the data from the API endpoint
d3.json('/data/').then(function(data) {

    // Create the chart
    var svg = d3.select('#chart');
    var margin = {top: 20, right: 20, bottom: 30, left: 40};
    var width = +svg.attr('width') - margin.left - margin.right;
    var height = +svg.attr('height') - margin.top - margin.bottom;
    var g = svg.append('g').attr('transform', 'translate(' + margin.left + ',' + margin.top + ')');
  
    var x = d3.scaleBand().rangeRound([0, width]).padding(0.1);
    var y = d3.scaleLinear().rangeRound([height, 0]);
  
    x.domain(data.map(function(d) { return d.sector; }));
    y.domain([0, d3.max(data, function(d) { return d.impact; })]);
  
    g.append('g')
      .attr('class', 'axis axis-x')
      .attr('transform', 'translate(0,' + height + ')')
      .call(d3.axisBottom(x));
  
    g.append('g')
      .attr('class', 'axis axis-y')
      .call(d3.axisLeft(y).ticks(10, '%'))
      .append('text')
      .attr('class', 'axis-title')
      .attr('transform', 'rotate(-90)')
      .attr('y', 6)
      .attr('dy', '0.71em')
      .attr('text-anchor', 'end')
      .text('Impact');
  
    g.selectAll('.bar')
      .data(data)
      .enter().append('rect')
      .attr('class', 'bar')
      .attr('x', function(d) { return x(d.sector); })
      .attr('y', function(d) { return y(d.impact); })
      .attr('width', x.bandwidth())
      .attr('height', function(d) { return height - y(d.impact); });
  
});
