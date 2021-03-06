# -*- coding: utf-8 -*-


#use __slots__
#############################################################
# class Student(object):
#     __slots__ = ('name', 'age','score') # 用tuple定义允许绑定的属性名称


# s= Student()
# s.name ='Wn'
# s.age = 18
# s.score = 99

# s.sex ='man'  Error  sex isn't involve in __slots__
#############################################################

#use @property
#############################################################
# class Student(object):

# 	@property
# 	def score(self):
# 	    return self._score
	
# 	@score.setter
# 	def set_score(self, value):
# 		if not isinstance(value,int):
# 			raise ValueError('score must be an integer!')
# 		if value < 0 or value >100 :
# 			raise ValueError('score must between 0 ~ 100!')
# 		self._score = value    

class Student(object):

    @property
    def score(self):
        return self._score

    @score.setter
    def score(self, value):
        if not isinstance(value, int):
            raise ValueError('score must be an integer!')
        if value < 0 or value > 100:
            raise ValueError('score must between 0 ~ 100!')
        self._score = value
	
    def __init__(self,name):
            self.name = name    

    def __str__(self) :
        return 'Student name is %s' % self.name

    __repr__ = __str__


s = Student('Wn')
s.score = 99
print s.score
print s.name
print s
