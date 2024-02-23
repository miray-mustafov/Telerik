from commands.base.base_command import BaseCommand


class ViewSystemCommand(BaseCommand):
    def execute(self):
        view_system = self.app_data.view_system()

        return view_system
