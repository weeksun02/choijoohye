def validclock12(time):
    """
    12시간 시각을 나타내는 시:분am, 시:분pm 또는 시:분:초am, 시:분:초pm 형식이 올바른지 검사한다.
    """
    # 시:분 또는 시:분:초 형식으로 나눔
    (hour, colon1, rest) = time.partition(":")
    
    # 시 부분 체크 (한 자리 시는 1자리여야 하고 두 자리 시는 2자리여야 함)
    if colon1 != ":" or not hour.isdigit() or (len(hour) == 1 and int(hour) == 0) or (len(hour) == 2 and hour.startswith("0")):
        return False
    
    # am 또는 pm이 포함된 나머지 부분을 처리
    if "am" in rest:
        minuteplus, am_or_pm = rest.split("am")
        am_or_pm = "am"
    elif "pm" in rest:
        minuteplus, am_or_pm = rest.split("pm")
        am_or_pm = "pm"
    else:
        return False
    
    # 분과 초 분리
    (minute, colon2, second) = minuteplus.partition(":")
    
    # 초가 없는 경우 처리
    if colon2 == "":
        second = "00"  # 초가 없으면 00으로 처리
    elif colon2 != ":" or len(second) != 2 or not second.isdigit():  # 초가 있을 경우 2자리여야 함
        return False

    # 분 및 시의 범위 확인
    if len(minute) != 2 or not minute.isdigit() or not (0 <= int(minute) <= 59):
        return False
    
    # 시, 분, 초 범위 확인
    if not (1 <= int(hour) <= 12 and 0 <= int(minute) <= 59 and 0 <= int(second) <= 59):
        return False

    # am 또는 pm이 올바른지 확인
    if am_or_pm not in ["am", "pm"]:
        return False
    
    return True


print(validclock12("1:30am"))  # True
print(validclock12("9:12pm"))  # True
print(validclock12("3:05am"))  # True
print(validclock12("10:14pm")) # True
print(validclock12("11:59pm")) # True
print(validclock12("12:00am")) # True
print(validclock12("12:00pm")) # True
print(validclock12("1:30:30am"))  # True (초가 포함된 시각)
print(validclock12("12:59:59pm")) # True (초가 포함된 시각)
print(validclock12("0:15am"))  # False
print(validclock12("09:18pm")) # False (한 자리 수는 0으로 시작할 수 없음)
print(validclock12("3:5am"))   # False (분이 2자리가 아님)
print(validclock12("00:00pm")) # False (시간이 0이면 안됨)
print(validclock12("5:60am"))  # False (분이 60을 넘음)
print(validclock12("10:14:61pm")) # False (초가 60을 넘음)
print(validclock12("03:15am")) # False (한 자리 시간 앞에 0이 붙으면 안됨)
