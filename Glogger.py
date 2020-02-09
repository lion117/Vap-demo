# -*- coding: utf-8 -*-
"""
@author: LEO
Date:  2020/2/8
Email:	lion_117@126.com
All Rights Reserved Licensed under the Apache License
"""

import os, path,sys
import  logging

gLogger = logging.getLogger("pylog")
gLogger.setLevel(logging.INFO)
rf_handler = logging.StreamHandler(sys.stderr)  #默认是sys.stderr
rf_handler.setLevel(logging.DEBUG)
rf_handler.setFormatter(logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s"))

f_handler = logging.FileHandler('pylog.log')
f_handler.setLevel(logging.INFO)
f_handler.setFormatter(logging.Formatter("%(asctime)s - %(levelname)s - %(filename)s[:%(lineno)d] - %(message)s"))

gLogger.addHandler(rf_handler)
gLogger.addHandler(f_handler)



if __name__ == '__main__':
    pass
