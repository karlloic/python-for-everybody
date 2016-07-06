# Downloading images
import urllib

image = urllib.urlopen('https://www2.bac-assets.com/content/images/ContextualSiteGraphics/Logos/en_US/boa_logo.gif')

fhandle = open('boaLogo.gif', 'w')
size = 0
while True:
    data = image.read(100000)
    if len(data) < 1:
        break
    fhandle.write(data)
    size += len(data)
print size, 'Bytes'
fhandle.close()
