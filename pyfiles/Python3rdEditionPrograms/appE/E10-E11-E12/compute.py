from numpy import sin, linspace, pi
import matplotlib.pyplot as plt
import string
import random
import os
import glob

# our model
def sine_plot(A,B,C):
    fname = "static/" + ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(8)) + ".png"
    x = linspace(0,4*pi,500)
    y = (A * sin(B * x)) + C
    plt.figure()
    plt.plot(x,y)
    plt.title("Sine wave with A=%s, B=%s, C=%s" % (A,B,C))
    if not os.path.isdir('static'):
        os.mkdir('static')
    else:
        # Remove old plot files
        for filename in glob.glob(os.path.join('static', '*.png')):
            os.remove(filename)
    plt.savefig(fname)
    return fname
