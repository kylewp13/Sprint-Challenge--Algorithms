'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''
def count_th(word):
  def recur(word, start):
    count = 0
    if start >= len(word) - 1:
      return 0
    if word[start] + word[start + 1] == 'th':
      count += 1
    return recur(word, start + 1) + count
  return recur(word, 0)