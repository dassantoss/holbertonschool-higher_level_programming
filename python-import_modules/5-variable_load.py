#!/usr/bin/python3
if __name__ == "__main__":
    import variable_load_5
    for var in dir(variable_load_5):
        if not var.startswith('__'):
            print("{}".format(getattr(variable_load_5, var)))
