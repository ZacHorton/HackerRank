from string import punctuation

def fun(s):
  # return True if s is a valid email, else return False
  if s.count("@") != 1 or s.count(".") != 1:
    return False 
  at_index = s.find("@")
  dot_index = s.find(".")

  username = s[0:at_index]
  websitename = s[at_index+1:dot_index]
  extension = s[dot_index+1:]
  if username == "" or websitename == "" or extension == "":
    return False

  username_punctuations = punctuation
  username_punctuations = username_punctuations.replace("-", "")
  username_punctuations = username_punctuations.replace("_", "")
  username_pass = True
  for x in username:
    for y in username_punctuations:
      if x == y:
        username_pass = False
        break

  websitename_punctuations = punctuation
  website_pass = True
  for x in websitename:
    for y in websitename_punctuations:
      if x == y:
        website_pass = False
        break

  if len(extension) > 3:
    return False
  extension_punctuations = punctuation
  extension_punctuations += "0123456789"
  extension_pass = True
  for x in extension:
    for y in extension_punctuations:
      if x == y:
        extension_pass = False
        break
  
  if username_pass is True and website_pass is True and extension_pass is True:
    return True
  else:
    return False

def filter_mail(emails):
    return list(filter(fun, emails))

if __name__ == '__main__':
    n = int(input())
    emails = []
    for _ in range(n):
        emails.append(input())

filtered_emails = filter_mail(emails)
filtered_emails.sort()
print(filtered_emails)
