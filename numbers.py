def number_to_words(number):
  if number == 0:
    return "zero"
  elif number == 1:
    return "one"
  elif number == 2:
    return "two"
  elif number == 3:
    return "three"
  elif number == 4:
    return "four"
  elif number == 5:
    return "five"
  elif number == 6:
    return "six"
  elif number == 7:
    return "seven"
  elif number == 8:
    return "eight"
  elif number == 9:
    return "nine"
  elif number == 10:
    return "ten"
  elif number == 11:
    return "eleven"
  elif number == 12:
    return "twelve"
  elif number == 13:
    return "thirteen"
  elif number == 14:
    return "fourteen"
  elif number == 15:
    return "fifteen"
  elif number == 16:
    return "sixteen"
  elif number == 17:
    return "seventeen"
  elif number == 18:
    return "eighteen"
  elif number == 19:
    return "nineteen"
  elif number == 20:
    return "twenty"
  elif number < 20:
    return number_to_words(number // 10) + " " + number_to_words(number % 10)
  elif number < 100:
    if number % 10 == 0:
      return number_to_words(number // 10) + "ty"
    else:
      return number_to_words(number // 10) + "- " + number_to_words(number % 10)
  else:
    return "invalid number"


number = int(input("Enter a number between 0 and 100: "))

if number >= 0 and number <= 100:
  print(f"{number} is {number_to_words(number)}")
else:
  print("Invalid number")
