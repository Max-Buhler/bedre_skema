from module.module import *
from view import *
from control import *

#Laver en instans af control
control = Controller(UserModel(),View())
#Kører programmet
control.updateView()