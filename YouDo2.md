Keep on implementing our chatbot

## Stage 4 (Easy)

Now you will teach your bot to count. It's going to become an expert in numbers!

In this stage, you will program the bot to count from 0 to any positive number users enter.

### Example

```python
Hello! My name is Aid.
I was created in 2020.
Please, remind me your name.
> Max
What a great name you have, Max!
Let me guess your age.
Enter remainders of dividing your age by 3, 5 and 7.
> 1
> 2
> 1
Your age is 22; that's a good time to start programming!
Now I will prove to you that I can count to any number you want.
> 5
0 !
1 !
2 !
3 !
4 !
5 !
Completed, have a nice day!
```


You don't need to repeate previous work you have done.


## Stage 5 (Hard)

Lucky tickets are a kind of mathematical entertainment. A ticket is considered lucky if the sum of the first 3 digits equals the sum of the last 3 digits of the ticket number.

You are supposed to write a program that checks whether the two sums are equal. The code snippet below displays "Lucky" if they are and "Ordinary" if they are not.

Now teach your bot to detect lucky ticket numbers by adding the missing code 


```python
print("Hi, I will detect a lucky ticket for you!!!")

ticket = ...

half1 =  ...
half2 = ...

if half1 == half2:
    print("Lucky")
else:
    print("Ordinary")

```
## Stage 6 (Easy)

You will improve your simple bot so that it can give you a test and check your answers. The test should be a multiple-choice quiz about programming with any number of options. Your bot has to repeat the test until you answer correctly and congratulate you upon completion.

Your bot can ask anything you want, but there are two rules for your output:

* the line with the test should end with the question mark character;
* an option starts with a digit followed by the dot (1., 2., 3., 4.)

If a user enters an incorrect answer, the bot may print a message:

```
Please, try again.
```

The program should stop on the correct answer and print `Congratulations, have a nice day!` at the end.

Start with the following code

```python
def greet(bot_name, birth_year):
    print('Hello! My name is ' + bot_name + '.')
    print('I was created in ' + birth_year + '.')


def remind_name():
    print('Please, remind me your name.')
    name = input()
    print('What a great name you have, ' + name + '!')


def guess_age():
    print('Let me guess your age.')
    print('Enter remainders of dividing your age by 3, 5 and 7.')

    rem3 = int(input())
    rem5 = int(input())
    rem7 = int(input())
    age = (rem3 * 70 + rem5 * 21 + rem7 * 15) % 105

    print("Your age is " + str(age) + "; that's a good time to start programming!")


def count():
    print('Now I will prove to you that I can count to any number you want.')

    num = int(input())
    curr = 0
    while curr <= num:
        print(curr, '!')
        curr = curr + 1


def test():
    print("Let's test your programming knowledge.")
    # write your code here
    print('Completed, have a nice day!')


def end():
    print('Congratulations, have a nice day!')


greet('Aid', '2020')  # change it as you need
remind_name()
guess_age()
count()
# ...
end()

```

Example output
```
Hello! My name is Aid.
I was created in 2020.
Please, remind me your name.
> Max
What a great name you have, Max!
Let me guess your age.
Enter remainders of dividing your age by 3, 5 and 7.
> 1 
> 2
> 1
Your age is 22; that's a good time to start programming!
Now I will prove to you that I can count to any number you want.
> 3
0 !
1 !
2 !
3 !
Let's test your programming knowledge.
Why do we use methods?
1. To repeat a statement multiple times.
2. To decompose a program into several small subroutines.
3. To determine the execution time of a program.
4. To interrupt the execution of a program.
> 4
Please, try again.
> 2
Congratulations, have a nice day!

```



