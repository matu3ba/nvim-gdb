import re

class ShowAllCommands(gdb.Command):
  """
  show all-commands

  Show GDB's complete command history.  Unlike 'show commands' this
  lists everything in GDB's command history.
  """

  def __init__(self):
    super().__init__("show all-commands", gdb.COMMAND_OBSCURE)

  def invoke(self, arg, from_tty):
    start = 1
    last_command_number = 0
    all_commands = []
    get_more = True
    while get_more:
      found_new_line = False
      output = gdb.execute(f"show commands {start}", False, True)
      for line in output.splitlines():
        g = re.search(r'^\s+(\d+)', line).group(1)
        if not g:
          break
        if int(g) <= last_command_number:
          continue
        last_command_number = int(g)
        all_commands.append(line)
        found_new_line = True
      if not found_new_line:
        break
      start = "+"

    for line in all_commands:
      print(line)

ShowAllCommands()
