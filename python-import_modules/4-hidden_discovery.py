#!/usr/bin/python3
if __name__ == "__main__":
    import hidden_4
    names = sorted(name for name in dir(hidden_4) if not name.startswith('__'))
    for name in names:
        print(name)
