from pybaseball.pybaseball import statcast
from pybaseball.pybaseball import statcast_batter
from pybaseball.pybaseball import playerid_lookup
import pandas as pd

playerid_lookup('bichette','bo')


start_dt = '2022-09-01'
end_dt = '2022-09-30'
team = 'TOR'


output = statcast(start_dt, end_dt, team)
output.to_csv('Pitching.csv', index = False)
# output.to_csv('D:\Documents\Projects\BaseballBot\\test.csv', index = False)
