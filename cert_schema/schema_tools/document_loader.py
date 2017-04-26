import requests
import validators


class InvalidUrlError(Exception):
    pass


def load_document(url):
    """
    :param url:
    :return:
    """
    result = validators.url(url)
    if result:
        response = requests.get(
            url, headers={'Accept': 'application/ld+json, application/json'}
        )
        return response.text
    raise InvalidUrlError('Could not validate ' + url)


def jsonld_document_loader(url):
    """
    Retrieves JSON-LD at the given URL. Propagates BlockcertValidationError is url is invalid
    or doesn't exist
    :param url: the URL to retrieve
    :return: JSON-LD at the URL
    """
    data = load_document(url)
    return {
        'contextUrl': None,
        'documentUrl': url,
        'document': data
    }
