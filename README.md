# Python exercises in TDD style - COMPLETE

Forked from bast/python-tdd-exercises, this repo contained a set of Python functions, and the goal was to make corresponding predefined unit tests pass.
This was not only a great way of practicing/implementing the RED-GREEN-REFACTOR methodology in my Python programming, but also a good way of testing my Python programming skills. 
My setup: PyCharm IDE and pytest.
COMPLETED 16/07/2020, 21;56

[![Build Status](https://travis-ci.org/LIOHN/python-tdd-exercises.svg?branch=master)](https://travis-ci.org/LIOHN/python-tdd-exercises/builds)
[![Coverage Status](https://coveralls.io/repos/LIOHN/python-tdd-exercises/badge.png?branch=master)](https://coveralls.io/r/LIOHN/python-tdd-exercises?branch=master)

After you fork, edit this `README.md` and rename "bast" to your GitHub username or namespace to make the badges point to your fork.


## Inspiration
- [Python Koans](https://github.com/gregmalcolm/python_koans)
- [46 Simple Python Exercises](http://www.ling.gu.se/~lager/python_exercises.html)
- [Programming Python for Bioinformatics](http://homepages.stca.herts.ac.uk/~comqdp1/BioInf/)


## You can do this exercise too
- Fork bast/python-tdd-exercises for a new copy of the exercises (don't fork this one, I've already solved them).
- Login to [Travis CI](https://travis-ci.org) with your GitHub account and activate this repo for testing.
- Login to [Coveralls](https://coveralls.io) with your GitHub account and activate this repo for code coverage analysis.
- Implement missing functions to make the unit tests pass (run tests either locally or let Travis run them for you each time you push changes).
- Increase the test coverage to 100% by making [all lines](https://coveralls.io/r/LIOHN/python-tdd-exercises?branch=master) green.


## How to run tests locally (Linux or Mac OS X)
First clone the project. Locally running the unit testing requires either [pytest](http://pytest.org)or [nose](https://nose.readthedocs.org).

Then you can run the tests with:
```
$ py.test -vv exercises.py
```

You can run a single test case like this:
```
$ py.test -vv exercises.py -k test_character_statistics
```

Or alternatively with [nose](https://nose.readthedocs.org):
```
$ nosetests exercises.py
```
