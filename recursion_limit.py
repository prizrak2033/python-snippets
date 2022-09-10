import sys
print(sys.getrecursionlimit())
#
# sys.setrecursionlimit()  Change recursion limit
# CPython implementation does not optimize tail recursion; unbridled
# recursion causes a stack overflow.
#
