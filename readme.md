# xyzFile2Animation

A small python script to create video out of xyz file.

## examples

```bash
python ./main.py -xyz "./examples/alanine-dipeptide-3x250ns-heavy-atom-positions.xyz" -batch 200
```

Note that to create a `mov` file, run this before the above line in your terminal: `export GKS_WSTYPE=mov`.

Or, using a `npz` file, note that to use this you have to use my tweaked version of  [mogli](https://github.com/li012589/mogli).

```bash
python ./main.py -filename "./examples/alanine-dipeptide-3x250ns-heavy-atom-positions.npz" -batch 200 -name arr_0 -smile "CC(=O)NC(C)C(=O)NC" -scaling 10 -fixy 23.222
```

