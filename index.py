import os
import clr

# Forcer Python/Windows à trouver toutes les DLL 
dossier = os.path.dirname(os.path.abspath(__file__))
os.chdir(dossier)
os.environ["PATH"] = dossier + os.pathsep + os.environ["PATH"]

try:
  clr.AddReference(os.path.join(dossier, "Suprema.UFScanner.dll"))
  from Suprema import UFScannerManager

  manager = UFScannerManager(None)
  statut = manager.Init()
  print("1. Démarrage SDK :", statut)
  print("2. Lecteurs détectés :", manager.Scanners.Count)

  if manager.Scanners.Count > 0:
    scanner = manager.Scanners[0]
    print("3. Modèle trouvé :", scanner.ScannerType, "| Série :", scanner.Serial)
    print("\nPosez votre doigt sur le lecteur maintenant...")

    scanner.Timeout = 5000
    res_capture = scanner.CaptureSingleImage()
    if str(res_capture) == "OK":
      print("SUCCÈS ! Empreinte capturée avec succès !")
    else:
      print("Échec capture :", res_capture)
  else:
    print(
        "\nLe SDK fonctionne, mais ne voit pas le lecteur (problème de pilote"
        " USB)."
    )

  manager.Uninit()

except Exception as e:
  print("\nERREUR BLOQUANTE :", e)
