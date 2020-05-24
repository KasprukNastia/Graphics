from PIL import Image
from pylab import *

im = array(Image.open('images/when_will_you_marry_paul_gauguin.jpg'))
figure(figsize =(15,15))

#negative image
im2 = 255 - im

im3 = 170 + im

im4 = im % 160

subplot(3,4,1)
imshow(im2)
title('Negative')

subplot(3,4,2)
imshow(im3)
title('Custom 1')

subplot(3,4,3)
imshow(im4)
title('Custom 2')

show()
