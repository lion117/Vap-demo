# -*- coding: utf-8 -*-

import sys, os, time
import logging
import vapoursynth as vs
# import  vs_macro
from vapoursynth import core


import mvsfunc as mvf
src = core.ffms2.Source(source=r"e:\\media\\stand.mp4")
flt = mvf.BM3D(src, sigma=3.0, profile1="fast")
dst = src + flt
dst.set_output()
enable_v210 = True
