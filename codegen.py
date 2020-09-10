import parser
import tokengen

class compiler:
  # augments can be set here
  aug = "None"

  # build base sceleton 
  def scel(tokens):
    state="d"
    finalcode=""
    debug=open("build/debug.txt","w+")
    print("=== Building C sceleton ===")
    with open("build/temp.c","w+") as f:
      
      #translate Revo to C for compilation using parser
      print("=== Starting translation ===")
      
      f.write("#include <stdio.h> \n")
      
      
      #check keywords and display information about keywords
      if state =="d":
       print("------------" + (' ' * 15)  + "   " + "endoparse " + "||| " + "description")
       debug.write(str("------------" + (' ' * 15)  + "   " + "endoparse " + "||| " + "description"+"\n"))
      
      for token in tokens:
        #print(tokens)
        rev_bit = token[2]
          
        #print("token[1]",token[1])


        ############
        if token[1].startswith("print"):
            line =  []
            word = ""
            
            for word in tokens[tokens.index(token):]:
              #print("word =",word)
              if word[1] == "line-end":
                break
              else:
                #word = list(str(word[1]))
                finword = word[1].strip("print")
                #print("finword =",finword)
                line.append(finword)
            #print(line)
            finalcode += "\n printf"+str(line[0])+" "
            continue
        
        ########################
        # SQUARE FUNCTION
        ########################


        if token[1].startswith("sq"):
            line =  []
            word = ""
            
            for word in tokens[tokens.index(token):]:
              #print("word =",word)
              
              if word[1] == "line-end":
                break
              else:
                finword = word[1].strip("sq")
                #print("finword =",finword)
                line.append(finword)
            
            #print(line)
            finalcode += "\n sqrt"+str(line[0])+" "

        ########################
        # INPUT FUNCTION
        ########################

        if token[1].startswith("input"):
            line =  []
            word = ""
            
            for word in tokens[tokens.index(token):]:
              #print("word =",word)
              
              if word[1] == "line-end":
                break
              else:
                finword = word[1].strip("input")
                #print("finword =",finword)
                line.append(finword)
            
            #print(line)
            finalcode += "\n scanf"+str(line[0])+" "

        ########################
        # Main FUNCTION
        ########################


        if token[1].startswith("main"):
            line =  []
            word = ""
            
            for word in tokens[tokens.index(token):]:
              #print("word =",word)
              
              if word[1] == "line-end":
                break
              else:
                finword = word[1].strip("main")
                #print("finword =",finword)
                line.append(finword)
            
            #print(line)
            finalcode += "\n int main()"+str(line[0])+" "


        ############
        
        else:
          if token[1] == "line-end":
            #print(tokens)
            #print(tokens[tokens.index(token)-1])
            #input()
            if tokens[tokens.index(token)-1][1] in tokengen.token_data.operators:
              finalcode += "\n"
            else:
              finalcode += ";\n"
          
          else:
            #if state =="d":
            #  print(rev_bit)
            if rev_bit == None:
              finalcode += " "+str(token[1])+" "
            else:
              if rev_bit.startswith("//"):
                finalcode+=""
                continue
              finalcode += " "+str(rev_bit)+" "
        
        if state =="d":
          debug.write(str("--- > Token: " + token[1] + (' ' * (15-len(token[1])))  + "<---- " + "||| " + str(rev_bit)+"\n"))
          print("--- > Token: " + token[1] + (' ' * (15-len(token[1])))  + "<---- " + "||| " + str(rev_bit))
      
      #if state =="d":
        #print(finalcode)
      f.write(finalcode)
      f.close()