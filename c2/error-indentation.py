    # Indentation error(字下げエラー)
# Pythonは字下げでブロックを明示する為、字下げズレがエラーの原因になる。
# エラーとして起き易いのは字下げが混濁してエラーではなく意図しない挙動になるパターン。
boolean = True
if boolean:
print("Trueだよ")   # この行のインデントがおかしい