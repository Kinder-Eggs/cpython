import importlib
import sys
from zoneinfo import ZoneInfo

tz1 = ZoneInfo("Asia/Tokyo")
tz2 = ZoneInfo("America/Sao_Paulo")

# C
print("C")

import datetime

try:
    print("Tokyo: ", datetime.date.today(tz=tz1))
    print()
    print("SP: ", datetime.date.today())
except:
    print("C with error")

print("\n\n\n")

# Python
print("Python")

sys.modules['_datetime'] = None # cause ImportError
datetime = importlib.reload(importlib.import_module('datetime')) 


try:
    print("Tokyo: ", datetime.date.today(tz=tz1))
    print()
    print("SP: ", datetime.date.today(tz=tz2))
    print()
    print("Local: ", datetime.date.today())
except:
    print("Python with error")