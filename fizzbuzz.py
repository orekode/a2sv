


def fizzbuzz(n):

    answer = []
    
    for i in range(n):
        index = i + 1
        test_3 = index % 3 == 0
        test_5 = index % 5 == 0
        test_3_5 = test_3  and test_5
        
        if(test_3_5):
            answer.append('FizzBuzz')
        elif(test_3):
            answer.append('Fizz')
        elif(test_5):
            answer.append('Buzz')
        else:
            answer.append(str(index))

    return answer


print(fizzbuzz(15))
    