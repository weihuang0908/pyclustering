"""!

@brief Examples of usage and demonstration of abilities of hierarchical algorithm in cluster analysis.

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

from pyclustering.cluster.hierarchical import hierarchical;

from pyclustering.support import read_sample;
from pyclustering.support import draw_clusters;
from pyclustering.support import timedcall;

from pyclustering.samples.definitions import SIMPLE_SAMPLES, FCPS_SAMPLES;

def template_clustering(number_clusters, path, ccore = True):
    sample = read_sample(path);
    
    hierarchical_instance = hierarchical(sample, number_clusters, ccore)
    (ticks, result) = timedcall(hierarchical_instance.process);
    
    print("Sample: ", path, "\t\tExecution time: ", ticks, "\n");
    
    clusters = hierarchical_instance.get_clusters();
    draw_clusters(sample, clusters);
    
def cluster_sample1():
    template_clustering(2, SIMPLE_SAMPLES.SAMPLE_SIMPLE1);
    
def cluster_sample2():
    template_clustering(3, SIMPLE_SAMPLES.SAMPLE_SIMPLE2);
    
def cluster_sample3():
    template_clustering(4, SIMPLE_SAMPLES.SAMPLE_SIMPLE3);
    
def cluster_sample4():
    template_clustering(5, SIMPLE_SAMPLES.SAMPLE_SIMPLE4);
    
def cluster_sample5():
    template_clustering(4, SIMPLE_SAMPLES.SAMPLE_SIMPLE5);    
    
def cluster_elongate():
    "NOTE: Not applicable for this sample"
    template_clustering(2, SIMPLE_SAMPLES.SAMPLE_ELONGATE);

def cluster_lsun():
    "NOTE: Not applicable for this sample"
    template_clustering(3, FCPS_SAMPLES.SAMPLE_LSUN);  
    
def cluster_target():
    "NOTE: Not applicable for this sample"
    template_clustering(6, FCPS_SAMPLES.SAMPLE_TARGET);     

def cluster_two_diamonds():
    template_clustering(2, FCPS_SAMPLES.SAMPLE_TWO_DIAMONDS);  

def cluster_wing_nut():
    template_clustering(2, FCPS_SAMPLES.SAMPLE_WING_NUT); 
    
def cluster_chainlink():
    "NOTE: Not applicable for this sample"
    template_clustering(2, FCPS_SAMPLES.SAMPLE_CHAINLINK);     
    
def cluster_hepta():
    template_clustering(7, FCPS_SAMPLES.SAMPLE_HEPTA); 
    
def cluster_tetra():
    template_clustering(4, FCPS_SAMPLES.SAMPLE_TETRA);    
    
def cluster_engy_time():
    template_clustering(2, FCPS_SAMPLES.SAMPLE_ENGY_TIME);
    
def experiment_execution_time(ccore = False):
    template_clustering(2, SIMPLE_SAMPLES.SAMPLE_SIMPLE1, ccore);
    template_clustering(3, SIMPLE_SAMPLES.SAMPLE_SIMPLE2, ccore);
    template_clustering(4, SIMPLE_SAMPLES.SAMPLE_SIMPLE3, ccore);
    template_clustering(5, SIMPLE_SAMPLES.SAMPLE_SIMPLE4, ccore);
    template_clustering(4, SIMPLE_SAMPLES.SAMPLE_SIMPLE5, ccore);
    template_clustering(2, SIMPLE_SAMPLES.SAMPLE_ELONGATE, ccore);
    template_clustering(3, FCPS_SAMPLES.SAMPLE_LSUN, ccore); 
    template_clustering(6, FCPS_SAMPLES.SAMPLE_TARGET, ccore); 
    template_clustering(2, FCPS_SAMPLES.SAMPLE_TWO_DIAMONDS, ccore);
    template_clustering(2, FCPS_SAMPLES.SAMPLE_WING_NUT, ccore);
    template_clustering(2, FCPS_SAMPLES.SAMPLE_CHAINLINK, ccore);
    template_clustering(7, FCPS_SAMPLES.SAMPLE_HEPTA, ccore);
    template_clustering(4, FCPS_SAMPLES.SAMPLE_TETRA, ccore);
    template_clustering(2, FCPS_SAMPLES.SAMPLE_ENGY_TIME, ccore);
    
    
cluster_sample1();
cluster_sample2();
cluster_sample3();
cluster_sample4();
cluster_sample5();
cluster_elongate();
cluster_lsun();
cluster_target();
cluster_two_diamonds();
cluster_wing_nut();
cluster_chainlink();
cluster_hepta();
cluster_tetra();
cluster_engy_time();
 
experiment_execution_time(False);   # Python code
experiment_execution_time(True);    # C++ code + Python env.
