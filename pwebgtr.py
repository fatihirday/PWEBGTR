import urllib.request
import ssl
import re

https_sslv3_handler = urllib.request.HTTPSHandler(context=ssl.SSLContext(ssl.PROTOCOL_SSLv3))
opener = urllib.request.build_opener(https_sslv3_handler)
urllib.request.install_opener(opener)
resp = opener.open('https://www.toroslaredas.com.tr/Pages/Bilgilendirme/PlanliBakim/Planli-Kesinti-Listesi-ve-Haritasi.aspx')
data = resp.read().decode('utf-8')

m = re.findall ( '<h3 (?:[^>=]|=\'[^\']*\'|="[^"]*"|=[^\'"][^\s>]*)*?>(.*?)</h3>', data, re.DOTALL|re.MULTILINE)

f = open('kesintiler.txt', 'w')
for item in m:
  f.write("%s\n" % item)
 
f.close
	
print('İşlem Tamamlandı')
