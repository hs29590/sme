import cv2
import urllib2
import numpy as np
import sys
import time

host = "192.168.0.105:8080"
if len(sys.argv)>1:
    host = sys.argv[1]

focusStr = 'http://' + host + '/focus';
shotStr = 'http://' + host + '/shot.jpg';

print 'Focusing.. and waiting';

urllib2.urlopen(focusStr); 

time.sleep(2);

print 'Capturing..';

bytes = urllib2.urlopen(shotStr).read()
a = bytes.find('\xff\xd8')
b = bytes.find('\xff\xd9')
if a!=-1 and b!=-1:
    jpg = bytes[a:b+2]
    bytes= bytes[b+2:]
    i = cv2.imdecode(np.fromstring(jpg, dtype=np.uint8),cv2.IMREAD_COLOR)
    print 'Saving.. to test.jpg';
    cv2.imwrite('test.jpg',i);
    cv2.imshow(host,i)
    cv2.waitKey(0);
exit()
