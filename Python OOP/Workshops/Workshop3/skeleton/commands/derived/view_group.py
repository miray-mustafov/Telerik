from commands.base.base_command import BaseCommand


class ViewGroupCommand(BaseCommand):
    def execute(self):
        tgroup_id = int(self.params[0])
        view = self.app_data.view_group(tgroup_id)

        return view
