import urllib
from bs4 import BeautifulSoup

with open('2024_05_08_14_20.html', 'r', encoding='utf-8') as file:
    soup = BeautifulSoup(file, 'html.parser')

# 假设我们要提取所有<p>标签中的内容

# 提取具有特定ID的元素
# 例如，提取ID为"my-id"的元素
elements1 = soup.find_all(class_='text-dark')
#print(len(elements))
#print(elements.count())
total=elements1[len(elements1)-1].text
print(total)
elements2=soup.find_all(class_='text-success')
success=elements2[len(elements2)-6].text
print(success)
