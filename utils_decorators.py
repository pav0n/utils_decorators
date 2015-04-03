# -*- coding: utf-8 -*-
__author__ = 'Juan Pavón'
__email__ = 'pavon.gnu@gmail.com'
__copyright__ = 'Copyright(c) 2015, Juan Pavón'
__license__ = 'LGPLv3'
__version__ = '1.0'
__status__ = 'Development'

def autolog(request=None,logger=None):
  """ decorador para logger ajustado para web2py """
  def wrapper(action):
    def f(*a, **b):
        if request:
            if logger:
                logger.info("%s %s %s %s %s",request.controller,
                             request.function,request.args,a, b)
            else:
                print request.controller,request.function,request.args,a, b
        else:
            if logger:
                logger.info("%s %s %s",action.__name__, a, b)
            else:
                print action.__name__, a, b
        return action(*a, **b)
    return f
  return wrapper
