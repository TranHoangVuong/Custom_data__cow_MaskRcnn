import cv2 
import sys

from regex import F

from visualize_cv2 import model, display_instances, class_names

def objectVideo(self):
    stream = cv2.VideoCapture(self)
    count_frame = 0
    while True:
        
        ret, frame = stream.read()
        count_frame += 1
        if not ret:
            print('unable to fetch frame')
            break
        
        if count_frame == 1: 
            results = model.detect([frame], verbose=1)
            #visualize results
            r = results[0]
            if len(r['rois'])==0:
                masked_image = frame
            else:
                masked_image = display_instances(frame, r['rois'], r['masks'], r['class_ids'], class_names, r['scores'])
                cv2.putText(frame, "Cow number: " + str(len(r['class_ids'])), (10, 70), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0 , 255), 2)
            count_frame = 0
            cv2.imshow("masked_image", masked_image)
            
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
            
    stream.release()
    cv2.destroyAllWindows("masked_image")