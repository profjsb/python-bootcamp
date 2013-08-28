# We first verify that indeed, `display_latex` doesn't do anything for this class:

print "Calling display_latex:"
display_latex(c2)

# Now we grab the latex formatter

latex_f = ip.display_formatter.formatters['text/latex']

# And register for our `AnotherCircle` class, the desired $\LaTeX$ format function. In this case we can use a simple lambda:

latex_f.for_type(AnotherCircle, lambda x: r"$\bigcirc \LaTeX$" )

# Calling `display_latex` once more now gives a different result:

print "Calling display_latex again:"
display_latex(c2)
