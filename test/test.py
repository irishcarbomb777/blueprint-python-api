import numpy as np
from libs.handlerLib import handler

def main(event, context):
    def fn(event, context):
        a = np.arange(4)
        b = a[2]
        b = int(b)
        return b
    return handler(fn(event,context))
