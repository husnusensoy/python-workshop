# Simple Chat Bot
Digital personal assistants help people to drive cars, plan their day, buy something online. In a sense, they are simplified versions of artificial intelligence with whom you can talk.

In this project, you will develop step by step a simple bot that will help you study programming.

## Important Points to Note

* Ensure that your code is properly formated using **black**
* Your code follows **PEP8** rules (VsCode underlines in case of a problem)
  * Ensure that your variable names follow Python conventions (no camel type but snake)
  * Proper use of spacing

## Stage 1 (Medium)

Give a name to your bot (bot_name) and a birth_year (which is set to be 2020 ). Start with the following code block. 

```python
bot_name = 'Aid' # You can change bot's name
birth_year = 2020

# Write your code here
```


Ensure that you obtain following output

```
Hello! My name is Aid.
I was created in 2020.
```

### Hints

* Remember that starting with Python 3.x we using f-strings to interpolate variables into strings.


## Stage 2 (Hard)

Our bot learns to greet you. Now add the following capability into your code. Ensure that program prints and asks for your name 

```
Please, remind me your name.
>
```

Assuming that you provide **Jack** as your name

```
Please, remind me your name.
> Jack
```

Program prints 

```
What a great name you have, Jack!

```

### Hints

Please do start with the following Python code

```python
print('Hello! My name is Aid.')
print('I was created in 2020.')
print('Please, remind me your name.')

# reading a name

print('What a great name you have, {your_name}!')

```

* Remeber that `ìnput('prompt')`function is used to read user input string

## Stage 3  (Hard)

You bot now tries to estimate your age by using a simple bath trick. Start with the following code block and implement an age guess skill

```python
print('Hello! My name is Aid.')
print('I was created in 2020.')
print('Please, remind me your name.')

name = input()

print('What a great name you have, ' + name + '!')
print('Let me guess your age.')
print('Enter remainders of dividing your age by 3, 5 and 7.')

# reading all remainders

print("Your age is {your_age}; that's a good time to start programming!")
```


### Hints

Note that we have the following identity for ages in [0,104] range

`age = (remainder3 * 70 + remainder5 * 21 + remainder7 * 15) % 105`

So it is trivial to calculate age given the 3 remainders.

* Remember that python uses `%`operator to calculate remainder.
 

