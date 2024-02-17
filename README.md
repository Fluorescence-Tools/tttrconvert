# tttrconvert

A ``tttrconvert`` is a very basic tool to convert time-tagged time-resolved files into different formats. ``tttrconvert`` to read 
and write TTTR files ``tttrconvert`` uses ``tttrlib``. The tool ``tttrconvert`` can be embedded 
in other software and is part of ChiSurf.

Currently, the tool has only very basic functions (it is probably not
what you want).

![tttrconvert GUI][1]

## Building and installation
``tttrconvert`` can be installed from the source code in a python environment that
resolves all necessary dependencies. Alternatively, ``tttrconvert`` can be installed via conda.

### Source
To install ``tttrconvert`` from the source code clone the git repository and run the
setup script.

```commandline
git clone https://github.com/fluorescence-tools/tttrconvert
cd tttrconvert
python setup.py install
```
After installing ``tttrconvert`` you can open the GUI from the commandline.

```commandline
tttrconvert
```

### Conda
`tttrconvert` can be installed using conda, best in a separate
environment

```bash
conda create tttrconvert
mamba install tttrconvert -c tpeulen
```

To us the tool activate the tttrconvert environment and start the tool
from the command line.
```bash
conda activate tttrconvert
tttrconvert
```

# Usage

## Graphical user interface
First, select the input file type. Next, add files to the file list by drag-and-drop. Finally,
select the output file format and save/convert the files.


[1]: doc/gui.png "tttrconvert GUI"
