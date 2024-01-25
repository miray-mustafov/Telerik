from commands.base.base_command import BaseCommand


class AddTestGroupCommand(BaseCommand):

    def execute(self):
        name = self.params[0]
        tgroup = self.app_data.add_testgroup(name)

        return f"Group #{tgroup.id} created"
