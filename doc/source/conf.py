# -*- coding: utf-8 -*-
#
# polar2grid documentation build configuration file, created by
# sphinx-quickstart on Thu Apr 19 23:17:38 2012.
#
# This file is execfile()d with the current directory set to its containing dir.
#
# Note that not all possible configuration values are present in this
# autogenerated file.
#
# All configuration values have a default; values that are commented out
# serve to show the default.

import os
import sys
import urllib.request
import ftplib
from shutil import copyfileobj
from datetime import datetime

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#sys.path.insert(0, os.path.abspath('.'))
print("Adding the following directories to PYTHONPATH:")
BASE_PATH = "../../../"
for dirname in [x for x in os.listdir(BASE_PATH) if os.path.isdir(os.path.join(BASE_PATH, x)) and x.startswith("polar2grid")]:
    print("\t ", os.path.realpath(os.path.join(BASE_PATH, dirname)))
    sys.path.insert(0, os.path.abspath(os.path.join(BASE_PATH, dirname)))
sys.path.append(os.path.abspath(os.path.dirname(__file__)))

# Handle building documentation for polar2grid or geo2grid
is_geo2grid = 'geo' in os.getenv('POLAR2GRID_DOC', 'polar').lower()

# Hack to download example images instead of storing them in git
images = (
    "https://bin.ssec.wisc.edu/pub/CSPP/p2g_v_2_1_examples/amsr2/images_basic/gcom-w1_amsr2_btemp_36.5h_20160719_190300_wgs84_fit.jpg",
    "https://bin.ssec.wisc.edu/pub/CSPP/p2g_v_2_1_examples/amsr2/images_nrl/gcom-w1_amsr2_btemp_89.0ah_20160719_190300_lcc_fit.jpg",
    "https://bin.ssec.wisc.edu/pub/CSPP/p2g_v_2_1_examples/amsr2/images_nrl/gcom-w1_amsr2_btemp_89.0ah_20160719_190300_lcc_fit.basic_overlay_example.png",
    "https://bin.ssec.wisc.edu/pub/CSPP/p2g_v_2_1_examples/amsr2/images_nrl/gcom-w1_amsr2_btemp_89.0ah_20160719_190300_lcc_fit.advanced_overlay.png",
    "https://bin.ssec.wisc.edu/pub/CSPP/p2g_v_2_1_examples/viirs/overlay/npp_viirs_true_color_20170305_193251_lcc_fit_overlay.png",
    "https://bin.ssec.wisc.edu/pub/CSPP/p2g_v_2_1_examples/viirs/images_basic/npp_viirs_true_color_20170305_193251_lcc_fit.jpg",
    "https://bin.ssec.wisc.edu/pub/CSPP/p2g_v_2_1_examples/viirs/dnb/VIIRS_DNB_Enhancement_Comparison.png",
    "https://bin.ssec.wisc.edu/pub/CSPP/p2g_v_2_1_examples/viirs/images_basic/npp_viirs_true_color_20170319_183246_miami.jpg",
    "https://bin.ssec.wisc.edu/pub/CSPP/p2g_v_2_1_examples/modis/images_basic/terra_modis_false_color_20170319_163000_miami.jpg",
    "https://bin.ssec.wisc.edu/pub/CSPP/p2g_v_2_1_examples/modis/awips/SSEC_AWIPS_aqua_modis_bt28_211e_20170308_181800.nc.png",
    "https://bin.ssec.wisc.edu/pub/CSPP/p2g_v_2_1_examples/modis/awips/SSEC_AWIPS_aqua_modis_vis02_211e_20170308_181800.nc.png",
    "https://bin.ssec.wisc.edu/pub/CSPP/p2g_v_2_1_examples/amsr2/images_nrl/gcom-w1_amsr2_btemp_89.0ah_20160719_190300_lcc_fit_color.jpg",
    "https://bin.ssec.wisc.edu/pub/CSPP/p2g_v_2_1_examples/viirs/merge/VIIRS_False_Color_Side_by_Side_Example_P2G.png",
    "https://bin.ssec.wisc.edu/pub/CSPP/p2g_v_2_1_examples/viirs/overlay/VIIRS_true_color_in_google_earth.jpg",
    "https://bin.ssec.wisc.edu/pub/CSPP/p2g_v_2_1_examples/viirs/merge/my_false_color.jpg",
    "https://bin.ssec.wisc.edu/pub/CSPP/p2g_v_2_1_examples/modis/awips/modis_true_color_awips_20170308_1818.png",
    "https://www.ssec.wisc.edu/~davidh/polar2grid/scmi_grids/scmi_grid_LCC.png",
    "https://www.ssec.wisc.edu/~davidh/polar2grid/scmi_grids/scmi_grid_Mercator.png",
    "https://www.ssec.wisc.edu/~davidh/polar2grid/scmi_grids/scmi_grid_Pacific.png",
    "https://www.ssec.wisc.edu/~davidh/polar2grid/scmi_grids/scmi_grid_Polar.png",
    "https://www.ssec.wisc.edu/~davidh/polar2grid/scmi_grids/scmi_grid_GOES_EAST.png",
    "https://www.ssec.wisc.edu/~davidh/polar2grid/scmi_grids/scmi_grid_GOES_STORE.png",
    "https://www.ssec.wisc.edu/~davidh/polar2grid/scmi_grids/scmi_grid_GOES_TEST.png",
    "https://www.ssec.wisc.edu/~davidh/polar2grid/scmi_grids/scmi_grid_GOES_WEST.png",
    "https://bin.ssec.wisc.edu/pub/CSPP/p2g_v_2_1_examples/viirs/dnb/HNCC_DNB_Band_Example.png",
    "https://bin.ssec.wisc.edu/pub/CSPP/p2g_v_2_1_examples/modis/awips/modis_true_color_example.png",
    "https://bin.ssec.wisc.edu/pub/CSPP/p2g_v_2_1_examples/modis/awips/modis_vis02_example.png",
    "https://bin.ssec.wisc.edu/pub/CSPP/p2g_v_2_1_examples/acspo/VIIRS_M16_ACSPO_SST_composite_example.png",
    "https://bin.ssec.wisc.edu/pub/CSPP/p2g_v_2_1_examples/acspo/npp_viirs_sst_20191216_072134_acspo_sst.png",
    "https://bin.ssec.wisc.edu/pub/CSPP/p2g_v_2_1_examples/acspo/npp_viirs_sst_20191216_072134_acspo_sst_wcolor.png",
    "https://bin.ssec.wisc.edu/pub/CSPP/p2g_v_2_1_examples/acspo/npp_viirs_sst_20191216_072134_acspo_sst_rescaled_wcolor.png",
    "https://bin.ssec.wisc.edu/pub/CSPP/p2g_v_2_1_examples/acspo/npp_viirs_sst_20191216_072134_acspo_sst_rescaled_wcolor_colortable_resize.png",
    "https://bin.ssec.wisc.edu/pub/CSPP/p2g_v_2_1_examples/acspo/npp_viirs_sst_20191216_072134_acspo_sst_final_resize.png",
    "https://bin.ssec.wisc.edu/pub/CSPP/g2g_examples/ahi/HIMAWARI-8_AHI_true_color_20181112_233020_perth_example.png",
    "https://bin.ssec.wisc.edu/pub/CSPP/g2g_examples/ahi/HIMAWARI-8_AHI_true_color_20181112_233020_perth.png",
    "https://bin.ssec.wisc.edu/pub/CSPP/g2g_examples/abi/abi_20181219_1745_montage.jpg",
    "https://bin.ssec.wisc.edu/pub/CSPP/g2g_examples/abi/GOES-16_ABI_RadC_natural_color_20181219_174215_GOES-East.png",
    "https://bin.ssec.wisc.edu/pub/CSPP/g2g_examples/abi/GOES-16_ABI_RadC_true_color_20190104_195718_GOES-East.png",
    "https://bin.ssec.wisc.edu/pub/CSPP/g2g_examples/abi/GOES-16_ABI_RadF_true_color_night_20181112_123034_GOES-East.jpg",
    "https://bin.ssec.wisc.edu/pub/CSPP/g2g_examples/abi/GOES-16_ABI_RadF_true_color_night_20181112_123034_GOES-East_new.png",
    "https://bin.ssec.wisc.edu/pub/CSPP/g2g_examples/abi/GOES-16_ABI_RadF_true_color_night_microphysics_20181112_123034_GOES-East.jpg",
    "https://bin.ssec.wisc.edu/pub/CSPP/g2g_examples/abi/GOES-16_ABI_RadF_true_color_night_microphysics_20181112_123034_GOES-East_new.png",
    "https://bin.ssec.wisc.edu/pub/CSPP/g2g_examples/abi/my_goes16_abi_naturalcolor.png",
)
script_path = os.path.dirname(os.path.realpath(__file__))
image_dst = os.path.join(script_path, '_static', 'example_images')
os.makedirs(image_dst, exist_ok=True)

