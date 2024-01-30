from commands.base.base_command import BaseCommand


class RemoveGroupCommand(BaseCommand):
    def execute(self):
        tgroup_id = int(self.params[0])
        self.app_data.remove_group_by_id(tgroup_id)

        return f"Group #{tgroup_id} removed"
