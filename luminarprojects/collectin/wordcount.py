sent = "haiii good morning and i need a good and nice smile"
word = sent.split(" ")
print(word)
dic = { }
for words in word:
    if words not in dic:
        dic[words]=1
    else:
        dic[words] +=1
for k,v in dic.items():# to print in different line
    print(k," : ",v)   # to print continously as a  just give print(dic)