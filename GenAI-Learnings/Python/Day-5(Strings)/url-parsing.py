url = 'https://www.kaggle.com/datasets'
protocol = url[:url.find(':')]
print(protocol)
dot_one = url.find('.')
dot_two = url.find('.',dot_one+1)
domain = url[dot_one+1:dot_two]
print(domain)
page_name = url[url.find('/',dot_two):]
print(page_name)
