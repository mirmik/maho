#!/usr/bin/env python3
# coding: utf-8

import licant
import licant.install
import os
import sys

licant.execute("maho.g.py")

licant.cxx_static_and_shared(
    name="libraries",
    static_lib="libmaho.a",
    shared_lib="libmaho.so",
    mdepends= [
        "maho",
    ],
    defines=[],
    cxx_flags="",
    cc_flags="",
    ld_flags="",
    cxxstd="c++17",
    ccstd="c11",
    optimize="-O3"
)

licant.cxx_application("runtests",
                       sources=[
                           "tests/*.cpp",
                           "tests/base/*.cpp",
                           "tests/rga/*.cpp",
                           "tests/cga/*.cpp",
                       ],
                       cxxstd="c++20",
                       ccstd="c11",
                       cxx_flags="-g -fPIC -Werror=all -Wno-gnu-zero-variadic-macro-arguments -Weffc++",
                       include_paths=["./tests", "."],
                       )

licant.install.install_library(
    tgt="install",
    uninstall="uninstall",
    libtgt=["libmaho.so", "libmaho.a"],
    hroot="maho",
    headers="maho")

licant.fileset("all", targets=["runtests", "libmaho.so", "libmaho.a"])

licant.ex("all")
