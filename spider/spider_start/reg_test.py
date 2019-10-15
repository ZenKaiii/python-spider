import re

#提取字符串
#替换
#搜索

info = "姓名:zzz 生日:1999年2月27日 本科:2017年9月1日"

# print(re.findall("\d{4}",info))
# print(re.match(".*生日.*\d{4}",info)) #match从字符串最开始匹配
# print(re.search("生日.*\d{4}",info))

match_result = re.match(".*生日.*?(\d{4}).*本科.*?(\d{4})",info)
print(match_result.group(1))
print(match_result.group(2))

result = re.sub("\d{4}","2019",info)
print(info)
print(result)

name = "my name is ZenKai"
print(re.search("zenkai",name ,re.IGNORECASE).group())

name = """
my name is
zenkai
"""
print(re.search("zenkai",name ,re.DOTALL).group())
