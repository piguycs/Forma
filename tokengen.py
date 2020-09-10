import parser, re
class token_data:
  keywords = [
    "main",     # main
    "end",
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
    "close",    # close a file
    "supercoolfunction",     # does something
    "sq",        # square
    "amk"
  ]
  operators = [
    "{",        # used in functions
    "}"
  ]


  def peak_next_char(line,word,pos):
    line = line.split(" ")
    word = line[word]
    return word[pos]

class tokenizer:
  #for checking each node for integrity
  def stat_check(code):
    #put code into a list
    lines = code.readlines()
    print(len())
  def create_tokens(code):
    print("=== Starting token gen ===")
    #create an empty token list
    tokens = []
    #put code into a list
    lines = code.readlines()
    #god forbid me from touching a computer for using this method
    lines += "\n\n"
    #gen nodes based on presence
    f=0
    for i,token in enumerate(lines,start=0):
      f+=1
      #remove newlines from tokens and entries
      if "\n" in token:
        print(token)
        newline=True
      token = token.rstrip()
      #parse a token
      if token.startswith(tuple(token_data.keywords)) or token.startswith(tuple(token_data.operators)):
        match  = set(token).intersection(set(token_data.keywords))
        a = re.search(r'\b('+str(match)+')\b', token)
        if a != None:
          token = token[a.start():]
        parse_data = parser.parse(token,True,None)
        print("parsed",token,"data =",parse_data)
        #tokens.append([f,"line-end",None])
      else:
        parse_data = None
      #check for line-end
      if newline == True:
        tokens.append([f,"line-end",None])
        newline = False
      #create a 2d array for each token
      tokens.append([i,token,parse_data])
    #append new line for last entry
    tokens.append([f,"line-end",None])
    return tokens