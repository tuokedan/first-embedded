x = input('请输入一行字符：')
alpha = 0
empty = 0
number = 0
el = 0
for i in x:
    if i.isalpha():
        alpha +=1
    elif i == ' ':
        empty +=1
    elif i.isdigit():
        number +=1
    else:
        el +=1

print('该行字符中字母的个数是：{}'.format(alpha))
print('该行字符中空格的个数是：{}'.format(empty))
print('该行字符中数字的个数是：{}'.format(number))
print('该行字符中其它字符的个数是：{}'.format(el))







