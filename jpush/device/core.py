#!/usr/bin/env python
from jpush import common
import json

DEVICE_BASEURL = "https://device.jpush.cn/"
DEVICE_URL = DEVICE_BASEURL + "v3/device/"
TAG_URL = DEVICE_BASEURL + "v3/tag/"
TAGLIST_URL = TAG_URL + "list/"
ALIAS_URL = DEVICE_BASEURL + "v3/alias/"

class Device(object):
    """Device info query/update..

    """
    def __init__(self, jpush):
        self._jpush = jpush 
        self.entity = None

    def send(self, method, url, body, content_type=None, version=3):
        """Send the request
        
        """
        response = self._jpush._request(method, body,
            url, content_type, version=3)
        return DeviceResponse(response)

    def get_taglist(self):
        """Get deviceinfo with registration id.
        """
        url = common.TAGLIST_URL
        body = None
        info = self.send("GET", url, body)

    def get_deviceinfo(self, registration_id):
        """Get deviceinfo with registration id.
        """
        url = common.DEVICE_URL + registration_id + "/"
        body = None
        info = self.send("GET", url, body)
        print info

    def set_deviceinfo(self, registration_id, entity):
        """Update deviceinfo with registration id.
        """
        url = common.DEVICE_URL + registration_id + "/"
        body = json.dumps(entity)
        print url, body
        info = self.send("POST", url, body)
        print info

    def delete_tag(self, tag, platform=None):
        """Delete registration id tag.
        """
        url = common.TAG_URL + tag + "/"
        body = None
        if platform:
            body = platform
        print url, body
        info = self.send("DELETE", url, body)
        print info

    def update_tagusers(self, tag, entity):
        """Add/Remove specified tag users.
        """
        url = common.TAG_URL + tag + "/"
        body = json.dumps(entity)
        print url, body
        info = self.send("POST", url, body)
        print info

    def check_taguserexist(self, tag, registration_id):
        """Check registration id whether in tag.
        """
        url = common.TAG_URL + tag + "/exist/"
        body = registration_id
        print url, registration_id 
        info = self.send("GET", url, body)
        print info

    def delete_alias(self, alias, platform=None):
        """Delete appkey alias.
        """
        url = common.ALIAS_URL + alias + "/"
        body = None
        if platform:
            body = platform
        print url, body
        info = self.send("DELETE", url, body)
        print info

    def get_aliasuser(self, alias, platform=None):
        """Get appkey alias users.
        """
        url = common.ALIAS_URL + alias + "/"
        body = None
        if platform:
            body = platform
        print url, body
        info = self.send("GET", url, body)
        print info
    
class DeviceResponse(object):
    """Response to a successful device request send.

    Right now this is a fairly simple wrapper around the json payload response,
    but making it an object gives us some flexibility to add functionality
    later.

    """
    payload = None

    def __init__(self, response):
        if 0 != len(response.content):
            data = response.json()
            self.payload = data
        elif 200 == response.status_code:
            self.payload = "success"

    def __str__(self):
        return "Device response Payload: {0}".format(self.payload)
