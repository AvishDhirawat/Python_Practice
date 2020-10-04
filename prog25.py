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
