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

... Show  two examples here. a simple one with just start and end time, and one with filters. Show the corresponding ffmpeg command??

## How to install

Since `htmlvid` is written in python, it should ideally work cross-platform. (Have I tested it???) You can get it via `pip` by running this command:

    sudo pip install htmlvid

If you wish to install it manually, download the source code (Download Zip) and run the following commands:

    cd /path/to/htmlvid
    python setup.py install

Make sure you have `configargparse` installed. (Or `sudo pip install configargparse`)

## How to get FFmpeg

There are three ways to get `FFmpeg`. One is through your favorite package manager (if it includes support for libvpx and libx264). A second way is to download a prebuilt binary. The third way is to install from source.

It is recommended for Window users to download the binary, mac users to use `homebrew`, and for linux users to install from source.

***Important:*** Each method uses it's own flags for compiling `FFmpeg` so not every feature of `htmlvid` might work. If you follow the recommended way for your OS, you shouldn't have a problem. Every method has support for both WebM and MP4.

### Installing from a package manager

#### OSX

##### Homebrew

    brew install ffmpeg --with-libvpx --with-libvorbis --with-fdk-aac --with-libass

##### Macports

    sudo port install ffmpeg +vorbis +x264 +gpl +libfdk-aac +nonfree

#### Linux

##### apt-get

You will have to use Jon Severinsson's PPA:

    sudo apt-get remove ffmpeg
    sudo apt-get purge libav-tools # Removes libav/avconv
    sudo add-apt-repository ppa:jon-severinsson/ffmpeg
    sudo apt-get update
    sudo apt-get install ffmpeg

