print("Hello World")

print('yo')

print("mama")

# damn

import os
import sys
from glob import glob
from pathlib import Path

cur_dir = Path(os.getcwd()).expanduser()
print(cur_dir)

views_file = list(cur_dir.glob('**/%s.sql' % '*'))

views_name = tuple(f.name.strip(".sql") for f in views_file)
print(views_name)
