## How to install

*Note*: Since `htmlvid` is written in Python it should (ideally) work cross-platform. However, I can't guarantee it will work on Windows out of the box because I don't have access to a windows install. Let me know if it works for you, and if you had to tweak something, a pull request is welcome!

You can get it via `pip` by running this command:

    sudo pip install htmlvid

If you wish to install it manually, download the source code (Download Zip) and run the following commands:

    cd /path/to/htmlvid
    python setup.py install

Make sure you have `configargparse` installed, either manually or by using `sudo pip install configargparse`.

Already have `FFmpeg`? You might not be finished yet! Read on.

## How to get FFmpeg

If you already have `FFmpeg` installed, check that it was built with support for  libvpx and libx264 by running `ffmpeg -buildconf` and looking for the lines `--enable-libvpx` and `--enable-libx264`. If it was, you're good to go.

There are three ways to get `FFmpeg`. One way is through your favorite package manager (if it includes support for libvpx and libx264). A second way is to download a prebuilt binary. The third way is to install from source.

It is recommended for Mac users to use [homebrew](http://brew.sh/), for Linux users to install from source, and for Windows users to install the binary.

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

Just go to the corresponding website for your operating system and download the build specified. You will then have to unpack the binary and either add it's location to your PATH, or move it to a directory already in your PATH. For Mac and Linux, I suggest moving it to `/usr/local/bin`. For Windows, follow [these instructions](http://www.wikihow.com/Install-FFmpeg-on-Windows#Enabling_FFmpeg_in_the_Command_Line_sub).

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

    tar xjvf ffmpeg-x.x.x.tar.bz2 # Extract archive
    cd ffmpeg-x.x.x
    ./configure --enable-pthreads --enable-libvpx --enable-libvorbis --enable-libx264 --enable-libfdk-aac --enable-libass --enable-gpl --enable-nonfree
    sudo make install

Congrats! You just compiled your own `FFmpeg` copy with all the features we need.

