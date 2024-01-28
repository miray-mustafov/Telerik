from commands.base.base_command import BaseCommand


class TestReportCommand(BaseCommand):
    def execute(self):
        test_id = int(self.params[0])
        report = self.app_data.report_test(test_id)

        return report
