def reverse(s): 
  str = "" 
  for i in s: 
    str = i + str
  return str


def reverseWords(input): 
      
    # split words of string separated by space 
    inputWords = input.split(" ") 
    inputWords=inputWords[-1::-1] 
  
    # now join words with space 
    output = ' '.join(inputWords) 
      
    return output 
s = str(input("Input: "))
#s = "thammu darling  lets go"
print ("Output  : ",end="") 
#print (reverse(s)) 

print(reverseWords(reverse(s)))