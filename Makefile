debug_kgml2graph:
	ipython -pylab -i -c "from parse_KGML import *; (graph, nodes, genes, reactions) = KGML2Graph('hsa00510_n-glycan.xml')"
