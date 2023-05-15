#!/usr/bin/env python3

import things

for task in things.upcoming():
    print(task['type'], task['title'], task['start_date'], task['deadline'])
    print(task)