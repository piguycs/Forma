
def parse(token,compiles,line):
  if token.startswith('//') == True:
    if compiles == True:
      return "//"
    else:
      return "comment"
  if token.startswith('if') == True:
    if compiles == True:
      return "if"
    else:
      return "if statement"
  if token.startswith('print') == True:
    if compiles == True:
      return "printf"
    else:
      return "display a value"
  if token.startswith('line-end') == True:
    if compiles == True:
      return " "
    else:
      return " "
  if token.startswith('int') == True:
    if compiles == True:
      return " "
    else:
      return "create an integer value"
  if token.startswith('}') == True:
    if compiles == True:
      return "}"
    else:
      return "end of bracket"
  if token.startswith('{') == True:
    if compiles == True:
      return "{"
    else:
      return "start of bracket"
  if token.startswith('input') == True:
    if compiles == True:
      return " "
    else:
      return "input from keyboard"
  if token.startswith('open') == True:
    if compiles == True:
      return "fopen"
    else:
      return "open file"
  if token.startswith('read') == True:
    if compiles == True:
      return "fscanf"
    else:
      return "read all data from file"
  if token.startswith('close') == True:
    if compiles == True:
      return "fclose"
    else:
      return "close file"
  if token.startswith('main') == True:
    if compiles == True:
      return " "
    else:
      return "create a main function"
  if token.startswith('re_void') == True:
    if compiles == True:
      return "static void"
    else:
      return "create a main function"
  if token.startswith('supercoolfunction') == True:
    if compiles == True:
      return '''printf("This is an epic function to demonstrate the use cases for this easily modifiable language")'''
    else:
      return "cool function"
  else:
    return "No assinged type or value"