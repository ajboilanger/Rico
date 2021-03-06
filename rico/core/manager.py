import pprint
import curses
import re, os, sys
from rico.modules.ip import IP
from rico.util.debug import Debug
from rico.util.parse import Parse
from rico.gui.gui import Window

class Manager():
    def __init__(self, tokens, targets):
        Debug.debug_log()
        # set the passed in targets to vars for easier use
        self._targets_ip = targets['ip']

        # set the passed in tokens to vars for easier use
        self._token_ip = tokens['ip']

        # dict holds all the results with the target as the key
        self._dict_ip = {}

    def initialize(self):
        Debug.debug_log()
        for target in self._targets_ip:
            self._dict_ip[target] = IP.recon(self._token_ip, target)

    def run(self):
        Debug.debug_log()
        for k1, v1 in self._dict_ip.items():
            for k2, v2 in v1.items():
                print('########################################')
                print('# {:^38}'.format(k2))
                print('########################################')
                Parse.print_dict(v2)
            #ip_window = Window(value)
            #ip_window.display()


