# -*- coding: utf-8 -*-
# case_manager.py

from test.vim_testing import vim_test_manager
from test.vnf_testing import vnf_test_manager
import logging


CASES = {'vim', 'vnf'}


class CaseManager(object):
    """Represents Case Manager's Functions
    """
    def __init__(self):
        pass

    def start(self, case, tool, **kwargs):
        if case not in CASES:
            # Todo : Error Log
            pass
        if str(case) == 'vim':
            vim_test_manager.start(tool, kwargs)
        elif str(case) == 'vnf':
            vnf_test_manager.start(tool)
