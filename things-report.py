#!/usr/bin/env python3

import things

print("#Deadlines")


for task in things.deadlines():
    print('-', task['type'], task['title'], task['start_date'], task['deadline'])


for task in things.upcoming():
    print(task['type'], task['title'], task['start_date'], task['deadline'])
    # print(task)