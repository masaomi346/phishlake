"""
Add a new mitmproxy option.

Log outgoing IP Geolocation Service.
author: @masaomi346

Usage:

    mitmproxy -s ipinfo.py
"""
from mitmproxy import ctx, http, log
from mitmproxy.addons import termlog
import json
import datetime

class IPInfo:
    def __init__(self):
        self.outfile = '/home/mitmproxy/logs/IPInfo.log'

    def load(self, loader):
        loader.add_option(
            name = "IPInfo",
            typespec = bool,
            default = True,
            help = "Log outgoing IP Geolocation Service",
        )

    def response(self, flow):
        ipinfo_domain = ['ip-api.com','geoiptool.com','api.ipregistry.co','ipinfo.io','geoplugin.net','extreme-ip-lookup.com','blackbox.ipinfo.app','ipapi.co','api.ipify.org']
        for domain in ipinfo_domain:
            if flow.request.pretty_host.endswith(domain):
                time = datetime.datetime.now()
                data = {}
                data['time'] = time.strftime("%Y-%m-%d %H:%M:%S")
                data['url'] = flow.request.pretty_url
                data['response'] = flow.response.get_text()
                with open(self.outfile, 'a', encoding='utf-8') as fd:
                    json.dump(data, fd)
                    fd.write('\n')
                break

addons = [
    IPInfo()
]
