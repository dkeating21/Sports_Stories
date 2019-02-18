import requests
from bs4 import BeautifulSoup
from appendCSV import *
from file_system import *

file = open("fixtures.txt", "r")
for line in file:

    filename = line.replace('\n', "").replace('/',"").replace('-', " ")
    rugbyfile = createFile(line)
    if rugbyfile is False:

        print("File " + filename + " up to date")

    else:

        page = requests.get('https://www.ultimaterugby.com/match/' + line + '/commentary')
        """
        url = https://www.ultimaterugby.com/match/team1-vs-team2-at-stadium-date/number-increments-based-on-league/commentary
        """
        soup = BeautifulSoup(page.content, 'html.parser')

        match_data = soup.find_all("div", {"class": "block-summary match-summary"})
        for match in match_data:

            info = ["Date", "Event", "Card Colour", "Time", "Conversion", "For"]
            writeToFile(info, rugbyfile)

            host = match.find_all("div", {"class": "team-home"})
            for home in host:
                homeTeam = home.text.strip()
                homeTeam = homeTeam.lower()

            visitor = match.find_all("div", {"class": "team-away"})
            for away in visitor:
                awayTeam = away.text.strip()
                awayTeam = awayTeam.lower()

            dateOfMatch = match.find_all("div", {"class": "status-ko"})
            for date in dateOfMatch:
                dateString = date.text.strip()

            scores = match.find_all("div", {"class": "score-cell"})
            homeScore = scores[0].text
            awayScore = scores[1].text

            #info = ["", "", "", "", homeTeam, homeScore]
            #writeToFile(info, rugbyfile)
            #info = ["", "", "", "", awayTeam, awayScore]
            #writeToFile(info, rugbyfile)

            event_strings = ["event event-home", "event event-away"]

            team = 0
            for check_who_event_for in event_strings:
                game_data = soup.find_all("div", {"class": check_who_event_for})
                for event_type in game_data:
                    time_of_event = event_type.find_all("div", {"class": "time"})
                    #player_of_event = event_type.find_all("div", {"class": "bubble"})
                    for times in time_of_event:
                        event_time = times.text
                        event_time = event_time.replace('\n', "").replace('\t', "").replace("'", "")

                    """
                    for player in player_of_event:
                        player_event = player.text
                        player_event = player_event.replace('\n', " ").replace('\t', " ")
                        print(player_event)
                    """

                    if check_who_event_for == "event event-home":
                        whatTeam = homeTeam
                        if whatTeam == "kings":
                            whatTeam = "southern kings"
                        elif whatTeam == "cardiff":
                            whatTeam = "cardiff blues"
                        elif whatTeam == "glasgow":
                            whatTeam = "glasgow warriors"
                        elif whatTeam == "treviso":
                            whatTeam = "benetton"
                    else:
                        whatTeam = awayTeam
                        if whatTeam == "kings":
                            whatTeam = "southern kings"
                        elif whatTeam == "cardiff":
                            whatTeam = "cardiff blues"
                        elif whatTeam == "glasgow":
                            whatTeam = "glasgow warriors"
                        elif whatTeam == "treviso":
                            whatTeam = "benetton"


                    if "Missed Penalty" in event_type.text:
                        info = ["Penalty", "", event_time, "Missed", whatTeam]
                        writeToFile(info, rugbyfile)

                    if "Penalty Try" in event_type.text:
                        info = ["Try", "", event_time, conversion, whatTeam]
                        writeToFile(info, rugbyfile)

                    elif "Try" in event_type.text:
                        info = ["Try", "", event_time, conversion, whatTeam]
                        writeToFile(info, rugbyfile)

                    elif "Kick at Goal" in event_type.text:
                        info = ["Penalty", "", event_time, "Scored", whatTeam]
                        writeToFile(info, rugbyfile)

                    elif "Drop Goal" in event_type.text:
                        info = ["Drop Goal", "", event_time, "", whatTeam]
                        writeToFile(info, rugbyfile)

                    elif "Missed Conversion" in event_type.text:
                        conversion = "Missed"

                    elif "Conversion" in event_type.text:
                        conversion = "Converted"

                    elif "Card" in event_type.text:
                        if "Yellow" in event_type.text:
                            colour = "Yellow"
                        elif "Red" in event_type.text:
                            colour = "Red"
                        info = ["Card", colour, event_time, "", whatTeam]
                        writeToFile(info, rugbyfile)

                    elif "Substitution" in event_type.text:
                        info = ["Substitution", "", event_time, "", whatTeam]
                        writeToFile(info, rugbyfile)
                team = team + 1