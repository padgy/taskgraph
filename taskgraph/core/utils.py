from os.path import dirname, basename, isfile, join
import glob
from typing import List

def list_files_from_current_directory(file) -> List[str]:
    modules = glob.glob(join(dirname(file), "*.py"))
    return [ basename(f)[:-3] for f in modules if isfile(f) and not f.endswith('__init__.py')]