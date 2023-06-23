import pandas as pd
import numpy as np
import random

# Helper functions are functions that don't necessarily exist to be called directly, 
#   but exist to be used by other functions to complete their work.

# Part 2 Functions ======================================

adjectives = ['blue', 'large', 'grainy', 'substantial', 'potent', 'thermonuclear']

nouns = ['food', 'house', 'tree', 'bicycle', 'toupee', 'phone']

def random_phrase():
    adj = random.choice(adjectives)
    #noun = np.random.choice(nouns)
    #random_index = random.randint(0, len(nouns)-1)
    #noun = nouns[random_index]
    noun = random.sample(nouns, 1)[0] # ['food']

    return adj + ' ' + noun

# print(random_phrase())
# print(random_phrase())
# print(random_phrase())

def random_float(min_val, max_val):
    return random.uniform(min_val, max_val)

# print(random_float(2,4))
# print(random_float(2,4))
# print(random_float(2,4))

def random_bowling_score():
    return random.randint(0, 300)

# print(random_bowling_score())
# print(random_bowling_score())
# print(random_bowling_score())

def silly_tuple():
    return (random_phrase(), round(random_float(1,5), 1), random_bowling_score())

# print(silly_tuple())
# print(silly_tuple())
# print(silly_tuple())

def silly_tuple_list(num_tuples):
    tuple_list = []
    for item in range(num_tuples):
        tuple_list.append(silly_tuple())

    return tuple_list

# print(silly_tuple_list(3))
# print(silly_tuple_list(6))
# print(silly_tuple_list(2))

# Part 3 Functions ======================================

test_df = pd.DataFrame(np.array([[1,2,3],[4,5,6],[7,8,9]]))
null_df = pd.DataFrame(np.array([[1,np.nan,3],[4,5,np.nan],[np.nan,8,9]]))

def null_count(df):
    return df.isnull().sum().sum()

# print(null_count(test_df))
# print(null_count(null_df))

def train_test_split(df, frac=0.8):
    train = df.sample(frac=frac)
    test = df.drop(train.index).sample(frac=1.0)
    return train, test

#print(train_test_split(test_df))

def randomize(df, seed):
    return df.sample(frac=1.0, random_state=seed)

#print(randomize(test_df, 10))

address_df = pd.DataFrame({'address': ['890 Jennifer Brooks\nNorth Janet, WY 24785',
                                    '8394 Kim Meadow\nDarrenville, AK 27389',
                                    '379 Cain Plaza\nJosephburgh, WY 06332',
                                    '5303 Tina Hill\nAudreychester, VA 97036']})
    
def addy_split(addy_series):
    # Blank DataFrame
    df = pd.DataFrame()

    # Lists to add info
    city_list = []
    state_list = []
    zip_list = []

    for addy in addy_series:
        # Find the values in the strings
        second_half = addy.split('\n')[1]
        city = second_half.split(',')[0]
        state = second_half.split()[-2]
        zip = second_half.split()[-1]
        
        # Add the strings to lists
        city_list.append(city)
        state_list.append(state)
        zip_list.append(zip)
    
    # Add the lists as new columns on the df
    df['city'] = city_list
    df['state'] = state_list
    df['zip'] = zip_list

    return df

#print(addy_split(address_df['address']))

def abbr_2_st(state_series, abbr_2_st=True):
    state_dict = {"AL":"Alabama","AK":"Alaska","AZ":"Arizona","AR":"Arkansas","CA":"California","CO":"Colorado","CT":"Connecticut","DE":"Delaware","FL":"Florida","GA":"Georgia","HI":"Hawaii","ID":"Idaho","IL":"Illinois","IN":"Indiana","IA":"Iowa","KS":"Kansas","KY":"Kentucky","LA":"Louisiana","ME":"Maine","MD":"Maryland","MA":"Massachusetts","MI":"Michigan","MN":"Minnesota","MS":"Mississippi","MO":"Missouri","MT":"Montana","NE":"Nebraska","NV":"Nevada","NH":"New Hampshire","NJ":"New Jersey","NM":"New Mexico","NY":"New York","NC":"North Carolina","ND":"North Dakota","OH":"Ohio","OK":"Oklahoma","OR":"Oregon","PA":"Pennsylvania","RI":"Rhode Island","SC":"South Carolina","SD":"South Dakota","TN":"Tennessee","TX":"Texas","UT":"Utah","VT":"Vermont","VA":"Virginia","WA":"Washington","WV":"West Virginia","WI":"Wisconsin","WY":"Wyoming"}

    def abbrev_replace(abbrev):
        return state_dict[abbrev]
    
    def state_replace(state_name):
        reverse_state_dict = dict((v, k) for k, v in state_dict.items())
        return reverse_state_dict[state_name]
    
    if abbr_2_st:
        return state_series.apply(abbrev_replace)
    else:
        return state_series.apply(state_replace)
    
addy_states = addy_split(address_df['address'])['state']

full_state_names_column = abbr_2_st(addy_states)

# print(abbr_2_st(full_state_names_column, abbr_2_st=False))

def list_2_series(list_2_series, df):
    pass

def rm_outlier(df):
    pass

def split_dates(date_series):
    pass