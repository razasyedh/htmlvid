# htmlvid

An `FFmpeg` wrapper for creating HTML5 snippets of videos.

## Overview

`htmlvid` is a command line tool that lets you easily extract parts of videos so that you can share them online. It lets you choose between the WebM and MP4 formats, which are becoming increasingly dominant on the web as HTML5 video formats. (Even Twitter and Imgur use them for GIFs) These provide numerous advantages over the outdated GIF format including more colors, immensely smaller filesizes, and smoother playback.

`htmlvid` is written in Python. It uses `FFmpeg` to encode videos. It's only dependency is `configargparse`. (For config file support)

## Features

#### Easy to use.

You just need to set the start time and duration and you're good to go. No need to write a complicated `FFmpeg` command.

#### Sane defaults.

If you were to just use `FFmpeg` without specifying options like `-b:v` and `-crf`, the default quality would be abysmal. `htmlvid` chooses recommended defaults that give you a good output quality.

#### Get your desired quality easily

It's very easy to tweak the quality and bitrate to your liking. Fast action scenes looking blurry? Just add more bitrate!  Have a huge 1920p video? Just set the output width and you'll get a file that is easier to share. You can even set a size limit on the output file.

#### Configurable

You can set every option that you can specify on the command line in a config file. You can even use presets by choosing custom config files.

#### Filters

`FFmpeg` has a large amount of filters. The most useful ones are integrated directly into `htmlvid` (eg: `scale` for changing the output width and `subtitles` for embedding subtitles.). If you find you need to use more filters, just give them to `htmlvid` (`-F`) and it'll pass them along.

## Example usage

Here's a simple command to create a 5-second WebM from 5 minutes and 10 seconds into a video:

    htmlvid -s 5:10 -t 5 -o snippet.webm video.mkv

Here's a slightly more advanced command for creating a MP4 of a movie from the specified time ranges, limiting the size to 2 Megabytes, with a width of 400 pixels.

    htmlvid -f mp4 -s 40:26.324 -t 40:38 -l 2M -w 400 movie.mkv

## Installing

Please see [installing.md](./installing.md)

## How to use

For help using `htmlvid`, run it with the `-h` option to see a nice help message detailing each option. Technically, the only required option is the path to the video, but you'll most likely want to set the start time and video duration each time also. The quality and bitrate options already use sane defaults.

The default config file is located at `~/.htmlvid`. Instructions for the config file and possible values for each option are documented inside the config file.

For more help see [faq.md](./faq.md) and don't hesitate to reach out if something is unclear in the documentation.

*Note:* If you are making these to share with others, try not to make the clips too long. Gfycat sets a 15 second limit on their videos and I think that's reasonable. If you plan to encode any longer than a few minutes, you should probably be using `FFmpeg` directly.

## License

`htmlvid` is licensed under the MIT license.

## References

* [FFmpeg WebM Encoding Guide](https://trac.ffmpeg.org/wiki/Encode/VP8)

* [FFmpeg MP4 Encoding Guide](https://trac.ffmpeg.org/wiki/Encode/H.264)

* [How mediacru.sh Handles Video For The Web](https://blog.mediacru.sh/2013/12/23/The-right-way-to-encode-HTML5-video.html)

* [FFmpeg Documentation](http://www.FFmpeg.org/ffmpeg-all.html#Description)

* [FFmpeg Filters Documentation](https://www.ffmpeg.org/FFmpeg-filters.html)

* [FFmpeg Utilities Documentation](https://www.ffmpeg.org/ffmpeg-utils.html)

* [How To Replace avconv With (The Real) FFmpeg And Have It Work Right?](http://askubuntu.com/questions/373322/how-to-replace-avconv-with-the-real-ffmpeg-and-have-it-work-right)
