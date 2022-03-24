#!/usr/bin/env python3
import os
from matplotlib import pyplot as plt
import wave
import struct
import array
import numpy as np
from scipy.fft import fft,fftfreq

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
def plot_fft(fft,n):
    (xf,yf) = fft
    fig, ax = plt.subplots() 
    ax.plot(xf, 2.0/n * np.abs(yf[0:n//2]))
    ax.set_xlim(0, 1000)
    plt.grid()
    plt.show()

    return

def find_fundamental(v, md, n):
    
    xf = fftfreq(n, 1/md["framerate"])[:n//2]
    yf = fft(v)
    mbin = np.argmax(np.abs(yf))
    print(mbin, xf[mbin])
    #currently returning error because amplitudes is empty

    return (xf, yf)

standinArg="audiocheck.net_sin_500Hz_-3dBFS_3s.wav"

with wave.open(standinArg,'rb') as wav:
    md=get_meta_data(wav)
    n=22000 #md["framerate"]
    samples=[]

    print(md)
    if(md["channels"]>1):
        print("WARNING: SOFTWARE DOES NOT CURRENTLY SUPPORT STEREO\n")
    while True:
        framebytes=wav.readframes(1)
        if(len(framebytes)==0):
            break
        s=struct.unpack("<h", framebytes)[0]
        samples.append(s)

    f = find_fundamental(samples[:n], md, n)
    plot_fft(f,n)

    #pyplot.plot(samples[:n],'ro')
    #pyplot.show()


