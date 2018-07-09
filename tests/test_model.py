#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Tests for `ransom_c2c_detector` package."""


import unittest
import os
from ransom_c2c_detector import ransom_c2c_detector
from ransom_c2c_detector.model import URLModel

class TestModel(unittest.TestCase):
    """Tests for `ransom_model` package."""

    def setUp(self):
        """Set up test fixtures, if any."""
        self.m = URLModel()
        self.path = os.path.join( os.path.dirname(os.path.realpath(__file__))\
                            ,'../ransom_c2c_detector')
        self.m.get_model(os.path.join(self.path,'model.plk'))
    def tearDown(self):
        """Tear down test fixtures, if any."""

    def test_pass_case(self):
        """Test Basic Feature test"""
        data = [3.72161172397,0.0983116818692,0.00230044273391,\
                0.000342348510784,0.000510790448219]
        res = self.m.pred(data)
        self.assertEqual(res[0],1)

    def test_clean(self):
        """test_clean"""
        data = [0,10,0,0,0]
        self.assertEqual(self.m.pred(data)[0],0)
