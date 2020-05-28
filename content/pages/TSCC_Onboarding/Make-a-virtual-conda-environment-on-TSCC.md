# Make a virtual conda environment on TSCC

**Authors**: Clarence Mah, Brian Yee<br>
**Last Updated**: 5-07-20


If you need to install or run a particular software, you've got two options:

1. Run a systemwide copy via modules
2. Install it yourself (typically straightforward with conda).

## Installing software yourself with conda environments

**WARNING** - this is easy to get messed up. While this is a nice tool, it is not absolutely necessary upon initial setup and might be best to wait and configure environments after you have a better understanding of how they work.

On TSCC, the easiest way to create a virtual environment is by making one via conda. Here’s how you do it (replace `myenv` with the name of your choice, and `python=3.6 samtools` with the packages (space-delimited) you want to install):

```
conda create --name myenv python=3.6 samtools
```

The previous command shows how you can specify (or not) the version you want to have installed in a particular environment. In this case, we want python3.6 and the latest compatible samtools version in this environment.

**Note:** You can also create an environment using `conda` to install all the Anaconda Python packages, and then using `pip` in the environment to install the remaining packages, like so:

```
conda create --yes --name ENVIRONMENT_NAME pip numpy scipy cython matplotlib nose six scikit-learn jupyter networkx pandas tornado statsmodels setuptools pytest pyzmq jinja2 pyyaml pymongo biopython markupsafe seaborn joblib semantic_version
source activate ENVIRONMENT_NAME
conda install --yes --channel https://conda.binstar.org/daler pybedtools
conda install --yes --channel https://conda.binstar.org/kyleabeauchamp fastcluster
pip install gspread brewer2mpl husl gffutils matplotlib-venn HTSeq misopy
pip install https://github.com/YeoLab/clipper/tarball/master
pip install https://github.com/YeoLab/gscripts/tarball/master
pip install https://github.com/YeoLab/flotilla/tarball/master
```

These commands is how the `base` environment was created.

Then activate your environment with:

```
source activate $USER
```

You’ll probably stay in this environment all the time.

## Warning:

Make sure to add `source activate $USER` to your `~/.bashrc` file! Then you will always be in your environment

If you need to switch to another environment, then exit your environment with:

```
source deactivate
```
