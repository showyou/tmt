import os
import sys

sys.path.insert(
    0,
    os.path.abspath(os.path.dirname(__file__)).rsplit("/",1)[0],
)


def test_mail():
    import mail
    import jsonfile

    userdata = jsonfile.read(homePath + "user/twdata_tmt")
    user = userdata["user"]
    passWord = userdata["pass"]
    from_addr = user
    to_addr = userdata["mail"]
    msg = test_mail.create_message2(from_addr, to_addr, u'テスト'.encode("iso-2022-jp"), u'あーてすてす'.encode("iso-2022-jp"), 'ISO-2022-JP')
    send_via_gmail(from_addr, to_addr, msg)
    if len(sys.argv) < 3:
        print "usage tmt.py user mail"
        print "use test mode"
        tmt.sendTmt("ha_ma","showyou41@gmail.com")
        exit()
    tmt.sendTmt(sys.argv[1],sys.argv[2])


if __name__ == '__main__':
    import nose
    nose.main()
