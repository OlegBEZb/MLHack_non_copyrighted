import numpy as np
from PIL import Image

img = Image.open('/home/user/env2/GAN_hack/biggan/beach1.png')
lr_img = np.array(img)

from ISR.models import RDN

rdn = RDN(weights='psnr-small')
sr_img = rdn.predict(lr_img)
sr = Image.fromarray(sr_img)
sr.show()
sr = sr.save("beach1_sr.jpg")
