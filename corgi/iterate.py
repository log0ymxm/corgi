from collections import defaultdict
from itertools import groupby


def groupdict(col, fn, value_fn=list):
    "Performs a groupby on a collection and consumes the generator result into a python dict."
    sorted_col = sorted(col, key=fn)
    return defaultdict(list, {k: value_fn(v) for k, v in groupby(sorted_col, key=fn)})