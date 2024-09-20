import os,json
from textwrap import indent

EngFold = 'English Project'
vocab = 'Vocabulary.json'
homeFold = os.path.join(os.path.expanduser('~'), EngFold)

class setting():
    def __init__(self):
        self.isFolder()


    def isFolder(self):
        if not os.path.exists(homeFold):
            os.mkdir(homeFold)
        if not os.path.exists(os.path.join(homeFold, vocab)):
            data = dict()
            with open(os.path.join(homeFold, vocab), 'w') as f:
                json.dump(data,f, indent=4)

    def add_words(self,data):
        with open(os.path.join(homeFold, vocab), 'w') as f:
            json.dump(data, f, indent=4)
            print('write in json file',data)


    def get_dictanory(self):
        return json.load(open(os.path.join(homeFold, vocab)))
