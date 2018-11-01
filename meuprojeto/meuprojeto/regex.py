import re

url = 'www.site.com/clientes/17686'
end = re.split(r'(clientes)/(?P<id>\d+)', url)
print(end)