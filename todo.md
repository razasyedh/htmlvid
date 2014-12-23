## Todo

- test for build flags and selectively show options. High priority because we want to allow people to use htmlvid with a fault or non-complete installation.
- make pip package
- Figure out why the MP4 preset is set to slow
- linux + mac binaries don't contain ffprobe ... use `ffmpeg -i` instead?
- take away bitrate option? Choose proper encoding modes.
- Add ogg format
- make filters autoappend a list
- s/User sent/Received/ --keyboard interrupt
- try different thread numbers webM supposedly can't be 0. detect threads using python?
- `\r` might not work on Windows. might need it on the end instead
- make sure the escaping for filters and -O isn't OS specific
- embed filter (extract the subs) (libass needed? subtitle filter fallback?). Make the '0' argument optional?
- fix what prints during each verbosity level and simplify the verbose code.
  - `-q` option?
  - use logging library?
  - maybe a function that takes verbosity level. should print to stderr.
  - make verbosity a number instead?
- `ffmpeg -buildconf 2>NULLDEVICE` put info in epilog and verbose. `ENABLE_FLAGS_CHECK`. Or in the form: available formats.
- package using pyexe (or pyinstaller) and py2app??

## Bugs
- subprocess failing because it can't find the file if it's a relative path.
  - give twopass file a name and just delete it after. same with vstats. no need for temp folder. Or append current directory? (`os.getcwd()`)
- mp4 bitrate has no effect when using `-crf`
- conflicts between option set in config and when conflicting option used in command line
- mp4 size with -l is a bit high. (also, compensate for sound)
  - 683k - 128k (desired audio bitrate) = 555k video bitrate
  - -b:a 128k # Acceptable values: 128/160/192/320

## Planned Features

- code to check if the user has python installed and in their PATH
  - Might not need it:
    - env: python: No such file or directory
    - windows users would need to call python first (include in FAQ)
- check if FFmpeg installed and in path?
  - http://stackoverflow.com/questions/377017/test-if-executable-exists-in-python
  - subprocess raises OSError No such file or directory but will fail silently on windows if exe is not found.
- option to take snapshot at time? should require -s (`-vframes dur out%02d.jpg`)
- option to mux in sound?
  - option to chose which audio track to include?
- gif support???

## Timeline

- Finalize all encoding settings (for video and sound)
- Create pip package (hopefully will have stable syntax by then)
- Fix command line experience (filenames, temp directory, configs, verbosity)
- Implement a minimum number of filters
- Cross-platform testing and use of different audio encoders
- Release
- Continue Development
  - Implement more filters
  - Subcommands?
  - gif support?
  - API uploading

## Misc

### Ideas

- Interesting filters: lut, color, colorbalance, curves, deshake, gradfun,
histeq, hue, smooth, pad, drawtext, drawbox?, removelogo, tile, vignette, zoompan?
- Option to upload result to gfycat/mediacrush?
   - http://www.gfycat.com/api
   - https://mediacru.sh/docs/api
- sub-commands to concat/cut/convert_to_gif??

### Modes
  b:v only: average bitrate mode  
  b:v w/ minrate+maxrate: constant bitrate mode  
  crf only: constant quality mode  
  crf and b:v: b:v has no effect for MP4 and needed for max bitrate for webm  
  constant quality mode is recommended for libpvx
