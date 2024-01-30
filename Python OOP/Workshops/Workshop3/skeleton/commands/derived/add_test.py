from commands.base.base_command import BaseCommand
from models.test_group import TestGroup


class AddTestCommand(BaseCommand):

    def execute(self):
        tgroup_id, descrp = self.params
        tgroup_id = int(tgroup_id)
        tst = self.app_data.create_and_add_test_to_tgroup(tgroup_id, descrp)

        return f"Test #{tst.id} added to group #{tgroup_id}"
