import sys, traceback

class CustomException:
    @staticmethod
    def getExceptionMsg(e, moduleName, className):
        errStr = ("\n***** " + str(e) + " exception occurred in module [" + moduleName + "] ----> Class [" + className +
                  "] *****\n\n")
        errStr = errStr + traceback.format_exc()
        return errStr
    
    @staticmethod
    def getExceptionMsg(e, moduleName, className, funcName):
        errStr = ("\n***** [" + str(e) + "] exception occurred in module [" + moduleName + "] ----> Class [" + className +
                   "] ----> Func [" + funcName + "] *****\n\n")
        errStr = errStr + traceback.format_exc()
        return errStr
        