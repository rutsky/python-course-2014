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
version = '15.03.2014'
# The full version, including alpha/beta/rc tags.
release = '15.03.2014'

# There are two options for replacing |today|: either, you set today to some
# non-false value, then it is used:
today = '15.03.2014'
# Else, today_fmt is used as the format for a strftime call.
#today_fmt = '%B %d, %Y'


# Place custom static assets in the _static directory and uncomment
# the following lines to include them

slide_footer = '<div class="left">15.03.2014</div>' \
    '<div class="center"><a href="http://school30.spb.ru/">ФМЛ № 30</a>. Владимир Владимирович Руцкий</div>'
