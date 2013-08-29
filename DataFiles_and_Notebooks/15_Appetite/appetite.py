#! /usr/bin/env python
# this file was originall written by Brad Cenko for 2012 UCB Python Bootcamp
# modified and extended by Paul Ivanov for the 2013 UCB Python Bootcamp

import sqlite3, os, smtplib
from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText
import NothingToSeeHere # Email password stored in this (private) file
from NothingToSeeHere import username as email_addr

# Global variables
piDB = "piDB.sql"
# Need to change this to a path you can write to

import logging
logging.basicConfig(level=logging.INFO, format="%(levelname)s: %(message)s")
log = logging.getLogger(__name__)

###########################################################################

def create_friends_table(filename=piDB):

    """Creates sqlite database to store basic information on my buddies"""

    conn = sqlite3.connect(filename)
    c = conn.cursor()

    c.execute('''CREATE TABLE CYCLISTS (f_name text, l_name text,
               email text, status text)''')

    ins_tpl= 'INSERT INTO CYCLISTS VALUES ("%s", "%s", "%s", "%s")'

    l = []
    l += [ins_tpl % ( "Paul", "Ivanov", email_addr, 'committed')]
    l += [ins_tpl % ( "Dan", "Coates", email_addr, 'committed')]
    l += [ins_tpl % ( "James", "Gao", email_addr, 'casual')]
    l += [ins_tpl % ( "Sara", "Emery", email_addr, 'committed')]
    l += [ins_tpl % ( "Jonathan", "Giffard", email_addr, 'weekender')]
    l += [ins_tpl % ( "Janet", "Young", email_addr, 'weekender')]

    for s in l:
        print s
        c.execute(s)

    conn.commit()
    c.close()

    return

############################################################################

def retrieve_random_cyclist(filename=piDB, kind="committed"):

    """Returns the name and email address of a random cyclist"""

    conn = sqlite3.connect(filename)
    c = conn.cursor()

    c.execute("SELECT f_name, l_name, email FROM CYCLISTS WHERE status" + \
              " = '%s' ORDER BY RANDOM() LIMIT 1" % kind)
    row = c.fetchall()
    
    conn.commit()
    c.close()
    if len(row)== 0:
        raise ValueError("There are no people who are '%s'" % kind ) 

    return [row[0][0], row[0][1], row[0][2]]

###########################################################################

###############################################################################

def email_cyclist(address, f_name, l_name, myemail=NothingToSeeHere.username):

    """Generate and send an email to address with a request to observe
    the given supernova."""
    
    # Create the message
    msg = MIMEMultipart()
    msg["From"] = myemail
    msg["To"] = address
    msg["Subject"] = "Let's go for a ride, %s" % f_name

    # Write the body, making sure all variables are defined.
    msgstr = r"""Hey %s,

    Wanna go for a bike ride later on today?

    best,
    pi
    -- 
                       _
                      / \
                    A*   \^   -
                 ,./   _.`\\ / \
                / ,--.S    \/   \
               /  `"~,_     \    \
         __o           ?
       _ \<,_         /:\
    --(_)/-(_)----.../ | \
    --------------.......J
    Paul Ivanov
    http://pirsquared.org
    """  % f_name
    msg.attach(MIMEText(msgstr))

    # Configure the outgoing mail server
    log.info("sending out email") 
    mailServer = smtplib.SMTP("smtp.gmail.com", 587)
    mailServer.starttls()
    mailServer.login(myemail, NothingToSeeHere.password)

    # Send the message
    mailServer.sendmail(myemail, address, msg.as_string())
    mailServer.close()

    
    return

###############################################################################
    
def go_cycling(filename=piDB, myemail=NothingToSeeHere.username):
    """Script to go cycling with one of my cycling buddies.
    Grabs
    and emails that student to request follow-up observations."""

    # See if the department database exists.  If not, create it.
    if not os.path.exists(filename):
        create_friends_table(filename=filename)

    # Select a random graduate student to do our bidding
    [f_name, l_name, address] = retrieve_random_cyclist(filename=filename)

    # Email the student
    email_cyclist(address, f_name, l_name, myemail=myemail)

    print "I emailed %s %s at %s about going cycling." % (f_name, l_name,
                                                          address)

###############################################################################
