#!/usr/bin/env bash

set -euxo pipefail

# ver=$1
# [ -z $ver ] && echo "Please specify package version." && exit

# $stage_dir is where we'll install our package files.
stage_dir=/tmp/pacparser_$RANDOM
rm -rf /tmp/pacparser_*
mkdir -p $stage_dir
echo "DESTDIR=$stage_dir"

if [[ ! -f src/Makefile ]]; then
  echo "Call this script from the root of the source directory"
  exit 1
fi

# Build pactester and pacparser library and install in $stage_dir
make -C src 2>&1 | tee mk.log
DESTDIR=$stage_dir make -C src install 2>&1 | tee mk-install.log
# Build python module and install it in $stage_dir
make -C src pymod 2>&1 | tee mk-pymod.log
DESTDIR=$stage_dir make -C src install-pymod 2>&1 | tee mk-pymod-install.log