for image_url in images:
    image_fn = os.path.basename(image_url)
    image_pathname = os.path.join(image_dst, image_fn)
    if os.path.isfile(image_pathname):
        continue
    elif image_url.startswith('http://') or image_url.startswith('https://'):  # or image_url.startswith('ftp://'):
        print("Downloading example image: {}".format(image_url))
        with urllib.request.urlopen(image_url) as remote_img, open(image_pathname, 'wb') as local_img:
            copyfileobj(remote_img, local_img)
    elif image_url.startswith('ftp://'):
        print("Downloading example image: {}".format(image_url))
        parts = image_url.split("/")
        server = parts[2]
        ftp_fn = "/".join(parts[3:])
        ftp = ftplib.FTP(server, user='ftp')  # hope for anonymous
        out_file = open(image_pathname, 'wb')
        ftp.retrbinary('RETR {}'.format(ftp_fn), out_file.write)
    else:
        raise ValueError("Not sure how to download image: {}".format(image_url))

# -- Customize setup -----------------------------------------------------------


def setup(app):
    app.add_stylesheet('prettytables.css')
    app.add_config_value('is_geo2grid', is_geo2grid, 'env')

# -- General configuration -----------------------------------------------------
rst_epilog = """
.. |ssec| replace:: :abbr:`SSEC (Space Science and Engineering Center)`
.. |cspp| replace:: :abbr:`CSPP (Community Satellite Processing Package)`
.. |viirs| replace:: :abbr:`VIIRS (Visible/Infrared Imager Radiometer Suite)`
.. |default_grid_config| replace:: "grids.conf"
"""

