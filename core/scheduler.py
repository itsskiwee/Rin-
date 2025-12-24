from pathlib import Path

def next_interval(decision):
  """
  return sleep time based on agent decision
  """
  if decision == "directory_changed":
    return 10
  else:
    return 300
