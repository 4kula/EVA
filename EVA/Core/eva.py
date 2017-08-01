#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os, time
from multiprocessing import Process
from Modules.misc import Misc as _m
from Modules.archive import Archive as _a


class Eva:
    # designate as property to Mutable Static(s) that are synced across INSTANCES
    _core = {
        '_up' : True,
        'procs' : []
    }

    def get_core(self):
        """Getter for the _core container that houses all shared variables between instanced classes
        """
        return self._core

    def set_core(self, kvp):
        """Setter for the _core container that houses all shared variables between instanced classes
        """
        for key, value in kvp.iteritems():
            self._core[key] = value

    core = property(get_core, set_core)

    # container for variable that CAN be instanced
    _this = {}

    def __init__(self):
        """Class initializer, sets the pid for current instance.
        """
        self._this['pid'] = os.getpid()
        return

    def initiate(self):
        """Core function of EVA to listen for input and then act accordingly.
        """
#        while (self._core['_up']):
#            cmd = self.input_to_command()
#
#            # each command's action will be it's own process
#            p = Process(target=self._input_to_command(), args=())
#            (self._core['procs']).append(p)
#            p.start()

        _a.test()

        return

    def input_to_command(self):
        """Get user's input and execute/handle the command async
        """
        usrInput = raw_input('(~˘▾˘)~: ')
        if (usrInput == 'quit'):
            self._core['_up'] = False
        print usrInput
        return

    def testing(self):
        _m.say('START - {}'.format(self._this['pid']))
        time.sleep(4)
        _m.say('END - {}'.format(self._this['pid']))
