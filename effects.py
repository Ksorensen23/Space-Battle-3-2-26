import time
import sys

def typewriter(str):
  for char in str
    sys.stdout.write(char)
    sys.stdout.flush()
    time.sleep(1)

def textCleanUp(input):
  if input.isdigit():
    retVal = "error no answer selected"
  else:
    retVal = input.upper()
  return retVal
