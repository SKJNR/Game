import pandas as pd
def gam(x_1, x_2, x_3, x_4, x_5, x_6, x_7, x_8, x_9):
    X = pd.DataFrame(columns=[['H-off_avg', 'H-off_ops', 'H-pit_whip', 'H-pit_k/9', 'V-off_avg',
                               'V-off_ops', 'V-pit_whip', 'V-pit_k/9', 'ballpark_id_ANA01',
                               'ballpark_id_ARL02', 'ballpark_id_ATL02', 'ballpark_id_ATL03',
                               'ballpark_id_BAL12', 'ballpark_id_BOS07', 'ballpark_id_CHI11',
                               'ballpark_id_CHI12', 'ballpark_id_CIN09', 'ballpark_id_CLE08',
                               'ballpark_id_DEN02', 'ballpark_id_DET05', 'ballpark_id_HOU03',
                               'ballpark_id_KAN06', 'ballpark_id_LOS03', 'ballpark_id_MIA02',
                               'ballpark_id_MIL06', 'ballpark_id_MIN04', 'ballpark_id_NYC20',
                               'ballpark_id_NYC21', 'ballpark_id_OAK01', 'ballpark_id_PHI13',
                               'ballpark_id_PHO01', 'ballpark_id_PIT08', 'ballpark_id_SAN02',
                               'ballpark_id_SEA03', 'ballpark_id_SFO03', 'ballpark_id_STL10',
                               'ballpark_id_STP01', 'ballpark_id_TOR02', 'ballpark_id_WAS11']])
    dict = {}

    X = X.append(dict, ignore_index=True)

    X["H-off_avg"] = x_1
    X["H-off_ops"] = x_2
    X["H-pit_whip"] = x_3
    X["H-pit_k/9"] = x_4
    X["V-off_avg"] = x_5
    X["V-off_ops"] = x_6
    X["V-pit_whip"] = x_7
    X["V-pit_k/9"] = x_8
    X[f"ballpark_id_{x_9}"] = 1
    X = X.fillna(0)
    return X
