from module import *
from view import *

class Controller:
    def __init__(self,model,view):
        self.__model = model
        self.__view = view
    
    def updateView(self):
        data = self.__model.getSkema({'type': 'skema', 'week': f'{self.__view.week}', 'year': f'{self.__view.year}'})
        self.__view.draw(data,self)

control = Controller(UserModel(),View())
control.updateView()