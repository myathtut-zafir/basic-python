import re
tex="Ths is agene phone is 408-555-1234. Call Soon !"
pattern='phone'
print(re.search(pattern,tex))
# pattern='NOT'
match=re.search(pattern,tex)
print(match.span()) # type: ignore
print(match.start()) # type: ignore
tex='my phone once,my phone twice'
match=re.findall('phone',tex)
for ma in re.finditer('phone',tex):
    print(ma.span())

phone= "my phone is 408-222-1234"
# ph=re.search('\d\d\d-\d\d\d-\d\d\d\d',phone)
# ph=ph.group()
# print(ph)
ph=re.search(r'\d{3}-\d{3}-\d{4}',phone)
print(ph)
phone_pattern=re.compile(r'(\d{3})-(\d{3})-(\d{4})')
result=re.search(phone_pattern,phone)
print(result.group(1))
#quantifiers
