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

        data['@context'] = 'https://raw.githubusercontent.com/digital-certificates#'
        data['type'] = 'DigitalCertificate'

        data['certificate']['@context'] = 'https://raw.githubusercontent.com/digital-certificates#'
        data['certificate']['type'] = 'Certificate'

        data['certificate']['issuer']['@context'] = 'https://raw.githubusercontent.com/digital-certificates#'
        data['certificate']['issuer']['type'] = 'Issuer'

        data['assertion']['@context'] = 'https://raw.githubusercontent.com/digital-certificates#'
        data['assertion']['type'] = 'Assertion'

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
    convert('../examples/1.1.0/sample_unsigned_cert.json', 'v2_sample_unsigned_cert.json')
