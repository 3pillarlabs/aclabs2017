# kinda C-like formatting
# %r prints the "raw programmer's version of a variable"
formatter  = "%r %r %r %r"

# Python's twist. Does not work for Python 3.6 "formatter" has been depricated since version 3.4

print formatter % (1, 2, 3, 4)
print formatter % ("one", "two", "three", "four")
print formatter % (True, False, False, True)
print formatter % (formatter, formatter, formatter, formatter)
print formatter % (
    "I had this thing",
    "That you could type up right.",
    "But it didn't sing.",
    "So I said goodnight."
)
