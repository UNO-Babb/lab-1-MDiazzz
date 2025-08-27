#FirstProgram.py
#Name: Michelle Diaz
#Date:8/27/2025
#Assignment: First Program

def main():
  print("First Program")
  #Say hello
  print("Hello")
  #Ask for the user's name
  Name = input("Your name: ")
  #Use the user's name in the program.
  print ("Hello" + Name)
  #Ask the user for their age.
  Age = int (input("Your age: "))
  #Tell the user what year they were born in.
  #Assume that they have not had their birthday yet this year.
  print(2025 - Age - 1)

#Call the main function if this is the file being run.
if __name__ == '__main__':
    main()
