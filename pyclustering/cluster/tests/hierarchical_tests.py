"""!

@brief Unit-tests for hierarchical algorithm.

@authors Andrei Novikov (spb.andr@yandex.ru)
@date 2014-2015
@copyright GNU Public License

@cond GNU_PUBLIC_LICENSE
    PyClustering is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.
    
    PyClustering is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.
    
    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <http://www.gnu.org/licenses/>.
@endcond

"""

import unittest;

from pyclustering.samples.definitions import SIMPLE_SAMPLES, FCPS_SAMPLES;

from pyclustering.cluster.hierarchical import hierarchical;
from pyclustering.support import read_sample;

from random import random;

class Test(unittest.TestCase):
    def templateClusteringResults(self, path, number_clusters, expected_length_clusters, ccore = False):
        sample = read_sample(path);
        
        hierarchical_instance = hierarchical(sample, number_clusters, ccore);
        hierarchical_instance.process();
        
        clusters = hierarchical_instance.get_clusters();
        
        assert sum([len(cluster) for cluster in clusters]) == len(sample);
        assert sum([len(cluster) for cluster in clusters]) == sum(expected_length_clusters);
        assert sorted([len(cluster) for cluster in clusters]) == expected_length_clusters;
    
    def testClusteringSampleSimple1(self):
        self.templateClusteringResults(SIMPLE_SAMPLES.SAMPLE_SIMPLE1, 2, [5, 5]);
        self.templateClusteringResults(SIMPLE_SAMPLES.SAMPLE_SIMPLE1, 1, [10]);

    def testClusteringSampleSimple2(self):
        self.templateClusteringResults(SIMPLE_SAMPLES.SAMPLE_SIMPLE2, 3, [5, 8, 10]);        
        self.templateClusteringResults(SIMPLE_SAMPLES.SAMPLE_SIMPLE2, 1, [23]);

    def testClusteringSampleSimple3(self):
        self.templateClusteringResults(SIMPLE_SAMPLES.SAMPLE_SIMPLE3, 4, [10, 10, 10, 30]);        
        self.templateClusteringResults(SIMPLE_SAMPLES.SAMPLE_SIMPLE3, 1, [60]);
        
    def testClusteringSampleSimple4(self):
        self.templateClusteringResults(SIMPLE_SAMPLES.SAMPLE_SIMPLE4, 5, [15, 15, 15, 15, 15]);
        self.templateClusteringResults(SIMPLE_SAMPLES.SAMPLE_SIMPLE4, 1, [75]);
        
    def testClusteringSampleSimple5(self):
        self.templateClusteringResults(SIMPLE_SAMPLES.SAMPLE_SIMPLE5, 4, [15, 15, 15, 15]);
        self.templateClusteringResults(SIMPLE_SAMPLES.SAMPLE_SIMPLE5, 1, [60]); 

    def testClusteringByCore(self):
        self.templateClusteringResults(SIMPLE_SAMPLES.SAMPLE_SIMPLE1, 2, [5, 5], ccore = True);
        self.templateClusteringResults(SIMPLE_SAMPLES.SAMPLE_SIMPLE1, 1, [10], ccore = True);
        self.templateClusteringResults(SIMPLE_SAMPLES.SAMPLE_SIMPLE2, 3, [5, 8, 10], ccore = True);
        self.templateClusteringResults(SIMPLE_SAMPLES.SAMPLE_SIMPLE2, 1, [23], ccore = True);
        self.templateClusteringResults(SIMPLE_SAMPLES.SAMPLE_SIMPLE3, 4, [10, 10, 10, 30], ccore = True);
        self.templateClusteringResults(SIMPLE_SAMPLES.SAMPLE_SIMPLE3, 1, [60], ccore = True);
        self.templateClusteringResults(SIMPLE_SAMPLES.SAMPLE_SIMPLE4, 5, [15, 15, 15, 15, 15], ccore = True);
        self.templateClusteringResults(SIMPLE_SAMPLES.SAMPLE_SIMPLE4, 1, [75], ccore = True);
        self.templateClusteringResults(SIMPLE_SAMPLES.SAMPLE_SIMPLE5, 4, [15, 15, 15, 15], ccore = True);
        self.templateClusteringResults(SIMPLE_SAMPLES.SAMPLE_SIMPLE5, 1, [60], ccore = True);
        
    
    def templateClusterAllocationOneDimensionData(self, ccore_flag):
        input_data = [ [random()] for i in range(10) ] + [ [random() + 3] for i in range(10) ] + [ [random() + 5] for i in range(10) ] + [ [random() + 8] for i in range(10) ];
        
        hierarchical_instance = hierarchical(input_data, 4, ccore_flag);
        hierarchical_instance.process();
        clusters = hierarchical_instance.get_clusters();
        
        assert len(clusters) == 4;
        for cluster in clusters:
            assert len(cluster) == 10;
                
    def testClusterAllocationOneDimensionData(self):
        self.templateClusterAllocationOneDimensionData(False);
        
    def testClusterAllocationOneDimensionDataByCore(self):
        self.templateClusterAllocationOneDimensionData(True);

if __name__ == "__main__":
    unittest.main();
