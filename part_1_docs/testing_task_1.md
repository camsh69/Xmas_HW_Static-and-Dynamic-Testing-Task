### Testing task 1:

# Carry out static testing on the code below.

# Comment on any errors that you see below.

Note that we are only looking for errors here.

**Not** any issues with, i.e.:
Thinking that methods should be renamed or should be class level, or using string interpolation etc.

These aren't errors but rather standards that vary from developer to developer.

Only comment on errors that would stop the tests running.

```python

class CardGame:


  def check_for_ace(self, card):
# should be if card.value == 1
    if card.value = 1:
      return True
# missing colon
    else
      return False

# dif should be def, missing coma in parameters
  dif highest_card(self, card1 card2):
# if statement should be indented
  if card1.value > card2.value:
# card should be card1
    return card
  else:
    return card2


# indentation errors
def cards_total(self, cards):
# total should have value assigned, e.g. total = 0
  total
  for card in cards:
    total += card.value
    return "You have a total of" + total

```
