print("----------=Dualfish Interpreter V1.0=----------\n <==> Type 'help' for a list of commands! <==>\n    <==> Type 'g' to run a .dufi file! <==>    ")
Register1 = 0
Register2 = 0
CurRegChoice = 0 #current register
AltRegChoice = 1 #non selected register
SR = [Register1, Register2] #selected register
Alphabet = [[" ","a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"], [" ","`","~","!","@","#","$","%","^","&","*","(",")","-","_","=","+","[","{","]","}","\\\\","|",";",":","'",'"',",","<",".",">","/","?","Σ","Δ"," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "]]
AlphORSymb = 0
CommentMode = False
run = True
while run:
    print("")
    User_Input = input("DuFi>> ").lower()
    if User_Input == "help":
        print("Functions:\ni = increment current register by 1\nd = decrement current register by 1\ns = square "
              "current register\nc = cube current register\n* = double current register\n+ = add registers together ("
              "into the selected register)\n- = subtract unselected register from selected register\n\no = output "
              "selected register\n0 = output both registers side by side\na = output alphabetical character (space is "
              "0) (1-26 lowercase) (27 - 52 uppercase)\n^ = switch 'a' to symbol-mode (1-34 symbols)\nv "
              "= switch 'a' back to alphabet-mode\n\n< = switch to register1\n> = switch to register2\nr = resets both "
              "registers to 0\n\n'=' = the start and end of a comment\n: = user input (INT)\ng = run a program\ne = stop/end the program")
    else:
        if User_Input == "g":
            try:
                User_Input = input("File Name: ")
                with open(User_Input+".dufi") as file:
                    User_Input = file.read()
            except FileNotFoundError:
                print("File Not found! Is it in the same directory as this application?")

        for i in User_Input:
#COMMENTS (im so sorry for how shitty this system is. but it is what it is.)
            if i == "=":
                if not CommentMode:
                    CommentMode = True
                else:
                    CommentMode = False
#MATH FUNCTIONS
            if not CommentMode:
                if i == "i":  # increment reg
                    SR[CurRegChoice] += 1
                elif i == "d":  # decrement reg
                    SR[CurRegChoice] -= 1
                elif i == "s":  # square reg
                    SRvalue = SR[CurRegChoice]
                    SR[CurRegChoice] = SRvalue ** 2
                    # SR[CurRegChoice] *= SR[CurRegChoice]
                elif i == "c":  # cube reg
                    SRvalue = SR[CurRegChoice]
                    SR[CurRegChoice] = SRvalue ** 3
                elif i == "*":  # double selected reg
                    SR[CurRegChoice] = SR[CurRegChoice] * 2
# OUTPUT FUNCTIONS
                elif i == "o":  # output selected reg
                    print(SR[CurRegChoice], end="")
                elif i == "0":  # output both reg
                    print(SR)
                elif i == "a":  # output alphabetical character from selected reg
                    SRvalue = SR[CurRegChoice]
                    if SRvalue not in range(0, 52):
                        print("('a' error! value not in range!)")
                        break
                    else:
                        print(Alphabet[AlphORSymb][SRvalue], end="")
                elif i == "^":
                    AlphORSymb = 1
                elif i == "v":
                    AlphORSymb = 0
# ADV MATH FUNCTIONS
                elif i == "+":  # add reg values
                    SRvalue = SR[CurRegChoice]
                    ARvalue = SR[AltRegChoice]
                    SR[CurRegChoice] = SRvalue + ARvalue
                elif i == "-":  # subtract reg values
                    SRvalue = SR[CurRegChoice]
                    ARvalue = SR[AltRegChoice]
                    SR[CurRegChoice] = SRvalue - ARvalue
# REGISTER CONTROL FUNCTIONS
                elif i == "<":  # set reg to 1
                    CurRegChoice = 0
                    AltRegChoice = 1
                elif i == ">":  # set reg to 2
                    CurRegChoice = 1
                    AltRegChoice = 0
                elif i == "r":  # reset values
                    SR = [Register1, Register2]
# MISC FUNCTIONS
                elif i == ":": #input
                    UI = int(input("Input: "))
                    if isinstance(UI, int):
                        SR[CurRegChoice] = UI
                    else:
                        SR[CurRegChoice] = 0
                elif i == "e":  # exit program
                    run = False
                elif i == " " or "\n":  # ignore whitespace
                    pass
                else:
                    pass