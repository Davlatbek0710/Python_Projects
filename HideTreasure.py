line1 = [" ", " ", " "]
line2 = [" ", " ", " "]
line3 = [" ", " ", " "]

Square = [line1, line2, line3]
position = input("Enter the position to hide the treasure: ")

abc = ["a", "b", "c"]
letter = abc.index(position[0].lower())
num = int(position[1]) -1
Square[letter][num] = "X"
print(Square[0])
print(Square[1])
print(Square[2])
