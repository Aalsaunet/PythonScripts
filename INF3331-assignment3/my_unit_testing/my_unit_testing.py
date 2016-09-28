class UnitTest(object):

    def __init__(self, func, args, kwargs, res):    # make test
        self.function = func
        self.a = args[0]
        self.b = args[1]
        self.rechecks = kwargs["num_rechecks"]
        self.expected_result = res

    def __call__(self):                             # run test
        result = self.function(self.a, self.b, self.rechecks)
        if result == self.expected_result:
            return True
        else:
            return False
