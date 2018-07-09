#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Tests for `ransom_c2c_detector` package."""


import unittest

from ransom_c2c_detector import ransom_c2c_detector


class TestRansom_c2c_detector(unittest.TestCase):
    """Tests for `ransom_c2c_detector` package."""

    def setUp(self):
        """Set up test fixtures, if any."""

    def tearDown(self):
        """Tear down test fixtures, if any."""

    def test_entropy(self):
        """Test Entropy."""
        c2 = ransom_c2c_detector.RansomC2CDetector()
        self.assertEqual(c2.entropy('google.co.in'),2.8553885422075336)

    def test_corpus(self):
        pass

    def test_bigrams(self):
        pass

    def test_trigrams(self):
        pass

    def test_clean_url(self):
        pass

