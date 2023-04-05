import requests
import binascii
import random
import string
from requests_toolbelt.utils import dump
 

def encode_multipart_formdata(fields, files):
    boundary = '----WebKitFormBoundary' + ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(16))
    body = []

    for key, value in fields.items():
        body.extend([
            '--' + boundary,
            'Content-Disposition: form-data; name="{}"'.format(key),
            '',
            value
        ])

    for key, value in files.items():
        filename, file_contents, content_type = value
        if isinstance(file_contents, bytes):
            file_contents = file_contents.decode('utf-8')
        body.extend([
            '--' + boundary,
            'Content-Disposition: form-data; name="{}"; filename="{}"'.format(key, filename),
            'Content-Type: {}'.format(content_type),
            '',
            file_contents
        ])

    body.extend(['--{}--'.format(boundary), ''])
    content_type = 'multipart/form-data; boundary={}'.format(boundary)

    return '\r\n'.join(body), content_type

 
# Example usage
url = 'http://httpbin.org/post'
 
fields = {'keyType': 'RSA_2048'}
files = {'key': ('key.pem', open('key.pem', 'rb').read(), 'application/x-x509-ca-cert'),
         'cert': ('crt.pem', open('crt.pem', 'rb').read(), 'application/x-x509-ca-cert'),
         'caChain': ('cacert.pem', open('cacert.pem', 'rb').read(), 'application/x-x509-ca-cert')}

#headers = {'Content-Type': 'multipart/form-data'}
data, content_type = encode_multipart_formdata(fields, files)
headers = {'Content-Type': content_type}
 
response = requests.post(url, headers=headers, data=data)
#print(response.text)
print(dump.dump_all(response).decode("utf-8"))
    
