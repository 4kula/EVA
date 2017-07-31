#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os

# houses most of the utlity functions for eva
class Misc:
    # container for variable that is SUPPOSED to be instanced
    _this = {}

    def __init__(self):
        """Class initializer, sets the pid for current instance.
        """
        self._this['pid'] = os.getpid()
        return

    @staticmethod
    def say(raw):
        """Simple print that has the command line marker appended to the front
        """
        print '(~˘▾˘)~: {}'.format(raw)
