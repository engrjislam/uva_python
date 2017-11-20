def main():
    test = int(input())
    case = 1
    while test > 0:
        websites, scores = [], []
        for i in range(0, 10):
            website, score = input().split(" ")
            websites.append(website)
            scores.append(int(score))
        
        max_score = max(scores)
        selectted_websites = []
        
        for x in range(0, 10):
            if scores[x] == max_score:
                selectted_websites.append(websites[x])
        
        print("Case #{}:".format(case))
        
        sorted(selectted_websites, key=lambda x:x[4])
        for x in selectted_websites:
            print(x)
            
        case += 1
        test -= 1

main()