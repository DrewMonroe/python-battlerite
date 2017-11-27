# python-battlerite

This library provides a wrapper around the Battlerite REST API and is a work in progress.

### Installation
```bash
git clone https://github.com/DrewMonroe/python-battlerite.git
cd battlerite
pip install .
```

### Usage
```python
b = BattleriteAPI("insert-your-api-key-here")
# Will print information about your account
print(b.get_player_information(playerName="your-username"))
# Will print information about matches that you've played in
print(b.get_match_information(playerName="your-username"))
```
