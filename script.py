import re

#Extracting Domain Name and TLD

def domain_name(url):
    pattern = re.compile(r"(https?://|www\.)?(HTTPS?://|WWW\.)?(www\.)?([a-z0-9]+)?([/a-z0-9]+|[?a-z0-9]+|[-a-z0-9]+|[=&a-zA-z0-9]+[.a-zA-z0-9]+)?")
    domain_tld = pattern.sub(r"\4",url)
    return domain_tld


try:
    #Script
    
    file = open('url.txt', 'r')
    read = file.readlines()

    with open('domain_names.txt', 'w') as result:
        for url in read:
            domain = domain_name(url.lower())
            result.write(domain)          
    file.close()
    
    print("Done :)")
    
except:
    print("Error!")