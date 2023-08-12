import pyqrcode
url = pyqrcode.create('https://www.instagram.com/gdscatauni/')
url.svg('gdscatauni.svg', scale=8)
url.eps('gdscatauni.eps', scale=2)
print(url.terminal(quiet_zone=1))