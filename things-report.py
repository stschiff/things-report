#!/usr/bin/env python3

import things

print("# Deadlines\n")

for task in things.deadlines():
    print('- [ ]', task['type'], task['title'], task['start_date'], task['deadline'])
print("")

print("# Upcoming\n")

for task in things.upcoming():
    print('- [ ]', task['type'], task['title'], task['start_date'])
print("")

print("# Digital\n")

for t in ["Digital", "coding", "schreiben", "Recherche", "Email/Chat"]:
    print("##", t, "\n")
    for task in things.tasks(tag=t):
        print('- [ ]', task['title'])
    print("")

for t in ["planen/denken", "lesen", "Anrufe", "unterwegs 🏃🏽", "daheim 🏡",
          "Institut 🏢", "Warten auf ⌛️"]:
    print("#", t, "\n")
    for task in things.tasks(tag=t):
        print('- [ ]', task['title'])
    print("")
