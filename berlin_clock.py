"""
Berlin Clock WIKI:
https://en.wikipedia.org/wiki/Mengenlehreuhr
"""

def valid_time(t):
    # check if the time format is correct
    try:
        h, m, s = map(int, t.split(':'))
        if h < 0 or m < 0 or s < 0:
            return "Data value can't be negative"
        if h > 23:
            return "Hour must be lower then 24"
        elif m > 59 or s > 59:
            return "Minute or second must be lower then 60"
        return [s % 2 == 0, h // 5, h % 5, m // 5, m % 5]
    except:
        return "Wrong time format! Use this one hh:mm:ss"


def berlin_clock(time):
    print("\n### Berlin Clock ###\n")
    print("-----\nEntered time: {}".format(time))
    vt = valid_time(time)
    if type(vt) == list:
        if vt[0]:
            print('Y')
        else:
            print('O')
        print(vt[1]*'R' + (4-vt[1])*'O')
        print(vt[2]*'R' + (4-vt[2])*'O')
        l_line = list(vt[3]*'Y' + (11-vt[3])*'O')
        if l_line[2] == 'Y':
            l_line[2] = 'R'
        if l_line[5] == 'Y':
            l_line[5] = 'R'
        if l_line[8] == 'Y':
            l_line[8] = 'R'
        print("".join(l_line))
        print(vt[4]*'Y' + (4-vt[4])*'O')
    else:
        print(vt)
    print("-----")


def simple_berlin_clock(time):
    # simple version
    print("\n\n---Simple version---")
    print("\nEntered time: {}".format(time))
    vt = valid_time(time)
    if type(vt) == list:
        for i in vt:
            print(i * '|#|')
    else:
        print(vt)
    print("-----")


def current_time_berlin_clock():
    # current time version
    print("\n\n---Current time version---")
    import datetime
    cur_time = datetime.datetime.now()
    print("\nCurrent time is: {}:{}:{}".format(cur_time.hour, cur_time.minute, cur_time.second))
    vt = valid_time(cur_time.strftime("%H:%M:%S"))
    for i in vt:
        print(int(i) * '|#|')
    print("-----")


def main():
    time = "17:15:57"
    berlin_clock(time)
    simple_berlin_clock(time)
    current_time_berlin_clock()


main()

