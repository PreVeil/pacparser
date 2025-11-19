#!/usr/bin/env bash

set -euxo pipefail

rm -rf \
 rust_ffi/target/ \
 src/jsapi_buildstamp \
 src/libpacparser.1.dylib \
 src/libpacparser.dylib \
 src/pacparser.o \
 src/pymod/pacparser_o_buildstamp \
 src/spidermonkey/js-buildstamp \
 src/spidermonkey/js/src/Darwin_DBG.OBJ/ \
 src/spidermonkey/js/src/jsautocfg.h \
 src/spidermonkey/libjs.a \
 src/pymod/build/ \
 src/pymod/dist/ \
 src/pymod/pacparser.egg-info/
