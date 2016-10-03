#!/usr/bin/python2.7
# -*- coding: utf-8 -*-

from Color import Color
from CrackResult import CrackResult

import time

class CrackResultWPS(CrackResult):
    def __init__(self, bssid, essid, pin, psk):
        self.result_type = 'WPS'
        self.bssid = bssid
        self.essid = essid
        self.pin   = pin
        self.psk   = psk
        super(CrackResultWPS, self).__init__()

    def dump(self):
        if self.essid:
            Color.pl('{+} %s: {C}%s{W}' % (      'ESSID'.rjust(12), self.essid))
        Color.pl('{+} %s: {C}%s{W}'     % (      'BSSID'.rjust(12), self.bssid))
        Color.pl('{+} %s: {C}WPA{W} ({C}WPS{W})' % 'Encryption'.rjust(12))
        Color.pl('{+} %s: {G}%s{W}'     % (     'WPS PIN'.rjust(12), self.pin))
        Color.pl('{+} %s: {G}%s{W}'     % ('PSK/Password'.rjust(12), self.psk))

    def to_dict(self):
        return {
            'type'  : self.result_type,
            'date'  : self.date,
            'essid' : self.essid,
            'bssid' : self.bssid,
            'pin'   : self.pin,
            'psk'   : self.psk
        }

if __name__ == '__main__':
    crw = CrackResultWPS('AA:BB:CC:DD:EE:FF', 'Test Router', '01234567', 'the psk')
    crw.dump()
    crw.save()

