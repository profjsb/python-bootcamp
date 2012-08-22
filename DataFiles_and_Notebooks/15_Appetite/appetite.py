#! /usr/bin/env python

import sqlite3, os, urllib2, smtplib
from lxml import etree
from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText
import NothingToSeeHere # Email password stored in this (private) file

# Global variables
MYSNURL = "http://astro.berkeley.edu/~cenko/public/BootCamp/SNeInfo.html"
ASTROPEEPSDB = "/Users/cenko/BootCamp/2012B/appetite/astropeeps.sql"
# Need to change this to a path you can write to

###########################################################################

def create_astro_table(filename=ASTROPEEPSDB):

    """Creates sqlite database to store basic information on astronomy department"""

    conn = sqlite3.connect(filename)
    c = conn.cursor()

    c.execute('''CREATE TABLE ASTROPEEPS (f_name text, l_name text,
               email text, status text)''')
    c.execute('''INSERT INTO ASTROPEEPS VALUES ("Josh", "Bloom",
               "jbloom@astro.berkeley.edu", "Faculty")''')
    c.execute('''INSERT INTO ASTROPEEPS VALUES ("Berian", "James",
               "berian@astro.berkeley.edu", "Postdoc")''')
    c.execute('''INSERT INTO ASTROPEEPS VALUES ("Joey", "Richards",
               "joeyrichar@gmail.com", "Postdoc")''')
    c.execute('''INSERT INTO ASTROPEEPS VALUES ("Adam", "Morgan",
               "amorgan@astro.berkeley.edu", "Student")''')
    c.execute('''INSERT INTO ASTROPEEPS VALUES ("Chris", "Klein",
               "cklein@berkeley.edu", "Student")''')
    c.execute('''INSERT INTO ASTROPEEPS VALUES ("Isaac", "Shivvers",
               "ishivvers@berkeley.edu", "Student")''')
    c.execute('''INSERT INTO ASTROPEEPS VALUES ("Dan", "Starr",
               "dstarr@astro.berkeley.edu", "Staff")''')
    c.execute('''INSERT INTO ASTROPEEPS VALUES ("Henrik", "Brink",
               "henrikbrink@gmail.com", "Student")''')

    conn.commit()
    c.close()

    return

############################################################################

def retrieve_random_gradstudent(filename=ASTROPEEPSDB, student="Student"):

    """Returns the name and email address of a random graduate student"""

    conn = sqlite3.connect(filename)
    c = conn.cursor()

    c.execute("SELECT f_name, l_name, email FROM ASTROPEEPS WHERE status" + \
              " = '%s' ORDER BY RANDOM() LIMIT 1" % student)
    row = c.fetchall()
    
    conn.commit()
    c.close()

    return [row[0][0], row[0][1], row[0][2]]

###########################################################################

def retrieve_sn_info(sn_name, url=MYSNURL):

    """Given the name of a supernova, retrieves the object's coordinates,
    host galaxy, and type (if they exists) by reading through the provided
    URL.  Otherwise returns a list of None."""

    # Download the HTML from the SNe URL
    flob = urllib2.urlopen(url)
    s = flob.read()
    flob.close()
    html = etree.HTML(s)

    # Find all lines following the <table> tag
    rows = html.find('.//table')

    # Loop over the table rows
    for row in rows:

        # Check if matches name given SN
        if (sn_name == row[0].text):

            # Get important info
            coords = [row[1].text.replace(" ", ":"),
                      row[2].text.replace(" ", ":")]
            host = row[3].text
            sntype = row[4].text
            return [host, coords, sntype]

    # If no match found, return a whole lot of nothing
    return [None, None, None]

###############################################################################

def email_student(address, f_name, l_name, sn_name, host, coords, sntype,
                  myemail="bradcenko@gmail.com"):

    """Generate and send an email to address with a request to observe
    the given supernova."""
    
    # Create the message
    msg = MIMEMultipart()
    msg["From"] = myemail
    msg["To"] = address
    msg["Subject"] = "Observations of %s" % sn_name

    # Write the body, making sure all variables are defined.
    msgstr = "Hi %s %s,\n\n" % (f_name, l_name)
    msgstr += "I just found out about %s, and it seems neat.  " % sn_name
    if (host == None):
        msgstr += "The host galaxy is unknown.  "
    else:
        msgstr += "The host galaxy is %s.  " % host
    if (coords == None):
        msgstr += "I do not know the coordinates.  "
    else:
        msgstr += "The location is: RA=%s; Dec=%s.  " % (coords[0], coords[1])
    if (sntype == None):
        msgstr += "I do not know the type.\n\n"
    else:
        msgstr += "The type is %s.\n\n" % sntype
    msgstr += "Here's an image of the field: \n"
    finder = "http://qmorgan.org.org/fc/fcserver.py?ra=%s&dec=%s&src_name=%s&cont_str=Contact:+Brad+Cenko+(bradcenko@gmail.com)" % (coords[0], coords[1], sn_name)
    msgstr += finder + "\n\n"
    msgstr += "Could you please arrange some new observations?  "
    msgstr += "I am really busy drinking right now.\n\n"
    msgstr += "Thanks,\nBrad"
    msg.attach(MIMEText(msgstr))

    # Configure the outgoing mail server
    mailServer = smtplib.SMTP("smtp.gmail.com", 587)
    mailServer.starttls()
    mailServer.login(myemail, NothingToSeeHere.passwd)

    # Send the message
    mailServer.sendmail(myemail, address, msg.as_string())
    mailServer.close()

    print "Finder: %s" % finder
    
    return

###############################################################################
    
def do_science(sn_name, filename=ASTROPEEPSDB, url=MYSNURL,
               myemail="bradcenko@gmail.com"):

    """Script to do cutting edge science. Takes a supernova name, finds
    some information about it on a webpage, picks a random graduate student,
    and emails that student to request follow-up observations."""

    # See if the department database exists.  If not, create it.
    if not os.path.exists(filename):
        create_astro_table(filename=filename)

    # Select a random graduate student to do our bidding
    [f_name, l_name, address] = retrieve_random_gradstudent(filename=filename)

    # Find out some information about the supernova
    [host, coords, sntype] = retrieve_sn_info(sn_name, url=url)

    # Email the student
    email_student(address, f_name, l_name, sn_name, host, coords, sntype,
                  myemail=myemail)

    print "I emailed %s %s at %s about %s." % (f_name, l_name, address, sn_name)
    
    # Faculty job here I come!
    return

###############################################################################
