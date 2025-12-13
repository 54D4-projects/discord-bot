# 🤖 FEM Trading Bot

Wielofunkcyjny bot Discord stworzony dla społeczności FEM Trading. Bot integruje śledzenie kryptowalut, system zgłoszeń (ticketów) oraz sztuczną inteligencję (OpenAI) do pomocy użytkownikom.

## ✨ Główne Funkcje

### 1. 📉 Śledzenie Kursu Bitcoina
* Bot co godzinę automatycznie pobiera aktualne dane o Bitcoinie (Cena, High/Low 24h, Zmiana procentowa).
* Wysyła estetyczny Embed na skonfigurowany kanał.

### 2. 🎫 System Ticketów (Wsparcia)
* Użytkownicy mogą otworzyć prywatne zgłoszenie za pomocą przycisku na kanale pomocy.
* Bot tworzy nowy, prywatny kanał (widoczny tylko dla autora i administracji).
* Nadaje nazwę kanału w formacie `użytkownik_ticket`.
* Możliwość zamknięcia zgłoszenia komendą `!close_ticket`.

### 3. 🧠 Asystent AI
* Zintegrowany z modelem GPT-4o-mini (OpenAI).
* Komenda `!pomoc <pytanie>` pozwala uzyskać natychmiastową odpowiedź od sztucznej inteligencji w języku polskim.

### 4. 🛡️ Administracja
* Komenda `!pomoc_admina` do szybkiego wezwania pomocy.

---

## 🛠️ Instalacja i Wymagania

Bot wymaga zainstalowanego **Python 3.8+**.

1. **Sklonuj repozytorium lub pobierz pliki:**
   ```bash
   git clone <twoj-link-do-repo>
