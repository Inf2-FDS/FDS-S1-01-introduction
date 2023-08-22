# FDS Labs

## Running the labs using Noteable (supported)

These Jupyter notebook labs should work on the University of Edinburgh
[Noteable](https://noteable.edina.ac.uk) Jupyter notebook server, as
described in the course materials.

**Running the labs using Noteable is the recommended way to run these labs.**

## Running the labs from your laptop (not supported)

If you would like to run Jupyter notebooks on your own machine, you
should first install Jupyter:

1. [Install miniconda as described here](https://docs.conda.io/en/latest/miniconda.html)
2. From the command line, cd into this directory
3. From the command line install the correct versions of the Python
   packages you need using conda:
   ```
   conda env create -f environment.yml
   ```

To start Jupyter lab:

1. At a command line, activate the "fds" environment created in the
   installation steps above
   ```
   conda activate fds
   ```

2. Type `jupyter lab`

We don't actively support running Jupyter on your own machine. If you
have problems, we can't promise to help you fix them - the recommended
method is to use Noteable.
