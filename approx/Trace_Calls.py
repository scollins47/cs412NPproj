DEBUG = False


class Trace_Calls:
#Credit goes to Richard Pattis for his Illustrate_Recursive class.
    def __init__(self,f):
        self.f = f
        self.calls = 0
        self.trace = False
        self.record = []


    def illustrate(self,*args,**kargs):

        self.indent = 0
        self.trace = True
        answer = self.__call__(*args,**kargs)
        self.trace = False
        return answer

    # def __call__(self,*args,**kargs):  # bundle arbitrary arguments to this call
    #     self.calls += 1
    #     return self.f(*args,**kargs)  # unbundle arbitrary arguments to call f

    def display_records(self):
        return self.record

    def __call__(self,*args,**kargs):

        if self.trace:
            if self.indent == 0:
                print('Starting recursive illustration'+30*'-')
            print (self.indent*"."+"calling", self.f.__name__+str(args)+str(kargs))
            self.indent += 2
        self.calls += 1
        answer = self.f(*args,**kargs)
        if answer != None:
            self.record.append(answer)
        if self.trace:
            self.indent -= 2
            print (self.indent*"."+self.f.__name__+str(args)+str(kargs)+" returns", answer)
            if self.indent == 0:
                print('Ending recursive illustration'+30*'-')
        return answer
    def called(self):
        return self.calls

    def get_recursive_calls(self):
        return self.calls - 1

    def reset(self):
        self.calls = 0
        self.record = []


def trace(f):
    trace.recursive_calls = 0
    trace.depth = 0


    def _f(*args, **kwargs):


        print("  " * trace.depth, ">", f.__name__, args, kwargs)
        if trace.depth >= 1:
            trace.recursive_calls += 1
        trace.depth += 1
        res = f(*args, **kwargs)
        trace.depth -= 1
        print("  " * trace.depth, "<", res)
        print("recursive calls so far: {}".format(trace.recursive_calls))
        return res
    return _f

