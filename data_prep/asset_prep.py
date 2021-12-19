"""
This file prepares the data for use by the Asset class.
"""
import numpy as np
import pandas as pd

"""
Preparing investment by asset type.
We sort BEA data into 4 major categories, with accompanying minor categories:
    Equipment:
        Information processing equipment
        Industrial equipment
        Transportation equipment
        Other equipment
    Structures:
        Commercial and health care
        Manufacturing
        Power and communication
        Mining
        Other
    Intellectual property:
        Software
        Research and development
        Artistic
    Residential:
        Residential equipment
        Housing units
        Other residential structures
We remove the following asset types:
    Religious structures
    Brokers' commissions and other ownership transfer costs
    Other residential structures (dormitories and fraternity/sorority houses)
    Research and development by nonprofit institutions serving households
    These have indexes 56, 71, 73, 93, 94, 95
We also remove several unnecessary group totals.
"""
# Read in investment data
inv_type_data = pd.read_csv('BEA_investment_type.csv')
asset_type_data = pd.read_csv('BEA_asset_type.csv')
types = np.array(inv_type_data['asset_type'])
# Fix naming of asset types
types[36] = 'Office'
types[45] = 'Other commercial'
types[62] = 'Railroad structures'
types[64] = 'Other structures'
types[77] = 'Prepackaged software'
inv_type_data['asset_type'] = types
asset_type_data['asset_type'] = types
# Remove irrelevant asset types
unwanted_indexes = [56, 71, 73, 93, 94, 95]
group_indexes = [0, 1, 2, 9, 16, 17, 24, 33, 34, 35, 37, 38, 47, 48, 52, 55,
                 60, 65, 66, 68, 69, 74, 75, 76, 80, 81, 82, 90, 96]
inv_type_data.drop(unwanted_indexes, axis=0, inplace=True)
inv_type_data.drop(group_indexes, axis=0, inplace=True)
inv_type_data.reset_index(inplace=True)
asset_type_data.drop(unwanted_indexes, axis=0, inplace=True)
asset_type_data.drop(group_indexes, axis=0, inplace=True)
asset_type_data.reset_index(inplace=True)


"""
Adjusting by business type.

We split it between the corporate and noncorporate business sectors, and drop
the nonbusiness private sectors. Note that BEA data treats S corporations as
corporations.
"""
# Import investment history by investor type
inv_firm_data = pd.read_csv('BEA_investment_firm.csv')
inv_firm_data.set_index('firm_type', inplace=True)
inv_firm_data.transpose()
# Compute shares for corporations and sole proprietorships/partnerships
inv_firm_data['All types'] = inv_firm_data['Corporate'] + inv_firm_data['Noncorporate']
inv_firm_data['corp_share'] = inv_firm_data['Corporate'] / inv_firm_data['All types']
inv_firm_data['ncorp_share'] = (inv_firm_data['Sole proprietorships'] + inv_firm_data['Partnerships']) / inv_firm_data['All types']
inv_firm_data.transpose()


"""
Adjusting by BLS breakdown.

So far, we have not done a cross-tabulation effectively. This section rescales
the investment amounts based on the comparison of asset totals across major
asset types for the private business sector.

We first adjust investment totals to just use the private business total from
BEA Fixed Assets data, Table 6.1 for 2014.
"""









