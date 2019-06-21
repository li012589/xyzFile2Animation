import numpy as np
import matplotlib.pyplot as plt
import mogli
import gr
import os

import argparse

parser = argparse.ArgumentParser()
parser.add_argument("-filename",default=None,help="name of the data file")
parser.add_argument("-output",default=None,help="name of the output files")
parser.add_argument("-batch",default=100,type=int,help="number of time steps to show")
parser.add_argument("-bond",default=1.2,type=float,help="mogli's bong_param")
parser.add_argument("-name",default=None,help = 'name of the data saved in npz file')
parser.add_argument("-smile",default=None,help = "Smile expression of the molecule")
parser.add_argument("-scaling",default=10,type=float,help = "scaling factor of npz data, default is for nm to ångströms")
parser.add_argument("-fixx",default=0,type=float,help="fix x axis")
parser.add_argument("-fixy",default=23.222,type=float,help="fix y axis")
parser.add_argument("-fixz",default=0,type=float,help="fix z axis")
args = parser.parse_args()

if args.output is not None:
    os.environ["GKS_WSTYPE"] = args.output[-3:]
    os.environ["GKS_FILEPATH"] = args.output

if args.filename.endswith('.xyz'):
    molecules = mogli.read(args.filename)
elif args.filename.endswith('.npz'):
    fixs = np.array([args.fixx,args.fixy,args.fixz])
    molecules = mogli.load(args.filename,args.name,args.smile,args.scaling,fixs)

for t in range(args.batch):

    gr.clearws()
    gr.setviewport(0, 0.7, 0, 0.7)
    gr.setwindow(0.1, 0.9, 0.05, 0.85)
    mogli.draw(molecules[t], bonds_param=args.bond, camera=((10, 0, 10),
                                                       (0, 0, 0),
                                                       (0, 1, 0)))

    gr.updatews()
