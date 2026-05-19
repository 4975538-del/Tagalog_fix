import re

# 检查修复后的文件
with open('vocabulary_fixed_safe.js', 'r', encoding='utf-8') as f:
    content = f.read()

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