from rembg import remove
from PIL import Image
inpath=input('Enter image path: ')
outpath='output.png'
inp=Image.open(inpath)
outp=remove(inp)
outp.save(outpath)