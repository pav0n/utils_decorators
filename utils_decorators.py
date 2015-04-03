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
