# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.paging import Paged


class KeyValuePaged(Paged):
    """
    A paging container for iterating over a list of :class:`KeyValue <azure.configurationservice.models.KeyValue>` object
    """

    _attribute_map = {
        'next_link': {'key': '@nextLink', 'type': 'str'},
        'current_page': {'key': 'items', 'type': '[KeyValue]'}
    }

    def __init__(self, *args, **kwargs):

        super(KeyValuePaged, self).__init__(*args, **kwargs)
class KeyPaged(Paged):
    """
    A paging container for iterating over a list of :class:`Key <azure.configurationservice.models.Key>` object
    """

    _attribute_map = {
        'next_link': {'key': '', 'type': 'str'},
        'current_page': {'key': 'items', 'type': '[Key]'}
    }

    def __init__(self, *args, **kwargs):

        super(KeyPaged, self).__init__(*args, **kwargs)
class LabelPaged(Paged):
    """
    A paging container for iterating over a list of :class:`Label <azure.configurationservice.models.Label>` object
    """

    _attribute_map = {
        'next_link': {'key': 'nextLink', 'type': 'str'},
        'current_page': {'key': 'items', 'type': '[Label]'}
    }

    def __init__(self, *args, **kwargs):

        super(LabelPaged, self).__init__(*args, **kwargs)
