Design-related TODO list:

1. Check out [bibserver](https://github.com/okfn/bibserver) since it can be useful. Check out http://holtzermann17.github.io/skelodml/bibserver-setup.html and https://github.com/okfn/bibserver/issues/256 when installing.
2. Make a decision about initial program design.
3. Make a decision about initial technologies to use.
4. Check out other applications such as:
  - https://github.com/jasonzou/MyPapers

#### Graph creation
- [NetworkX](https://networkx.github.io/): static plotting, currently in use. Can _export_ to use in D3.js. [Example](https://www.udacity.com/wiki/creating-network-graphs-with-python#creating-network-graphs-with-python)
- [Graph-tool](https://graph-tool.skewed.de/) (alternative to NetworkX): seems much powerful and fast (Boost-based).  Supports Graphviz.

#### Graph plotting
- [NetworkX](https://networkx.github.io/): simple and easy static plotting. Can _export_ to use in D3.js.
- [Graphviz](http://www.graphviz.org/Documentation.php) Provides proweful static visualization.
- [Bokeh](http://bokeh.pydata.org/en/latest/) General purpose python plotting (static I think), D3.js-like.
- D3.js, interactive.
	- Binding for JS: http://pyjs.org/ (in case 3D.js is used perhaps we can use this)