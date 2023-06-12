
import pandas as pd
import numpy as np
from scipy import stats

def get_stat_par(outcomes, policies):
    pol_dict = {}

    for policy in policies.cat.categories:
        pol_dict[policy] = pd.DataFrame(columns=outcomes.columns)

        # Filter outcomes for the current policy
        policy_outcomes = outcomes.loc[policies == policy]

        # Calculate statistical parameters for each outcome using describe()
        describe_stats = policy_outcomes.describe([.1,.25,.50,.75,.90,.95,.99])
        pol_dict[policy] = describe_stats

    return pol_dict