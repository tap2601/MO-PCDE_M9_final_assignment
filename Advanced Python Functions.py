#!/usr/bin/env python
# coding: utf-8

# # Codio Coding Activity 9.3: Advanced Python *Functions*
# 
# ### Learning Outcome Addressed
# 
# - 5. Write code using advanced Python *functions*.
# 
# 
# ## Index:
# 
# - [Question 1](#Question-1)
# - [Question 2](#Question-2)
# - [Question 3](#Question-3)
# - [Question 4](#Question-4)
# - [Question 5](#Question-5)
# - [Question 6](#Question-6)
# - [Question 7](#Question-7)
# - [Question 8](#Question-8)
# - [Question 9](#Question-9)

# ## Advanced Python Functions
# 
# ## Question 1
# 
# *2 points*
# 
# Define a Python *function, `mult`*, that takes a variable number of arguments.
# 
# Your *function* should return the result of the multiplication of all the arguments passed to it.
# 
# Test your *function* with the inputs `2`, `6`, `6`, and `8`. Assign the result to *`ans1a`*.
# 
# Next, test your *function* with the inputs `5`, `10.0`, `2`, `3`, and `1`. Assign the result to *`ans1b`*.

# In[5]:


### GRADED

### YOUR SOLUTION HERE
ans1a = None
ans1b = None

def mult():
    pass
# YOUR CODE HERE

def mult(*args):
    result = 1
    for i in args:
        result = i*result
    return result

ans1a = mult(2,6,6,8)
ans1b = mult(5,10.0,2,3)
# raise NotImplementedError()


# In[ ]:





# ## Question 2
# 
# *2 points*
# 
# Define a Python *function, `subtract_from_ten`*, that takes, as input, a fixed argument *`a = 10`* and a variable number of arguments *`args`*.
# 
# Your *function* should return the result of subtraction of all the arguments in *`args`* from *`a`*.
# 
# Test your *function* with the inputs `1`, `2`, and `3`. Assign the result to *`ans2a`*.
# 
# Next, test your *function* with the inputs `5`, `10`, `1`, and `2`. Assign the result to *`ans2b`*.

# In[6]:


### GRADED

### YOUR SOLUTION HERE
ans2a = None
ans2b = None

def subtract_from_ten():
    pass
# YOUR CODE HERE
def subtract_from_ten(a =10, *args):
    result = 10
    for i in args:
        result = result -i
    return result

ans2a = subtract_from_ten(10, 1,2,3)
ans2b = subtract_from_ten(10, 5,10,2,1)
# raise NotImplementedError()


# In[ ]:





# ## Question 3
# 
# *4 points*
# 
# Define a Python *function, `subtract_from_highest`*, that takes, as input, a variable number of arguments *`args`*.
# 
# Your *function* should return the result of subtraction of all the arguments in *`args`* from the highest number,  with the exception of subtracting itself.
# 
# For example, the result of 
# ```Python
# subtract_from_highest(20,10,4)
# ```
# should be 6.
# 
# Test your *function* with the inputs `1`, `2`, and `3`. Assign the result to *`ans3a`*.
# 
# Next, test your *function* with the inputs `15`, `25`, `1`, and `3`. Assign the result to *`ans3b`*.

# In[7]:


### GRADED

### YOUR SOLUTION HERE
ans3a = None
ans3b = None

def subtract_from_highest():
    pass
# YOUR CODE HERE
def subtract_from_highest( *args):
    result = max(args)
    for i in args:
        if i != max(args):
            result = result-i
    return result

ans3a = subtract_from_highest(10, 1,2,3)
ans3b = subtract_from_highest(10, 5,25,2,3,1)
# raise NotImplementedError()


# In[ ]:





# ## Question 4
# 
# *2 points*
# 
# Define a Python *function, `mult_keyword`*, that takes a variable number of keyword arguments.
# 
# Your *function* should return the result of the multiplication of all the arguments passed to it.
# 
# Test your *function* with the inputs `(a =2, b = 3, c = 4)`. Assign the result to *`ans4a`*.
# 
# Next, test your *function* with the inputs`(a = 1, b = 5, c = 2, d = 3)` Assign the result to *`ans4b`*.

# In[8]:


### GRADED

### YOUR SOLUTION HERE
ans4a = None
ans4b = None

def mult_keyword():
    pass
# YOUR CODE HERE
def mult_keyword( **kwargs):
    result = 1
    for i in kwargs:
        result = result*kwargs[i]
    return result


ans4a = mult_keyword(a =2, b = 3, c = 4)
ans4b= mult_keyword(a = 1, b = 5, c = 2, d = 3)
# raise NotImplementedError()


# In[ ]:





# ## Question 5
# 
# *2 points*
# 
# Define a Python *function, `concatenate`*, that takes a variable number of *strings* and concatenates them.
# 
# Your *function* should return the result of the concatenation of all the *strings* passed to it.  Example: if you pass: "Having", "Fun", "With", "Python", "!" to your *function*, it should return: "HavingFunWithPython!"
# 
# Test your *function* with the inputs `"We", "Are", "Practicing", "Passing", "Unnamed", "Arguments!"`. Assign the result to *`ans5a`*.
# 
# Next, test your *function* with the inputs`"We", "Are", "Using", "The", "Unpacking", "Operator"`. Assign the result to *`ans5b`*.

# In[9]:


### GRADED

### YOUR SOLUTION HERE
ans5a = None
ans5b = None

def concatenate():
    pass
# YOUR CODE HERE
def concatenate( *args):
    result = ''
    for word in args:
        result = result + word
    return result


ans5a = concatenate("We", "Are", "Practicing", "Passing", "Unnamed", "Arguments!")
ans5b = concatenate("We", "Are", "Using", "The", "Unpacking", "Operator!")
# raise NotImplementedError()


