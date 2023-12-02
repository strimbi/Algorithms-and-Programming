class TextFormatter:

    # Blue colouring
    BLUE_COL = '\033[94m'
    # Red Colouring
    RED_COL = '\033[91m'
    # Green colouring
    GREEN_COL = '\033[92m'
    # Reset formatting and styling
    RESET = '\033[0m'
    # Yellow colouring
    YELLOW_COL = '\033[93m'


class X(str):
    def __repr__(self):
        return "'%s'" % self
