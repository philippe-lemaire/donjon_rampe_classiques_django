from django.template.defaulttags import register


@register.filter
def get_item(dictionary, key):
    if isinstance(dictionary, dict):
        return dictionary.get(key)
    elif isinstance(dictionary, tuple):
        return dictionary[int(key)]
