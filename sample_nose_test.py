def test_sample_nosetest():
    assert 'HELLO' == 'hello'.upper()

#python -m nose sample_nose_test.py
#python -m nose sample_nose_test.py -v
#nosetests  sample_nose_test.py -v

def add2num(a,b):
    return a+b

def test_sum_2pos_num():
    assert add2num(6, 7)==13

def test_sum_1pos_and_1neg_num():
    assert add2num(-10, 9)==-1


from nose.tools import ok_, eq_
def test_using_ok():
    ok_(2+3==5)

def test_using_eq():
    eq_(2+3, 5)


from nose.tools import raises

@raises(TypeError)
def test_using_raises():
    eq_(2+'3', 5)


#nosetests test.test_module1 -v --with-xunit


from nose.tools import raises

class SampleTestClass:

    @raises(TypeError)
    def test_sample1(self):
        pow(2, '4')

    @raises(Execption)
    def test_sample2(self):
        max([7, 8, '4'])

    @raises(Exception)
    def test_sample3(self):
        int('hello')