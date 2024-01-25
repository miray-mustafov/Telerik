from commands.base.base_command import BaseCommand


class AddTestRunCommand(BaseCommand):
    def execute(self):
        test_id, test_result, runtime_ms = self.params
        test_id = int(test_id)
        self.app_data.create_and_add_trun_to_test(test_id, test_result, runtime_ms)

        return f"TestRun registered"
