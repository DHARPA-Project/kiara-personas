function _1(md){return(
md`# Kiara features`
)}

function _kiaraFeats(update,tree,kiara,graph)
{
  setTimeout(function() { update(tree(kiara)); }, 100);
  return graph(kiara, {label: d => d.data.name})
}


function _dx(){return(
50
)}

function _dy(){return(
180
)}

function _tree(d3,dx,dy){return(
d3.tree().nodeSize([dx, dy]).separation((a, b) => (a.parent == b.parent ? 1 : 2) / a.depth)
)}

function _treeLink(d3){return(
d3.linkHorizontal().x(d => d.y).y(d => d.x)
)}

function _graph(tree,d3,width,dx,treeLink,$0){return(
function graph(root, {
  label = d => d.data.id, 
  highlight = () => false,
  marginLeft = 130
} = {}) {
  root = tree(root);

  let x0 = Infinity;
  let x1 = -x0;
  root.each(d => {
    if (d.x > x1) x1 = d.x;
    if (d.x < x0) x0 = d.x;
  });

  const svg = d3.create("svg")
      .attr("viewBox", [0, 0, width, x1 - x0 + dx * 5
                       ])
      .style("overflow", "visible")
      .attr("id", "kiara-features");
  
  const g = svg.append("g")
      .attr("font-family", "Palanquin")
      .attr("font-size", 15)
      .attr("transform", `translate(${marginLeft},${dx - x0})`);
    
  const link = g.append("g")
    .attr("fill", "none")
    .attr("stroke", "#555")
    .attr("stroke-opacity", 0.4)
    .attr("stroke-width", 1.5)
  .selectAll("path")
    .data(root.links())
    .join("path")
      //.attr("stroke", d => highlight(d.source) && highlight(d.target) ? "red" : null)
      //.attr("stroke-opacity", d => highlight(d.source) && highlight(d.target) ? 1 : null)
      .attr("d", treeLink);
  
  const node = g.append("g")
      .attr("stroke-linejoin", "round")
      .attr("stroke-width", 3)
    .selectAll("g")
    .data(root.descendants())
    .join("g")
      .attr("transform", d => `translate(${d.y},${d.x})`);

  node.append("circle")
      .attr("cx", d => d.depth == 1 ? 1:0)
      .attr("fill", d => highlight(d) ? "red" : d.children ? "#555" : "#999")
      .attr("r", 2.5);

  node.append("rect")
    .filter(function(d) {
      return d.depth == 1
    })
    .attr("x",  d => d.children ? -6 : 6)
    .attr("y", "0.31em")
    .style("fill", "lightgrey")
    .style("opacity", "1"); 

  node.append("text")
      .attr("fill", "black")
      .attr("font-size", function (d) {
        if (d.depth == 0) {
          return 18
        }
      })
      .attr("class", function(d) {
        return d.data.name.split(' ').join('_')
      })
      //.attr("stroke", "white")
      //.attr("paint-order", "stroke")
      .attr("dy", "0.31em")
      .attr("x", d => d.children ? -6 : 6)
      .attr("text-anchor", d => d.children ? "end" : "start")
      .html(label);


  node.on("mouseover", (e,d) => {
    
      const elClass = `${"."}${d.data.name.split(' ').join('_')}`
   
      if (d.depth == 2) {
         d3.selectAll(elClass)
        .attr("fill", "rgb(9, 105, 218)")
        .attr("font-weight", "bold")
      }
    
      if (d.depth == 1) {
        const a = d.data.name.split(' ').join('_')
        const b = a.split('/').join('_')

        const rectid = `${"#rect-"}${b}`
        
         d3.selectAll(rectid)
          .style("fill", "rgba(9, 105, 218, 0.7)")
        }
    
     
    })
    .on("mouseout", (e,d) => {
      
      d3.selectAll("text")
        .attr("fill", "black")
        .attr("font-weight", "normal")
      
      d3.selectAll("rect")
        .style("fill", "lightgrey")
    })

    .on("click", (e,d) => {

      $0.value = d.data.name
      
    })
  
  return svg.node();

}
)}

function _clicked(){return(
"Kiara"
)}

function _update(d3){return(
function update(data) {
  
   d3.selectAll("text")
          .each(function(d) { d.bbox = this.getBBox(); });

  const xMargin = 4
  const yMargin = 2                  

  d3.selectAll("rect")
          .data(data)
          .filter(function(d) {
      return d.depth == 1
    })
          .join("rect")
            .attr("id", function(d) {
              const a = d.data.name.split(' ').join('_')
              const b = a.split('/').join('_')
              return "rect-" + b

            } )
            .attr("x", d => -(172 + 2* xMargin))
            .attr("width", d => 172 + 2 * xMargin)
            .attr("height", d => d.bbox.height + 3 * yMargin)
            //.attr("id", function(d){console.log(d)})
            .attr('transform', function(d) {
                return `translate(-${xMargin}, -${d.bbox.height * 0.8 + yMargin})`
            });
  
}
)}

function _yMargin(){return(
2
)}

function _kiara(d3){return(
d3.hierarchy({
  name: "Kiara Personas",
  children: [
    {name: "Modules/Pipelines Users",
      children: [
        {name: "CLI"},
        {name: "Data registry"},
        {name: "Pipeline"}
      ]},
    {
      name: "Modules/Pipelines Creators",
      children: [
        {name: "CLI"},
        {name: "Data registry"},
        {name: "Pipeline"},
        {name: "Plugin"},
        {name: "Python API"},
      ]},

    {
      name: "Pipeline-Apps Creators",
      children: [
        {name: "CLI"},
        {name: "Data registry"},
        {name: "Pipeline"},
        {name: "Plugin"},
        {name: "Python API"},
      ]
    },

    {
      name: "Front-End Developers",
      children: [
        {name: "Rest API"},
        {name: "Workflow object"},
      ]
    }
  ]
})
)}

function _style(html){return(
html`
  <style>
    @import url('https://fonts.googleapis.com/css2?family=Palanquin:wght@400;700&display=swap');
  text {
    cursor: pointer;
  }
</style>`
)}

export default function define(runtime, observer) {
  const main = runtime.module();
  main.variable(observer()).define(["md"], _1);
  main.variable(observer("viewof kiaraFeats")).define("viewof kiaraFeats", ["update","tree","kiara","graph"], _kiaraFeats);
  main.variable(observer("kiaraFeats")).define("kiaraFeats", ["Generators", "viewof kiaraFeats"], (G, _) => G.input(_));
  main.variable(observer("dx")).define("dx", _dx);
  main.variable(observer("dy")).define("dy", _dy);
  main.variable(observer("tree")).define("tree", ["d3","dx","dy"], _tree);
  main.variable(observer("treeLink")).define("treeLink", ["d3"], _treeLink);
  main.variable(observer("graph")).define("graph", ["tree","d3","width","dx","treeLink","mutable clicked"], _graph);
  main.define("initial clicked", _clicked);
  main.variable(observer("mutable clicked")).define("mutable clicked", ["Mutable", "initial clicked"], (M, _) => new M(_));
  main.variable(observer("clicked")).define("clicked", ["mutable clicked"], _ => _.generator);
  main.variable(observer("update")).define("update", ["d3"], _update);
  main.variable(observer("yMargin")).define("yMargin", _yMargin);
  main.variable(observer("kiara")).define("kiara", ["d3"], _kiara);
  main.variable(observer("style")).define("style", ["html"], _style);
  return main;
}
