import sys
import os
import re

try:
    with open(sys.argv[1], "r") as file:
        for lines in file.readlines():
            result = re.findall(sys.argv[2], lines)
            if len(result)>0:
                print(lines.strip())
finally:
    if file:
        file.close()
