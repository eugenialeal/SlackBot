import os
import time
import json
import base64
import getpass
import requests
import pandas as pd
import pygsheets

def timeit(method):
    """Decorator to log the time in seconds/minutes format
    Usage:
    @timeit
    def main():
        pass
    Ref:
    https://medium.com/pythonhive/python-decorator-to-measure-the-execution-time-of-methods-fa04cb6bb36d
    """

    def timed(*args, **kw):
        ts = time.time()
        result = method(*args, **kw)
        te = time.time()
        if 'log_time' in kw:
            name = kw.get('log_name', method.__name__.upper())
            kw['log_time'][name] = int((te - ts) * 1000)
        else:
            if (te - ts) <= 60:
                print('%r  %2.2f s' % (method.__name__, (te - ts)))
            else:
                print('%r  %2.2f m' % (method.__name__, (te - ts)/60))
        return result
    return timed
  
  def post_influx(file=None):
    """Decorator to log success/failure to influx
    
    Keyword arguments:
    file -- string, the current path of the file
    
    Usage:
    
    @timeit
    @post_influx(file=sys.argv[0])
    def main():
        pass
        
    if __name__ == '__main__':
        main()
    
    """
