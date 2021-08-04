import notify2
import ping_test


def notify():
    ping = ping_test.output_log()
    print(ping)
    notify2.init('Ping')
    n = notify2.Notification("Ping Notifier")
    n.set_urgency(notify2.URGENCY_NORMAL)
    n.set_timeout(1000)
    result = f'📡 >> {ping}'.format(*ping)
    n.update('🖥️ Ping', result)
    n.show()
    return


notify()
