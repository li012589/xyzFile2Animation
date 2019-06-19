import numpy as np
import matplotlib.pyplot as plt
import mogli
import gr

import argparse

parser = argparse.ArgumentParser()
parser.add_argument("-xyz",default=None,help="name of the xyz file")
parser.add_argument("-output",default=None,help="name of the output files")
parser.add_argument("-batch",default=100,type=int,help="number of xyz to show")
parser.add_argument("-bond",default=1.2,type=float,help="mogli's bong_param")
args = parser.parse_args()

molecules = mogli.read(args.xyz)

for t in range(args.batch):

    gr.clearws()
    gr.setviewport(0, 0.7, 0, 0.7)
    gr.setwindow(0.1, 0.9, 0.05, 0.85)
    mogli.draw(molecules[t], bonds_param=args.bond, camera=((10, 0, 10),
                                                       (0, 0, 0),
                                                       (0, 1, 0)))

    gr.updatews()
