#Dictionary
text=input('enter your text')
text2=text.split()
sub= {
    "good":"bad",
    "bad":"good"
}
for item in text2:
    print( sub.get(item,item) )