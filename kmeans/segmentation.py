from PIL import Image;

from support import draw_image_segments;

from samples.definitions import IMAGE_SIMPLE_SAMPLES;

from kmeans import kmeans;


def template_segmentation_image(source, start_centers):
    image_source = Image.open(source);
    
    data = [pixel for pixel in image_source.getdata()];

    (clusters, centers) = kmeans(data, start_centers);
    draw_image_segments(source, clusters);
    
    del image_source;
    
    
def segmentation_image_simple1():
    template_segmentation_image(IMAGE_SIMPLE_SAMPLES.IMAGE_THREE_OBJECT1, [[255, 0, 0], [0, 0, 255], [180, 136, 0], [255, 255, 255]]);

def segmentation_image_simple2():
    template_segmentation_image(IMAGE_SIMPLE_SAMPLES.IMAGE_THREE_OBJECT2, [[255, 0, 0, 128], [0, 0, 255, 128], [180, 136, 0, 128], [255, 255, 255, 128]]);
    
def segmentation_image_simple3():
    template_segmentation_image(IMAGE_SIMPLE_SAMPLES.IMAGE_THREE_OBJECT3, [[255, 0, 0, 128], [0, 0, 255, 128], [180, 136, 0, 128]]);    
    
def segmentation_image_simple4():
    template_segmentation_image(IMAGE_SIMPLE_SAMPLES.IMAGE_TWO_COLOR_SET, [[0, 128, 0, 128], [255, 0, 0, 128]]);        
    
segmentation_image_simple1();
segmentation_image_simple2();
segmentation_image_simple3();
segmentation_image_simple4();