# If your documentation needs a minimal Sphinx version, state it here.
#needs_sphinx = '1.0'

# Add any Sphinx extension module names here, as strings. They can be extensions
# coming with Sphinx (named 'sphinx.ext.*') or your custom ones.
extensions = ['sphinx.ext.autodoc', 'sphinx.ext.graphviz', 'sphinx.ext.todo', 'sphinx.ext.coverage',
              'sphinx.ext.imgmath', 'sphinx.ext.intersphinx', 'sphinx.ext.napoleon',
              'sphinx.ext.ifconfig', 'sphinx.ext.viewcode', 'sphinxarg.ext',
              'doi_role', 'toctree_filter']

numfig = True

# graphviz_dot = 'dot'

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# The suffix of source filenames.
source_suffix = '.rst'

# The encoding of source files.
#source_encoding = 'utf-8-sig'

# The master toctree document.
master_doc = 'index'

# General information about the project.
if is_geo2grid:
    project = u'Geo2Grid'
    version = '1.0.2'
    release = '1.0.2'
else:
    project = u'Polar2Grid'

    # The version info for the project you're documenting, acts as replacement for
    # |version| and |release|, also used in various other places throughout the
    # built documents.
    #
    # The short X.Y version.
    version = '2.3'

    # The full version, including alpha/beta/rc tags.
    release = '2.3'

rst_epilog += """
.. |project| replace:: {}
.. |script| replace:: {}.sh
.. |script_literal| replace:: ``{}.sh``
.. |project_env| replace:: ${}_HOME
.. |cspp_abbr| replace:: {}
.. |cspp_title| replace:: {}
""".format(project, project.lower(), project.lower(), project.upper(),
           'CSPP Geo' if is_geo2grid else 'CSPP LEO',
           'CSPP for Geostationary Satellites' if is_geo2grid else 'CSPP for Low Earth Orbiter Satellites',
           )

# Custom TOCTree filtering
toc_filter_exclude = ['polar2grid'] if is_geo2grid else ['geo2grid']

copyright = u'2012-{:%Y}, University of Wisconsin SSEC'.format(datetime.utcnow())

# The language for content autogenerated by Sphinx. Refer to documentation
# for a list of supported languages.
#language = None

# There are two options for replacing |today|: either, you set today to some
# non-false value, then it is used:
#today = ''
# Else, today_fmt is used as the format for a strftime call.
#today_fmt = '%B %d, %Y'

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
exclude_patterns = [
    "glue_scripts/common_opts.rst"
    ]

# The reST default role (used for this markup: `text`) to use for all documents.
#default_role = None

# If true, '()' will be appended to :func: etc. cross-reference text.
#add_function_parentheses = True

# If true, the current module name will be prepended to all description
# unit titles (such as .. function::).
#add_module_names = True

# If true, sectionauthor and moduleauthor directives will be shown in the
# output. They are ignored by default.
#show_authors = False

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = 'sphinx'

# A list of ignored prefixes for module index sorting.
#modindex_common_prefix = []


# -- Options for HTML output ---------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
html_theme = 'alabaster'

