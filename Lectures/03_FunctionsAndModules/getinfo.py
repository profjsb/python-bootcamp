
import os
import sys

def getinfo(path="."):
    """
Purpose: make simple use of os and sys modules
Input: path (default = "."), the directory you want to list
    """
    print("You are using Python version ",end=" ")
    print(sys.version)
    print("-" * 40)
    print("Files in the directory " + str(os.path.abspath(path)) + ":")
    for f in os.listdir(path): 
        print(f)