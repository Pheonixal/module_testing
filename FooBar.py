def foobarqix(num):
    answer = ''
    if num % 3 == 0:
        answer = answer + "Foo"
    elif num % 5 == 0:
        answer = answer + "Bar"
    elif num % 7 == 0:
        answer = answer + "Qix"
    else:
        return num
    for i in str(num):
        if i == '3':
            answer = answer + "Foo"
        elif i == '5':
            answer = answer + "Bar"
        elif i == '7':
            answer = answer + "Qix"
    print(num, answer)
    return answer

def in_range(start, end):
    for number in range(start,end):
        foobarqix(number)

in_range(1,100)