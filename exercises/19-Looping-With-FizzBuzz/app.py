def fizz_buzz():
    # your code here
    for x in range(100):
        idx = x+1
        if idx%3 == 0 and idx%5 == 0:
            print("FizzBuzz")
        elif idx%3 == 0:
            print("Fizz")
        elif idx%5 == 0:
            print("Buzz")
        else: 
            print(idx)
            
fizz_buzz()