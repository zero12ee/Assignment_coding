def character_extractor():
   text = input("Please enter a string: ")
   length = len(text)
   if length % 2 == 1:
      print(f"The middle character of the string is: {text[length // 2]}") 
   else:
      middle_1 = text[(length // 2) - 1]
      middle_2 = text[length // 2]
      print(f"The middle characters of the string are: {middle_1} and {middle_2}")
character_extractor()
