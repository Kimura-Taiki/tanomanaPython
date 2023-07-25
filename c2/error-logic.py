    # Logic error(論理エラー)
# エラー自体は起きないが挙動が意図したものと違うというエラー。
# 一番良く起きて一番厄介なエラー。
lives = 3
print("Your Lives is " + str(lives))
print("You lost a life!")
print("Your Lives is " + str(lives))
lives -= 1  # この行は残りライフの数を数える前に入れておくべきだった