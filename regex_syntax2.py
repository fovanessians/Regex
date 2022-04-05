import re

regex = r"self." 64 matches
regex = r"[a-z]self" 46
regex = r"p..a.e$" 0
regex = r"t..ch" 14

gr[ea]y (greay or gray) 0 matches
regex = r"gr[ea]y"


regex = r"[A-Za-z]"

test_str = "Notice: keep off the grass"

matches = re.finditer(regex, test_str)

regex = r"[0-9][0-9][0-9]-[0-9]"

test_str = "555-666-7899"

matches = re.finditer(regex, test_str)   --- 1 match


see[^mn] matches seek and see but not seem or seen or see

/h[a.]t/ the period is literal

/var[[(][0-9][\])]/       ***** \] ***** had to escape the closing bracket so it does not get confused with actually closing the bracket

\d - DIgit 0-9
\w letters and 0-9 and underscore (hyphen not included)
\s whitespace
\D not digit same as ^\d
\W not character
\S no whitespace

Repetition:
* preceding item 0 or more times
+ preceding item 1 or more times
? preceding item zero or 1 time

/apples*/ matches apple, apples, applessssss
/apple+/ matches apples and applessssssss but not apple
/\d\d\d+/ matches numbers with 3 digits or more

{ start quantified repetition of preceding item
} End quantified ......
\d{4,8} matches numbers with 4 to 8 digits
\d{4} matches numbers with exactly 4 digits, min and max are 4

the expression goes as far as it can, if it is not done then it gives back a digit to finish the expression. (give back as little)

Lazy expression
/.*?[0-9]+/
Page 266

# coding=utf8
# the above tag defines encoding for this document and is for Python 2.x compatibility

import re

regex = r"[\"].*?[\"]" - everything between quotes

() - group expression

(in)?dependent - "in" is optional

| is an OR operator
leftmost gets precedence
/apple|orange/

/(AA|BB|CC){4}/ AABBAACC CCCCBBBB

peanut(butter)? - greedy
peanut(butter)?? - lazy


regex = r"(my|your|thy)self"

match do or does followed by no not or nothing 

[Dd]o(es)? no(t(hing)?)?
[Dd]o(es)? (no(t?))|(nothing)

ANCHORS -------------------------

^ start of str/line
$end of str or line
\A start of string never end of line
\Z end of string never end of line
represent a position not an actual charachter

/^apple$/ or /|Aapple\Z/

re.MULTILINE for using the ^ and $

WORD BOUNDARIES ------
\b start or end of word
\B not a word boundary
reference a position not an actual character.

/\B\w+\B/ fineds 2 matches in "This is a test." answer hi & es
