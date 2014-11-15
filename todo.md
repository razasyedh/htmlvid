## Todo

- take away bitrate option? Choose proper encoding modes.
- linux + mac binaries don't contain ffprobe ... use `ffmpeg -i` instead?
- try different thread numbers webM supposedly can't be 0
- test that milliseconds work properly
- `\r` might not work on Windows. might need it on the end instead
- embed filter (extract the subs) (libass needed?). Make the '0' argument optional?
- fix what prints during each verbosity level and simplify the verbose code.
  - maybe a function that takes verbosity level. should print to stderr.
  - make verbosity a number instead?
- remove default width??
- Figure out why the MP4 preset is set to slow
- make sure the escaping for filters and -O isn't OS specific
- `ffmpeg -buildconf 2>NULLDEVICE` put info in epilog and verbose. `ENABLE_FLAGS_CHECK`
- make pip package
- package using pyinstaller or pyexe??

## Bugs
- subprocess failing because it can't find the file if it's a relative path.
  - give twopass file a name and just delete it after. same with vstats. no need for temp folder. Or append current directory? (`os.getcwd()`)
- mp4 bitrate has no effect when using `-crf`
- conflict between option set in config and when conflicting option used in command line
- mp4 size with -l is a bit high. (also, compensate for sound)
  - 683k - 128k (desired audio bitrate) = 555k video bitrate
  - -b:a 128k # Acceptable values: 128/160/192/320
- `calculate_duration()` has weird behavior with millisecond values. 5.5 counts as 5.005

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
-  Option to upload result to gfycat/mediacrush?
   - http://www.gfycat.com/api
   - https://mediacru.sh/docs/api
- sub-commands to concat/cut/convert_to_gif??

## Timeline

- Finalize all encoding settings (for video and sound)
- Fix command line experience (filenames, temp directory, configs, verbosity)
- Implement minimum number of filters
- Cross-platform testing and using different audio encoders
- Create pip package and release
- Implement more filters
- Subcommands?
- Ogg/gif support?

## Misc Info

### Modes
  b:v only: average bitrate mode
  b:v w/ minrate+maxrate: constant bitrate mode
  crf only: constant quality mode
  crf and b:v: b:v has no effect for MP4 and needed for max bitrate for webm
  constant quality mode is recommended for libpvx
