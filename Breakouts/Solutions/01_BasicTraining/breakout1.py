## solutions to the breakout #1 (Day 1)
sent = ""
while True:
    newword = raw_input("Please enter a word in the sentence (enter . ! or ? to end.): ")
    if newword == "." or newword == "?" or newword == "!":
        if len(sent) > 0:
            # get rid of the nasty space we added in
            sent = sent[:-1]
        sent += newword
        break
    
    sent += newword + " "
    print "...currently: " + sent
print "--->" + sent
###  created by Josh Bloom at UC Berkeley, 2010,2012 (ucbpythonclass+bootcamp@gmail.com)
