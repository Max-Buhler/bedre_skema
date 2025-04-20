

class Controller:
    def __init__(self,model,view):
        #Model og view gives sådan at controller kan interegere med dem
        self.__model = model
        self.__view = view
    
    def updateView(self):
        #Data hentes fra model med en request, som bruger data fra view i forhold til år og uge
        data = self.__model.getSkema({'type': 'skema', 'week': f'{self.__view.week}', 'year': f'{self.__view.year}'})
        #Data sendes til view, hvor et nyt skema laves
        self.__view.draw(data,self)

