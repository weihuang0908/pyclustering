"""!

@brief General definitions of samples.

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

import pyclustering.samples as samples;
import os;

class SIMPLE_SAMPLES:
    SAMPLE_SIMPLE1          = samples.__path__[0] + os.sep + "samples" + os.sep + "SampleSimple1.txt";
    SAMPLE_SIMPLE2          = samples.__path__[0] + os.sep + "samples" + os.sep + "SampleSimple2.txt";
    SAMPLE_SIMPLE3          = samples.__path__[0] + os.sep + "samples" + os.sep + "SampleSimple3.txt";
    SAMPLE_SIMPLE4          = samples.__path__[0] + os.sep + "samples" + os.sep + "SampleSimple4.txt";
    SAMPLE_SIMPLE5          = samples.__path__[0] + os.sep + "samples" + os.sep + "SampleSimple5.txt";
    SAMPLE_SIMPLE6          = samples.__path__[0] + os.sep + "samples" + os.sep + "SampleSimple6.txt";
    SAMPLE_ELONGATE         = samples.__path__[0] + os.sep + "samples" + os.sep + "SampleElongate.txt";
    SAMPLE_DENSITIES1       = samples.__path__[0] + os.sep + "samples" + os.sep + "SampleDensities1.txt";
    SAMPLE_DENSITIES2       = samples.__path__[0] + os.sep + "samples" + os.sep + "SampleDensities2.txt";


class FCPS_SAMPLES:
    SAMPLE_ATOM             = samples.__path__[0] + os.sep + "samples" + os.sep + "SampleAtom.txt";
    SAMPLE_CHAINLINK        = samples.__path__[0] + os.sep + "samples" + os.sep + "SampleChainlink.txt";
    SAMPLE_ENGY_TIME        = samples.__path__[0] + os.sep + "samples" + os.sep + "SampleEngyTime.txt";
    SAMPLE_GOLF_BALL        = samples.__path__[0] + os.sep + "samples" + os.sep + "SampleGolfBall.txt";
    SAMPLE_HEPTA            = samples.__path__[0] + os.sep + "samples" + os.sep + "SampleHepta.txt";
    SAMPLE_LSUN             = samples.__path__[0] + os.sep + "samples" + os.sep + "SampleLsun.txt";
    SAMPLE_TARGET           = samples.__path__[0] + os.sep + "samples" + os.sep + "SampleTarget.txt";
    SAMPLE_TETRA            = samples.__path__[0] + os.sep + "samples" + os.sep + "SampleTetra.txt";
    SAMPLE_TWO_DIAMONDS     = samples.__path__[0] + os.sep + "samples" + os.sep + "SampleTwoDiamonds.txt";
    SAMPLE_WING_NUT         = samples.__path__[0] + os.sep + "samples" + os.sep + "SampleWingNut.txt";


class GRAPH_SIMPLE_SAMPLES:
    GRAPH_BROKEN_CIRCLE1            = samples.__path__[0] + os.sep + "graphs" + os.sep + "GraphBrokenCircle1.grpr";
    GRAPH_BROKEN_CIRCLE2            = samples.__path__[0] + os.sep + "graphs" + os.sep + "GraphBrokenCircle2.grpr";
    GRAPH_FIVE_POINTED_FRAME_STAR   = samples.__path__[0] + os.sep + "graphs" + os.sep + "GraphFivePointedFrameStar.grpr";
    GRAPH_FIVE_POINTED_STAR         = samples.__path__[0] + os.sep + "graphs" + os.sep + "GraphFivePointedStar.grpr";
    GRAPH_ONE_CIRCLE1               = samples.__path__[0] + os.sep + "graphs" + os.sep + "GraphOneCircle1.grpr";
    GRAPH_ONE_CIRCLE2               = samples.__path__[0] + os.sep + "graphs" + os.sep + "GraphOneCircle2.grpr";
    GRAPH_ONE_CIRCLE3               = samples.__path__[0] + os.sep + "graphs" + os.sep + "GraphOneCircle3.grpr";
    GRAPH_ONE_CROSSROAD             = samples.__path__[0] + os.sep + "graphs" + os.sep + "GraphOneCrossroad.grpr";
    GRAPH_ONE_LINE                  = samples.__path__[0] + os.sep + "graphs" + os.sep + "GraphOneLine.grpr";
    GRAPH_TWO_CROSSROADS            = samples.__path__[0] + os.sep + "graphs" + os.sep + "GraphTwoCrossroads.grpr";
    GRAPH_FULL1                     = samples.__path__[0] + os.sep + "graphs" + os.sep + "GraphFull1.grpr"
    GRAPH_FULL2                     = samples.__path__[0] + os.sep + "graphs" + os.sep + "GraphFull2.grpr"
    GRAPH_SIMPLE1                   = samples.__path__[0] + os.sep + "graphs" + os.sep + "GraphSimple1.grpr"
    GRAPH_SIMPLE2                   = samples.__path__[0] + os.sep + "graphs" + os.sep + "GraphSimple2.grpr"
    GRAPH_SIMPLE3                   = samples.__path__[0] + os.sep + "graphs" + os.sep + "GraphSimple3.grpr"
    
    
class GRAPH_DSJC_SAMPLES:
    DSJC_250_5                      = samples.__path__[0] + os.sep + "graphs" + os.sep + "DSJC250.5.grpr";
    DSJC_500_1                      = samples.__path__[0] + os.sep + "graphs" + os.sep + "DSJC500.1.grpr";
    DSJC_500_5                      = samples.__path__[0] + os.sep + "graphs" + os.sep + "DSJC500.5.grpr";
    DSJC_500_9                      = samples.__path__[0] + os.sep + "graphs" + os.sep + "DSJC500.9.grpr";
    DSJC_1000_1                     = samples.__path__[0] + os.sep + "graphs" + os.sep + "DSJC1000.1.grpr";
    DSJC_1000_5                     = samples.__path__[0] + os.sep + "graphs" + os.sep + "DSJC1000.5.grpr";
    DSJC_1000_9                     = samples.__path__[0] + os.sep + "graphs" + os.sep + "DSJC1000.9.grpr";
    
    
class IMAGE_SIMPLE_SAMPLES:
    IMAGE_SIMPLE01                  = samples.__path__[0] + os.sep + "images" + os.sep + "ImageSimple01.png";
    IMAGE_SIMPLE02                  = samples.__path__[0] + os.sep + "images" + os.sep + "ImageSimple02.png";
    IMAGE_SIMPLE03                  = samples.__path__[0] + os.sep + "images" + os.sep + "ImageSimple03.png";
    IMAGE_SIMPLE04                  = samples.__path__[0] + os.sep + "images" + os.sep + "ImageSimple04.png";
    IMAGE_SIMPLE05                  = samples.__path__[0] + os.sep + "images" + os.sep + "ImageSimple05.png";
    IMAGE_SIMPLE06                  = samples.__path__[0] + os.sep + "images" + os.sep + "ImageSimple06.png";
    IMAGE_SIMPLE07                  = samples.__path__[0] + os.sep + "images" + os.sep + "ImageSimple07.png";
    IMAGE_SIMPLE08                  = samples.__path__[0] + os.sep + "images" + os.sep + "ImageSimple08.png";
    IMAGE_SIMPLE09                  = samples.__path__[0] + os.sep + "images" + os.sep + "ImageSimple09.png";
    IMAGE_SIMPLE10                  = samples.__path__[0] + os.sep + "images" + os.sep + "ImageSimple10.png";
    IMAGE_SIMPLE11                  = samples.__path__[0] + os.sep + "images" + os.sep + "ImageSimple11.png";
    IMAGE_SIMPLE_BEACH              = samples.__path__[0] + os.sep + "images" + os.sep + "ImageSimpleBeach.png";
    IMAGE_SIMPLE_BUILDING           = samples.__path__[0] + os.sep + "images" + os.sep + "ImageSimpleBuilding.png";
    IMAGE_SIMPLE_FRUITS             = samples.__path__[0] + os.sep + "images" + os.sep + "ImageSimpleFruits.png";
    IMAGE_SIMPLE_FRUITS_SMALL       = samples.__path__[0] + os.sep + "images" + os.sep + "ImageSimpleFruitsSmall.png";
    
    
class IMAGE_MAP_SAMPLES:
    IMAGE_WHITE_SEA                 = samples.__path__[0] + os.sep + "images" + os.sep + "ImageWhiteSea.png";
    IMAGE_WHITE_SEA_SMALL           = samples.__path__[0] + os.sep + "images" + os.sep + "ImageWhiteSeaSmall.png";
    IMAGE_NILE                      = samples.__path__[0] + os.sep + "images" + os.sep + "ImageNile.png";
    IMAGE_NILE_SMALL                = samples.__path__[0] + os.sep + "images" + os.sep + "ImageNileSmall.png";
    

class IMAGE_REAL_SAMPLES:
    IMAGE_FIELD_FLOWER              = samples.__path__[0] + os.sep + "images" + os.sep + "ImageFieldFlower.png";
    
    
class IMAGE_DIGIT_SAMPLES:    
    @staticmethod
    def GET_LIST_IMAGE_SAMPLES(digit):
        default_path = samples.__path__[0] + os.sep + "images" + os.sep + "digits" + os.sep;
        number_sample_digits = 20;
        
        name_file_pattern = "Digit_%d_Sample%.2d.png";
        list_image_samples = [];
        
        for index_image in range(1, number_sample_digits, 1):
            file_path = default_path + (name_file_pattern % (digit, index_image));
            list_image_samples.append(file_path);
            
        return list_image_samples;
    
    LIST_IMAGES_DIGIT_0             = GET_LIST_IMAGE_SAMPLES.__func__(0);
    LIST_IMAGES_DIGIT_1             = GET_LIST_IMAGE_SAMPLES.__func__(1);
    LIST_IMAGES_DIGIT_2             = GET_LIST_IMAGE_SAMPLES.__func__(2);
    LIST_IMAGES_DIGIT_3             = GET_LIST_IMAGE_SAMPLES.__func__(3);
    LIST_IMAGES_DIGIT_4             = GET_LIST_IMAGE_SAMPLES.__func__(4);
    LIST_IMAGES_DIGIT_5             = GET_LIST_IMAGE_SAMPLES.__func__(5);
    LIST_IMAGES_DIGIT_6             = GET_LIST_IMAGE_SAMPLES.__func__(6);
    LIST_IMAGES_DIGIT_7             = GET_LIST_IMAGE_SAMPLES.__func__(7);
    LIST_IMAGES_DIGIT_8             = GET_LIST_IMAGE_SAMPLES.__func__(8);
    LIST_IMAGES_DIGIT_9             = GET_LIST_IMAGE_SAMPLES.__func__(9);
    