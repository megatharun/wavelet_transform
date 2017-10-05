
''' 
Copyright (c) 2017, Megat Harun Al Rashid bin Megat Ahmad, Suhairy bin Sani and Shukri bin Mohd.
All rights reserved.
Redistribution and use in source and binary forms, with or without modification, are permitted
provided that the following conditions are met:
1.  Redistributions of source code must retain the above copyright notice, this list of conditions
    and the following disclaimer.
2. Redistributions in binary form must reproduce the above copyright notice, this list of conditions
    and the following disclaimer in the documentation and/or other materials provided with the distribution.
3. Neither the name of the copyright holder nor the names of its contributors may be used to endorse
    or promote products derived from this software without specific prior written permission.
THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND
ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE DISCLAIMED.
IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT,
INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING,
BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE,
DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY
OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE
OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED
OF THE POSSIBILITY OF SUCH DAMAGE.
'''

import numpy as np

import matplotlib.pyplot as plt
import matplotlib.cm as cm

# WT.py for displaying wavelet transformation

class WT_Display(object):
    
    def __init__(wtd,filename):
        
        # Extracting data from file
        fh = open(filename)
        wtd.fhList = open(filename).readlines()
        fh.close()
        wtd.freq = np.array(wtd.fhList[2:][0].split(',')[1:]).astype(np.float)
        
        data = []
        for i,j in enumerate(wtd.fhList[2:][1:]):
            data = data + [j.split(',')]
            
        data = np.array(data).astype(np.float)
        
        wtd.T = data.T[0]
        
        wtd.data2 = np.repeat(data[:,1:], 10).reshape(1000,1000).T
    
    # Display image
    def imageView(wtd,imageFile = 'obj_ort_test.jpeg', intPol = 'spline36',\
                 colorMap = cm.gist_rainbow_r):
        
        fig, ax = plt.subplots()

        cax = ax.imshow(wtd.data2, interpolation=intPol, cmap=colorMap)

        ax.set_ylim(ymin=0,ymax=1000)
        ax.set_xticklabels([0,0,20,40,60,80,100])
        ax.set_xlabel(r'Time,[$\mu$s]')
        ax.set_ylabel(r'Frequency, [kHz]')
        cbar = fig.colorbar(cax)
        
        plt.savefig(imageFile)

        plt.show()