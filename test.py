# import string
#
# lowAlpha = string.ascii_lowercase
# morse = [".-", "-...", "-.-.", "-..", ".", "..-.", "--.", "....", "..", ".---", "-.-", ".-..", "--", "-.", "---", ".--.", "--.-", ".-.", "...", "-", "..-", " ...-", ".--", "-..-", "-.--", "--.."]
# alpha = dict(zip(lowAlpha, morse))
# def define(dictionary, key):
#     lis = []
#     for i in key:
#         if i in dictionary:
#             lis.append(dictionary[i])
#         else:
#             lis.append(" ")
#     return " ".join(lis)
#
#
# while True:
#     _input = input("请输入英文：")
#     if _input == "exit()":
#         break
#     else:
#         print(define(alpha, _input))
text = "严"

utf8_data = text.encode("utf-8")
print(utf8_data)
for i in utf8_data:
    print(i)
binary_data = ' '.join([format(byte, '08b') for byte in utf8_data])
print(binary_data)
print(format(32, "08b"))


