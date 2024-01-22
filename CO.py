CO_SUITED={
    "AK":"Raise",
    "AQ":"Raise",
    "AJ":"Raise",
    "AT":"Raise",
    "A9":"Raise",
    "A8":"Raise",
    "A7":"Raise",
    "A6":"Raise",
    "A5":"Raise",
    "A4":"Raise",
    "A3":"Raise",
    "A4":"Raise",
    "A2":"Raise",
    "KQ":"Raise",
    "KJ":"Raise",
    "KT":"Raise",
    "K9":"Raise",
    "K8":"Raise",
    "K7":"Raise or Call",
    "K6":"Raise or Call",
    "K5":"Fold",
    "K4":"Raise or Call",
    "K3":"Fold",
    "K2":"Fold",
    "QJ":"Raise",
    "QT":"Raise",
    "Q9":"Raise",
    "Q8":"Raise or Call",
    "Q7":"Fold",
    "Q6":"Fold",
    "Q5":"Fold",
    "Q4":"Fold",
    "Q3":"Fold",
    "Q2":"Fold",
    "JT":"Raise",
    "J9":"Raise",
    "J8":"Raise or Call",
    "J7":"Fold",
    "J6":"Fold",
    "J5":"Fold",
    "J4":"Fold",
    "J3":"Fold",
    "J2":"Fold",
    "T9":"Raise",
    "T8":"Raise or Call",
    "T7":"Fold",
    "T6":"Fold",
    "T5":"Fold",
    "T4":"Fold",
    "T3":"Fold",
    "T2":"Fold",
    "98":"Raise",
    "97":"Fold",
    "96":"Fold",
    "95":"Fold",
    "94":"Fold",
    "93":"Fold",
    "92":"Fold",
    "87":"Raise or Call",
    "86":"Fold",
    "85":"Fold",
    "84":"Fold",
    "83":"Fold",
    "82":"Fold",
    "76":"Raise or Call",
    "75":"Fold",
    "74":"Fold",
    "73":"Fold",
    "72":"Fold",
    "65":"Raise",
    "64":"Fold",
    "63":"Fold",
    "62":"Fold",
    "54":"Fold",
    "53":"Fold",
    "52":"Fold",
    "43":"Fold",
    "42":"Fold",
    "42":"Fold",
}

CO_OFF_SUITED={
    "AK":"Raise",
    "AQ":"Raise",
    "AJ":"Raise",
    "AT":"Raise",
    "A9":"Raise or Call",
    "A8":"Raise or Call",
    "A7":"Fold",
    "A6":"Fold",
    "A5":"Fold",
    "A4":"Fold",
    "A3":"Fold",
    "A4":"Fold",
    "A2":"Fold",
    "KQ":"Raise",
    "KJ":"Raise",
    "KT":"Raise",
    "K9":"Fold",
    "K8":"Fold",
    "K7":"Fold",
    "K6":"Fold",
    "K5":"Fold",
    "K4":"Fold",
    "K3":"Fold",
    "K2":"Fold",
    "QJ":"Raise",
    "QT":"Raise",
    "Q9":"Fold",
    "Q8":"Fold",
    "Q7":"Fold",
    "Q6":"Fold",
    "Q5":"Fold",
    "Q4":"Fold",
    "Q3":"Fold",
    "Q2":"Fold",
    "JT":"Raise or Call",
    "J9":"Fold",
    "J8":"Fold",
    "J7":"Fold",
    "J6":"Fold",
    "J5":"Fold",
    "J4":"Fold",
    "J3":"Fold",
    "J2":"Fold",
    "T9":"Fold",
    "T8":"Fold",
    "T7":"Fold",
    "T6":"Fold",
    "T5":"Fold",
    "T4":"Fold",
    "T3":"Fold",
    "T2":"Fold",
    "98":"Fold",
    "97":"Fold",
    "96":"Fold",
    "95":"Fold",
    "94":"Fold",
    "93":"Fold",
    "92":"Fold",
    "87":"Fold",
    "86":"Fold",
    "85":"Fold",
    "84":"Fold",
    "83":"Fold",
    "82":"Fold",
    "76":"Fold",
    "75":"Fold",
    "74":"Fold",
    "73":"Fold",
    "72":"Fold",
    "65":"Fold",
    "64":"Fold",
    "63":"Fold",
    "62":"Fold",
    "54":"Fold",
    "53":"Fold",
    "52":"Fold",
    "43":"Fold",
    "42":"Fold",
    "42":"Fold",
}

CO_PAIR ={
    "AA":"Raise",
    "KK":"Raise",  
    "QQ":"Raise",  
    "TT":"Raise",  
    "99":"Raise",     
    "88":"Raise",  
    "77":"Raise",  
    "66":"Raise",  
    "55":"Raise",  
    "44":"Fold",  
    "33":"Fold",  
    "22":"Fold",  
}

def main():
    print("1:",end='')
    first=input()
    print("2:",end='')
    second=input()
    print("Suited?(Y or N):",end='')
    is_suit=input()
    if is_suit == 'Y':
        is_suit = True
    elif is_suit == 'N':
        is_suit = False
    else:
        print("error")

    print(result(first,second,is_suit))


def result(a,b,is_suit):
    if card_num(a) == card_num(b):
        return CO_PAIR[a+b]
    if card_num(a) > card_num(b):
        if is_suit:
            return CO_SUITED[a+b]
        else:
            return CO_OFF_SUITED[a+b]
    else:
        if is_suit:
            return CO_SUITED[b+a]
        else:
            return CO_OFF_SUITED[b+a]

def card_num(card):
    if card=='A':
        return 14
    elif card=='K':
        return 13
    elif card=='Q':
        return 12 
    elif card=='J':
        return 11
    elif card=='T':
        return 10
    else:
        return int(card)


if __name__ == "__main__":
    main()