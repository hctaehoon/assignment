input_string = input("단어를 입력해주세요":)
output_string = ''.join(sorted(input_string, reverse=True))
if input_string == output_string:
    print("회문자가 맞습니다.")
else:
    print("회문자가 아닙니다.")
