this_is_variable = 10
and_this_is_another_variable = "Hello!"

print("Py" "thon")
print("Wa" " " "Sans")
print("what" "the" "fuck" "how" "it" "is" "possible")
print(10 * "a")
print("'i am done.'")

# (3 * "a") "no"
# there goes syntax error
# does not work with variable and etc

this_works = "\r\nThis works "
this_works += "Like C# and Node"

print(this_works)

print(this_works[2])
print(this_works[3])
print(this_works[4])
print(this_works[5])

print(this_works[7:13])
print(this_works[14:])

word = "This"

print(word[-4:]) # mirrored?


print(word[:2] + word[2:])
# 시작 위치는 포함되는데, 종료 위치는 포함되지 않음

#  +---+---+---+---+---+---+
#  | P | y | t | h | o | n |
#  +---+---+---+---+---+---+
#  0   1   2   3   4   5   6
# -6  -5  -4  -3  -2  -1   0

s = "superlongenglishword"

# print(len(s))

# a, b = 0, 1
# while a < 10:
#    print(a)
#    a, b = b, a + b

a = 0
while a < 10:
   print(a, end=" ")
   a = a + 1