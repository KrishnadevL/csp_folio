class palindrome:
    def palindrome(self, string):
        if string == string[::-1]:
            return "is a palindrome"
        else:
            return "is not a palindrome"

n = 1

while n == 1:
    string = input("Type a word: ")

    obj = palindrome()
    f = obj.palindrome(string)

    print(string, f)
    n = int(input("Press 1 to Try Again!  "))