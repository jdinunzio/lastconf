# -*- coding: utf-8 -*-

def deep_merge_dict(dct1, dct2):
    result = deep_clone_dict(dct1)

    for k, v in dct2.items():
        if is_dict_like(v):
            subdct1 = dct1.get(k, {})
            subdct2 = dct2.get(k)
            v = deep_merge_dict(subdct1, subdct2)

        result[k] = v

    return result


def deep_clone_dict(dct):
    result = {}

    for k, v in dct.items():
        if is_dict_like(v):
            v = deep_clone_dict(v)

        result[k] = v

    return result


def is_dict_like(obj):
    return hasattr(obj, 'items')
