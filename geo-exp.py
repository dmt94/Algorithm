def get_follower_prediction(follower_count, influencer_type, num_months):
        if influencer_type == "fitness":
            return follower_count * (4 ** (num_months - 1))
        if influencer_type == "cosmetic":
            return follower_count * (3 ** (num_months - 1))
        return follower_count * (2 ** (num_months - 1))

# geometric sequence formula
# total = a1 * r^(n-1)
# total = total followers after a set amount (n) = number of months
# n = total number of months
  # n --> keeps going, each month an = a1 * r^(n-1)
# r = set ratio 
# a1 = starting integer (IN THIS CASE, current folower_count)