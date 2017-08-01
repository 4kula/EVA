#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os, sys
from misc import Misc as _m

# data storage will be done thorugh sqlite
class Archive:
    # container for variable that CAN be instanced
    _this = {
        'pid' : os.getpid(),
        'source' : '{}/Storage/1501624879.sqlite'.format(os.path.dirname(sys.modules['__main__'].__file__))
    }

    @staticmethod
    def run_query(query):
        """Runs the query
        """
        # Connecting to the database file
        conn = sqlite3.connect(Archive._this['source'])
        c = conn.cursor()
        c.execute(query)
        result = c.fetchall()
        conn.close()
        return result

    @staticmethod
    def get(directive):
        """Retrieve operations : expecting table, column, and value or raw
        """
        if ('raw' in directive):
            # throw up the raw query
            query = raw
        else:
            # fill in the table, column and value
            query = 'SELECT * FROM {} WHERE {} = \"{}\"'.format(directive['table'], directive['column'], directive['value'])

        # return the result of the query
        return Archive.run_query(query)

    @staticmethod
    def put(directive):
        """Update operations
        """
        return

    @staticmethod
    def set(directive):
        """Create operations
        """
        return

    @staticmethod
    def test(directive={}):
        print Archive._this['source']
        return
