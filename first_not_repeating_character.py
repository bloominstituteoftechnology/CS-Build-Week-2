s = "abacabad"

def first_not_repeating_character(s):

  nothing = s
  # Check that the string exists
  while len(nothing) > 0:
    # Evaluate the character at index 0
    curr = nothing[0]
    # Iterate through entire string, looking for char[0] again
    if curr in nothing[1:]:
      # If it repeats, remove all instances from the string
      nothing = nothing.replace(curr, '')
    # If the char doesn't repeat, return the char[0]
    else:
      return curr
  # If there are only repeating characters, per instructions return '_'
  return '_'
