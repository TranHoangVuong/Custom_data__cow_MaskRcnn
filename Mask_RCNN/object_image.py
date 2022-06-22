import sys

from matplotlib.pyplot import title
from visualize_cv2 import model, display_instances, class_names

import cv2

from mrcnn.visualize import random_colors, get_mask_contours, draw_mask
def objectImage(imgin):
#imgin = cv2.imread("C:/Users/ASUS/Desktop/AiCuoiKi_final/Mask_RCNN/images/test_image/download3.jpg")
    imgin = cv2.cvtColor(imgin, cv2.COLOR_BGR2RGB)
    r =  model.detect([imgin])[0]

    object_count = len(r["class_ids"])

    print('so bo:',len(r["class_ids"]))

    imgout = display_instances(imgin, r['rois'], r['masks'], r['class_ids'], class_names, r['scores'])
    cv2.putText(imgout, "Cow number: " + str(len(r['class_ids'])), (10, 70), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0 , 255), 2)
    return imgout

