# ex4


fhand = open('mbox.txt')


def look(fhand):
    for i in fhand:
        print(i)

def conf(fhand):
    spam_conf = []
    for i in fhand:
        if i.startswith("X-DSPAM-Confidence:"):
            spam_conf.append(str(i))
    return(spam_conf)

def conf_vals_lst(fhand):
    spam_conf = conf(fhand)
    conf_val = []
    for i in spam_conf:
        sppos = i.find(" ")
        conf_val.append(float(i[sppos:]))
    return(conf_val)

def conf_avg(fhand):
    conf_val = conf_vals_lst(fhand)
    avg = sum(conf_val) / len(conf_val)
    return avg
