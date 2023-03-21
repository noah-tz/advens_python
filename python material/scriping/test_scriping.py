import df_macabbi




def test_macabbi():
    assert type(df_macabbi.parser(df_macabbi.games[0])) == dict


    