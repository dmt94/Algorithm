# ocialytics needs a new tool that allows 
# big brands to see how many of an influencer's followers are 
# loyal to their brand. Complete the get_avg_brand_followers function. 
# It takes two inputs:
# all_handles: a 2-dimensional list, or "list of lists" of strings representing instagram user handles on a per-influencer basis.
# brand_name: a string.

# get_avg_brand_followers 
# returns the average number of handles 
# that contain the brand_name across all the lists. 
# Each list represents the audience of a single influencer.

all_handles = [
    ["cosmofan1010", "cosmogirl", "billjane321"],
    ["cosmokiller", "gr8", "cosmojane3"],
    ["iloveboots", "paperthin"]
]
brand_name = "cosmo"
# each list in all_handles reprsent an influencer
# for each influencer/list, the strings are usernames that represent influencer's followers

def get_avg_brand_followers(all_handles, brand_name):
    average_handle = 0
    for handles in all_handles:
        for handle in handles:
            if brand_name in handle:
                average_handle += 1
    return average_handle / len(all_handles)