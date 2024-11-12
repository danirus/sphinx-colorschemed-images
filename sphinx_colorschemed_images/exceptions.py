import re

RED_HL = "\033[31m"
BLUE_HL = "\033[34m"
END_HL = "\033[0m"


class CSIExtensionError(Exception):
    def __init__(self, message):
        message = self.format(message)
        super().__init__(message)

    def format(self, message):
        return re.sub(
            r"hl\((?P<identifier>\w+)\)",
            rf"{BLUE_HL}\g<identifier>{END_HL}",
            message,
        )
