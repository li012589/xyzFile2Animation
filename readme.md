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

To generate a video, you can use the `-output` option, e.g.

```bash
python ./main.py -filename "./examples/alanine-dipeptide-3x250ns-heavy-atom-positions.npz" -batch 200 -name arr_0 -smile "CC(=O)NC(C)C(=O)NC" -scaling 1 -fixy 0 -output test2.mov
```

To fix bonds according to SMILES, use `-fix_bond` option.( also requires my version of mogli)

## To generate image with mogli

```bash
python ./draw.py -filename "./interpolation.npz" -batch 201 -step 1 -concat inputs.txt -name arr_0 -smile "CC(=O)NC(C)C(=O)NC" -scaling 1 -fixy 0 -output testdf.png -fix_bond
```

To generate video using generated image files:

```bash
ffmpeg -f concat -safe 0 -i inputs.txt -c:v libx264 -r 30 -pix_fmt yuv420p out.mp4
```

