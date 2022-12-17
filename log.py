import math

def get_influencer_score(num_followers, average_engagement_percentage):
    return average_engagement_percentage * math.log(num_followers, 2)

def test(num_followers, average_engagement_percentage):
    influencer_score = round(
        get_influencer_score(num_followers, average_engagement_percentage)
    )
    print(
        f"Using num_followers: {num_followers} and average_engagement_percentage: {average_engagement_percentage}"
    )
    print(f"Influencer score: {influencer_score}")
    print("----")


def main():
    test(40000, 0.3)
    test(43000, 0.1)
    test(100000, 0.6)
    test(200, 0.8)


main()