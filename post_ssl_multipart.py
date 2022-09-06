import requests
import random,string
from requests_toolbelt import MultipartEncoder
import binascii
import io
import os

file1 = "filename1"
file2 = "filename2"
file3 = "filename3"

def encode_multipart_formdata(fields):
    #boundary = binascii.hexlify(os.urandom(16)).decode('ascii')
    boundary = '----WebKitFormBoundary' \
             + ''.join(random.sample(string.ascii_letters + string.digits, 16))

    body = (
        "".join("--{}\r\n"
                "Content-Disposition: form-data; name=\"{}\"\r\n"
                "\r\n"
                "{}\r\n".format(boundary, field, value)
                for field, value in fields.items()) +
        "--{}--\r\n".format(boundary)
    )
    
    content_type = "multipart/form-data; boundary=%s" % boundary

    return body, content_type


def main():

    with open(file1, 'rb') as key_f:
        key_data = key_f.read()
    with open(file2, 'rb') as crt_f:
        crt_data = crt_f.read()
    with open(file3, 'rb') as ca_f:
        ca_data = ca_f.read()

    fields = {
        'keyType': 'RSA_2048',
        'key': key_data,
        'cert': crt_data,
        'caChain': ca_data
    }

    formdata, content_type = encode_multipart_formdata(fields)
    print("#########formdata##############")
    print(formdata)
    print("#########content-type##############")
    print(content_type)

    headers = {
        "Connection": "keep-alive",
        "Content-Type": content_type
    }

    r = requests.post('http://httpbin.org/post', headers=headers, data=formdata)

    #print(r.text)

if __name__ == "__main__":
    main()
    
