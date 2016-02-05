import urllib2

manager = urllib2.HTTPPasswordMgrWithDefaultRealm()
manager.add_password(None, 'http://www.oxienerji.com', 'login', 'key')
handler = urllib2.HTTPBasicAuthHandler(manager)

director = urllib2.OpenerDirector()
director.add_handler(handler)

req = urllib2.Request('http://www.oxienerji.com', headers = {'Accept' : 'text/html'})

result = director.open(req)
# result.read() will contain the data
# result.info() will contain the HTTP headers

# To get say the content-length header
length = result.info()['Content-Length']
