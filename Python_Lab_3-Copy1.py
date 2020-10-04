#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# def fibbo(no_of_terms):
    sum_no=0
    temp1=0
    temp2=1
    i=0
    print(temp1,end=" ")
    while i<no_of_terms:
        if(temp1<2):
            temp1=temp1+1
            print(temp1,end=" ")
        else:
            sum_no=temp1+temp2
            temp1=temp2
            temp2=sum_no
            print(sum_no,end=" ")
        i=i+1


# In[42]:


no_of_terms=int(input("Enter the Number of Terms : "))
fibbo(no_of_terms)


# In[49]:


#WAP to print Fibonnacci series using Reccursion
def fibbo(n):
    if(n<2):
        return n;
    else:
        return (fibbo(n-1)+fibbo(n-2));
for i in range(no_of_terms):
    print(fibbo(i),end=" ")


# In[54]:


x=int(input("Enter a Number : "))
z = lambda x: x**3
z(x)


# In[55]:


import sys
a=sys.argv
print(a)


# In[62]:


str1="Hello World"


# In[63]:


str1.upper()


# In[64]:


str1.replace('h','H')


# In[65]:


str1.replace('l','L')


# In[66]:


str1.replace('l','L',1)


# In[80]:


str1.index('l')


# In[81]:


str1.find('d')


# In[82]:


str1.find('a')


# In[83]:


str1.index('a')


# In[88]:


str1="Barry_Allen"
str2="Barry_Allen"


# In[89]:


id(str1)


# In[90]:


id(str2)


# In[91]:


# Take a String as a Input if Entered string exists in Already defined string then print string exist otherwise not
# Write a function count_letter with two parameters words and letters and count number of occurance of that latter in the word
# Write a func Change_Case which change case of all the letters 
# Write a func Count_Vowels with 1 Parameters i.e. words and count number of occurance of vowels and change each vowel with specific letter i.e x
# Write a func Mirror_Text with 2 parameters (str1,str2) and display output in given form str1str1str2str2|str2str2str1str1


# In[111]:


str1=" My name is Barry_Allen"
str2="And I am the Fastest Man Alive"


# In[112]:


str3=input("Enter a String : ")


# In[113]:


if(str3 in str2 or str3 in str1):
    print(str3)
# print(id(str3))


# In[115]:


def Count_Letter(word,letter):
    count=0
    for i in range(len(word)):
        if(letter==word[i]):
            count=count+1
    print("Count = ",count)


# In[117]:


word=input("Enter a Word : ")
letter=input("Enter a Letter : ")
Count_Letter(word,letter)


# In[123]:


def Change_Case():
    simple_str=input("Enter a String : ")
    changed_str=simple_str.swapcase()
    print(changed_str)


# In[124]:


Change_Case()


# In[142]:


def Count_Vowels(word):
    a,e,i,o,u=0,0,0,0,0
    word=input("Enter a Word : ")
    for j in range(len(word)):
        if(word[j]=='a' or word[j]=='A'):
            a=a+1
        elif(word[j]=='e' or word[j]=='E'):
            e=e+1
        elif(word[j]=='i' or word[j]=='I'):
            i=i+1
        elif(word[j]=='o' or word[j]=='O'):
            o=o+1
        elif(word[j]=='u' or word[j]=='U'):
            u=u+1
    print("Occurance of Vowels:\n a = {} e = {} i= {} o = {} u = {}".format(a,e,i,o,u))


# In[143]:


Count_Vowels(word)


# In[145]:


def Mirror_Text(str1,str2):
    print(str1,str1,str2,str2,end="")
    str1=str1[::-1]
    str2=str2[::-1]
    print(str2,str2,str1,str1)


# In[149]:


str1=input("Enter String 1 : ")
str2=input("Enter String 2 : ")


# In[150]:


Mirror_Text(str1,str2)


# In[ ]:




