# How I understood the problem

I understood the problem as needing object wrapper for the URI call. The wrapper needs to validate the structure of the URI and to act as a object oriented wrapper to use the URI programmaticly.

# Choices

I chose python 3 to do this task as it has a fast turnaround and a good standard library with urllib.

# Challenges

The challenges I faced in the came due python 3 strings being iterable and dictionary adding each iteration as own element.

# Compromises

There is a bug in the software when a same parameter is given twice then the program only considers the last given value. I didn't fix this due to shortage of time needing to redesing acceptance.
