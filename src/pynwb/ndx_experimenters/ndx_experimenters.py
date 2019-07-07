import os
from os import path

from hdmf.utils import popargs
from pynwb import load_namespaces, NWBFile as NWBFile_core, register_class, docval

name = 'ndx-experimenters'

here = path.abspath(path.dirname(__file__))
ns_path = os.path.join(here, 'spec', name + '.namespace.yaml')

load_namespaces(ns_path)


@register_class('NWBFile_experimenters', name)
class NWBFile(NWBFile_core):
    @docval(*NWBFile_core.__init__.__docval__['args'] +
            [{'name': 'experimenters', 'type': 'array_data', 'shape': (None,), 'default': None, 'doc': 'doc'}])
    def __init__(self, **kwargs):
        experimenters = popargs('experimenters', kwargs)
        super(NWBFile, self).__init__(**kwargs)
        self.experimenters = experimenters
