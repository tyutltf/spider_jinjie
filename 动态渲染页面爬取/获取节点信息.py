from selenium import webdriver

#获取属性
'''源码
<a href="/" class="zu-top-link-logo" id="zh-top-link-logo" 
data-za-c="view_home" data-za-a="visit_home" 
data-za-l="top_navigation_zhihu_logo">知乎</a>
'''
browser=webdriver.Chrome()
url='http://www.zhihu.com/explore'
browser.get(url)
logo=browser.find_element_by_class_name('zu-top-link-logo')
print(logo)
print(logo.text)
print(logo.get_attribute('id'))

#获取文本值
input=browser.find_element_by_class_name('zu-top-add-question')
print(input.text)

#获取其他属性
print(input.id)  #获取节点id
print(input.location)  #获取节点在页面的相对位置
print(input.tag_name)  #获取标签名称
print(input.size)  #获取节点的大小