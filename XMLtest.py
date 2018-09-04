from lxml import objectify
import pandas as pd

path = 'seaborn-data/Performance_MNR.xml'
# 解析xml文件
parsed = objectify.parse(open(path))
# 获取 xml文件根节点引用
root = parsed.getroot()
print(root)
data = []
skip_fields = ['PARENT_SEQ', 'INDICATOR_SEQ',
               'DESIRED_CHANGE', 'DECIMAL_PLACES']
for elt in root.INDICATOR:
    el_data = {}
    for child in elt.getchildren():
        if child.tag in skip_fields:
            continue
        el_data[child.tag] = child.pyval
    data.append(el_data)
perf = pd.DataFrame(data)
perf.head() # 前五行
print(perf)