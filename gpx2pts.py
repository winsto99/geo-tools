# gpx2pts.py
# Extracts geographic points from a gpx file
# Brendan Hasz
# winsto99@gmail.com

import string as s
import sys
import matplotlib.pyplot as plt
import numpy as np

def gpx2pts(fname):
    '''
    Given a filename for a gpx file, this function returns a list of
    3d points from the kml file
    '''
    pts = []
    with open(fname, 'r') as f:
        while True: #while we're not yet at end of file
            l = f.readline()  #read a new line
            if not l: break  #if we've reached EOF, quit

            # If this is the start of a coords BLOCK (don't include single pts)
            if s.find(l,'<trkpt')!=-1: #if this is a trkpt line
                p = l.split('\"'); #parse the line
                pts.append([float(p[1]), float(p[3])])  #parse this line + save

    return pts 


# TESTER
fname_IN = sys.argv[1]
print "Extracting points from "+fname_IN
pts = np.array(gpx2pts(fname_IN))
print "Done!"

# TEST BY PLOTTING
x = pts[:,0]
y = pts[:,1]
fig = plt.figure()
ax = fig.add_subplot(111)
ax.plot(x, y)
ax.set_aspect('equal')
plt.title('A gpx path')
plt.show()
