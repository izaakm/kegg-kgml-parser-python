import unittest as U
from parse_KGML import *

class _BaseKGMLFile(U.TestCase):
    """
    base test class
    """
    nodes = []
    edges = []
    pathway_file = ''
    pathway_type = ''

    @classmethod
    def setUpClass(cls):
        (tree, graph, nodes, genes, reactions) = KGML2Graph(cls.pathway_file)
        cls.graph = graph

    def setUp(self):
        pass

    def test_nodes(self):
        self.assertEqual(self.nodes, self.graph.nodes())

class _BaseKOFile(_BaseKGMLFile):
    """
    KGML file corresponding to a KO pathway
    (beginning with ko)
    """
    pathway_type = 'ko'

class _BaseOrganismFile(_BaseKGMLFile):
    """
    KGML file corresponding to an organism
    (i.e. not a 'ko0000x' file)
    """
    pathway_type = 'o'

class test_GlycolisisHSA00010(_BaseOrganismFile):
    """
    """
    pathway_file = './data/hsa00010.xml'
    nodes = ['PCK1', 'BPGM', 'ALDH3A1', 'GAPDH', 'LDHAL6A', 'TPI1', 'AKR1A1', 'FBP1', 'PKLR', 'Carbon fixation in photosynthetic organisms', 'PFKL', 'PGK1', 'PDHA1', 'GPI', 'Starch and sucrose metabolism', 'DLD', 'ACSS2', 'GCK', 'PGM1', 'ENO1', 'DLAT', 'ALDOA', 'GALM', 'Propanoate metabolism', 'G6PC', 'PGAM4', 'ALDH2', 'Pentose phosphate pathway', 'ADH1A', 'Citrate cycle (TCA cycle)']

    edges = []


# nodes = ['ALG8', 'ALG9', 'GCS1', 'ST6GAL1', 'ALG2', 'ALG3', 'ALG1', 'ALG6', 'GANAB', 'ALG5', 'DOLPP1', 'ALG10B', 'DAD1', 'Other glycan degradation', 'Keratan sulfate biosynthesis', 'High-mannose type N-glycan biosynthesis', 'MGAT5B', 'B4GALT1', 'DPM3', 'DPM2', 'DPM1', 'DPAGT1', 'MAN2A1', 'MGAT1', 'MGAT2', 'MGAT3', 'Fructose and mannose metabolism', 'ALG11', 'ALG12', 'ALG13', 'ALG14', 'MAN1A2', 'Glycosylphosphatidylinositol(GPI)-anchor biosynthesis', 'MGAT4B', 'RFT1', 'FUT8']
