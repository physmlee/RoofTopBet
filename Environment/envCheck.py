import sys
import numpy as np
import cv2
import scipy as sp
import pandas as pd
import matplotlib as mpl

# Check Python
print("{name:>20}".format(name="python") + ": ", sys.version)
assert sys.version_info.major == 3
assert sys.version_info.minor == 9
assert sys.version_info.micro == 13

# Check numpy
print("{name:>20}".format(name="numpy") + ": ", np.__version__)
assert np.__version__ == "1.16.6"

# Check opencv
print("{name:>20}".format(name="opencv") + ": ", cv2.__version__)
assert cv2.__version__ == "4.5.5"

# Check scipy
print("{name:>20}".format(name="scipy") + ": ", sp.__version__)
assert sp.__version__ == "1.7.3"

# Check pandas
print("{name:>20}".format(name="pandas") + ": ", pd.__version__)
assert pd.__version__ == "1.2.4"

# Check matplotlib
print("{name:>20}".format(name="matplotlib") + ": ", mpl.__version__)
assert mpl.__version__ == "3.4.3"

print("\nEnvironment Version Check PASSED!\n")
