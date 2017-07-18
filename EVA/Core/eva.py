#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os, time


class Eva:
    # designate as property to Mutable Static(s) that are synced across INSTANCES
    _core = {
        '_up' : True,
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

    # container for variable that is SUPPOSED to be instanced
    _this = {}

    def __init__(self):
        """Class initializer, sets the pid for current instance.
        """
        self._this['pid'] = os.getpid()
        return

    def initiate(self):
        """Core function of EVA to listen for input and then act accordingly.
        """
        while (self._core['_up']):
            #self._input_to_command()

            self.testing()

        return

    def _input_to_command(self):
        """Get user's input and execute/handle the command async
        """
        usrInput = raw_input('(~˘▾˘)~: ')
        if (usrInput == 'quit'):
            self._core['_up'] = False
        print usrInput
        return

    def testing(self):
        print '(~˘▾˘)~: START - {}'.format(self._this['pid'])
        time.sleep(4)
        print '(~˘▾˘)~: END - {}'.format(self._this['pid'])
