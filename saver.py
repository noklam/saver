import inspect
from copy import deepcopy


def retrieve_name(var):
        """
        Gets the name of var. Does it from the out most frame inner-wards.
        :param var: variable to get name from.
        :return: string
        """
        for fi in reversed(inspect.stack()):
            names = [var_name for var_name, var_val in fi.frame.f_locals.items() if var_val is var]
            if len(names) > 0:
                return names[0]
            
            
def save_variable(x):
    global _master
    _master = {}
    _master[retrieve_name(x)] = deepcopy(x)
    
    
def recover_variable(x):
    global _master
    name = retrieve_name(x)
    return _master[name]
        
