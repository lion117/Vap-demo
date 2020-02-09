# -*- coding: utf-8 -*-
"""
@author: LEO
Date:  2020/2/8
Email:	lion_117@126.com
All Rights Reserved Licensed under the Apache License
"""

import os, path

# from  Glogger import gLogger
import vapoursynth as vs
from vapoursynth import core
import mvsfunc as mvf
import havsfunc
import time
import datetime

import os, path,sys
import  logging
gLogger = logging.getLogger("pylog")
gLogger.setLevel(logging.INFO)
rf_handler = logging.StreamHandler(sys.stderr)  #默认是sys.stderr
rf_handler.setLevel(logging.DEBUG)
rf_handler.setFormatter(logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s"))

f_handler = logging.FileHandler('pylog.log')
f_handler.setLevel(logging.INFO)
f_handler.setFormatter(logging.Formatter("%(asctime)s - %(levelname)s - %(filename)s[:%(lineno)d] - %(message)s"))

gLogger.addHandler(rf_handler)
gLogger.addHandler(f_handler)


class TestMain():
    _noiseFile  = os.path.join(os.getcwd(),"image/my.bmp")
    # _noiseFile  = os.path.join(os.getcwd(),"image/face_boy.bmp")
    # _noiseFile  = os.path.join(os.getcwd(),"image/face_girl.bmp")
    # _noiseFile  = os.path.join(os.getcwd(),"image/girl.bmp")
    # _noiseFile  = os.path.join(os.getcwd(),"image/moon.bmp")
    # _noiseFile  = os.path.join(os.getcwd(),"image/man.bmp")
    _noiseVideo  = os.path.join(os.getcwd(),"video/dance82_output_0.mp4")

    @classmethod
    def runTest(cls):
        gLogger.info(u"hello world")



    @classmethod
    def runTestKNLMeansCLDenoisyImag(cls):
        lVSrc = core.ffms2.Source(source=cls._noiseFile)
        lst = datetime.datetime.now()
        for _ in range(30):
            flt = core.knlm.KNLMeansCL(lVSrc, 1, 3, 3,6,"RGB")
        lTotal  = (datetime.datetime.now()- lst).microseconds/1000
        gLogger.info("totla cost time:%d "%(lTotal ))
        lVSrc = core.text.Text(lVSrc, ["src"])
        flt = core.text.Text(flt, ["dst"])
        dst = core.std.StackHorizontal((lVSrc, flt))
        dst.set_output()
        gLogger.info("end cost time:%d "%((datetime.datetime.now()- lst).microseconds/1000 ))
        gLogger.info(lVSrc)
        enable_v210 = True
        gLogger.info(type(lVSrc))
        with open("compimage.rgb","wb") as rawfile:
            dst.output(rawfile)


    @classmethod
    def runTestKNLMeansCLDenoisyVideo(cls):
        lVSrc = core.ffms2.Source(source=cls._noiseVideo)
        lst = datetime.datetime.now()
        flt = core.knlm.KNLMeansCL(lVSrc, 3, 3, 3,3)
        lTotal  = (datetime.datetime.now()- lst).microseconds/1000
        gLogger.info("denoise cost time:%d "%(lTotal ))
        lVSrc = core.text.Text(lVSrc, ["src"])
        flt = core.text.Text(flt, ["dst"])
        dst = core.std.StackHorizontal((lVSrc, flt))
        dst.set_output()
        gLogger.info("end cost time:%d "%((datetime.datetime.now()- lst).microseconds/1000 ))
        gLogger.info(lVSrc)
        enable_v210 = True
        with open("denoise_dst_dance.yuv","wb") as rawfile:
            flt.output(rawfile)
            gLogger.info("output cost time:%d "%((datetime.datetime.now()- lst).microseconds/1000 ))


if __name__ == "__vapoursynth__":
    TestMain.runTest()
    # TestMain.runTestKNLMeansCLDenoisyImag()
    TestMain.runTestKNLMeansCLDenoisyVideo()

else:
    TestMain.runTest()
    # TestMain.runTestKNLMeansCLDenoisyImag()
    TestMain.runTestKNLMeansCLDenoisyVideo()
