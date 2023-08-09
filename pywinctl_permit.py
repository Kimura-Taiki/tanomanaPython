# $ python
import pywinctl as pwc

print("PyWinCtl_permit.pyへ来たぞー")

# Permission設定前ならFalseになる。
pwc.checkPermissions()
# False

# # 適当なコマンドでPermission設定を出す。
# pwc.getActiveWindow()

# # Permission設定済みならTrueになる。
# pwc.checkPermissions()
# # True