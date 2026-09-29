# AI Career Agent – n8n

Automatisation de la recherche et du suivi des candidatures grâce à **n8n**, **OpenAI/Gemini**, Gmail, Google Sheets, Google Drive et Google Calendar.

## Fonctionnalités

* Analyse du profil et des demandes de candidature
* Recherche d'offres de stage et d'emploi
* Analyse du CV fourni
* Génération d'e-mails de candidature
* Confirmation avant l'envoi d'une candidature
* Envoi d'e-mails avec CV en pièce jointe
* Suivi des candidatures avec Google Sheets
* Relances automatiques
* Détection des réponses des recruteurs
* Création de rappels d'entretiens dans Google Calendar
* Notifications par e-mail

## Architecture

```text
User / Chat
     |
     v
 AI Career Agent
     |
     +---- CV / Google Drive
     +---- Recherche Web
     +---- Gmail
     +---- Google Sheets
     +---- Google Calendar
     |
     v
Suivi et automatisation des candidatures
```

## Technologies

* n8n
* OpenAI / Google Gemini
* Gmail API
* Google Sheets
* Google Drive
* Google Calendar
* Webhooks

## Installation

1. Installer ou ouvrir une instance n8n.
2. Importer le fichier `workflow.json`.
3. Configurer les credentials :

   * Gmail
   * Google Drive
   * Google Sheets
   * Google Calendar
   * OpenAI ou Google Gemini
4. Remplacer les placeholders par vos propres IDs et paramètres.
5. Configurer le webhook.
6. Activer le workflow.

## Configuration

Les informations personnelles et identifiants ont été remplacés par des placeholders dans la version GitHub.

Exemples :

```text
YOUR_EMAIL@gmail.com
YOUR_GOOGLE_SHEET_ID
YOUR_GMAIL_CREDENTIAL_ID
YOUR_GOOGLE_SHEETS_CREDENTIAL_ID
YOUR_GOOGLE_CALENDAR_CREDENTIAL_ID
YOUR_GOOGLE_DRIVE_CREDENTIAL_ID
YOUR_OPENAI_CREDENTIAL_ID
YOUR_GEMINI_CREDENTIAL_ID
```


## Auteur

Salma Bellamine

