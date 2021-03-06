# Future Imports for py2/3 backwards compat.
from __future__ import (absolute_import, division, print_function,
                        unicode_literals)
from builtins import object
from future import standard_library
standard_library.install_aliases()


class AssetHostTypes(object):
    Empty = ''
    Guest = 'GUEST'
    Hypervisor = 'HYPERVISOR'
    Physical = 'PHYSICAL'
    Mobile = 'MOBILE'


class NodeScanStatus(object):
    UNKNOWN = ''
    COMPLETE = 'C'


# NOTE: the tags below are available but are currently not copied to a NodeBase object
# id
# idType
# isMobile
# scanEngineName
# scanStatusTranslation
# vulnerabilityCount
class NodeBase(object):
    def InitializeFromJSON(self, json_dict):
        self.id = json_dict['nodeID']
        self.asset_id = json_dict['assetID']
        self.host_name = json_dict['hostName']
        self.os_name = json_dict['operatingSystem']
        self.ip_address = json_dict['ipAddress']
        self.scan_id = json_dict['scanID']
        self.scan_status = json_dict['scanStatus']
        self.scan_duration = json_dict['duration']  # TODO: is this in ms?

    def __init__(self):
        self.id = 0
        self.asset_id = 0
        self.ip_address = ''
        self.host_name = ''
        self.os_name = ''
        self.scan_id = 0
        self.scan_status = NodeScanStatus.UNKNOWN
        self.scan_duration = 0


class Node(NodeBase):
    @staticmethod
    def CreateFromJSON(json_dict):
        node = Node()
        NodeBase.InitializeFromJSON(node, json_dict)
