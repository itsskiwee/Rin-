import time
import os
import platform
from core.identity import load_identity
from tools.system import on_directory_change
from logs.logger import log
from memory.memory import store, recall
from tools.tasks import init_tasks, add_task, get_tasks
from core.scheduler import next_interval
from tools.email import fetch_unread_emails
init_tasks()
identity = load_identity()

def fetch_upcoming_events():
    return[]

def observe():
    emails = fetch_unread_emails()
    events = fetch_upcoming_events()
    context = {
        "time": time.strftime("%Y-%m-%d %H:%M:%S"),
        "cwd": os.getcwd(),
        "platform": platform.system(),
        "user": os.getenv("USER"),
        "emails": emails,
        "events": events,
    }
    if emails:
        log(f"Observed {len(emails)} new emails")
    if events:
        log(f"Observed {len(events)} upcoming events")
    return context
  
def think(context):
    print("\nThinking with identity:")
    print(identity)
    last = recall("last_context")
    print("\nLast remembered context:")
    print(last)
    print("\nObserved context:")
    for k, v in context.items():
        print(f"-{k}: {v}")
    if last and last.get("cwd") != context.get("cwd"):
        decision = "directory_changed"
    else:
        decision = "no_change"
    print("\nDecision", decision)
    log(f"Decision made: {decision}")
    return decision

def act(decision, context):
    log(f"Action executed: {decision}")
    if decision == "directory_changed":
        last = recall("last_context")
        title = f"Directory changed from{last.get('cwd')} to {>
        add_task(title)
        print("Acting: noticed directory change")
        on_directory_change(last.get("cwd"), context.get("cwd">
    else:
        print("Acting: nothing to do")
    tasks = get_tasks()
    if tasks:
        print("\nPending tasks:")
        for task in tasks:
            print(f"- [{task[0]}] {task[1]}")

while True:
    context = observe()
    decision = think(context)
    act(decision, context)
    store("last_context", context)
    time.sleep(5)


