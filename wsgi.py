import sys

path = '/home/hnguyen2107/the_flask'
if path not in sys.path:
    sys.path.append(path)

from main import app as application
