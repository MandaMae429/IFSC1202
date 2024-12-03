class User:
  def __init__(self, username, password):
    self.UserName = username
    self.Password = password
class UserList:
  def __init__(self, filename):
    self.Userlist = []
    self.FileName = filename
  def ReadUserFile(self):
    f = open(self.FileName, "r")
    for line in f:
      line = line.split(",")
      self.Userlist.append(User(line[0].strip(),line[1].strip()))
    f.close()
  def WriteUserFile(self):
    f = open(self.FileName, "w")
    for x in range(len(self.Userlist)):
      f.write(self.Userlist[x].UserName + "," + self.Userlist[x].Password)
      #Avoid empty line in Outfile
      if x != len(self.Userlist)-1:
        f.write("\n")
    f.close()
  def DisplayUserList(self):
    maxu = 8
    maxp = 8
    #find max user and Password length for adjusting display
    for user in self.Userlist:
      if len(user.Password) > maxp:
        maxp = len(user.Password)
      if len(user.UserName) > maxu:
        maxu = len(user.UserName)
    print("{0:>{2}} {1:>{3}}".format("Username", "Password",maxu,maxp))
    print("{0:>{2}} {1:>{3}}".format("-"*maxu, "-"*maxp,maxu,maxp))
    for user in self.Userlist:
      print("{0:>{2}} {1:>{3}}".format(user.UserName, user.Password,maxu,maxp))
  def FindUsername(self, username):
    for user in self.Userlist:
      if user.UserName == username:
        return self.Userlist.index(user)
    return -1
  def ChangePassword(self, username, password):
    index = self.FindUsername(username)
    if index != -1:
      self.Userlist[index].Password = password
  def AddUser(self, username, password):
    if self.FindUsername(username) == -1:
      self.Userlist.append(User(username, password))
  def DeleteUser(self, username):
    index = self.FindUsername(username)
    if index != -1:
      self.Userlist.pop(index)
  def Strength(self, password):
    strength = 0
    if len(password) >= 8:
      strength += 1
    if any(char.isupper() for char in password):
      strength += 1
    if any(char.islower() for char in password):
      strength += 1
    if any(char.isdigit() for char in password):
      strength += 1
    if any(char in "!@#$%^&*()_+{}[]:;<>?/\|" for char in password):
      strength += 1
    return strength
  def T(self,num):
    print(self.Userlist[num].UserName)
#Main
ulist=UserList("Final Project Passwords.txt")
ulist.ReadUserFile()
while True:
  print("\n1) Add a New User")
  print("2) Delete an Existing User")
  print("3) Change Password on an Existing User")
  print("4) Display All Users")
  print("5) Save Changes to File")
  print("6) Quit\n")
  uselect = input("Enter your selection: ")
  #Catch not numbers
  if uselect.isdigit() == False:
    print("\nInvalid Selection")
    continue
  uselect = int(uselect)
  #Add User
  if uselect == 1:
    username = input("\nEnter a username: ")
    if ulist.FindUsername(username) != -1:
      print("\nUsername Already Exists")
    else:
      print("\nPassword Guidelines:\nShould have at least 8 characters\nShould contain at least 1 uppercase letter\nShould contain at least 1 lowercase letter\nShould include a number\nShould include a special character\n")
      password = ""
      while True:
        password = input("\nEnter a password: ")
        if ulist.Strength(password) < 5:
          print("\nThis password is weak - " + str(ulist.Strength(password)))
        else:
          break
      ulist.AddUser(username, password)
      if ulist.FindUsername(username)==-1:
        print("\nSomething went wrong, please try again")
      print("\nUser Added")
  #Delete User
  if uselect == 2:
    username = input("\nEnter a username: ")
    if (ulist.FindUsername(username) == -1):
      print("/nUsername not found")
    else:
      ulist.DeleteUser(username)
  #Change password
  if uselect == 3:
    username = input("Enter a username: ")
    if ulist.FindUsername(username) == -1:
      print("\nUsername Not Found")
  #Print Users
  if uselect == 4:
    ulist.DisplayUserList()
  #Save to file
  if uselect == 5:
    ulist.WriteUserFile()
    print("\nChanges Saved")
  #Quit
  if uselect == 6:
    break
  #Catch unsused numbers
  if uselect < 1 or uselect > 6:
    print("\nInvalid Selection")