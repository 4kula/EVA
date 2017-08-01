#!/usr/bin/env python
# -*- coding: utf-8 -*-

from Misc as _m

# from simple command mappings to understanding data and taking action
class Comprehension:
    # container for variable that is SUPPOSED to be instanced
    _this = {}

    def __init__(self):
        """Class initializer, sets the pid for current instance.
        """
        self._this['pid'] = os.getpid()
        return

    @staticmethod
    def decipher_command(self, input):
        """Takes the user input and decipher to understand the desired action
        1st Iteration will be a simple verb -> noun dictionary search
        """
