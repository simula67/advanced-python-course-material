__author__ = 'ravi'
import re
import StringIO
content = """
12.21
34.43

90.09
12.34
56.78
"""
pattern = r"(\d)(\d)\.\2\1"

for line in StringIO.StringIO(content):
    m = re.search(pattern, line)
    if m:
        print m.groups()
