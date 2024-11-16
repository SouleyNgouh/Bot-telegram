import telebot  
from dotenv import load_dotenv  
import os  

# Charger les variables d'environnement  
load_dotenv()  

# Création de l'instance du bot  
bot = telebot.TeleBot("7922927810:AAGrxvMXEBlw2CHqmcEDVOP0A5rdF-irh7I")  

# Suppression du webhook  
bot.remove_webhook()  
print("Webhook supprimé avec succès!")
