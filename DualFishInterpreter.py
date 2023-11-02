print("----------=Dualfish Interpreter V0.7=----------\n <==> Type 'help' for a list of commands! <==>")
#Pre defined values
Register1 = 0
Register2 = 0
RegisterChoice = 0 #current register
RegisterAlt = 1 #non selected register
SelectedRegister = [Register1, Register2]
Alphabet = [" ","a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
SymbolAlphabet = [" ","`","~","!","@","#","$","%","^","&","*","(",")","-","_","=","+","[","{","]","}","\\\\","|",";",":","'",'"',",","<",".",">","/","?","Σ","Δ"]
run = True
while run:
    print("")
    User_Input = input("DuFi>> ").lower()
    if User_Input == "help":
        print("Commands:\ni = increment current register by 1\nd = decrement current register by 1\ns = square current register\nc = cube current register\n* = double current register\n+ = add registers together (into the selected register)\n- = subtract unselected register from selected register\nf = flip the +- signs of a value\no = output selected register\n0 = output both registers side by side\na = output alphabetical character (space is 0) (1-26 lowercase) (27 - 52 uppercase)\n< = switch to register1\n> = switch to register2\nr = resets both registers to 0\ne = stop/end the program")
    else:
        if User_Input == "g":
            try:
                User_Input = input("File Name: ")
                with open(User_Input+".dufi") as file:
                    User_Input = file.read()
            except FileNotFoundError:
                print("File Not Found! is it in the same directory as the interpreter?")

        for i in User_Input:
            if i == "i": #increment reg
                SelectedRegister[RegisterChoice] += 1
            elif i == "d": #decrement reg
                SelectedRegister[RegisterChoice] -= 1
            elif i == "s": #square reg
                SRvalue = SelectedRegister[RegisterChoice]
                SelectedRegister[RegisterChoice] = SRvalue * SRvalue
                #SelectedRegister[RegisterChoice] *= SelectedRegister[RegisterChoice]
            elif i == "c": #cube reg
                SRvalue = SelectedRegister[RegisterChoice]
                SelectedRegister[RegisterChoice] = SRvalue * SRvalue * SRvalue
            elif i == "o": #output selected reg
                print(SelectedRegister[RegisterChoice], end="")
            elif i == "0": #output both reg
                print(SelectedRegister)
            elif i == "a": #output alphabetical character from selected reg
                SRvalue = SelectedRegister[RegisterChoice]
                print(Alphabet[SRvalue], end="")
            elif i == "*": #double selected reg
                SelectedRegister[RegisterChoice] = SelectedRegister[RegisterChoice]*2
            elif i == "+": #add reg values
                SRvalue = SelectedRegister[RegisterChoice]
                ARvalue = SelectedRegister[RegisterAlt]
                SelectedRegister[RegisterChoice] = SRvalue + ARvalue
            elif i == "-": #subtract reg values
                SRvalue = SelectedRegister[RegisterChoice]
                ARvalue = SelectedRegister[RegisterAlt]
                SelectedRegister[RegisterChoice] = SRvalue - ARvalue
            elif i == "f": #converts the register from negative to positive, or vise versa
                SRvalue = SelectedRegister[RegisterChoice]
                if SRvalue < 0:
                    SRvalue = abs(SRvalue)
                elif SRvalue > 0:
                    SRvalue = -abs(SRvalue)
                else:
                    pass
                SelectedRegister[RegisterChoice] = SRvalue
            elif i == "<": #set reg to 1
                RegisterChoice = 0
                RegisterAlt = 1
            elif i == ">": #set reg to 2
                RegisterChoice = 1
                RegisterAlt = 0
            elif i == "r": #reset values
                SelectedRegister = [Register1, Register2]
            elif i == "e": #end/exit program
                run = False
            elif i == " " or "  ": #ignore whitespace
                pass
            else: #throw an error
                print("Unrecognized Character Detected!")