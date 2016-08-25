#! /usr/bin/env python

import json


def update(old_file, new_file):
    """
    update old_file (1.1) to new_file (1.2.0)
    :param old_file:
    :param new_file:
    :return:
    """
    with open(old_file) as v_old:
        data = json.load(v_old)

        data['@context'] = 'https://w3id.org/blockcerts#'
        data['@type'] = 'DigitalCertificate'

        data['verify']['@type'] = 'VerificationObject',
        data['recipient']['@type'] = 'Recipient',
        data['certificate']['@type'] = 'Certificate'
        data['certificate']['issuer']['@type'] = 'Issuer'
        data['assertion']['@type'] = 'Assertion'

        hashed = data['recipient']['hashed']
        if str(hashed).lower() == 'true':
            data['recipient']['hashed'] = True
        else:
            data['recipient']['hashed'] = False

        # fix images
        if 'image' in data['certificate']:
            data['certificate']['image:certificate'] = data['certificate']['image']
            del data['certificate']['image']

        if 'image' in data['certificate']['issuer']:
            data['certificate']['issuer']['image:logo'] = data['certificate']['issuer']['image']
            del data['certificate']['issuer']['image']

        # update subtitle
        if 'subtitle' in data['certificate']:
            if data['certificate']['subtitle']['content']:
                # update if non-blank string
                temp = data['certificate']['subtitle']['content']
                del data['certificate']['subtitle']['content']
                data['certificate']['subtitle'] = temp
            else:
                # this field is optional now
                del data['certificate']['subtitle']

        with open(new_file, 'w') as v_new:
            json.dump(data, v_new)


if __name__ == '__main__':
    update('../../examples/1.1.0/sample_unsigned_cert-1.1.0.json', 'v2_sample_unsigned_cert.json')
