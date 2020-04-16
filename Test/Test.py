import random, time

# Run function and statistic performance.
def PrintPerformance(func):
    def RunFunctionAndPrintPerformance(*args, **kw):
        startTime = time.time()
        retValue = func(*args, **kw)
        endTime = time.time()
        elapsedTime = endTime - startTime
        print("Run {} in {:6.3} seconds.".format(func, elapsedTime))
        return retValue
    return RunFunctionAndPrintPerformance

def ReturnPerformance(func):
    def RunFunctionAndReturnPerformance(*args, **kw):
        startTime = time.time()
        retValue = func(*args, **kw)
        endTime = time.time()
        elapsedTime = endTime - startTime
        return (retValue, elapsedTime)
    return RunFunctionAndReturnPerformance


        