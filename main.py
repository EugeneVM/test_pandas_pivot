import pandas as pd


def make_pivot_table():
    spends = pd.read_csv("in_data_p.csv")
    installs = pd.read_csv("in_data_a.csv")
    installs = installs.astype(int, errors='ignore')
    spends = spends.astype(float, errors='ignore')
    df = pd.merge(
        installs, spends, how='left', left_index=True, right_index=True)
    df = df.pivot_table(
        index=['app', 'Date', 'Campaign', 'os'], values=['Installs', 'spend'],
        aggfunc='sum')
    df.rename(columns=str.lower, inplace=True)
    df.rename_axis(index=str.lower, inplace=True)
    df['cpi'] = df['spend'] / df['installs']
    df.to_csv('/Users/evgenijvarygin/Projects/Python/ja-test-task/out.csv',
              float_format='%.3f')
    text = "Всего потрачено: {:.2f}, всего установок: {}. ".format(
        df['spend'].sum(), df['installs'].sum())
    text += "\nСводная таблица сохранена в файл 'out.csv'"
    print(text)


if __name__ == "__main__":
    make_pivot_table()
