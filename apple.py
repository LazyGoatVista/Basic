class Connection(object):
    __slots__ = ['param1', 'param2', '_birth']  # 内存优化工具

    def __init__(self, param1, param2, birth):
        self.param1 = param1
        self.param2 = param2
        self.birth = birth

    @property
    def birth(self):
        return self._birth

    @birth.setter
    def birth(self, value):
        if not isinstance(value, int):
            raise ValueError('birth must be a integer!')
        self._birth = value

    @birth.deleter
    def birth(self):
        raise AttributeError('can not delete a attribute!')

    def __enter__(self):
        print('Enter!')

    def __exit__(self, type_, value, trace):  # 至少需要3个参数
        print('Exit!')

    def __str__(self):
        return 'My birth is %s' % self._birth


# conn = Connection('a', 'b')
# with conn as c:
#     pass
#
# print(conn)

c = Connection(1, 3, 1998)
c.birth = 2000
# del c.birth
print(c)

