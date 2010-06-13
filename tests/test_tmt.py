import os
import sys

sys.path.insert(
    0,
    os.path.abspath(os.path.dirname(__file__)).rsplit("/",1)[0],
)

def test_tmt():
    import datetime
    import tmt
    import sys
    if len(sys.argv) < 3:
        print "usage tmt.py user mail"
        print "use test mode"	
        tmt.sendTmt("ha_ma","showyou41@gmail.com")
        exit()
    tmt.sendTmt(sys.argv[1],sys.argv[2])

if __name__ == '__main__':
    import nose
    nose.main()

