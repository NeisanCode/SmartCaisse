import os
import clr

# 1. Charger la bibliothèque OpenBioMini.Core.dll
chemin_dll = os.path.join(os.path.dirname(__file__), "OpenBioMini.Core.dll")
clr.AddReference(chemin_dll)

from OpenBioMini import BioMiniController

# 2. Initialiser le lecteur
controller = BioMiniController()
init_ok = controller.Initialize()

print("Initialisation SDK :", init_ok)
print("Lecteur connecté   :", controller.IsConnected)

if init_ok and controller.IsConnected:
  print("Modèle :", controller.ScannerModel)
  print("Série  :", controller.ScannerSerial)
  print("\nPosez votre doigt sur le capteur...")

  resultat = controller.Capture(5000)
  if resultat.Success:
    print("Empreinte capturée ! Qualité :", resultat.Quality)
  else:
    print("Erreur capture :", resultat.ErrorMessage)

  controller.Dispose()
else:
  print("Aucun lecteur détecté par le SDK.")
