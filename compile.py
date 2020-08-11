#!/usr/bin/python3
from tokens import tokenizer, compiler
import os
import sys


#open file
class RevoMain:
  def __init__(self, filename):
    self.f = open(filename,"r")
  def main(self):
    tokenizer.gentokens(self.f)
  def build(self):
    compiler.scel(self.f,"b")
  def debug(self):
    compiler.scel(self.f,"d")

    


if __name__ == "__main__":
  if str(sys.argv[1]) in ["b","d"]:
    p = RevoMain(str(sys.argv[2]))
    if str(sys.argv[1]) == "b":
      p.build()
    else:
      p.debug()
    print("=== Output ===")
    os.system("gcc build/temp.c -o kavat")
    os.system("./kavat")
  else:
    print("Please specify function (build or debug)")
else:
  p = RevoMain("test.rv")
  p.build()
  print("=== Output ===")
  os.system("gcc build/temp.c ")
  os.system("./a.out")
