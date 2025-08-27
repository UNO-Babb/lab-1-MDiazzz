#MadLib.py
#Name: Michelle
#Date: 8/27/2025
#Assignment: Mad Lib

def main():
  print("Madlib")
  #Ask user for words
  Adjective = input("write an adjective: ")
  Noun = input("write a noun: ")
  Object = input("write an object: ")
  Verb = input("write a verb: ")
  Adverb = input ("write an adverb: ")
  Plural_Noun = input ("write a plural noun: ")
  #Print the story with the user supplied words.
  print("The " + Adjective + " cat jumped over the " + Noun + " and found a/an " + Object)
  print("It turned out it was an magical object that gave him the ability to " + Verb + "more " + Adverb) 
  print("He was the only one to percieve this ability and believed it helped him acquire " + Plural_Noun + " more easily")

#Call the main function if this is the file being run.
if __name__ == '__main__':
    main()