# Theme options are theme-specific and customize the look and feel of a theme
# further.  For a list of options available for each theme, see the
# documentation.
#html_theme_options = {}

# Add any paths that contain custom themes here, relative to this directory.
#html_theme_path = []

# The name for this set of Sphinx documents.  If None, it defaults to
# "<project> v<release> documentation".
#html_title = None

# A shorter title for the navigation bar.  Default is the same as html_title.
#html_short_title = None

# The name of an image file (relative to this directory) to place at the top
# of the sidebar.
html_logo = "_static/SSEC_logo_small24.png"

# The name of an image file (within the static path) to use as favicon of the
# docs.  This file should be a Windows icon file (.ico) being 16x16 or 32x32
# pixels large.
html_favicon = "_static/favicon.ico"

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']

# If not '', a 'Last updated on:' timestamp is inserted at every page bottom,
# using the given strftime format.
html_last_updated_fmt = '%b %d, %Y'

# If true, SmartyPants will be used to convert quotes and dashes to
# typographically correct entities.
html_use_smartypants = False

# Custom sidebar templates, maps document names to template names.
#html_sidebars = {}

# Additional templates that should be rendered to pages, maps page names to
# template names.
#html_additional_pages = {}

# If false, no module index is generated.
#html_domain_indices = True

# If false, no index is generated.
#html_use_index = True

# If true, the index is split into individual pages for each letter.
#html_split_index = False

# If true, links to the reST sources are added to the pages.
#html_show_sourcelink = True

# If true, "Created using Sphinx" is shown in the HTML footer. Default is True.
#html_show_sphinx = True

# If true, "(C) Copyright ..." is shown in the HTML footer. Default is True.
#html_show_copyright = True

# If true, an OpenSearch description file will be output, and all pages will
# contain a <link> tag referring to it.  The value of this option must be the
# base URL from which the finished HTML is served.
#html_use_opensearch = ''

# This is the file name suffix for HTML files (e.g. ".xhtml").
#html_file_suffix = None

# Output file base name for HTML help builder.
htmlhelp_basename = project.lower() + 'doc'


# -- Options for LaTeX output --------------------------------------------------

latex_elements = {
# The paper size ('letterpaper' or 'a4paper').
#'papersize': 'letterpaper',

# The font size ('10pt', '11pt' or '12pt').
#'pointsize': '10pt',

# Additional stuff for the LaTeX preamble.
    'preamble': r"""
\setcounter{tocdepth}{1}
\usepackage{pdflscape}

\def\ttl@save@mkschap #1{\vspace *{-20\p@ }{\parindent \z@ \raggedright
    \normalfont \interlinepenalty \@M \DOTIS {#1} \vskip -20\p@ }}
\makeatother

""",
    'classoptions': ',openany,oneside',
    'babel': '\\usepackage[english]{babel}',
    'printindex': '',
}

# new
"""
\renewcommand{\maketitle}{%
  \let\spx@tempa\relax
  \ifHy@pageanchor\def\spx@tempa{\Hy@pageanchortrue}\fi
  \hypersetup{pageanchor=false}% avoid duplicate destination warnings
  \begin{titlepage}%
    \let\footnotesize\small
    \let\footnoterule\relax
    \noindent\rule{\textwidth}{1pt}\par
      \begingroup % for PDF information dictionary
       \def\endgraf{ }\def\and{\& }%
       \pdfstringdefDisableCommands{\def\\{, }}% overwrite hyperref setup
       \hypersetup{pdfauthor={\@author}, pdftitle={\@title}}%
      \endgroup
    \begin{flushright}%
      \sphinxlogo
      \py@HeaderFamily
      {\Huge \@title \par}
      {\itshape\LARGE \py@release\releaseinfo \par}
      \vfill
      {\LARGE
        \begin{tabular}[t]{c}
          \@author
        \end{tabular}
        \par}
      \vfill\vfill
      {\large
       \@date \par
       \vfill
       \py@authoraddress \par
      }%
    \end{flushright}%\par
    \@thanks
  \end{titlepage}%
  \setcounter{footnote}{0}%
  \let\thanks\relax\let\maketitle\relax
  %\gdef\@thanks{}\gdef\@author{}\gdef\@title{}
  \if@openright\cleardoublepage\else\clearpage\fi
  \spx@tempa
}
"""



