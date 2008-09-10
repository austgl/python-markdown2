#!/usr/bin/env python
# Copyright (c) 2007-2008 ActiveState Software Inc.
# License: MIT (http://www.opensource.org/licenses/mit-license.php)

"""The markdown2 test suite entry point."""

import os
from os.path import exists, join, abspath, dirname, normpath
import sys
import logging

import testlib


testdir_from_ns = {
    None: os.curdir,
}

def setup():
    top_dir = dirname(dirname(abspath(__file__)))
    lib_dir = join(top_dir, "lib")
    sys.path.insert(0, lib_dir)

    pygments_dir = join(top_dir, "externals", "pygments")
    if exists(pygments_dir):
        sys.path.insert(0, pygments_dir)

if __name__ == "__main__":
    retval = testlib.harness(testdir_from_ns=testdir_from_ns,
                             setup_func=setup,
                             default_tags=["-knownfailure"])
    sys.exit(retval)

