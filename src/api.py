import requests
from datetime import datetime


def is_holiday(date: str, country: str = "FR") -> bool:
    """
    Vérifie si une date est un jour férié via une API publique.

    Retourne True si la date est fériée.
    Retourne False en cas d'erreur réseau ou de problème API.
    """

    try:
        year = datetime.strptime(date, "%Y-%m-%d").year

        url = f"https://date.nager.at/api/v3/PublicHolidays/{year}/{country}"

        response = requests.get(url, timeout=5)

        response.raise_for_status()

        holidays = response.json()

        for holiday in holidays:
            if holiday.get("date") == date:
                return True

        return False

    except requests.exceptions.Timeout:
        print("Erreur API : le serveur a mis trop de temps à répondre.")
        return False

    except requests.exceptions.ConnectionError:
        print("Erreur API : impossible de contacter le serveur.")
        return False

    except requests.exceptions.HTTPError as error:
        print(f"Erreur API HTTP : {error}")
        return False

    except ValueError:
        print("Erreur : format de date invalide.")
        return False

    except requests.exceptions.JSONDecodeError:
        print("Erreur API : réponse JSON invalide.")
        return False