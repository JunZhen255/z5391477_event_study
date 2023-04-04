lst1 = ['a']

lst2 = ['b', lst1]

lst2[1].append('c')
print(lst2)
print(lst1)

lst1 = ['a']
lst3 = ['b',['a']]
lst3[1].append('c')
print(lst1)

happy = False
if happy is True:
    print('i am happy')
print('this will print regardless of the value of happy')

happy = True
very_happy = True
if happy is True:
    print('i am happy')
    if very_happy is True:
        print('actually I am very happy!')
print('this will print regardless of the value of happy')


happy = True
if happy:
    print('i am happy')

1 == True

1 is True

var1 ='a'
var2 = 'a'
var3 = ['a']
var4 = ['a']

print(var1 == var2)

print(var1 is var2)

print(var3 == var4)

print(var3 is var4)

b = False
if b is True:
    print('b is True')
else:
    print('b is not true')

a = 0
b = True
if a != 0:
    print('a is non-zero')
elif b is True:
    print ('b is true')
elif a < 0 and b is True:
    print('a is negative and b is True')
else:
    print('none of the condition above hold')

a = -1
b = True
if a != 0:
    print('a is non-zero')
elif b is True:
    print ('b is true')
elif a < 0 and b is True:
    print('a is negative and b is True')
else:
    print('none of the condition above hold')


name = input('who are you?')
print(float(name))
print('welcome to class', name)

working_hours = input('hours')
weekly_hours = int(working_hours)
rate_a = 51.45
rate_b = 88.9
if weekly_hours  <= 35:
    print(f'the rate paid for weekly working hours under or equal to 35 is {rate_a}')
elif weekly_hours  > 35:
    print(f'the rate paid for weekly working hours greater than 35 is {rate_b}')

hours = input('Enter number of hours you worked this week: ')
hours = float(hours)
normal_rate = 51.45
overload_rate = 88.9
if hours > 35:
    pay = (35 * normal_rate) + ((hours - 35) * overload_rate)
 else:
    pay = hours * normal_rate
 print(f'This weekly payment is: {pay}')


 letter_lst = ['a','b','c','d']
 for letter in letter_lst:
     print(letter)


import yfinance
start = '2020-01-01'
end = None
tickers = ["QAN.AX", "WES.AX"]
for tic in tickers:
 df = yfinance.download(tic, start, end, ignore_tz=True)
 print(df)
 tic_base = tic.lower().split('.')[0]
 df.to_csv(f'{tic_base}_stk_prc.csv')

d = {
 "beauty": True,
 "truth": True,
 "red wheelbarrow": 100000,
 5: "fingers",
}
for key in d:
 print(key)

 for even in range(0, 10, 2):
     print(f"even is now {even}")

     letters = ["a", "b", "c", "d", "e"]
     for i, x in enumerate(letters):
         print(f"letters[{i}] --> {x}")


numbers = [3, 9, 1, 5, 7, 2, 11, 0, 3, 12, 3, 15]
largest_number = numbers[0]
for number in numbers:
    if number > largest_number:
    largest_number = number
print(largest_number)

numbers = [3, 9, 1, 5, 7, 2, 11, 0, 3, 12, 3, 15]
temp_largest = numbers[0]
print('Before', temp_largest)
for number in numbers:
 if number > temp_largest:
 temp_largest = number
 print(number, temp_largest)
print(f'The largest value is {temp_largest}')

numbers = [3, 9, 1, 5, 7, 2, 11, 0, 3, 12, 3, 15]
largest = max(numbers)
print (largest)


the_sum = 0
for i in range (1,101):
    the_sum= the_sum+1
print(the_sum)

for i in range (1,4):
    for j in  range (1,4):
    if i <= j:
        print (i,j)


for even in range(0, 10, 2):
         if even > 2:
             continue
print(even)


a = "Hi"
if a:
    a("There")
print(a)

s = ['a']
if 'a' in s or 'b' not in s:
    print(True)

    l = ["Fairfield",
         "Fairfield East",
         "Fairfield Heights",
         "Fairfield West",
         "Fairlight",
         "Fiddletown",
         "Five Dock",
         "Flemington",
         "Forest Glen",
         "Forest Lodge",
         "Forestville",
         "Freemans Reach",
         "Frenchs Forest",
         "Freshwater"]

    j = [ "Forest Glen",
         "Forest Lodge",
         "Forestville",]
    for i in l:
        if i != j:
            l.remove(i)
    print(l)

    first_names = ['Dwayne', 'Ryan', 'Mark', 'Ben', 'Vin']
    middle_names = ['"The Rock"', 'Rodney', 'Robert Michael', 'Geza', None]
    last_names = ['Johnson', 'Reynolds', 'Wahlberg', 'Affleck', 'Diesel']

    for first_name in first_names:
        for middle_name in middle_names:
            for last_name in last_names:
                if not first_name != middle_name:
                    if not middle_name != last_name:
                        if not last_name != first_name:
                            print(first_names, middle_names, last_names)


