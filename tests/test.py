from pywinauto.application import Application

# Run a target application
app = Application().start("notepad.exe")
# Select a menu item
app.UntitledNotepad.menu_select("帮助->关于记事本")
# Click on a button
app.关于记事本.OK.click()  # wrong
# Type a text string
app.UntitledNotepad.Edit.type_keys("pywinauto Works!", with_spaces=True)
