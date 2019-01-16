import checkSnapshot
import sys

message = checkSnapshot.checkVersion(sys.argv[1], '')
print(message)