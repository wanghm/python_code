import requests
import binascii
import random
import string
from requests_toolbelt.utils import dump
 
def encode_multipart_formdata(fields, files):
    boundary = '----WebKitFormBoundary' + ''.join(random.sample(string.ascii_letters + string.digits, 16))
    body = []
 
    for key, value in fields.items():
        body.append('--' + boundary)
        body.append('Content-Disposition: form-data; name="%s"' % key)
        body.append('')
        body.append(value)
 
    for key, value in files.items():
        body.append('--' + boundary)
        body.append('Content-Disposition: form-data; name="%s"; filename="%s"' % (key, value[0]))
        body.append('Content-Type: %s' % value[2])
        body.append('')
        body.append(value[1])
 
    body.append('--' + boundary + '--')
    body.append('')
 
    content_type = 'multipart/form-data; boundary=%s' % boundary
 
    return '\r\n'.join([str(item) for item in body]), content_type
 
# Example usage
url = 'http://httpbin.org/post'
 
fields = {'keyType': 'RSA_2048'}
files = {'key': ('key.pem', open('key.pem', 'rb').read(), 'application/x-x509-ca-cert'),
         'cert': ('crt.pem', open('crt.pem', 'rb').read(), 'application/x-x509-ca-cert'),
         'caChain': ('cacert.pem', open('cacert.pem', 'rb').read(), 'application/x-x509-ca-cert')}

headers = {'Content-Type': 'multipart/form-data'}
data, content_type = encode_multipart_formdata(fields, files)
 
response = requests.post(url, headers=headers, data=data)
#print(response.text)
print(dump.dump_all(response).decode("utf-8"))
    
