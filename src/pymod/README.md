## Build pacparser wheel for PreVeil


# win32:

### Prereq:

Set up tools:

1.  Install MinGW. Download the automated installer from here:
    http://sourceforge.net/projects/mingw/files/
    Running this installer lets you select what component you want to install.
    Default options (C-compiler and MinGW Development Toolkit) should work
    fine.

2.  Rename mingw32-make.exe to make.exe.
      rename C:\MinGW\bin\mingw32-make.exe C:\MinGW\bin\make.exe

3.  Add your MinGW directory's bin (C:\MinGW\bin) to your system path variable.

4.  Install 7-zip to extract .tar.gz files, if you don't have an equivalent
    program already.
    http://www.7-zip.org/download.html

5.  Install latest python. You'll need it to build python module.
    http://www.python.org/getit/


Notes: also need to have `python` and `wheel` in the env.

### Build:
Open an admin powershell.
```sh
    cd $path/pacparser
    make -C src -f Makefile.win32 pvmod
```

# macOS:

```sh
    cd $path/pacparser
    make -C src -f Makefile.win32 pvmod
```

Then the pacparser's wheel should be in `pymod/wheel/dist` for both platforms.
