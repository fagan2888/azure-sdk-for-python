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

try:
    from ._models_py3 import Key
    from ._models_py3 import KeyValue
    from ._models_py3 import Label
except (SyntaxError, ImportError):
    from ._models import Key
    from ._models import KeyValue
    from ._models import Label
from ._paged_models import KeyPaged
from ._paged_models import KeyValuePaged
from ._paged_models import LabelPaged

__all__ = [
    'Key',
    'KeyValue',
    'Label',
    'KeyValuePaged',
    'KeyPaged',
    'LabelPaged',
]
