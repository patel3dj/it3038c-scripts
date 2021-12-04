we first of all start virtual env and then create a script which dowanloads image

virtualenv ~/venv/pillow
source ~/venv/scripts/bin/activate
pip install pillow


Here we import PIL to downlaod the image and the its path 
from PIL import Image,ImageFilter
myImage = Image.open('/full/path/to/image.jpg')
myImage.load

in the end terminate the virtual env.