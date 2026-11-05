from anvil import *

from maple import register_maple
from willow import register_willow

if __name__ == "__main__":
    register_maple()
    register_willow()
    ANVIL.compile(extract_world=None)
    # ANVIL.package()
