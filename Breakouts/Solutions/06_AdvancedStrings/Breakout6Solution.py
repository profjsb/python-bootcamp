"""
  PYTHON BOOT CAMP ADVANCED STRINGS BREAKOUT SOLUTION; 
  created by Adam Morgan at UC Berkeley, 2010 (ucbpythonclass+bootcamp@gmail.com)
"""
#import regular expressions
import re
import sys

def reverse_extension(filename):
    '''Given a filename, find and reverse the extension at the end'''
    # First split the filename string by periods.  The last item in the 
    # resultant list (index -1) is assumed to be the extension.
    extension = filename.split('.')[-1]
    # Now let's strip off this old extension from the original filename
    base_name = filename.rstrip(extension)
    # And reverse the extension:
    r_extension = extension[::-1]
    # Now append the reversed extension to the base
    return base_name + r_extension

def count_occurances(filename, substring):
    ''' Count all occurances of the substring in the file'''
    my_file = open(filename,'r')
    string_file = my_file.read()
    count = string_file.count(substring)
    my_file.close()
    return count

def find_and_halve_numbers(line):
    ''' Find all occurances of numbers in a line, and divide them by 2
    
    Note! We're using regular expressions here to find the groups of numbers.  
    This is complex and you aren't expected to know how to do this.  The 
    rest of the function is straightforward, however.
    
    Another possible solution would be to split each line word by word
    with split() and test whether each "word" is a number
    '''
    split_line = re.split("(\d+)",line)    
    new_line = ''
    for item in split_line:
        if item.isdigit():
            # If the string contains only digits, convert to integer, divide by 2
            item = str(int(item)/2)
        new_line += item
    return new_line

def do_operations(filename):
    """Given a file, perform the following operations:
    1) Reverse the extension of the filename
    2) Delete every other line
    3) change occurance of words:
        love -> hate
        not -> is
        is -> not
    4) sets every number to half its original value
    5) count the number of words "astrology" and "physics"
    """
    # Open file for reading
    orig_file = open(filename,'r')
    # Get new filename for writing
    new_filename = reverse_extension(filename)
    new_file = open(new_filename,'w')
    
    index = 0
    # Loop over every line in the file
    for line in orig_file.readlines():
        index += 1
        # if we're on an odd numbered line, perform operations and write 
        # (this effectively deletes every other line)
        if index%2 == 1:
            # make the desired replacements
            newline = line.replace(' love ',' hate ')
            # make temp_is string so we don't overwrite all new instances of 'is'
            newline = newline.replace(' not ',' temp_is ')
            newline = newline.replace(' is ',' not ')
            newline = newline.replace(' temp_is ',' is ')
            
            # Divide all numbers by 2
            newline = find_and_halve_numbers(newline)
            
            # Write new line
            new_file.write(newline)
        
    print 'There are %i occurances of astrology and %i occurances of physics' % \
            (count_occurances(filename,'astrology'),count_occurances(filename,'physics'))
    orig_file.close()
    new_file.close()
    print 'Wrote %s' % (new_filename)

if __name__ == "__main__":
    if len(sys.argv) == 2:
        do_operations(sys.argv[1])
    else:
        print "dont know what to do with", repr(sys.argv[1:])
