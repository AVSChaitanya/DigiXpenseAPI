import re


def search_string(pattern, text) -> bool:
    """
    Full field regular matching

    :param pattern:
    :param text:
    :return:
    """
    result = re.search(pattern, text)
    if result:
        return True
    else:
        return False


def match_string(pattern, text) -> bool:
    """
    Regular match from the beginning of the field

    :param pattern:
    :param text:
    :return:
    """
    result = re.match(pattern, text)
    if result:
        return True
    else:
        return False


def is_phone(text: str) -> bool:
    """
    Check mobile number

    :param text:
    :return:
    """
    return match_string(r'^1[3-9]\d{9}$', text)
