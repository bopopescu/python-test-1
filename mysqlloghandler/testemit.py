import logging

class LoggingHandler(logging.Handler):
    def __init__(self):
        logging.Handler.__init__(self)
    def emit(self, record):
        assert isinstance(record, logging.LogRecord)
        print("LoggingHandler received LogRecord: {}".format(record))

        self.format(record)

        # List of LogRecord attributes expected when reading the
        # documentation of the logging module:

        expected_attributes = \
            "args,asctime,created,exc_info,filename,funcName,levelname," \
            "levelno,lineno,module,msecs,message,msg,name,pathname," \
            "process,processName,relativeCreated,stack_info,thread,threadName"

        for ea in expected_attributes.split(","):
            if not hasattr(record, ea):
                print("UNEXPECTED: LogRecord does not have the '{}' field!".format(ea))


formatter = logging.Formatter("%(asctime)s")
loggingHandler = LoggingHandler()
loggingHandler.setFormatter(formatter)
rootLogger = logging.getLogger()
rootLogger.addHandler(loggingHandler)

# emit an WARNING message
logging.warning("WARNING MESSAGE")
