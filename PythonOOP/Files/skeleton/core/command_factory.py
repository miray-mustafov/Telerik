from commands.create_directory import CreateDirectoryCommand
from commands.create_file import CreateFileCommand
from commands.delete_file import DeleteFileCommand
from commands.append_text import AppendTextCommand
from commands.read_file import ReadFileCommand
from commands.list_files import ListFilesCommand
from commands.count_files import CountFilesCommand
from commands.count_lines import CountLinesCommand


class CommandFactory:
    def create(self, input_line):
        cmd_name, *params = input_line.split()

        if cmd_name.lower() == "createdirectory":
            return CreateDirectoryCommand(params)
        if cmd_name.lower() == "createfile":
            return CreateFileCommand(params)
        if cmd_name.lower() == "appendtext":
            return AppendTextCommand(params)
        if cmd_name.lower() == "readfile":
            return ReadFileCommand(params)
        if cmd_name.lower() == "deletefile":
            return DeleteFileCommand(params)
        if cmd_name.lower() == "listfiles":
            return ListFilesCommand(params)
        if cmd_name.lower() == "countfiles":
            return CountFilesCommand(params)
        if cmd_name.lower() == "countlines":
            return CountLinesCommand(params)

        raise ValueError(f'No such command: {cmd_name}')
