<<<<<<< HEAD
# SmartCaisse — Frontend

Application de caisse pour la cantine SIAT : saisie des commandes, vérification faciale du client par webcam, bons de commande imprimables en PDF, et rapports financiers par travailleur.

## Prérequis

- [Node.js](https://nodejs.org/) **18 ou supérieur**
- Un navigateur avec accès à la webcam (pour la reconnaissance faciale)

Vérifier les versions installées :

```bash
node -v
```

## Installer pnpm

Choisis **une** des méthodes ci-dessous.

### Option 1 : avec npm

```bash
npm install -g pnpm
```

### Option 2 : avec Corepack (fourni avec Node.js)

```bash
corepack enable
corepack prepare pnpm@latest --activate
```

### Option 3 : Windows (PowerShell)

```powershell
iwr https://get.pnpm.io/install.ps1 -useb | iex
```

Vérifier l'installation :

```bash
pnpm -v
```

> Après l'installation, ferme et rouvre le terminal si la commande `pnpm` n'est pas reconnue.

## Installation du projet

Depuis le dossier `frontend` :

```bash
cd frontend
pnpm install
```

## Lancer le projet

Mode développement :

```bash
pnpm dev
```

L'application est disponible sur [http://localhost:5173](http://localhost:5173) (le port exact s'affiche dans le terminal).

Autres commandes utiles :

| Commande         | Description                              |
| ---------------- | ---------------------------------------- |
| `pnpm dev`       | Lance le serveur de développement        |
| `pnpm build`     | Génère la version de production (`dist`) |
| `pnpm preview`   | Prévisualise la version de production    |
| `pnpm lint`      | Vérifie le code avec ESLint              |

> Les scripts disponibles dépendent de ton `package.json`.

## Connexion (mode test)

| Champ        | Valeur                        |
| ------------ | ----------------------------- |
| Nom          | N'importe lequel (ex : `Sarah`) |
| Mot de passe | `1234`                        |

Ces identifiants sont codés en dur pour les tests. Ils devront être remplacés par une vraie authentification via l'API.

## Structure du projet

```
src/
├── App.jsx
└── features/
    └── caissiere/
        ├── components/    # composants d'interface (formulaire, rapport, modales...)
        ├── hooks/         # logique réutilisable (commandes, vérification faciale)
        ├── pages/         # page principale CaissePage
        ├── schemas/       # validation (réservé)
        ├── types/         # types (réservé)
        ├── utils.js       # calculs, agrégations, impression PDF
        ├── mockData.js    # données de test
        └── index.js       # API publique de la feature
```

Chaque feature expose uniquement ce qui est exporté dans son `index.js`.

## Dépendances principales

- React + React Router (`react-router-dom`)
- Tailwind CSS
- lucide-react (icônes)

Si une dépendance manque :

```bash
pnpm add react-router-dom lucide-react
```

## Dépannage

- **Page blanche** : vérifie que `App.jsx` enveloppe l'application dans un `<BrowserRouter>`, et ouvre la console du navigateur (F12) pour lire l'erreur.
- **Page sans style** : Tailwind CSS n'est pas configuré ou n'est pas importé dans le CSS global.
- **Caméra non détectée** : autorise l'accès à la webcam dans le navigateur. Sans caméra, l'application passe en mode test et valide l'identité automatiquement.
- **`pnpm` non reconnu** : rouvre le terminal ou réinstalle pnpm avec l'une des méthodes ci-dessus.
