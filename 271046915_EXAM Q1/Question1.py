#Question1
string=input("Enter the string:")
def reverse(string):
    if len(string) >1:
        return [string[:length+1]]
    else:
        reverse(string)