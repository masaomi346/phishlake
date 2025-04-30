"""
Add a new mitmproxy option.

Log outgoing BIN Check Service.
author: @masaomi346

Usage:

    mitmproxy -s bininfo.py
"""
from mitmproxy import ctx, http, log
from mitmproxy.addons import termlog
import json
import datetime

class BinCheck:
    def __init__(self):
        self.outfile = '/home/mitmproxy/logs/bincheck.log'

    def load(self, loader):
        loader.add_option(
            name = "BinCheck",
            typespec = bool,
            default = True,
            help = "Log outgoing BIN Check Service",
        )

    def response(self, flow):
        ipinfo_domain = ['lookup.binlist.net']
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
    BinCheck()
]
