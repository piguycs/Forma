import parser

class tokenizer:
  keywords = [
    "print",    # terminal output
    "//",       # comment
    "stat",     # code statistics
    "const",    # create a constant variable
    "redest",   # redestribute resources 
    "contort",  # clean the output logs in output.logs.rv
    "str",      # create string object
    "int",      # create integer object
    "bool",     # create boolean object
    "if",       # simple if statement
    "line-end", # system reserved
    "input",    # takes string input up to 100 characters 
    "open",     # open a file (same syntax as C)
    "read",     # read from a file
    "close"     # close a file
  ]
  operators = [
    "{",
    "}"
  ]

  tokens = []

  def peak_next_char(line,word,pos):
    line = line.split(" ")
    word = line[word]
    return word[pos]

  def gentokens(code):
    print("=== Starting tokenizer ===")
    #create code split list
    lines = code.readlines()
    imp=[]
    for line in lines:
      line = line[:-1]
      for i in line.split(" "):
        imp.append(i)
      imp.append("line-end")
    #check keywords and display information about keywords
    print("------------" + (' ' * 15)  + "   " + "revoval " + "||| " + "description")
    for token in imp:
      desc=""
      #is token a valid function?
      if token in tokenizer.keywords:
        revoval = "yes"
        #check parser for information about the token
        desc = parser.parse(token,False,line)
      else:
        revoval = "no"
      print("--- > Token: " + token + (' ' * (15-len(token)))  + "<---- " + revoval + (' ' * (4-len(revoval))) + "||| " + desc)


class compiler:
  # augments can be set here
  aug = "None"

  # build base sceleton 
  def scel(code,state):
    debug=""
    print("=== Building C sceleton ===")
    with open("build/temp.c","w+") as f:
      #translate Revo to C for compilation using parser
      print("=== Starting translation ===")
      #header
      f.write("#include <stdio.h> \n int main() {")
      #create code split list
      lines = code.readlines()
      imp=[]
      i=0
      finalcode = ""
      for line in lines:
        line = line[:-1]
        for i in line.split(" "):
          imp.append(i)
        imp.append("line-end")
      #check keywords and display information about keywords
      if state =="d":
       print("------------" + (' ' * 15)  + "   " + "revoval " + "||| " + "description")
      i=0
      variables=[]
      for token in imp:
        rev_bit=""
        #is token a valid function?
        if token in tokenizer.keywords or token in tokenizer.operators:
          revoval = "yes"
          #check parser for information about the token and if possible value
          rev_bit = parser.parse(token,True,line)
          if rev_bit == "//":
            i+=1
            f.write(str(rev_bit))
            if i == 2:
              i=0
          if token in ["int","bool","str"]:
              variables+=[rev_bit,imp[imp.index(token)+1],imp[imp.index(token)+2]]
              if state =="d":
                debug+="\nVariable created, variable info: {} {} {}".format(rev_bit,imp[imp.index(token)+1],imp[imp.index(token)+3])+"\n"
                print("Variable created, variable info:",rev_bit,imp[imp.index(token)+1],imp[imp.index(token)+3])
          if token == "print":
              line =  []
              word = ""
              for word in imp[imp.index(token):]:
                if word == "line-end":
                  break
                else:
                  line.append(word)
              if state =="d":
                debug+="Print found, info:"+" ".join(line)
                print("Print found, info:"," ".join(line))
              finalcode += " "+str(rev_bit)+" "
          else:
            if token in tokenizer.operators:
              finalcode += "\n"
            if token == "line-end":
              if imp[imp.index(token)-1] in tokenizer.operators:
                finalcode += "\n"
              else:
                finalcode += ";\n"
            else:
              if state =="d":
                print(rev_bit)
              finalcode += " "+str(rev_bit)+" "
        else:
          revoval = "no"
          finalcode += " "+str(token)+" "
        if state =="d":
          debug+=("\n--- > Token: " + token + (' ' * (15-len(token)))  + "<---- " + revoval + (' ' * (4-len(revoval))) + "||| " + str(rev_bit)+"\n")
          print("--- > Token: " + token + (' ' * (15-len(token)))  + "<---- " + revoval + (' ' * (4-len(revoval))) + "||| " + str(rev_bit))
      if state =="d":
        print(finalcode)
      f.write(finalcode)
      f.write("\nreturn 0;\n}")
      f.close()
      f= open("build/debug.txt","w+")
      f.write(debug)
      f.close()
