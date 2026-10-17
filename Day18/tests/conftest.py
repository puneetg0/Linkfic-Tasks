import sys
from pathlib import Path


DAY18_PATH = Path(__file__).resolve().parents[1]
if str(DAY18_PATH) not in sys.path:
    sys.path.insert(0, str(DAY18_PATH))
