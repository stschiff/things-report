./things-report.py > /tmp/todos.md
pandoc -o /tmp/todos.html --template template.html --metadata title="Things Report" /tmp/todos.md
open /tmp/todos.html