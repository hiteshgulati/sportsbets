import numpy as np
import pandas as pd

bet_format = {'A': 0, 'B': 0,'Amount':0 }
all_bets = []


def bet_on_trend(point_detail, bet_amount=100):
    bet = bet_format.copy()
    if point_detail['Bet_A'] <= point_detail['Bet_A_Pre']:
        bet['A'] = point_detail['Bet_A'] * bet_amount
    else:
        bet['B'] = point_detail['Bet_B'] * bet_amount
    bet['Amount'] = bet_amount
    all_bets.append(bet)
    return 0


def bet_anti_trend(point_detail, bet_amount=100):
    bet = bet_format.copy()
    if point_detail['Bet_A'] >= point_detail['Bet_A_Pre']:
        bet['A'] = point_detail['Bet_A'] * bet_amount
    else:
        bet['B'] = point_detail['Bet_B'] * bet_amount
    bet['Amount'] = bet_amount
    all_bets.append(bet)
    return 0


def net_return(winner):
    earned = 0
    spent = 0
    for each_bet in all_bets:
        earned += each_bet[winner]
        spent += each_bet['Amount']
    print("Earned: ", earned, "Spent: ", spent, "Gain/Loss%", ((earned/spent)-1)*100)


def run():
    file_name = "match.xlsx"
    match = pd.read_excel(file_name, sheet_name="Sheet1")
    for i, point_detail in match.iterrows():
        bet_on_trend(point_detail)
    net_return('A')
if __name__ == '__main__':
    run()
