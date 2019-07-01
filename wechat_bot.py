# coding: utf-8
import itchat
import time

DEFAULT_MINUTE = 0
DEFAULT_LATENCY = 0


def main():
    chatroom = input("Chatroom: ")
    msg = input("Message: ")
    hour = int(input("Hour: "))
    minute = input("Minute [{}]: ".format(DEFAULT_MINUTE))
    minute = int(minute or DEFAULT_MINUTE)
    latency = input("Latency(ms) [{}]: ".format(DEFAULT_LATENCY))
    latency = int(latency or DEFAULT_LATENCY)

    sess = itchat.new_instance()
    sess.auto_login()
    user_name = get_user_name_of_chatroom(sess, chatroom)
    wait_to(hour, minute, latency)
    sess.send_msg(msg, toUserName=user_name)
    sess.logout()


def get_user_name_of_chatroom(session, nickname) -> str:
    rooms = session.get_chatrooms()
    user_name = None
    for room in rooms:
        if room["NickName"] == nickname:
            user_name = room["UserName"]
            break
    return user_name


def wait_to(hour, minute, ahead_ms) -> None:
    target_sec = convert_to_sec(hour, minute)

    cur = time.localtime()
    cur_sec = convert_to_sec(cur.tm_hour, cur.tm_min, cur.tm_sec)
    time.sleep(target_sec - cur_sec - ahead_ms / 1000 - 60)

    cur = time.localtime()
    cur_sec = convert_to_sec(cur.tm_hour, cur.tm_min, cur.tm_sec)
    busy_wait(int(time.time()) - cur_sec + target_sec - ahead_ms / 1000)


def busy_wait(tm) -> None:
    while time.time() < tm:
        pass


def convert_to_sec(hour, minute=0, sec=0) -> int:
    return (hour * 60 + minute) * 60 + sec


if __name__ == "__main__":
    main()
