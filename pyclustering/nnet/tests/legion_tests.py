"""!

@brief Unit-tests for Local Excitatory Global Inhibitory Oscillatory Network (LEGION).

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

from pyclustering.nnet.legion import legion_network, legion_parameters;
from pyclustering.nnet import *;

from pyclustering.support import extract_number_oscillations;


class Test(unittest.TestCase):   
    def testUstimulatedOscillatorWithoutLateralPotential(self):
        params = legion_parameters();
        params.teta = 0;    # because no neighbors at all
     
        net = legion_network(1, [0], type_conn = conn_type.NONE, parameters = params);
        (t, x, z) = net.simulate(1000, 200);
         
        assert extract_number_oscillations(x) == 1;
         
         
    def testStimulatedOscillatorWithoutLateralPotential(self):
        params = legion_parameters();
        params.teta = 0;    # because no neighbors at all
         
        net = legion_network(1, [1], type_conn = conn_type.NONE, parameters = params);
        (t, x, z) = net.simulate(1000, 200);
         
        assert extract_number_oscillations(x) > 1;      
 
 
    def testStimulatedOscillatorWithLateralPotential(self):
        net = legion_network(1, [1], type_conn = conn_type.NONE);
        (t, x, z) = net.simulate(1000, 200);
         
        assert extract_number_oscillations(x) == 1;
         
     
    def testStimulatedTwoOscillators(self):
        net = legion_network(2, [1, 1], type_conn = conn_type.LIST_BIDIR);
        (t, x, z) = net.simulate(1000, 2000);
         
        assert extract_number_oscillations(x, 0) > 1;
        assert extract_number_oscillations(x, 1) > 1;
 
 
    def testUnstimulatedTwoOscillators(self):
        params = legion_parameters();
        params.teta_p = 2.5;
         
        net = legion_network(2, [0, 0], type_conn = conn_type.LIST_BIDIR, parameters = params);
        (t, x, z) = net.simulate(1000, 1000);
         
        assert extract_number_oscillations(x, 0) == 1;
        assert extract_number_oscillations(x, 1) == 1;
         
         
    def testMixStimulatedThreeOscillators(self):
        net = legion_network(3, [1, 0, 1], type_conn = conn_type.LIST_BIDIR);
        (t, x, z) = net.simulate(1000, 2000);
         
        assert extract_number_oscillations(x, 0) > 1;
        assert extract_number_oscillations(x, 1) == 1;   
        assert extract_number_oscillations(x, 2) > 1;       
 
    def testListConnectionRepresentation(self):
        net = legion_network(3, [1, 0, 1], type_conn = conn_type.LIST_BIDIR, type_conn_represent = conn_represent.LIST);
        (t, x, z) = net.simulate(1000, 2000);
 
        assert extract_number_oscillations(x, 0) > 1;
        assert extract_number_oscillations(x, 1) == 1;   
        assert extract_number_oscillations(x, 2) > 1;  
         
         
    # Tests regarded to various structures that can be used.
    def templateOscillationsWithStructures(self, type_conn):
        net = legion_network(4, [1, 1, 1, 1], type_conn = conn_type.LIST_BIDIR);
        (t, x, z) = net.simulate(500, 1000);
         
        for i in range(net.num_osc):
            assert extract_number_oscillations(x, i) > 1;
 
 
    def testStimulatedOscillatorListStructure(self):
        self.templateOscillationsWithStructures(conn_type.LIST_BIDIR);
 
    def testStimulatedOscillatorGridFourStructure(self):
        self.templateOscillationsWithStructures(conn_type.GRID_FOUR);
         
    def testStimulatedOscillatorGridEightStructure(self):
        self.templateOscillationsWithStructures(conn_type.GRID_EIGHT);
 
    def testStimulatedOscillatorAllToAllStructure(self):
        self.templateOscillationsWithStructures(conn_type.ALL_TO_ALL);
    
    
    # Tests regarded to synchronous ensembles allocation.
    def templateSyncEnsembleAllocation(self, stimulus, params, type_conn, sim_steps, sim_time, expected_clusters):
        net = legion_network(len(stimulus), stimulus, params, type_conn);
        (t, x, z) = net.simulate(sim_steps, sim_time);
        
        ensembles = net.allocate_sync_ensembles(0.1);
        assert ensembles == expected_clusters;
        
    def testSyncEnsembleAllocationOneStimulatedOscillator(self):
        params = legion_parameters();
        params.teta = 0; # due to no neighbors
        
        self.templateSyncEnsembleAllocation([1], params, conn_type.NONE, 2000, 500, [[0]]);
        
    def testSyncEnsembleAllocationThreeStimulatedOscillators(self):
        self.templateSyncEnsembleAllocation([1, 1, 1], None, conn_type.LIST_BIDIR, 1500, 1500, [[0, 1, 2]]);
        
    def testSyncEnsembleAllocationThreeMixStimulatedOscillators(self):
        parameters = legion_parameters();
        parameters.Wt = 4.0;
        
        self.templateSyncEnsembleAllocation([1, 0, 1], None, conn_type.LIST_BIDIR, 1500, 1500, [[0, 2], [1]]);
        
    def testSyncEnsembleAllocationTenMixStimulatedOscillators(self):
        self.templateSyncEnsembleAllocation([1, 1, 1, 0, 0, 0, 1, 1, 0, 0], None, conn_type.LIST_BIDIR, 1500, 1500, [[0, 1, 2], [3, 4, 5, 8, 9], [6, 7]]);


if __name__ == "__main__":
    unittest.main();