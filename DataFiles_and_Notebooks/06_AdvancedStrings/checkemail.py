"""
  PYTHON BOOT CAMP EXAMPLE; 
    created by Josh Bloom at UC Berkeley, 2010,2012 (ucbpythonclass+bootcamp@gmail.com)
"""
import string

## let's only allow .com, .edu, and .org email domains
allowed_domains = ["com","edu","org"]

## let's nix all the possible bad characters
disallowed = string.punctuation.replace(".","")

while True:
    res = raw_input("Enter your full email address: ")
    res = res.strip()   # get rid of extra spaces from a key-happy user
    if res.count("@") != 1:
        print "missing @ sign or too many @ signs"
        continue
    username,domain = res.split("@")

    ## let's look at the domain
    if domain.find(".") == -1:
        print "invalid domain name"
        continue
    if domain.split(".")[-1] not in allowed_domains:
        ## does this end as it should?
        print "invalid top-level domain...must be in " + ",".join(allowed_domains)
        continue
    goodtogo = True
    for s in domain:
        if s in disallowed:
            print "invalid character " + s
            ## cannot use continue here because then we only continue the for loop, not the while loop 
            goodtogo = False

        
    ## if we're here then we're good on domain. Make sure that 
    for s in username:
        if s in disallowed:
            print "invalid character " + s
            goodtogo = False

    if goodtogo:
        print "valid email. Thank you."
        break
