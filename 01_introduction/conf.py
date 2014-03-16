#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Язык программирования Python documentation build configuration file, created by
# sphinx-quickstart on Tue Feb 18 01:11:59 2014.
#
# This file is execfile()d with the current directory set to its
# containing dir.
#
# Note that not all possible configuration values are present in this
# autogenerated file.
#
# All configuration values have a default; values that are commented out
# serve to show the default.

import sys
import os

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
sys.path.insert(0, os.path.abspath('../common/conf/'))

from presentation_common import *

# -- General configuration ------------------------------------------------

# The version info for the project you're documenting, acts as replacement for
# |version| and |release|, also used in various other places throughout the
# built documents.
#
# The short X.Y version.
version = '22.02.2014'
# The full version, including alpha/beta/rc tags.
release = '22.02.2014'

# There are two options for replacing |today|: either, you set today to some
# non-false value, then it is used:
today = '22.02.2014'
# Else, today_fmt is used as the format for a strftime call.
#today_fmt = '%B %d, %Y'

slide_footer = slide_footer_template.format(today)
