#!/usr/bin/env python3

import things

print('<div class="content"><div class="container">')
print('<h2 class="title is-2">Deadlines</h2>\n')

for task in things.deadlines():
    pr_tag = '<span class="tag">project</span>' if task['type'] == 'project' else ""
    project_suffix = '<span class="content is-small">  ({})</span>'.format(task['project_title']) if 'project_title' in task else ''
    print('- ', pr_tag, task['title'], project_suffix, "(**!", task['deadline'], "**)")
print("")

print('<h2 class="title is-2">Next</h2>\n')

for t in ['Full Focus🧠', 'Short Dashes⚡️', 'Kommunikation', 'Hanging around🛋️',
          'Planning/Thinking💡', 'lesen📖', 'unterwegs🏃🏽',
          'daheim🏡', 'Institut🏢', 'Warten auf⌛️',
          'Arbeitsgruppe👩‍🚀', 'Kollegen👥', 'Meetings🪧',
          'Maria🙋‍♀️', 'Tickler⏰']:
    print('<h3 class="title is-3">{}</h3>\n'.format(t))
    for task in things.anytime(tag=t):
        if task['type'] != "to-do":
            continue
        if 'heading_title' in task and (task['heading_title'] == 'Reisevorbereitung' or task['heading_title'] == "Nach der Reise"):
            continue
        if "area_title" in task and task["area_title"] == "Command Center":
            continue
        if 'project' in task and  task['project'] == 'QQCyWPKKTCYoBonE61EjkP': # this is the template project
            continue
        project_suffix = '<span class="content is-small">  ({})</span>'.format(task['project_title']) if 'project_title' in task else ''
        print('- ', task['title'], project_suffix)
    print("")

print('</div></div>')