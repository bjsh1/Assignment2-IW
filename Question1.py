#1.Create a variable, paragraph, that has the following content:
# "Python is a great language!", said Fred. "I don't ever rememberhaving this much fun before."

class Pytalk:

    def __init__(self,name):
        self.name=name
    
    def python_talk(self):
        print(''' "Python is a great language!", said {}."I don't ever remember having this much fun before" '''.format(self.name))

talk=Pytalk('Fred')

talk.python_talk()