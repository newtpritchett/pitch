#!/usr/bin/env python3
import os
from matplotlib import pyplot
import wave
import struct
import numpy as np

def get_meta_data(wav):
    nchannels, sampwidth, framerate, nframes, comptype, compname =  wav.getparams()

    meta_data = {
            "channels":nchannels,
            "samplewidth":sampwidth,
            "framerate":framerate,
            "nframes":nframes,
            "comptype":comptype,
            "compname":compname
            }

    return meta_data

standinArg="audiocheck.net_sin_500Hz_-3dBFS_3s.wav"

with wave.open(standinArg,'rb') as wav:
    md=get_meta_data(wav)
    n=md["framerate"]//500
    samples=[]
    if(md["channels"]>1):
        print("WARNING: SOFTWARE DOES NOT CURRENTLY SUPPORT STEREO\n")
    while True:
        framebytes=wav.readframes(1)
        if(len(framebytes)==0):
            break
        s=struct.unpack("<h", framebytes)[0]
        samples.append(s)

    pyplot.plot(samples[:n],'ro')
    pyplot.show()


