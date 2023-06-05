from scipy import stats
import numpy as np
import pandas as pd

def get_stat_par(outcomes, policies):
    """
    Calculate statistical parameter of a list of numbers.

    INPUT:
        outcomes: The outcomes of the experiment as a dict()
        policies: The list of policies evaluated in the experiment

    OUTPUT:
        A dict() with the policies as keys containing data frames with the statistical parameters for every outcome.
        Parameters are:
        Mean: The mean is the average value of a dataset. It is calculated by summing all the values and dividing the sum by the number of values.

        Mode: The mode represents the most frequently occurring value(s) in a dataset. It is the value(s) that has the highest frequency.

        Median: The median is the middle value of a sorted dataset. It divides the dataset into two equal halves. If the dataset has an odd number of values, the median is the middle value. If the dataset has an even number of values, the median is the average of the two middle values.

        Standard Deviation: The standard deviation measures the spread or dispersion of the values in a dataset. It quantifies how much the values deviate from the mean. A higher standard deviation indicates greater variability in the dataset.

        Minimum: The minimum is the smallest value in a dataset.

        Maximum: The maximum is the largest value in a dataset.

        Range: The range is the difference between the maximum and minimum values in a dataset. It provides an indication of the spread of the dataset.

        Interquartile Range (IQR): The IQR is a measure of statistical dispersion. It is the range between the first quartile (25th percentile) and the third quartile (75th percentile) of a dataset. It represents the range of the middle 50% of the data.

        First Quartile (Q1): The first quartile is the value below which 25% of the data falls. It is also known as the 25th percentile.

        Third Quartile (Q3): The third quartile is the value below which 75% of the data falls. It is also known as the 75th percentile.

        Quartile Deviation (QD): The quartile deviation is half of the interquartile range. It provides a measure of the spread of the middle 50% of the data.

        Skewness: Skewness measures the asymmetry of a distribution. Positive skewness indicates a longer tail on the right side, while negative skewness indicates a longer tail on the left side.

        Kurtosis: Kurtosis measures the peakedness or flatness of a distribution. Higher kurtosis values indicate more extreme tails and a sharper peak, while lower values indicate lighter tails and a flatter peak.

    """

    outcome_adj = outcomes
    outcome_adj['policies'] = policies
    outcome_adj_df = pd.DataFrame(outcome_adj)

    pol_dict = {}

    for policy in policies.cat.categories:
        pol_dict[policy] = pd.DataFrame(index=['mean', 'mode', 'median', 'stdev', 'min', 'max', 'range', 'iqr', 'first_q', 'third_q','Quartile distance', 'skewness', 'kurtosis'])

        # Group the DataFrame by 'policies' column
        policy_group = outcome_adj_df.groupby('policies')

        # Calculate statistical parameters for each item
        for item in outcome_adj_df.select_dtypes(include='number').columns:
            data = policy_group.get_group(policy)[item]
            mean = data.mean()
            mode = tuple(data.mode())
            median = data.median()
            stdev = data.std()
            minimum = data.min()
            maximum = data.max()
            range_stat = maximum - minimum
            iqr = stats.iqr(data, interpolation = 'midpoint')
            first_q = np.percentile(data, 25, interpolation = 'midpoint')
            third_q = np.percentile(data, 75, interpolation = 'midpoint')
            qd = iqr / 2
            skewness = stats.skew(data)
            #kurtosis
            kurtosis = stats.kurtosis(data)
            pol_dict[policy][item] = [mean, mode, median, stdev, minimum, maximum, range_stat, iqr, first_q, third_q, qd, skewness, kurtosis]

    return pol_dict