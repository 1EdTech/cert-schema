import json


def certificate_bytes_to_json(cert_file_bytes):
    cert_string = cert_file_bytes.decode('utf-8')
    cert_json = json.loads(cert_string)
    return cert_json
