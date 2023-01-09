import pyqrcode
import png
s="sugamano"
url=pyqrcode.create(s)
url.svg("myqr.svg",scale=8)
url.png('myqr.png',scale=6)