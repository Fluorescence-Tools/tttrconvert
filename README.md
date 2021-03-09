# tttrconvert

A ``tttrconvert`` is a tool to convert time-tagged time-resolved files into different formats. ``tttrconvert`` to read 
and write TTTR files ``tttrconvert`` uses ``tttrlib``. The tool ``tttrconvert`` can be embedded 
in other software and is part of ChiSurf.

![tttrconvert GUI][1]

## Building and installation
``tttrconvert`` can be installed from the source code in a python environment that
resolves all necessary dependencies. Alternatively, ``tttrconvert`` can be installed via conda.

### Source
To install ``tttrconvert`` from the source code clone the git repository and run the
setup script.

```commandline
git clone https://gitlab.peulen.xyz/tpeulen/tttrconvert
cd tttrconvert
python setup.py install
```
After installing ``tttrconvert`` you can open the GUI from the commandline.

```commandline
tttrconvert
```

### Conda
``tttrconvert`` depends on common python packages such as ``numpy``. Additionally, ``tttrconvert`` depends on 
``tttrlib``. Thus, to install ``k2dist`` make sure that conda channels that provide packages for the necessary
dependencies are listed in the ``.condarc`` file 

```yaml
channels:
  - tpeulen
  - tpeulen/label/nightly
  - conda-forge
  - defaults
```

To avoid potential conflicts ``tttrconvert`` can be installed in a separate environment. 

```commandline
conda create -n test
conda install tttrconvert
conda activate tttrconvert
tttrconvert
```

# Usage

## Graphical user interface
First, select the input file type. Next, add files to the file list by drag-and-drop. Finally,
select the ouput file format and save/convert the files.

## Note on meta-data
The different TTTR file formats contain and support different meta-data. The meta-data may need to be 
edited separately.


[1]: doc/gui.png "tttrconvert GUI"
