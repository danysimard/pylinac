# **pylinac**

[![Latest Version](https://pypip.in/version/pylinac/badge.svg)](https://pypi.python.org/pypi/pylinac/)
[![Supported Python versions](https://pypip.in/py_versions/pylinac/badge.svg)](https://pypi.python.org/pypi/pylinac/)
[![License](https://pypip.in/license/pylinac/badge.svg)](https://pypi.python.org/pypi/pylinac/)

Pylinac provides TG-142 quality assurance (QA) tools to Python programmers as well as non-programmers in the field of 
therapy medical physics. The package comes in two flavors: source-level and GUI-level. The source-level
allows programmers and those familiar with Python to create custom tests with pylinac while the GUI-level will implement
pylinac into a GUI and executable that any user can use, without having to program software.

Below are the tools currently available; tools will be added one at a time as they are developed.

+ **[Starshot Analysis][star]** -
    Tools for analyzing film or superimposed EPID images for gantry, collimator, or MLC star (aka spoke) shots. Can determine
    the minimum circle that touches all the radiation spokes (wobble).
+ **[VMAT QA][vmat]** - 
    A module for analyzing EPID images after performing the Jorgensen et al tests for VMAT QA, specifically the Dose Rate & Gantry Speed 
    (DRGS) and MLC Speed (MLCS) tests. Can load the open and MLC field images and calculate segment ratios as per the Jorgensen protocol. 
    
----------------

**To get started, install, run the demos, view the API docs, and learn the module design, visit the [Full Documentation][docs].**

Code is Python 2/3 compatible thanks to [future][fut]. 


[docs]: http://pylinac.readthedocs.org/en/latest/index.html
[star]: http://pylinac.readthedocs.org/en/latest/starshot_docs.html
[vmat]: http://pylinac.readthedocs.org/en/latest/vmat_docs.html
[fut]: http://python-future.org/
