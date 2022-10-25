alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
while True:
    decision  = input("Do you want to 'encode' or 'decode' a message:\t")

    def enrypt(message,shift):
        i=0
        test = len(message)
        final_ceaser =''
        for c in message:
            letter = alphabet.index(c)
            new_letter = letter + shift
            ceaser = alphabet[new_letter]
            final_ceaser +=ceaser
        print(f"this is the encrypted message is {final_ceaser}")

    def decrypt(text,shift):
        test = len(text)
        final_ceaser=''
        #print("this is the encrypted message")
        for c in text:
            letter = alphabet.index(c)
            new_letter = letter - shift
            ceaser = alphabet[new_letter]
            final_ceaser +=ceaser
        print(f"the decypted message is {final_ceaser}")
        
    if decision == 'encode':
        message = input(f"enter the messsage to {decision} : ").lower()
        shift_number = eval(input("enter th shift variable:  "))
        for i in alphabet:
            if message not in alphabet:
                print("wrong variable")
                exit()
        enrypt(message=message,shift=shift_number)
        
    elif decision == 'decode':
        message = input(f"enter the messsage to {decision} : ").lower()
        shift_number = eval(input("enter th shift variable:  "))
        decrypt(text=message,shift=shift_number)
    else:
        print("unknown choice")