import matplotlib.pyplot as plt


def prep_plot_single_data(np_dates, np_feature_data, feature_name):
    plt.figure('Feature {}'.format(feature_name))
    plt.xlabel('Dates')
    plt.plot(np_dates, np_feature_data, 'ro', label=feature_name)
    plt.legend()


def plot_data():
    plt.show()
    plt.close()
