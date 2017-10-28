#test if can be work = =
import re
test = '用户输入的字符串'
if re.match(r'字', test):
    print('ok')
else:
    print('failed')