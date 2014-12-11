#!/usr/bin/env python

import unittest
import htmlvid
import configargparse

class TestArgumentTests(unittest.TestCase):
    def test_video_file(self):
        self.assertEqual("htmlvid", htmlvid.video_file("htmlvid"))
        self.assertRaises(configargparse.ArgumentTypeError,
                          htmlvid.video_file, "non_existant_file")
        self.assertEqual("-", htmlvid.video_file("-"))

    def test_time_stamp(self):
        self.assertEqual("00:00:03", htmlvid.time_stamp("3"))
        self.assertEqual("00:12:10", htmlvid.time_stamp("12:10"))
        self.assertEqual("01:02:56", htmlvid.time_stamp("01:02:56"))
        self.assertRaises(configargparse.ArgumentTypeError,
                          htmlvid.time_stamp, "123")

    def test_snip_duration(self):
        self.assertEqual("20", htmlvid.snip_duration("20"))
        self.assertEqual("00:01:10", htmlvid.snip_duration("1:10"))

    def test_crf(self):
        self.assertEqual(30, htmlvid.crf("30"))
        self.assertRaises(configargparse.ArgumentTypeError, htmlvid.crf, "-1")
        self.assertRaises(configargparse.ArgumentTypeError, htmlvid.crf, "64")

    def test_filesize(self):
        self.assertEqual("300K", htmlvid.filesize("300k"))
        self.assertEqual("500M", htmlvid.filesize("500M"))
        self.assertRaises(configargparse.ArgumentTypeError, htmlvid.filesize,
                          "1024")

    def test_ffmpeg_options(self):
        self.assertEqual("-pix_fmt yuv420p -level 3.0",
                         htmlvid.ffmpeg_options("\-pix_fmt yuv420p \-level 3.0"))
        self.assertRaises(configargparse.ArgumentTypeError,
                          htmlvid.ffmpeg_options, "\-r 23 \-s")
        self.assertRaises(configargparse.ArgumentTypeError,
                          htmlvid.ffmpeg_options, "\-loglevel")
        self.assertRaises(configargparse.ArgumentTypeError,
                          htmlvid.ffmpeg_options, "\-ss 7 \-t 10")

if __name__ == "__main__":
    unittest.main()
