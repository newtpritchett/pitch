#!/usr/bin/env python3
import os
from matplotlib import pyplot
import wave
import struct
import array
import numpy as np
from scipy import fftpack
from scipy import signal

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

def find_fundamental(v, md, nbins):
    sig_fft = fftpack.fft(v, n = nbins)
    power = abs(sig_fft)**2
    (peaks,amplitudes) = signal.find_peaks(power)
    print(max(amplitudes))
    #currently returning error because amplitudes is empty
    return peaks

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

    f = find_fundamental(samples, md, md["framerate"])

    #pyplot.plot(samples[:n],'ro')
    #pyplot.show()