l = ["Fairfield",
    "Fairfield East",
    "Fairfield Heights",
    "Fairfield West",
    "Fairlight",
    "Fiddletown",
    "Five Dock",
    "Flemington",
    "Forest Glen",
    "Forest Lodge",
    "Forestville",
    "Freemans Reach",
    "Frenchs Forest",
    "Freshwater"]

for i in l:
    if not i.startswith('Forest'):
        l.remove(i)
        print (i)

f_suburbs = dict()
f_suburbs["Fairfield"] = 18081
f_suburbs["Fairfield East"] = 5273
f_suburbs["Fairfield Heights"] = 7517
f_suburbs["Fairfield West"] = 11575
f_suburbs["Fairlight"] = 5840
f_suburbs["Fiddletown"] = 233
f_suburbs["Five Dock"] = 9356
f_suburbs["Flemington"] = None
f_suburbs["Forest Glen"] = None
f_suburbs["Forest Lodge"] = 4583
f_suburbs["Forestville"] = 8329
f_suburbs["Freemans Reach"] = 1973
f_suburbs["Frenchs Forest"] = 13473
f_suburbs["Freshwater"] = 8866

for key in f_suburbs.keys():
    if not key.startswith('Forest'):
        f_suburbs.pop(key)
        print(key)

for key_value_tuple in f_suburbs.items():
    print(f"key_value_tuple is {key_value_tuple}")


f_suburbs = dict()
f_suburbs["Fairfield"] = 18081
f_suburbs["Fairfield East"] = 5273
f_suburbs["Fairfield Heights"] = 7517
f_suburbs["Fairfield West"] = 11575
f_suburbs["Fairlight"] = 5840
f_suburbs["Fiddletown"] = 233
f_suburbs["Five Dock"] = 9356
f_suburbs["Flemington"] = None
f_suburbs["Forest Glen"] = None
f_suburbs["Forest Lodge"] = 4583
f_suburbs["Forestville"] = 8329
f_suburbs["Freemans Reach"] = 1973
f_suburbs["Frenchs Forest"] = 13473
f_suburbs["Freshwater"] = 8866

for i in f_suburbs.copy():
    if i.startswith('Forest'):
        f_suburbs.pop(i)
for key, value in list(f_suburbs.items()):
    if value is None:
        f_suburbs.pop(key)
for key, value in f_suburbs.items():
 print(f'{key}: {value}')

 for i in range(1, 101):
     if i % 3 == 0:
         i is Fizz
     if i % 5 == 0:
         i is Buzz
     if i % 3 == 0 and i % 5 == 0:
         i is FIZZ BUZZ
     print(i)

l = ["Fairfield",
    "Fairfield East",
    "Fairfield Heights",
    "Fairfield West",
    "Fairlight",
    "Fiddletown",
    "Five Dock",
    "Flemington",
    "Forest Glen",
    "Forest Lodge",
    "Forestville",
    "Freemans Reach",
    "Frenchs Forest",
    "Freshwater"]

for i in l:
    if i == l.index:
        print(f'{i}: {l(0)}')




l = ["Fairfield",
    "Fairfield East",
    "Fairfield Heights",
    "Fairfield West",
    "Fairlight",
    "Fiddletown",
    "Five Dock",
    "Flemington",
    "Forest Glen",
    "Forest Lodge",
    "Forestville",
    "Freemans Reach",
    "Frenchs Forest",
    "Freshwater"]

i = 0
for i in l:
    print(f'0: {i}')

i += 1



letters = ["a", "b", "c", "d", "e"]
# i is a counter variable
i = 0
for x in letters:
 print(f"letters[{i}] --> {x}")
 i += 1

 first_names = ['Dwayne', 'Ryan', 'Mark', 'Ben', 'Vin']
 middle_names = ['"The Rock"', 'Rodney', 'Robert Michael', 'Geza', None]
 last_names = ['Johnson', 'Reynolds', 'Wahlberg', 'Affleck', 'Diesel']

 for i in first_names:
     for j in middle_names:
         for x in last_names:
             if x == 'Johnson':
               print(i, j, x)

first_names = ['Dwayne', 'Ryan', 'Mark', 'Ben', 'Vin']
middle_names = ['"The Rock"', 'Rodney', 'Robert Michael', 'Geza', None]
last_names = ['Johnson', 'Reynolds', 'Wahlberg', 'Affleck', 'Diesel']

for i in first_names:
    for j in middle_names:
            for x in last_names:
                if x == 'Johnson':
                    if j == None:
                        print (i, x)
                    else:
                        print(i,j,x)

for i in first_names:
    for j in middle_names:
            for x in last_names:
                if x == 'Reynolds':
                    if j == None:
                        print(i, x)
                    else:
                        print(i, j, x)

for i in first_names:
    for j in middle_names:
            for x in last_names:
                if x == 'Wahlberg':
                    if j == None:
                        print(i, x)
                    else:
                        print(i, j, x)


for i in first_names:
    for j in middle_names:
            for x in last_names:
                if x == 'Affleck':
                    if j == None:
                        print(i, x)
                    else:
                        print(i, j, x)

for i in first_names:
    for j in middle_names:
            for x in last_names:
                if x == 'Diesel':
                    if j == None:
                        print(i, x)
                    else:
                        print(i, j, x)




