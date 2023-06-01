#!/usr/bin/env python3

import things

print("#Deadlines\n")

for task in things.deadlines():
    print('-', task['type'], task['title'], task['start_date'], task['deadline'])

print("\n#Upcoming\n")

for task in things.upcoming():
    print('-', task['type'], task['title'], task['start_date'])
    # print(task)

print("\n#Digital\n")

for task in things.tasks(tag="Digital"):
    print('-', task['type'], task['title'])

print("\n#Planen / Denken\n")
for task in things.tasks(tag="planen/denken"):
    print('-', task['type'], task['title'])

print("\n#lesen\n")
for task in things.tasks(tag="lesen"):
    print('-', task['type'], task['title'])

print("\n#Anrufe\n")
for task in things.tasks(tag="Anrufe"):
    print('-', task['type'], task['title'])

print("\n#Unterwegs\n")
for task in things.tasks(tag="unterwegs 🏃🏽"):
    print('-', task['type'], task['title'])

print("\n#Daheim\n")
for task in things.tasks(tag="daheim 🏡"):
    print('-', task['type'], task['title'])

print("\n#Institut\n")
for task in things.tasks(tag="Institut 🏢"):
    print('-', task['type'], task['title'])

print("\n#Warten auf\n")
for task in things.tasks(tag="Warten auf ⌛️"):
    print('-', task['type'], task['title'])

print("\n#Agendas\n")
for task in things.tasks(tag="Agendas🕰"):
    print('-', task['type'], task['title'])
