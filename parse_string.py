
str = "[{'author': 'Tom', 'message': 'Hi Isabelle, this is Tom', 'date': datetime.datetime(2023, 11, 23, 20, 8, 31, 745000)}, {'author': 'Isabelle', 'message': 'Hi Tom, this is Isabelle', 'date': datetime.datetime(2023, 11, 23, 20, 18, 32, 478000)}]"

list =str.split('},')

messages = []

for x in list:
    list2 = x.split(',')
    msg = list2[1]
    messages.append(msg)

for x in messages:
    print(x)