def bullets(chunks):
    print("bullets")
    final_string = "Your list in latex can be created with the following command: \n"
    final_string += "> \\begin{itemize} \n"
    
    for e in chunks:
        print(final_string)
        final_string += f"> \item {e} \n"
    
    final_string += "> \end{itemize}"
    return final_string

def numbers(chunks):
    print("numbers")
    final_string = "Your list in latex can be created with the following command: \n"
    final_string += "> \\begin{enumerate} \n"
    
    for e in chunks:
        print(final_string)
        final_string += f"> \item {e} \n"
    
    final_string += "> \end{enumerate}"
    return final_string

def simple_headline(chunks):
    print("simple headline")
    final_string = "Your list in latex can be created with the following command: \n"
    final_string += "> \\begin{description} \n"
    
    for e in chunks:
        print(final_string)
        final_string += "> \item["+ e + "]\hfill \\\ \n"
    
    final_string += "> \end{description}"
    return final_string