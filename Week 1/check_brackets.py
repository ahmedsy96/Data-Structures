# python3

from collections import namedtuple

Bracket = namedtuple("Bracket", ["char", "position"])


def are_matching(left, right):
    return (left + right) in ["()", "[]", "{}"]


def find_mismatch(text, sayac):
    sayac1 = 0
    
    opening_brackets_stack = []
    for i, next in enumerate(text,1):

        if next in "([{":
            if len(opening_brackets_stack)==0:
                opening_brackets_stack.append(next)
                sayac = i
                sayac1=sayac
            else :
                opening_brackets_stack.append(next)
                sayac =sayac1
                

            pass

        if next in ")]} " :
            # Process closing bracket, write your code here
             if len(opening_brackets_stack)> 0:
                 
                if opening_brackets_stack[-1] == "[" and next == "]":
                
                     opening_brackets_stack.pop()
                     
                     
                elif opening_brackets_stack[-1] == "(" and next == ")":
                
                    opening_brackets_stack.pop()
                    
                    
                elif opening_brackets_stack[-1] == "{" and next == "}":
                
                    opening_brackets_stack.pop()
                else : 
                    sayac = i
                    break

             else:
                opening_brackets_stack.append(0)
                sayac = i 
                break
                
            
                
             
        

            
            
    if len(opening_brackets_stack)==0 : 
        return "Success" 
    else : 
        return (sayac)


def main():
    sayac = 0
    text = input()
    mismatch = find_mismatch(text,sayac)
    # Printing answer, write your code here
    print(mismatch)


if __name__ == "__main__":
    main()
