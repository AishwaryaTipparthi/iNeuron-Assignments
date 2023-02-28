#!/usr/bin/env python
# coding: utf-8

# In[ ]:


1. In the below elements which of them are values or an expression? eg:- values can be
integer or string and expressions will be mathematical operators.


# In[ ]:


*        - expression
'hello'  - value
-87.8    - value
-        - expression
(-, expression)
+        - expression
6        - value


# In[ ]:


get_ipython().set_next_input('2. What is the difference between string and variable');get_ipython().run_line_magic('pinfo', 'variable')

Variables are used to store the data in a program. Its like an empty space where we can fill with some data or value. 
String is a value representing text. It is encolsed between the single or double qoutes, so we can use them to fill up a 
variable.


# In[ ]:


3. Describe three different data types.

Numeric data type: Numeric data type is used to hold numeric values. Integers, floating-point numbers and complex numbers falls
under python numbers category. They are defined as int, float and complex classes.
eg: 5 is an interger value
    12.6 is a floating value
    7+9j is a complex value
List data type: List is an ordered collection of similar or different types of items seperated by commas and enclosed within 
[] brackets.
eg: [53,"aish", 2.53, 5+4j]
Tuple data type: Tuple is an ordered sequence of items same as list. The only difference is that tuples are immutable. Tuples
once created cannot be modified. We use () parentheses to store items of a tuple
eg: (36,"aish", 483.12)
    


# In[ ]:


get_ipython().set_next_input('4. What is an expression made up of? What do all expressions do');get_ipython().run_line_magic('pinfo', 'do')

An expression is a combination of values, variables, operators, and calls to functions. Expressions need to be evalued.
The interpreter evaluates the expression and displays the result.
eg: x = x+10


# In[ ]:


5. This assignment statements, like spam = 10. What is the difference between an
get_ipython().set_next_input('expression and a statement');get_ipython().run_line_magic('pinfo', 'statement')

The main difference between expression and statement is statement represents an action or command.
eg: print statements - print'hello'
    assignment statements - x = 5, spam = 10
whereas expression is a combination of variables, operations and values that yeilds a result value.


# In[ ]:


get_ipython().set_next_input('6. After running the following code, what does the variable bacon contain');get_ipython().run_line_magic('pinfo', 'contain')
bacon = 22
bacon + 1


# In[4]:


bacon = 22
bacon + 1


# In[ ]:


get_ipython().set_next_input('7. What should the values of the following two terms be');get_ipython().run_line_magic('pinfo', 'be')
'spam' + 'spamspam'
'spam' * 3


# In[6]:


'spam' + 'spamspam'


# In[7]:


'spam' * 3


# In[ ]:


get_ipython().set_next_input('8. Why is eggs a valid variable name while 100 is invalid');get_ipython().run_line_magic('pinfo', 'invalid')

Because variable names cannot begin with a number.


# In[ ]:


9. What three functions can be used to get the integer, floating-point number, or string
version of a value? 

int(), float(), str()


# In[ ]:


get_ipython().set_next_input('10. Why does this expression cause an error? How can you fix it');get_ipython().run_line_magic('pinfo', 'it')
'I have eaten' + 99 + 'burritos'.


# In[14]:


'I have eaten'  +  str(99)  +  'burritos.'


# In[15]:


'I have eaten' + '99' + 'burritos.'


# In[ ]:




