Python 3.10.2 (tags/v3.10.2:a58ebcc, Jan 17 2022, 14:12:15) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
13+1
14
print("Hello")
Hello
import turtle as t
t.shape("turtle")

t.forward(100)
t.backward(100)
t.upward(10)
Traceback (most recent call last):
  File "<pyshell#8>", line 1, in <module>
    t.upward(10)
AttributeError: module 'turtle' has no attribute 'upward'
t.right(10)
t.forward(100)

t.backward(10)

t.right(30)
t.forward(100)

print("Hello")
Hello


print("Hello")
print("Hello")

SyntaxError: multiple statements found while compiling a single statement
