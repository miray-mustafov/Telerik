import unittest
from core.command_factory import CommandFactory
from unittest.mock import Mock
from core.models_factory import ModelsFactory
from commands.add_test_group import AddTestGroupCommand
from commands.add_test_run import AddTestRunCommand
from commands.remove_group import RemoveGroupCommand
from commands.test_report import TestReportCommand
from commands.view_group import ViewGroupCommand
from commands.view_system import ViewSystemCommand
from core.application_data import ApplicationData
from commands.add_test import AddTestCommand
from core.models_factory import ModelsFactory
from errors.application_error import ApplicationError


class Commands:
    addtest = 'addtest'
    addtestgroup = 'addtestgroup'
    removegroup = 'removegroup'
    addtestrun = 'addtestrun'
    testreport = 'testreport'
    viewgroup = 'viewgroup'
    viewsystem = 'viewsystem'
    invalid = 'invalid'


cmd = Commands


class CommandFactory_Should(unittest.TestCase):
    def test_init_sets_attributes(self):
        data = Mock()
        cmd_factory = CommandFactory(data)
        self.assertEqual(data, cmd_factory._app_data)
        self.assertIsInstance(cmd_factory._models_factory, ModelsFactory)

    def test_create_addtest_returns_instanceOf_AddTestCommand(self):
        cmd_factory = CommandFactory(Mock())
        command = cmd_factory.create(cmd.addtest)

        self.assertIsInstance(command, AddTestCommand)

    def test_create_addtestgroup_returns_instanceOf_AddTestGroupCommand(self):
        cmd_factory = CommandFactory(Mock())
        command = cmd_factory.create(cmd.addtestgroup)

        self.assertIsInstance(command, AddTestGroupCommand)

    def test_create_removegroup_returns_instanceOf_RemoveGroupCommand(self):
        cmd_factory = CommandFactory(Mock())
        command = cmd_factory.create(cmd.removegroup)

        self.assertIsInstance(command, RemoveGroupCommand)

    def test_create_addtestrun_returns_instanceOf_AddTestRunCommand(self):
        cmd_factory = CommandFactory(Mock())
        command = cmd_factory.create(cmd.addtestrun)

        self.assertIsInstance(command, AddTestRunCommand)

    def test_create_testreport_returns_instanceOf_TestReportCommand(self):
        cmd_factory = CommandFactory(Mock())
        command = cmd_factory.create(cmd.testreport)

        self.assertIsInstance(command, TestReportCommand)

    def test_create_viewgroup_returns_instanceOf_ViewGroupCommand(self):
        cmd_factory = CommandFactory(Mock())
        command = cmd_factory.create(cmd.viewgroup)

        self.assertIsInstance(command, ViewGroupCommand)

    def test_create_viewsystem_returns_instanceOf_ViewSystemCommand(self):
        cmd_factory = CommandFactory(Mock())
        command = cmd_factory.create(cmd.viewsystem)

        self.assertIsInstance(command, ViewSystemCommand)

    def test_create_raiseError_when_invalid_command_given(self):
        cmd_factory = CommandFactory(Mock())
        with self.assertRaises(ApplicationError):
            cmd_factory.create(cmd.invalid)
