def validclock24(time):
    """
    시:분 또는 시:분:초 형식이 올바른지 확인하는 함수.
    시:분 형식: 00:00 ~ 23:59 및 24:00 (단, 24:01 이상은 잘못된 형식)
    시:분:초 형식: 00:00:00 ~ 23:59:59 및 24:00:00 (단, 24:00:01 이상은 잘못된 형식)
    """
    # 시:분:초 형식이 가능한가
    (hour, colon1, rest) = time.partition(":")
    
    # 시 부분 체크
    if colon1 != ":" or len(hour) != 2 or not hour.isdigit():
        return False
    
    (minute, colon2, second) = rest.partition(":")
    
    # 시:분 형식 (초가 없을 때)
    if colon2 == "":
        if len(minute) != 2 or not minute.isdigit():  # 분이 2자리여야 함
            return False
        second = "00"  # 초가 없으면 00으로 처리
    elif colon2 != ":" or len(minute) != 2 or not minute.isdigit():  # 분이 2자리여야 함
        return False  # 초 정보가 있는데 형식이 잘못된 경우
    elif len(second) != 2 or not second.isdigit():  # 초가 있을 경우 2자리여야 함
        return False
    
    # 숫자인지 확인 및 범위 확인
    try:
        hour = int(hour)
        minute = int(minute)
        second = int(second)
    except ValueError:
        return False  # 숫자가 아닌 경우
    
    # 시각 범위 확인
    if (0 <= hour <= 23 and 0 <= minute <= 59 and 0 <= second <= 59) or (hour == 24 and minute == 0 and second == 0):
        return True
    
    return False


print(validclock24("00:00"))    # True
print(validclock24("00:30"))    # True
print(validclock24("09:58"))    # True
print(validclock24("12:15"))    # True
print(validclock24("23:59"))    # True
print(validclock24("24:00"))    # True
print(validclock24("7:07"))     # False (7:07는 잘못된 형식)
print(validclock24("07:121"))   # False (분이 2자리가 아님)
print(validclock24("13:4"))     # False (분이 2자리가 아님)
print(validclock24("00:60"))    # False (분이 60을 넘음)
print(validclock24("24:01"))    # False (24시에서 1분 이상)
print(validclock24("25:10"))    # False (24시 초과)
print(validclock24("12:30:45")) # True (초가 포함된 정상 시각)
print(validclock24("24:00:00")) # True (24시 00분 00초)
print(validclock24("23:59:59")) # True (하루 마지막 초)
print(validclock24("24:00:01")) # False (24시 00분 01초는 유효하지 않음)
