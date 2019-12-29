# pythonqualis - Test Frameworks for python

This repo is to demonstrate the usage of 

* doctest
* unittest
* nose
* pytest

with examples 

### Installation - Run Tests

```sh
## doctest run commands
$ python3 ‑m doctest sample_module.py
$ python3 ‑m doctest -v sample_tests.py

## unittest run commands
$ python -m unittest test_module1
$ python -m unittest test_module1 -v
$ python -m unittest test_module1.Testadd2num
$ python -m unittest test_module1.Testadd2num.test_sum_2pos_num
## unittest with main method 
$ if __name__ == '__main__':
    unittest.main()
$ python test_module1.py

## nose run commands
$ python -m nose sample_nose_test.py
$ python -m nose sample_nose_test.py -v
$ nosetests test.test_module1 -v
$ nosetests test.test_module1:Testadd2num -v
$ nosetests test.test_module1:Testadd2num.test_sum_2pos_num -v
$ nosetests -v
$ nosetests test.test_module1 -v --with-xunit

## pytest run commands
$ python -m pytest sample_pytest_test.py
$ py.test sample_pytest_test.py
$ py.test -v test
$ py.test -v test/test_module1.py
$ py.test -v test/test_module1.py::Testadd2num
$ py.test -v test/test_module1.py::Testadd2num::test_sum_2pos_num
$ py.test --resultlog=result.txt
$ py.test --junitxml=result.xml
```