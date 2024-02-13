from core.command_factory import CommandFactory
from core.engine import Engine

cmd_factory = CommandFactory()
engine = Engine(cmd_factory)

engine.start()
