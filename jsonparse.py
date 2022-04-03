import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from unicodedata import normalize


import urllib.request

fp = urllib.request.urlopen('https://gateway.pinata.cloud/ipfs/Qmb7CKP2ZMphibhPKJGd1GzX96Z3Uut1UHBWf35YWLNCsf')
mybytes = fp.read()

mystr = mybytes.decode("utf8")
fp.close()

print(mystr)



soup =  BeautifulSoup(mystr)

bruh=[]
texts = soup.find_all('a')
for text in texts:
    bruh.append(text.get_text())