# In[ ]:





# ## Question 6
# 
# *2 points*
# 
# Define a Python *function, `list_keys`*, that takes a variable number of named variables (a *dictionary*) and produces a comma delimited list of all the *keys* in the *dictionary*.
# 
# Your *function* should return a comma separated list of all the *keys* in the *dictionary*.  Example: if you pass: `key1 =2, key2 = 3, key3 = 4, key4 = 5` then your *function* should return `'key1, key2, key3, key4'`
# 
# 
# Test your *function* with the inputs `(a =2, b = 3, c = 4)`. Assign the result to *`ans6a`*.
# 
# Next, test your *function* with the inputs`(a = 1, b = 5, c = 2, d = 3)` Assign the result to *`ans6b`*.

# In[10]:


### GRADED

### YOUR SOLUTION HERE
ans6a = None
ans6b = None

def list_keys():
    pass
# YOUR CODE HERE
def list_keys( **kwargs):
    result = ''
    for key in kwargs.keys():
        if len(result) > 0:
            result = result + ', '
        result = result + key
    return result

ans6a = list_keys(a =2, b = 3, c = 4)
ans6b = list_keys(a = 1, b = 5, c = 2, d = 3)
# raise NotImplementedError()


# In[ ]:





# ## Question 7
# 
# *2 points*
# 
# Define a Python *function, `hello_user`*, that takes a variable number of named variables (a *dictionary*) containing contact information about a user, such as First Name, Last Name, and Email and returns `'Hello <First_Name>!'` where `<First_Name>` is the contact's First Name.
# 
# Example: With the input `First_Name=Bill, Last_Name=Gates, Email=Bill.Gates@xx.com` your *function* should return `'Hello Bill!'`
# 
# Test your *function* with the inputs `(First_Name="Elon", Last_Name="Musk", Email="Elon.Musk@yy.com")`. Assign the result to *`ans7a`*.
# 
# Next, test your *function* with the inputs`(First_Name="Jeff", Last_Name="Bezos", Email="Jeff.Bezos@zz.com")`. Assign the result to *`ans7b`*.

# In[11]:


### GRADED

### YOUR SOLUTION HERE
ans7a = None
ans7b = None

def hello_user():
    pass
def hello_user( **kwargs): 
    result = 'Hello '
    if "First_Name" in kwargs.keys():
        result = result + kwargs["First_Name"]
        return result
ans7a = hello_user(First_Name="Elon", Last_Name="Musk",
Email= "Elon.Musk@yy.com")
ans7b = hello_user(First_Name="Jeff", Last_Name="Bezos",
Email=" Jeff.Bezos@zz.com")
# YOUR CODE HERE
# raise NotImplementedError()


# In[ ]:





# ## Question 8
# 
# *2 points*
# 
# Define a Python *function, `display_user_total_assets`*, that takes three parameters:  First Name, Last Name and a *dictionary* containing a user's assets.
# 
# Example: If you were to pass `"John", "Smith", Car=30000, House=450000, Savings=1000000` then the *function* would return: `'John Smith: 1480000'`,  where `1480000` is the sum of all assets in the *dictionary*.
# 
# Test your *function* with the inputs ` "John", "Smith", Car=30000, House=450000, Savings=1000000`. Assign the result to *`ans8a`*.
# 
# Next, test your *function* with the inputs`"Joe", "Clark", Car=15000, House=250000`. Assign the result to *`ans8b`*.

# In[13]:


### GRADED

### YOUR SOLUTION HERE
ans8a = None
ans8b = None

def display_user_total_assets():
    pass
# YOUR CODE HERE
def display_user_total_assets(x,y, **kwargs):
    result = x + ' ' + y + ': '
    sum_assets = 0
    for x in kwargs.values():
        sum_assets = sum_assets + x
    result = result + str(sum_assets)
    return result

ans8a = display_user_total_assets("John", "Smith", Car=30000, House=450000, Savings=1000000)
ans8b = display_user_total_assets("Joe", "Clark", Car=15000, House=250000)
# raise NotImplementedError()


# In[ ]:





# ## Question 9
# 
# *2 points*
# 
# Define a Python *function, `display_user_total_assets2`*, that takes two parameters:  a variable *list* containing a user's name and a *dictionary* containing a user's assets. The *function* should return a *string* containing the person's name concatenated followed by a ":" and the sum of all assets.
# 
# Example: If you were to pass `"John", "S." "Smith","III", Car=30000, House=450000, Savings=1000000`, then the *function* would return: `John S. Smith III: 1480000`,  where `1480000` is the sum of all assets in the *dictionary*.
# 
# Test your *function* with the inputs ` "John", "S.", "Smith", "III", Car=30000, House=450000, Savings=1000000`. Assign the result to *`ans9a`*.
# 
# Next, test your *function* with the inputs`"Joe", "Clark", Car=15000, House=250000` Assign the result to *`ans9b`*.

# In[14]:


### GRADED

### YOUR SOLUTION HERE
ans9a = None
ans9b = None

def display_user_total_assets2():
    pass
# YOUR CODE HERE
def display_user_total_assets2(*args, **kwargs):
    result = ''
    for i in args:
        result = result + ' ' + i
    result = result + ': '
    sum_assets = 0
    for x in kwargs.values():
        sum_assets = sum_assets + x
    result = result + str(sum_assets)
    return result

ans9a = display_user_total_assets2("John", "S." "Smith", "III", Car=30000, House=450000, Savings=1000000)
ans9b = display_user_total_assets2("Joe", "Clark", Car=15000, House=250000)
# raise NotImplementedError()


# In[ ]:




