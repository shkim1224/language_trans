from flask import Flask

def outer_function(mess):
    def inner_function():
        print(mess)
    return inner_function

app = Flask(__name__)
#@app.route('/')
"""hi_func = outer_function('hi')
bye_func = outer_function('bye')
hi_func()
bye_func()"""

def decorator_fun(original_fun):
    def wrapper_func():
        print('wrapper executed this before'.format(original_fun.__name__))
        return original_fun()
    return wrapper_func
@decorator_fun
def display():
    print('display fun ran')

display()

"""decorator_fun('bye')
a = decorator_fun('hi')
a()"""




