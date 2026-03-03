import time
import sys

def typewriter(str, time):
  for char in str
    sys.stdout.write(char)
    sys.stdout.flush()
    time.sleep(time)

def textCleanUp(input):
  if input.isdigit():
    retVal = "error no answer selected"
  else:
    retVal = input.upper()
  return retVal
