import re
import sys

# 用二进制方式读取文件
with open('vocabulary_fixed_safe.js', 'rb') as f:
    content_bytes = f.read()

# 尝试解码
try:
    content = content_bytes.decode('utf-8')
except:
    content = content_bytes.decode('gbk', errors='replace')

# 搜索 goat 的条目
goat_match = re.search(r'{"tagalog":"goat".*?"grammar":"([^"]+)"', content)
if goat_match:
    grammar = goat_match.group(1)
    print('goat 的语法解析:')
    print(grammar)
    print()
    if '形容词 + ang + 名词 = 某物很...' in grammar:
        print('✓ 修复成功！')
    else:
        print('✗ 需要检查')
else:
    print('未找到 goat 条目')