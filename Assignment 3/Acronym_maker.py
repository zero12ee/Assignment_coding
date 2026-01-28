def make_acronym():
   phrase = input("Please kindly enter a phrase: ")
   acronym = ""

   index = 0
   while index < len(phrase) and phrase[index] == " ":
      index += 1
   if index < len(phrase):
      acronym += phrase[index].upper()

   space_index = phrase.find(" ", index)
   while space_index != -1 and space_index + 1 < len(phrase):
        
      next_index = space_index + 1
      while next_index < len(phrase) and phrase[next_index] == " ":
         next_index += 1
      if next_index < len(phrase):
         acronym += phrase[next_index].upper()
      space_index = phrase.find(" ", next_index)
   print(f"The acronym is: {acronym}")
make_acronym()
