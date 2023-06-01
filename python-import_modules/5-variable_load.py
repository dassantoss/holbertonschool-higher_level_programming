#!/usr/bin/python3
if __name__ == "__main__":
    import variable_load_5
    value = 0
    for var in dir(variable_load_5):
        if not var.startswith('__'):
            value = getattr(variable_load_5, var)
            print("{} = {}".format(var, value))
