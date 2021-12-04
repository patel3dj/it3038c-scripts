virtualenc ~/venvpillow
source ~/venv/scripts/bin/activate
pip install pillow

from PIL import Image,ImageFilter
myImage = Image.open('/full/path/to/image.jpg')
myImage.load

myImage.format
myImage.size
myImage.show()

blur = myImage.filter(ImageFilter(BLUR)).show()
quit()

deactivate
