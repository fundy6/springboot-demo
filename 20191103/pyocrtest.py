from pyocr import  tesseract
from PIL import Image
import urllib
import requests
import pytesseract
def download_img(img_url):

    r = requests.get(img_url,  stream=True)
    if r.status_code == 200:
        open('img.png', 'wb').write(r.content)
        return 'img.png'
if __name__ == '__main__':
    fileimage=download_img('https://login.sina.com.cn/cgi/pin.php?r=46430009&s=0&p=yf-f5e7af9d84c3fe0dfbacbac689ce38ba57bb')
    im = Image.open(fileimage)

    code = tesseract.image_to_string(im)

    print(code)