*Note:* Because of some developments in July 2011, Ubuntu only offers `avconv`, a fork of `FFmpeg`. The two are not completely compatible and I will only be supporting `FFmpeg`. (If you really must use `avconv`, open `htmlvid.py` and set `FFMPEG_BIN` to `avconv` and `FFPROBE_BIN` to `avprobe` but I haven't tested it and I can't guarantee it'll work.)

### Installing from a binary

***Important:*** The OSX and Linux binaries do not include `ffprobe`, so you cannot use the `--duplicate` option along with the `--limit` option since it is needed to find out the full video duration.

#### OSX

http://www.evermeet.cx/ffmpeg/

The latest build should be fine.

#### Linux

http://johnvansickle.com/ffmpeg/

Download one of the first two builds. (32-bit if you're unsure.)

#### Windows

http://ffmpeg.zeranoe.com/builds/

Just download one of the static builds. (32-bit if you're unsure.)

### Installing from source

First, [download the FFmpeg source code](https://www.ffmpeg.org/download.html). (It'll be the tar.bz2 file) Then follow [the specific instructions](http://trac.ffmpeg.org/wiki/CompilationGuide) for your operating system before building.

Minimum dependencies: `libvpx libvorbis libx264 libfdk-aac libass pkg-config yasm texi2html`

Once you have your environment properly setup and dependencies installed, you can continue.

The configuration flags we need are as follows:

    # For WebM support
        --enable-libvpx
        # For WebM sound
        --enable-libvorbis

    # For MP4 support
        --enable-libx264

		# For MP4 sound
		--enable-libfdk-aac
        # You can also use libfaac or libvo-aacenc instead. Or you could exclude it entirely and rely on ffmpeg's experimental aac encoding.
        # libfdk_aac > libfaac > Native FFmpeg AAC ≥ libvo_aacenc (https://trac.ffmpeg.org/wiki/Encode/AAC)
        # --enable-libfaac
        # --enable-libvo-aacenc

        # Allow use of GPL code. Needed for libx264.
        --enable-gpl
        # Allow use of non-free code. Needed for libfaac/libfdk-aac
        --enable-nonfree

    # Other
        # For subtitle support
        --enable-libass
        # For multithreading support
        --enable-pthreads
        # yasm is needed to optimize our build
        # texi2html is needed for documentation
		# Optional mp3 support with libmp3lame
		# --enable-libmp3lame

*Note:* These are just the minimum required flags needed for `htmlvid`. You might want to add more if you need support for other formats or if you use `ffmpeg` for other purposes. Run `./configure -help` for  a list of flags and their descriptions.

Finally, we can compile:

    tar xjvf ffmpeg-x.x.x.tar.bz2 # extract archive
    cd ffmpeg-x.x.x
    ./configure --enable-pthreads --enable-libvpx --enable-libvorbis --enable-libx264 --enable-libfdk-aac --enable-libass --enable-gpl --enable-nonfree
    sudo make install

Congrats! You just compiled your own `FFmpeg` copy with all the features we need.

## How to use

For help using `htmlvid`, run it with the `-h` option to see a nice help message detailing each option. Technically, the only required option is the path to the video, but you'll most likely want to set the start time and video duration each time also. The quality and bitrate options already use sane defauls.

The default config file is located at `~/.htmlvid`. Instructions for the config file and possible values for each option are documented inside the config file.

*Note:* if you are making these to share with others, try not to make the clips too long. Gfycat sets a 15 second limit on their videos and I think that's reasonable. If you plan to encode any longer than a few minutes, you should probably be using `FFmpeg` directly.

## Filehosts

| | Host | Max. Duration | Max. Filesize | Sound |
| ---: | :---: | :---: | :---: | :---: |
| Cross-browser: |  |  |  |  |
| | gfycat.com | 15 sec | None | ✗  |
| | mediacru.sh | None | 50 MB | ✓ |
| Other: |  |  |  |  |
| | pomf.se | None | 52 MB | ✓ |
| | 4chan.org | 2 min | 3 MB | ✗ |

For individual browser support see [here](http://www.w3schools.com/html/HTML5_video.asp) under "HTML Video - Browser Support". The gist of it is that Chrome and Firefox currently support both formats, while Safari and Internet Explorer only support MP4.

## FAQ

Here are some questions you might have.

> My conversions are taking too long.

Consider making the video width smaller (`-w`), or decreasing the bitrate. (`-b`) Two pass runs (`-p`) will take longer. Embedding subtitles (`-e`) will always take longer because instead of the usual fast seek, `FFmpeg` will have to seek from the start of the video to properly process the subtitles. Also, remember: try not to make your videos longer than 15 seconds.

> The output looks blurry/bad.

Consider increasing the bitrate (`-b`), especially if there is fast movement in the scene. You also might have set the quality (`-q`) value too high. (Lower is better)

> The progress doesn't update enough.

Unfortunately, `FFmpeg` only seems to report it's progress every ~700ms (the number varies widely) of the output duration, so the progress can only be that frequent. There is also a large delay in the beginning when `FFmpeg` doesn't report any progress at all, where it is probably processing and reading the input file.

> Can we get gif support too?

Well, here's the thing: `FFmpeg` does support gif conversion, but the problem is that it's not very good at all. The filesize ends up extremely large and the quality isn't the best. The best way to make them would be to: extract the frames of the video using `FFmpeg`, make a gif out of them using `imagemagick`'s `convert`, and further optimize the filesize using `gifsicle`. You'll have to constantly be decreasing quality and colors just to get a decent filesize. As you can see it is very tedious, especially getting the filesize right. That's why we're creating videos in the first place.

> How can I make my HD MP4's compatible with lower power mobile devices?

Pass the following options to `FFmpeg` (`-O`): `-pix_fmt yuv420p -profile:v baseline -level 3.0`. *Note*: This will result in a higher bitrate being used.

> Why don't you use *x* feature of FFmpeg/codec to get better quality and filesize?

`FFmpeg` has a lot of ways to tweak the output quality letting you choose between different modes and presets. The reason I only use the `-crf` and `-b:v` options is KISS (Keep It Simple Stupid). The more complicated options require better knowledge of `FFmpeg` and the video codecs which leads to more room for error. It is better suited for encoding large videos while our videos will be short snippets so we don't need that level of control. Lastly, the options for different codecs are widely different. (I already think it's too much to have to remember that `-crf` works on a different scale for WebM and MP4's.)

> Why not just use `FFmpeg` directly?

So you don't have to fumble with arcane `FFmpeg` syntax! (Instead you have to deal with `htmlvid`'s.) But seriously, `htmlvid` makes it much easier to simply create videos because it's options are specifically designed for the purpose. It's much more flexible in what type of options it takes and it solves many shortcomings of `FFmpeg`'s filters.

> A GUI would be much more useful.

I considered that. It would be pretty neat to have a thumbnail view of the video so you could choose the right times and a see the results of filters and such. Unfortunately I'm very new to programming, so maybe in some distant future.

> What's up with the default filenames?

I decided to experiment and use UNIX timestamps for the filenames. The time itself is not useful as files already have creation date metadata, but it serves to let you have the output videos ordered by creation time with short names.

> Which format is better?

Both [early](http://x264dev.multimedia.cx/archives/377) and [recent](https://gist.github.com/Hupotronic/4645784) comparisons done between WebM (VP8) and MP4 (H.264 using x264) concluded that MP4's were superior. Some areas in which WebM is worse: it's slower, it results in lower quality, it results in larger file sizes, it's worst at encoding high speed scenes, and it lacks hardware encoding in most devices (Important for smartphones).

So why would you still want to use WebM then? First, it's patent free. We should be supporting open formats. Second, the cons aren't bad enough to discount it for our use case. We can achieve decent quality and file size with WebM for our short snippets. Third, more websites support WebM uploads. Fourth, since we're usually uploading to hosts that will serve both WebM and MP4 depending on the browser, it doesn't matter which we choose. Lastly, both formats are being constantly worked on and their successors are in the works (H.265 and VP9), so there is room for improvement for both of them.

> I want to use a youtube video.

Use [`youtube-dl`](http://rg3.github.io/youtube-dl/) to download the file locally first or use [gfycat](http://www.gfycat.com/).

> I have a feature/bug request.

Open an issue and I'll see what I can do.

## License

`htmlvid` is licensed under the ...

## References

<!--Clean this up!!!-->

* [FFmpeg WebM Encoding Guide](https://trac.ffmpeg.org/wiki/Encode/VP8)

* [FFmpeg MP4 Encoding Guide](https://trac.ffmpeg.org/wiki/Encode/H.264)

* [How mediacru.sh Handles Video For The Web](https://blog.mediacru.sh/2013/12/23/The-right-way-to-encode-HTML5-video.html)

* [FFmpeg Documentation](http://www.FFmpeg.org/ffmpeg-all.html#Description)

* [FFmpeg Filters Documentation](https://www.ffmpeg.org/FFmpeg-filters.html)

* [How To Replace avconv With (The Real) FFmpeg And Have It Work Right?](http://askubuntu.com/questions/373322/how-to-replace-avconv-with-the-real-ffmpeg-and-have-it-work-right)

<!--Split into multiple files??-->
