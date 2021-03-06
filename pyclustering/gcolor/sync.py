'''

Graph coloring algorithm: Algorithm based on Sync Oscillatory Network

Based on article description:
 - J.Wu J, L.Jiao, W.Chen. Clustering dynamics of nonlinear oscillator network: Application to graph coloring problem. 2011.

Copyright (C) 2015    Andrei Novikov (spb.andr@yandex.ru)

pyclustering is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

pyclustering is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <http://www.gnu.org/licenses/>.

'''

from pyclustering.nnet import *;
from pyclustering.nnet.sync import sync_network;


class syncgcolor(sync_network):
    _positive_weight = None;
    _negative_weight = None;
    _reduction = None;
    
    def __init__(self, graph_matrix, positive_weight, negative_weight, reduction = None):
        number_oscillators = len(graph_matrix);
        super().__init__(number_oscillators, type_conn = conn_type.NONE);
        
        if (reduction == None):
            self._reduction = self._num_osc;
        else:
            self._reduction = reduction;
        
        self._positive_weight = positive_weight;
        self._negative_weight = negative_weight;
        
        self._create_connections(graph_matrix);
        
    
    def _create_connections(self, graph_matrix):
        "Create connection in the network in line with graph."

        "(in) graph_matrix     - matrix representation of the graph"
        
        for row in range(0, len(graph_matrix)):
            for column in range (0, len(graph_matrix[row])):
                self._osc_conn[row][column] = graph_matrix[row][column];
                
    
    def _phase_kuramoto(self, teta, t, argv):
        "Return result of phase calculation for oscillator in the network"
        
        "(in) teta     - value of phase of the oscillator with index argv in the network"
        "(in) t        - unused"
        "(in) argv     - index of the oscillator in the network"
        
        "Return new value of phase for oscillator with index argv"
        
        index = argv;
        phase = 0;
        
        for k in range(0, self.num_osc):
            if (self.has_connection(index, k) == True):
                phase += self._negative_weight * math.sin(self._phases[k] - teta);
            else:
                phase += self._positive_weight * math.sin(self._phases[k] - teta);
            
        return ( phase / self._reduction );        
    
    
    def process(self, order = 0.998, solution = solve_type.FAST, collect_dynamic = False):
        "Perform simulation of the network (perform solving of graph coloring problem"
        
        "(in) order            - defines when process of synchronization in the network is over. Range from 0 to 1."
        "(in) solution         - defines type (method) of solving diff. equation"
        "(in) collect_dynamic  - if True - return full dynamic of the network, otherwise - last state of phases"
        
        "Return dynamic of the network (time, phases)"
        
        return self.simulate_dynamic(order, solution, collect_dynamic);
    
    
    def get_clusters(self, tolerance = 0.1):
        "Return allocated clusters, when one cluster defines only one color"
        
        "(in) tolerance        - defines maximum deviation between phases"
        
        "Return allocated clusters [vertices with color 1], [vertices with color 2], ..., [vertices with color n]"
        
        return self.allocate_sync_ensembles(tolerance);
    
    def get_map_coloring(self, tolerance = 0.1):
        "Return coloring map for graph that has been processed"
        
        "(in) tolerance        - defines maximum deviation between phases"
        
        "Return colors for each node (index of node in graph), for example [color1, color2, color2, ...]"
        clusters = self.get_clusters(tolerance);
        
        coloring_map = [0] * self._num_osc;
        
        for color_index in range(len(clusters)):
            for node_index in clusters[color_index]:
                coloring_map[node_index] = color_index;
                
        return coloring_map;
    