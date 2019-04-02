import pandas as pd

from Utilities import Consts, plot_data


def smooth(df, window_size):
    rolling = df.rolling(window=window_size)
    rolling_mean = rolling.mean()
    new_df = rolling_mean[window_size - 1:]
    return new_df


def start_smooth(window_size):
    df = pd.read_csv('BTC-Samples.csv.gz', compression='gzip')
    df.sort_values(Consts.CREATED_UTC, inplace=True)
    df = df.tail(24 * 30)
    df.set_index([Consts.COIN_SYMBOL, Consts.DATE_UTC, Consts.CREATED_UTC], inplace=True)

    plot_data.prep_plot_single_data(df.index.levels[1], df['global_social-2897'], 'global_social-2897')
    plot_data.prep_plot_single_data(df.index.levels[1], df['individual_social-4009'], 'individual_social-4009')

    smooth_df = smooth(df, window_size)
    plot_data.prep_plot_single_data(smooth_df.index.levels[1][window_size - 1:], smooth_df['global_social-2897'], 'global_social-2897 smooth')
    plot_data.prep_plot_single_data(smooth_df.index.levels[1][window_size - 1:], smooth_df['individual_social-4009'], 'individual_social-4009 smooth')
    plot_data.plot_data()

    return smooth_df


if __name__ == "__main__":
    __window_size = 24
    df_s = start_smooth(window_size=__window_size)

