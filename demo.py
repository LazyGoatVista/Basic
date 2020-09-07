import functools


def log(text):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            print('%s function %s' % (text, func.__name__))
            return func(*args, **kwargs)
        return wrapper
    return decorator


@log('execute')
def hello():
    print('Sometimes naive!')


# hello = log('execute')(hello)  # 语法糖本质上就是这样调用的

hello()
# print(hello.__name__)
