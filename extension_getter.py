filename = input ("What's the filename? ")
extension = filename.split(".")
#note that in order to represent an object from a class as a string, use "repr".
print("The file extension is: ", repr(extension[-1]))
