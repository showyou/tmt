import os
import sys

sys.path.insert(
    0,
    os.path.abspath(os.path.dirname(__file__)).rsplit("/",1)[0],
)

def test_toDate():
    import datetime
    import toDate
    date = "Sat Dec 22 01:07:16 +0000 2007"
    date2 = toDate.toDate(date)
    if str(date2).startswith("2007-12-22 10:07:16"):
        return True
    else:
        return False


if __name__ == '__main__':
    import nose
    nose.main()

