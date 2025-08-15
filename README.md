# fractals
I'm sorry if anything is messy or incorrect! Here is a breakdown of the files, by order of release:
1. `square1.py` is an initial test/proof of concept of coding L-systems with turtle in Python. Edit and run in an IDE, or with `python square1.py`
2. `triangle1.py` is an implementation on the triangular grid. Run as above
3. `triangle2.py` adds the non-turn `0` and uses a simplified input via the command line. Run e.g. `python triangle2.py "+0-" <depth=1> <size=100>` in the command line (`<optional argument=default>`, in this case `rule="F+F0F-F"`)
4. `triangle3.py` allows for an input including or excluding "`F`"s, adds an optional angle argument (in degrees) for the turns `+` and `-`, removes the optional size argument- this can now be set once manually to account for different svg viewers, and corrects the scaling when iterating- accounting for other choices of angles. Run e.g. `python triangle3.py +0- <depth=1> <angle=120>` in the command line
5. `triangle4.py` prints the rules for the non-constant boundary letters and draws the left and right boundaries. Angle is fixed at 120 degrees. Run e.g. `python triangle4.py +0- <depth=1>` in the command line. Edit: this is broken! I'm working on it :)

You may need to install python and import packages such as canvasvg to run this code locally
