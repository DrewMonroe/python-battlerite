import requests


class BattleriteAPI(object):
    MATCH_URL = "https://api.dc01.gamelockerapp.com/shards/global/matches"
    PLAYER_URL = "https://api.dc01.gamelockerapp.com/shards/global/players"
    CASUAL_2V2 = "QUICK2V2"
    CASUAL_3V3 = "QUICK3V3"

    def __init__(self, key):
        self.header = {
          "Authorization": key,
          "Accept": "application/vnd.api+json"
        }

    def get_player_information(self, playerName=None, playerid=None):
        """Returns player information based upon a given player name
        playerName can be either a string (a single player name), or a list of
        strings (a list of player names)
        playerid can be either a string (a single player id), or a list of
        strings (a list of player ids)
        """
        if playerName is playerid is None:
            raise Exception("No information provided")

        query = {}

        if playerName is not None:
            names = playerName if type(playerName) != list else ','.join(playerName)
            query["filter[playerName]"] = names
        if playerid is not None:
            ids = playerid if type(playerid) != list else ','.join(playerid)
            query["filter[playerids]"] = ids

        r = requests.get(BattleriteAPI.PLAYER_URL,
                         headers=self.header,
                         params=query)

        return r.json()

    def get_match_information(self,
                              playerName=None,
                              playerids=None,
                              teamNames=None,
                              gameMode=None,
                              earliest=None,
                              latest=None,
                              matchid=None):
        """Get match information
        playerName can either be a string or a list of strings
        teamName can either be a string or a list of strings
        gameMode can either be a string or a list of strings
        earliest can either be a datetime obejct, or a string in iso8601 format
        latest can either be a datetime obejct, or a string in iso8601 format
        matchid is a string of the match ID
        """
        if playerName is teamNames is gameMode is earliest is latest is matchid is None:
            raise Exception("No information provided")

        query = {}

        if playerName is not None:
            playerName = playerName if type(playerName) != list else ','.join(playerName)
            query['filter[playerNames]'] = playerName
        if playerids is not None:
            playerids = playerids if type(playerids) != list else ','.join(playerids)
            query['filter[playerids]'] = playerids
        if teamNames is not None:
            teamNames = teamNames if type(teamNames) != list else ','.join(teamNames)
            query['filter[teamNames]'] = teamNames
        if gameMode is not None:
            gameMode = gameMode if type(gameMode) != list else ','.join(gameMode)
            query['filter[gameMode]'] = gameMode
        if earliest is not None:
            earliest = earliest if type(earliest) == str else earliest.isoformat()
            query['filter[createdAt-start]'] = earliest
        if latest is not None:
            latest = latest if type(latest) == str else latest.isoformat()
            query['filter[createdAt-end]'] = latest

        r = requests.get(BattleriteAPI.MATCH_URL,
                         headers=self.header,
                         params=query)
        return r.json()
