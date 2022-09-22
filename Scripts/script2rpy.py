"""
Original creator Alpuds
This script parses the WGP-script (non renpy code, human readable) into
code for the renpy script starting and ending at specified lines.
The produced code will go to standard out so it can be used by other tools (e.g., sed).

Usage: script2rpy -n NUMBER[ANOTHER_NUMBER...] FILE
       script2rpy -n START-END FILE
       script2rpy FILE

START is the line number to begin parsing the file.
END is the last line to parse.

NUMBER is a line number to parse.
Multiple lines can be specified with no spaces in between and
separated with commas (e.g., 1,3,5).

FILE is the file to parse and should be in plain text (e.g., .txt).
This file should be the human readable script, not renpy code.

If the only argument is FILE, then the script will
parse FILE completely.

Examples:
Parse lines 5-10 of the script.
script2rpy -n 5-10 wgp-script.txt

Parse lines 5, 8, and 10 of the script.
script2rpy -n 5,8,10 wgp-script.txt

Parse line 23 of the script.
script2rpy -n 23 wgp-script.txt
"""

import argparse
import re
import sys

# Dictionary to translate the characters' names into their
# brief forms for renpy.
character = {"kirara": "krr",
             "kirashima": "krs",
             "kaori": "kao",
             "scarlet": "sca",
             "scottlyn": "sco",
             "nekome": "nek",
             "mari": "mar",
             "atsuko": "ats",
             "kanou": "kan",
             "fumika": "fum",
             "haruka": "har",
             "brandon": "bra",
             "mc": "mc"}

"""
First positional argument (with number) will look like one of these:
4
1,2,3
5-10
"""
parser = argparse.ArgumentParser()
parser.add_argument("file", help="the file to parse")
parser.add_argument("-n", "--numbers", help="the line numbers to parse")

args = parser.parse_args()

# RE is any digit at least 1 or more time, then "-", and
# any digit at least 1 or more times.
# Matches with "14-20" and "50-10".
range_re = r"\d+-\d+" # Used to determine if the argument is a range.

# RE is any alphanumeric character ([a-zA-z0-9_]) at least 1 or more times
# and starts at the beginning.
# Matches with 'mc: "Yadi yada: That's it."' where 'mc:' is matched.
# ':' can be stripped off later.
char_re = r"^\w+:" # Used to extract the character thinking/talking from the text.

if args.numbers != None:
    num = re.match(range_re, args.numbers)
    if num:
        print("Handle the range of numbers")
    elif "," in args.numbers:
        print("Put the numbers in a list")
    else:
        try:
            args.numbers = int(args.numbers)
        except ValueError:
            sys.stderr.write(f"'{args.numbers}' is not valid for the option '-n'")
            exit()

# If the expression on line 79 evaluates to false,
# then this script should parse the entire file.
print("Parse FILE now that the numbers are set up")