
# -*- coding: utf-8 -*-

import sys, os, time
# import cv2, numpy
import logging
import vapoursynth as vs
# import  vs_macro
from vapoursynth import core

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


class MainRun():
    _curDir = os.getcwd()
    _tarDir = os.path.dirname(os.path.dirname(_curDir))
    _img = os.path.join(_tarDir, u"ShareMedia/Images/girl720p.png")
    # _video = core.ffms2.Source(source=r"e:\\media\\stand.mp4")
    # _vFile  = r"e:\\media\\stand.mp4"
    # _vFile1  = r"E:\media\noisy\dance82_output_0.mp4"
    _vFile1  = r"E:\media\noisy\noisy_files\pc3\1-1001.mp4"
    _noiseFile  = os.path.join(os.getcwd(),"image/my.bmp")

    @classmethod
    def runTest(cls):
        gLogger.info(u"hello world")

    @classmethod
    def runVapourSynthVer(cls):
        gLogger.info(core.version())

    @classmethod
    def runConvertRGB24(cls):
        # video = core.std.Transpose(cls._video)
        # video.set_output()
        enable_v210 = True


    @classmethod
    def runDenoisy(cls):
        import mvsfunc as mvf
        lNoiseFile  = r"E:\media\noisy\image\pureNoise.jpg"
        lVSrc = core.ffms2.Source(source=lNoiseFile)
        flt = mvf.BM3D(lVSrc, sigma=3.0, profile1="fast")
        # lVSrc = core.text.Text(lVSrc,["src"])
        flt = core.text.Text(flt,["dst"])
        # dst= core.std.StackHorizontal((lVSrc,flt))
        # dst.set_output()
        flt.set_output()
        enable_v210 = True
        gLogger.info(type(lVSrc))

    @classmethod
    def runKNLMeansCLDenoisy(cls):
        import mvsfunc as mvf
        import  havsfunc
        lVSrc = core.ffms2.Source(source=cls._vFile1)
        flt = havsfunc.KNLMeansCL(lVSrc,2,3,4,5)
        lVSrc = core.text.Text(lVSrc, ["src"])
        flt = core.text.Text(flt, ["dst"])
        dst = core.std.StackHorizontal((lVSrc, flt))
        dst.set_output()
        enable_v210 = True
        gLogger.info(type(lVSrc))

    @classmethod
    def runSaveVideoNode(cls):
        import mvsfunc as mvf
        import  havsfunc
        lVSrc = core.ffms2.Source(source=cls._vFile1)
        # flt = havsfunc.KNLMeansCL(lVSrc,2,3,4,1.8)
        gLogger.info(lVSrc.format)
        with open("vsraw.yuv","wb") as rawfile:
            lVSrc.output(rawfile)

    @classmethod
    def runKNLMeansCLDenoisyImage(cls):
        import mvsfunc as mvf
        import havsfunc
        lVSrc = core.ffms2.Source(source=cls._noiseFile)
        flt = havsfunc.KNLMeansCL(lVSrc, 1, 3, 3, 3)
        lVSrc = core.text.Text(lVSrc, ["src"])
        flt = core.text.Text(flt, ["dst"])
        dst = core.std.StackVertical((lVSrc, flt))
        # dst.set_output()
        gLogger.info(lVSrc)
        with open("vsraw-image.yuv", "wb") as rawfile:
            dst.output(rawfile)
        enable_v210 = True
        gLogger.info(type(lVSrc))


    @classmethod
    def runDiffDenoisyImage(cls):
        import mvsfunc as mvf
        import havsfunc
        lVSrc = core.ffms2.Source(source=cls._noiseFile)
        # flt = havsfunc.KNLMeansCL(lVSrc, 1, 3, 3, 3)
        flt = mvf.BM3D(lVSrc, sigma=[25,25,25], profile1="fast")

        lVSrc = core.text.Text(lVSrc, ["src"])
        flt = core.text.Text(flt, ["dst"])
        dst = core.std.StackVertical((lVSrc, flt))
        # dst.set_output()
        gLogger.info(lVSrc)
        with open("vsraw-pureFile", "wb") as rawfile:
            flt.output(rawfile)
        enable_v210 = True

    @classmethod
    def runRGBDenoise(cls):
        import mvsfunc as mvf
        import havsfunc
        lVSrc = core.ffms2.Source(source=cls._noiseFile)

        # flt = mvf.ToRGB(lVSrc,depth=8)
        flt = core.resize.Bicubic(clip=lVSrc, width=1536, height=864, format=vs.RGB24)

        gLogger.info(flt)
        gLogger.info(lVSrc)
        with open("vsraw-first.yuv", "wb") as rawfile:
            flt.output(rawfile)
        flt.set_output()

    @classmethod
    def runSMDenoise(cls):
        import mvsfunc as mvf
        import havsfunc
        lVSrc = core.ffms2.Source(source=cls._noiseFile)
        flt = mvf.ToRGB(lVSrc,depth=8)
        flt = havsfunc.SMDegrain(lVSrc,tr=2,thSAD=250,contrasharp=True,RefineMotion=True)

        gLogger.info(flt)
        gLogger.info(lVSrc)
        with open("vsraw-first-SMD.rgb", "wb") as rawfile:
            flt.output(rawfile)
        flt.set_output()


    @classmethod
    def runAntialiasing(cls):
        pass

    @classmethod
    def runImageStable(cls):
        pass

    @classmethod
    def runInsertFrame(cls):
        pass


    @classmethod
    def runVpType(cls):
        import mvsfunc as mvf
        lVSrc = core.ffms2.Source(source=cls._vFile1)
        gLogger.info(type(lVSrc[0]))




if __name__ == "__vapoursynth__":
    # MainRun.runTest()
    # MainRun.runConvertRGB24()
    # MainRun.runVapourSynthVer()
    # MainRun.runDenoisy()
    # MainRun.runKNLMeansCLDenoisy()
    # MainRun.runKNLMeansCLDenoisyImage()
    # MainRun.runDiffDenoisyImage()
    MainRun.runKNLMeansCLDenoisyImage()

else:
    # MainRun.runTest()
    # MainRun.runConvertRGB24()
    # MainRun.runVapourSynthVer()
    # MainRun.runDenoisy()
    # MainRun.runVpType()
    # MainRun.runSaveVideoNode()
    # MainRun.runKNLMeansCLDenoisy()
    # MainRun.runDiffDenoisyImage()
    # MainRun.runRGBDenoise()
    MainRun.runKNLMeansCLDenoisyImage()