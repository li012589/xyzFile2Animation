import numpy as np

import argparse

parser = argparse.ArgumentParser()
parser.add_argument("-prefix",default=None,help="prefix to add to all pathes")
parser.add_argument("-n",default=3,type=int,help="number of npy files to process")
parser.add_argument("-filename",default="saving.npz",help="name of npz file to save")
args = parser.parse_args()

n = args.n
filename = args.filename
prefix=args.prefix
if prefix is None:
    raise AssertionError("No prefix specified")

with open(prefix+".pdb","r") as text:
    lines = [l for l in text]
    lines = lines[1:-1]
No = []
Atom = []

for i in lines:
    if i.split()[-1] is not 'H':
        No.append(i.split()[1])
        Atom.append(i.split()[-1])

#lst = [(No[i],Atom[i]) for i in range(len(No))]
#print(lst)

smile = "".join(Atom)
print(smile)
no = np.array(No,dtype=np.int)

names = [prefix+"-"+str(i).zfill(3)+".npy" for i in range(n)]

datalist = []
for name in names:
    data = np.load(name)[:,no,:]
    datalist.append(data)
ret = np.concatenate(datalist,axis=0)
ret = ret.reshape(ret.shape[0],-1)
np.savez(filename,ret)


