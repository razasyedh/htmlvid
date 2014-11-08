#!/usr/bin/env python

import unittest
import htmlvid
import configargparse

class sample_default_args:
    format = "webm"
    quality = None
    limit = None
    bitrate = None
    twopass = False
    testrun = False
    verbose = None
    metadata = "testfile"
    to = "12"
    duplicate = False
    output = "testfile"

class expected_return_args:
    format = "webm"
    quality = 10
    limit = None
    bitrate = "750K"
    twopass = False
    testrun = False
    verbose = None
    metadata = "testfile"
    to = "12"
    duplicate = False
    output = "testfile.webm"

class TestArguments(unittest.TestCase):

    def setUp(self):
        pass

    # def test_crf(self):
    #     self.assertRaises(configargparse.ArgumentTypeError, htmlvid.crf("30"))

    # def test_bitrate_calculation(self):
    #     self.assertEqual("2978.91K", htmlvid.calculate_bitrate("2M", 5.5))

    def test_implied_values_set_correctly(self):
        sample = sample_default_args
        expected = expected_return_args
        htmlvid.set_implied(sample)
        self.assertEqual(expected, sample)

if __name__ == "__main__":
    unittest.main()
