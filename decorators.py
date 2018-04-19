def check_load(f):
    def inner(*args, **kwargs):
        self = args[0]
        if self.changed_data:
            self.__load__()
        return f(*args, **kwargs)
    return inner
