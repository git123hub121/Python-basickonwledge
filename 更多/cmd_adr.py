import sys
import os
import pickle


class Person(object):
    filename = 'info.txt'
    #filename1 = 'info.data'
    def __init__(self, name, phone):
        self.name = name
        self.phone = phone
        self.personlist = {self.name: self.phone}

    def add(self):
        self.name = input("Enter name:")
        if self.name in self.personlist.keys():
            print("The name is exist!")
            
        else:
            self.phone = input("Enter phone:")
            self.personlist[self.name] = self.phone
            print("Contact saved!")


    def Modify(self):
        self.name = input("Enter name:")
        if self.name in self.personlist.keys():
            self.phone = input("Enter new phone:")
            self.personlist[self.name] = self.phone
            print( "Contact saved!")

        else:
            print("The name is not in here!!")


    def delete(self):
        self.name = input("Enter name:")
        if self.name in self.personlist.keys():
            del self.personlist[self.name]
            print( "Deleted!!")

        else:
            print("The name is not in here!!")


    def search(self):
        self.name = input("Enter name:")
        if self.name in self.personlist.keys():
            print( 'Name:%s,Phone:%s' % (self.name, self.phone))

        else:
            print("The name is not in here!!")


    def save(self):
        f = file(self.filename, 'w')#f = open(self.filename1,'wb')
        pickle.dump(self.personlist, f)
        f.close()
        print("Your contacts list has been saved to file:%s successfully~" % self.filename)


    def load(self):
        if os.path.exists(self.filename):
            f = file(self.filename)#f = open(self.filename1,'rb')
            self.personlist = pickle.load(f)
            f.close()

    def show(self):
        for self.name, self.phone in self.personlist.items():
            print( "Name:%s  Phone number:%s" % (self.name, self.phone))



if __name__ == '__main__':
    #os.system('clear')
    command = ['add', 'modify', 'search', 'delete', 'quit', 'show']
    person = Person('', '')
    person.load()
    while True:
        print("The contact person:")

        str = input('What are you going to do(add/modify/search/delete/show/quit)?\n')
        if str in command:
            if str == 'add':
                person.add()
            elif str == 'modify':
                person.Modify()
            elif str == 'search':
                person.search()
            elif str == 'delete':
                person.delete()
            elif str == 'show':
                person.show()
            else:
                ch = input("Your contacts list hasn't  been saved,save it now?(Y/N)")
                if ch == 'y':
                    person.save()
                    sys.exit()
                else:
                    sys.exit()
                print("Exit the System")

                break
        else:
            print("Please input the command!")
