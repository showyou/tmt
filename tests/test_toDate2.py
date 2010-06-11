import os
import sys

sys.path.insert(
    0,
    os.path.abspath(os.path.dirname(__file__)).rsplit("/",1)[0],
)

def test_toDate():
    import datetime
    import toDate2
    date = "2008-02-24T06:39:37+00:00"
    date2 = toDate2.toDate2(date)
    if str(date2).startswith("2007-12-22 10:07:16"):
        return True
    else:
        return False


if __name__ == '__main__':
    import nose
    nose.main()