"""

% Change the title page to look a bit better, and fit in with the fncychap
% ``Bjarne'' style a bit better.
%
\makeatletter
\renewcommand{\maketitle}{%
  \let\spx@tempa\relax
  \ifHy@pageanchor\def\spx@tempa{\Hy@pageanchortrue}\fi
  \hypersetup{pageanchor=false}% avoid duplicate destination warnings
  \begin{titlepage}%
    \let\footnotesize\small
    \let\footnoterule\relax
    \noindent\rule{\textwidth}{1pt}\ifsphinxpdfoutput\newline\null\fi\par
    \ifsphinxpdfoutput
      \begingroup
      % These \defs are required to deal with multi-line authors; it
      % changes \\ to ', ' (comma-space), making it pass muster for
      % generating document info in the PDF file.
      \def\\{, }%
      \def\and{and }%
      \pdfinfo{
        /Author (\@author)
        /Title (\@title)
      }%
      \endgroup
    \fi
    \begin{flushright}%
      \sphinxlogo
      \py@HeaderFamily
      {\Huge \@title \par}
      {\itshape\LARGE \py@release\releaseinfo \par}
      \vfill
      {\large %changed by davidh, was LARGE
        \begin{tabular}[t]{c}
          \@author
        \end{tabular}
        \par}
      \vfill\vfill
      {\large
       \@date \par
       \vfill
       \py@authoraddress \par
      }%
    \end{flushright}%\par
    \@thanks
  \end{titlepage}%
  \setcounter{footnote}{0}%
  \let\thanks\relax\let\maketitle\relax
  %\gdef\@thanks{}\gdef\@author{}\gdef\@title{}
  \if@openright\cleardoublepage\else\clearpage\fi
  \spx@tempa
}
\def\ttl@save@mkschap #1{\vspace *{-20\p@ }{\parindent \z@ \raggedright
    \normalfont \interlinepenalty \@M \DOTIS {#1} \vskip -20\p@ }}
\makeatother
"""




# Grouping the document tree into LaTeX files. List of tuples
# (source start file, target name, title, author, documentclass [howto/manual]), toctree_only.
if is_geo2grid:
    latex_documents = [
      ('index', '{}_Documentation_{}.tex'.format(project, version), u'{} Documentation'.format(project),
       u'NOAA Community Satellite Processing Package \\and for Geostationary Satellites (CSPP Geo)', 'manual', True),
    ]
else:
    latex_documents = [
        ('index', '{}_Documentation_{}.tex'.format(project, version), u'{} Documentation'.format(project),
         u'Released through the \\and NOAA Community Satellite Processing Package (CSPP)', 'manual', True),
    ]

# The name of an image file (relative to this directory) to place at the top of
# the title page.
latex_logo = '_static/{}2G_PDF_Logos.png'.format('G' if is_geo2grid else 'P')

# latex_toplevel_sectioning = 'section'

# If true, show page references after internal links.
#latex_show_pagerefs = False

# If true, show URL addresses after external links.
#latex_show_urls = False

# Documents to append as an appendix to all manuals.
if is_geo2grid:
    latex_appendices = [
        'design_overview',
    ]
else:
    latex_appendices = [
        'misc_recipes',
        'design_overview',
    ]

# If false, no module index is generated.
latex_domain_indices = False

latex_engine = 'xelatex'


# -- Options for manual page output --------------------------------------------

# One entry per manual page. List of tuples
# (source start file, name, description, authors, manual section).
man_pages = [
    ('index', project.lower(), u'{} Documentation'.format(project),
     [u'David Hoese'], 1)
]

# If true, show URL addresses after external links.
#man_show_urls = False


# -- Options for Texinfo output ------------------------------------------------

# Grouping the document tree into Texinfo files. List of tuples
# (source start file, target name, title, author,
#  dir menu entry, description, category)
texinfo_documents = [
  ('index', project.lower(), u'{} Documentation'.format(project),
   u'David Hoese', project.lower(), 'One line description of project.',
   'Miscellaneous'),
]

# Documents to append as an appendix to all manuals.
#texinfo_appendices = []

# If false, no module index is generated.
#texinfo_domain_indices = True

# How to display URL addresses: 'footnote', 'no', or 'inline'.
#texinfo_show_urls = 'footnote'

intersphinx_mapping = {
    'python': ('https://docs.python.org/3', None),
    'numpy': ('https://docs.scipy.org/doc/numpy', None),
    'scipy': ('https://docs.scipy.org/doc/scipy/reference', None),
    'xarray': ('https://xarray.pydata.org/en/stable', None),
    'dask': ('https://docs.dask.org/en/latest', None),
    'pyresample': ('https://pyresample.readthedocs.io/en/stable', None),
    'trollsift': ('https://trollsift.readthedocs.io/en/stable', None),
    'satpy': ('https://satpy.readthedocs.io/en/stable', None),
    'trollimage': ('https://trollimage.readthedocs.io/en/stable', None),
}
