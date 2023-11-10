def solution(survey, choices):
    
    indicator1 = {"R": 0, "T": 0}
    indicator2 = {"C": 0, "F": 0}
    indicator3 = {"J": 0, "M": 0}
    indicator4 = {"A": 0, "N": 0}
    
    point = {1:3,2:2,3:1,4:0,5:1,6:2, 7:3}
    
    for sur, choice in zip(survey, choices):
        
        if choice < 4:
            if sur[0] in indicator1:
                indicator1[sur[0]] += point[choice] 
            elif sur[0] in indicator2:
                indicator2[sur[0]] += point[choice] 
            elif sur[0] in indicator3:
                indicator3[sur[0]] += point[choice] 
            elif sur[0] in indicator4:
                indicator4[sur[0]] += point[choice] 
        elif choice > 4:
            if sur[1] in indicator1:
                indicator1[sur[1]] += point[choice] 
            elif sur[1] in indicator2:
                indicator2[sur[1]] += point[choice] 
            elif sur[1] in indicator3:
                indicator3[sur[1]] += point[choice] 
            elif sur[1] in indicator4:
                indicator4[sur[1]] += point[choice] 
            elif sur[1] in indicator4:
                indicator4[sur[1]] += point[choice] 
        
    result = ""


    for indicator in [indicator1, indicator2, indicator3, indicator4]: 
        max_value = max(indicator.values())
        max_keys = [k for k, v in indicator.items() if v == max_value]
        result += max_keys[0]

    
    return result
