def domain_name(url):
    tmp = ['https://', 'http://', 'www.']
    for _ in tmp:
        url = url.replace(_, '')
    url = url.split('.')
    return url[0]

print(domain_name("http://github.com/carbonfive/raygun"))
print(domain_name("http://google.com"))
print(domain_name("http://www.zombie-bites.com"))
print(domain_name("http://google.co.jp"))
print(domain_name("www.xakep.ru"))
print(domain_name("https://youtube.com"))