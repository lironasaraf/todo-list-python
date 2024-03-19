import unittest
from tkinter import Tk
from tkinter.test.support import destroy_default_root
from main import TaskListApp, END

class TestTaskListApp(unittest.TestCase):
    def setUp(self):
        self.root = Tk()
        self.app = TaskListApp(self.root, 600, 410, 390, 160, 'ToDo List')
        self.app.draw_widgets()

    def test_add_task(self):
        initial_task_count = self.app.listbox.size()
        self.app.entry.insert(0, "Test Task")
        self.app.add_task()
        self.assertEqual(self.app.listbox.size(), initial_task_count + 1)

    def test_delete_task(self):
        self.app.listbox.insert(END, "Test Task")
        initial_task_count = self.app.listbox.size()
        self.app.listbox.select_set(0)
        self.app.delete_task()
        self.assertEqual(self.app.listbox.size(), initial_task_count - 1)

    def test_clear_tasks(self):
        self.app.listbox.insert(END, "Test Task 1")
        self.app.listbox.insert(END, "Test Task 2")
        self.app.clear_tasks()
        self.assertEqual(self.app.listbox.size(), 0)


    def tearDown(self):
        destroy_default_root()

if __name__ == '__main__':
    unittest.main()
