## FAQ

Here are some questions you might have.

> Where can I send a feature request or bug report?

Open an issue on the github page and I'll see what I can do.

> How can I make a conversion faster?

Consider making the video width smaller (`-w`), or decreasing the bitrate. (`-b`) Embedding subtitles (`-e`) will always take longer because instead of the usual fast seek, `FFmpeg` will have to seek from the start of the video to properly process the subtitles. Also, remember: try not to make your videos longer than 15 seconds.

> How can I make the output look less blocky?

Consider increasing the bitrate (`-b`), especially if there is fast movement in the scene. You might also have set the quality (`-q`) value too high. (Lower is better)

> Why is FFmpeg giving the error "No such file or directory"?

This is most likely due to problems with special characters in the path to your file or in a string you passed to `htmlvid`. There are two ways to remedy this:

1. Temporarily remove *all* single quotes and backslashes from *every* directory leading to your file (or move the file to a safe directory) *and* the file's filename. I'm serious. This is the best solution unless you want to enter *\\\\\'escaping hell\\\\\'*.

2. First read the FFmpeg documentation on [quoting and escaping for utilities](https://www.ffmpeg.org/ffmpeg-utils.html#Quoting-and-escaping) and [for filters](https://www.ffmpeg.org/ffmpeg-filters.html#Notes-on-filtergraph-escaping). Make sure you understand it. Then proceed to escape the special characters in your commandline invocation. You might need multiple escapes.

> Why doesn't the progress update fast enough?

Unfortunately, `FFmpeg` only seems to report it's progress every ~700ms (the number varies widely) of the output duration, so the progress can only be that frequent. There is also a large delay in the beginning when `FFmpeg` doesn't report any progress at all, where it is probably processing and reading the input file.

> Can we get gif support too?

Well, here's the thing: `FFmpeg` does support gif conversion, but the problem is that it's not very good at all. The filesize ends up extremely large and the quality isn't the best. The best way to make them would be to: extract the frames of the video using `FFmpeg`, make a gif out of them using `imagemagick`'s `convert`, and further optimize the filesize using `gifsicle`. You'll have to constantly be decreasing quality and colors just to get a decent filesize. As you can see it is very tedious, especially getting the filesize right. That's why we're creating videos in the first place.

> How can I make my HD MP4's compatible with lower power mobile devices?

Pass the following options to `FFmpeg` (`-O`): `-pix_fmt yuv420p -profile:v baseline -level 3.0`. *Note*: This will result in a higher bitrate being used.

> Why don't you use *x* feature of FFmpeg/codec to get better quality and filesize?

`FFmpeg` has a lot of ways to tweak the output quality letting you choose between different modes and presets. The reason I only use the `-crf` and `-b:v` options is KISS (Keep It Simple Stupid). The more complicated options require better knowledge of `FFmpeg` and the video codecs which leads to more room for error. They are better suited for encoding large videos while our videos will be short snippets so we don't need that level of control. Lastly, the options for different codecs are widely different. (I already think it's too much to have to remember that `-crf` works on a different scale for WebM and MP4's.)

> What's up with the default filenames?

I decided to experiment and use UNIX timestamps for the filenames. The time itself is not useful as files already have creation date metadata, but it serves to let you have the output videos ordered by creation time with short names.

> Which format is better?

Both [early](http://x264dev.multimedia.cx/archives/377) and [recent](https://gist.github.com/Hupotronic/4645784) comparisons done between WebM (VP8) and MP4 (H.264 using x264) concluded that MP4's were superior. Some areas in which WebM is worse: it's slower, it results in lower quality, it results in larger file sizes, it's worst at encoding high speed scenes, and it lacks hardware encoding in most devices (Important for smartphones).

So why would you still want to use WebM then? First, it's patent free. We should be supporting open formats. Second, the cons aren't bad enough to discount it for our use case. We can achieve decent quality and file size with WebM for our short snippets. Third, more websites support WebM uploads. Fourth, since we're usually uploading to hosts that will serve both WebM and MP4 depending on the browser, it doesn't matter which we choose. Lastly, both formats are being constantly worked on and their successors are in the works (H.265 and VP9), so there is room for improvement for both of them.

> How can I use a youtube video?

Use [`youtube-dl`](http://rg3.github.io/youtube-dl/) to download the file locally first or use [gfycat](http://www.gfycat.com/).

> What filehosts can I use and what are their limitations?

| | Host | Max. Duration | Max. Filesize | Sound |
| ---: | :---: | :---: | :---: | :---: |
| Cross-browser: |  |  |  |  |
| | gfycat.com | 15 sec | None | ✗  |
| | mediacru.sh | None | 50 MB | ✓ |
| Other: |  |  |  |  |
| | pomf.se | None | 52 MB | ✓ |
| | 4chan.org | 2 min | 3 MB | ✗ |

> I want to embed the snippet directly. Which formats are supported by browsers?

See [here](http://www.w3schools.com/html/HTML5_video.asp) under "HTML Video - Browser Support". The gist of it is that Chrome and Firefox currently support both formats, while Safari and Internet Explorer only support MP4.
