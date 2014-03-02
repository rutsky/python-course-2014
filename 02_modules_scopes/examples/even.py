def is_even(number):
   """Возвращает True, если number — чётный"""
   if number % 4 == 0: # Ошибка
       return True
   return False

def _test():
    assert is_even(4)
    assert not is_even(3)
    assert is_even(-20)
    assert is_even(2)

if __name__ == "__main__":
    _test()
