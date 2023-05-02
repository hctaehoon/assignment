input_string = input("단어만 입력:")
output_string = ''.join(input_string[::-1])
if input_string == output_string:
    print("회문자가 맞습니다.")
else:
    print("회문자가 아닙니다.")
