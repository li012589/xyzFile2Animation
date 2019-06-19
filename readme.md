# xyzFile2Animation

A small python script to create video out of xyz file.

## examples

```bash
python ./main.py -xyz "./examples/alanine-dipeptide-3x250ns-heavy-atom-positions.xyz" -batch 200
```

Note that to create a `mov` file, run this before the above line in your terminal: `export GKS_WSTYPE=mov`.