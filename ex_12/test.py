url = input('Enter url: ')
#url = "http://py4e-data.dr-chuck.net/known_by_Fikret.html";
#print(type(url))
#url = 'People that Fikret knows'

start_txt = url.find('by_')
end_txt = url.find('.html')

print(url[start_txt+3:end_txt])

#text = "X-DSPAM-Confidence:    0.8475";

#pos = text.find('0')

#print(float(text[pos:pos+6]))
