from anndata import AnnData

from anndata import read as read_h5ad
from anndata import read_csv, read_excel, read_hdf, read_loom, read_mtx, read_text, read_umi_tools

from .. import __version__

from . import load
from . import new_basic_function
from . import read_meth_file
# from ..readwrite import read, read_10x_h5, read_10x_mtx, write, read_params, write_params
# from . import datasets
# from . import export_to
# from . import logging
# from . import queries

from .. import functions  

# unfortunately, we cannot put this here as long as we have simple global
# variables in settings... they couldn't be set in this case...
# the main drawback is that we have to import set_figure_params
# to show in the docs for that reason...
# it would be nice to make the simple data types "properties of the
# module"... putting setters and getters for all of them wouldn't be very nice
from .. import settings
# for now - or maybe as the permanently favored solution - put the single function here
from ..settings import set_figure_params

# some stuff that is not actually documented...
from .. import utils

import sys
utils.annotate_doc_types(sys.modules[__name__], 'scanpy')
del sys


__doc__ = """\
Global API (deprecated)
=======================
.. deprecated:: 1.3.7
   Use the top level module instead: `import scanpy as sc`.
For the deprecated high-level API documented on this page, use `import scanpy.api as sc`.
Preprocessing: PP
------------------
Filtering of highly-variable genes, batch-effect correction, per-cell normalization, preprocessing recipes.
Basic Preprocessing
~~~~~~~~~~~~~~~~~~~
For visual quality control, see :func:`~scanpy.api.pl.highest_expr_gens` and
:func:`~scanpy.api.pl.filter_genes_dispersion` in the :doc:`plotting API
<plotting>`.
.. autosummary::
   :toctree: .
   load.extract_CG
   load.extract_CH
   new_basic_function.write_methlevel