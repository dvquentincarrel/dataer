import sys 
COLORS = ["\x1b[m", "\x1b[1m", "\t\x1b[33m", "\x1b[1;4m", "\x1b[0;35m", "\x1b[31m"]

preface="""\
Dataer is a utility to allow working on individual components of a web scanner scenario.
Enables bypassing module update when pushing modifications,
automatic building of data file, and exploding existing data file into its components."""

usage="{1}Usage:{0} dataer <command> [<FILE>]".format(*COLORS)

hints="see '{1}dataer -h{0}' for more informations".format(*COLORS)

help_msg="""\
{1}Usage{0}:
{2}dataer template{0}
{2}dataer unravel{0} {3}SOURCE{0}
{2}dataer build{0} {3}TARGET{0}
{2}dataer inject{0} {3}[DB_NAME]{0}
{2}dataer autofill{4}*{0}
{2}dataer update{0} {3}TARGET{4}*{0}
{4}*NIY{0}""".format(*COLORS)

def print_default():
    """Default message"""
    print(usage, file=sys.stderr)
    print(hints, file=sys.stderr)

def print_err(content: str):
    """Error message"""
    print("{6}ERROR{1}: {0}".format(content, *COLORS), file=sys.stderr)

def print_help():
    """Help message"""
    print(usage, file=sys.stderr)
    print("\n%s"%preface, file=sys.stderr)
    print("\n%s"%help_msg, file=sys.stderr)
