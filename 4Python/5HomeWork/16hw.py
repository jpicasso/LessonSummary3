
# write and read files

# In [ ]:


#writing files
s = 'hello world'
alist = [100,200,300,400,500]
with open('myfile.txt', 'w') as my_file:
    my_file.write(s)
    for i in range(0,len(alist),1):
        my_file.write("\n"+str(alist[i]))

# #convert text file into a list of words
x = 0
with open('article.txt', "r", encoding='utf8') as my_file:
    list_of_words = my_file.read().lower().split()
    for i in list_of_words:
        if i == 'the':
           x+=1

print(x) 

