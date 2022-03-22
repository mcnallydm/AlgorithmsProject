def dist(pt1, pt2):
    return abs(pt1[0]-pt2[0]) + abs(pt1[1]-pt2[1])

def min_max(house_list):
    x = 0
    y = 0
    minsum = -1     # Bottom left
    mindiff = -1    # Top left
    maxsum = -1     # Top right
    maxdiff = -1    # Bottom Right
    minsumpoint = []
    mindiffpoint = []
    maxsumpoint = []
    maxdiffpoint = []
    for house in house_list:    # O(n)
        sumxy = house[0]+house[1]
        diffxy = house[0]-house[1]
        if minsum==-1 or sumxy<minsum:
            minsum = sumxy
            minsumpoint = house
        if mindiff==-1 or diffxy<mindiff:
            mindiff = diffxy
            mindiffpoint = house
        if sumxy>maxsum:
            maxsum = sumxy
            maxsumpoint = house
        if diffxy>maxdiff:
            maxdiff = diffxy
            maxdiffpoint = house
    minmaxdist = max((maxsum-minsum), (maxdiff-mindiff))/2
    '''print(minmaxdist)'''
    lowerx = max(minsumpoint[0], mindiffpoint[0])
    upperx = min(maxsumpoint[0], maxdiffpoint[0])
    lowery = max(minsumpoint[1], maxdiffpoint[1])
    uppery = min(maxsumpoint[1], mindiffpoint[1])
    '''print("Lower Bound X:", lowerx)
    print("Upper Bound X:", upperx)
    print("Lower Bound Y:", lowery)
    print("Upper Bound Y:", uppery)'''
    sumdiffs = [minsumpoint, mindiffpoint, maxsumpoint, maxdiffpoint]
    corners = [[lowerx, lowery], [lowerx, uppery], [upperx, uppery], [upperx, lowery]]
    farthest1 = -1
    farthest2 = -1
    farpoint1 = []
    farpoint2 = []
    m1 = 1
    m2 = 1
    for idx in range(0,4):
        if dist(sumdiffs[idx], corners[idx])>farthest1:
            farthest1 = dist(sumdiffs[idx], corners[idx])
            farpoint1 = sumdiffs[idx]
        elif dist(sumdiffs[idx], corners[idx])>farthest2:
            farthest2 = dist(sumdiffs[idx], corners[idx])
            farpoint2 = sumdiffs[idx]
    if farpoint1==minsumpoint or farpoint1==maxsumpoint:
        m1 = -1
    if farpoint2==minsumpoint or farpoint2==maxsumpoint:
        m2 = -1
    if ((farpoint1==minsumpoint or farpoint1==maxsumpoint) and (farpoint2==minsumpoint or farpoint2==maxsumpoint))or ((farpoint1==mindiffpoint or farpoint1==maxdiffpoint) and (farpoint2==mindiffpoint or farpoint2==maxdiffpoint)):
        x = (farpoint1[0]+farpoint2[0])/2
        y = (farpoint1[1]+farpoint2[1])/2
    else:
        if farpoint1==minsumpoint or farpoint1==maxdiffpoint:
            intercept1 = farpoint1[1] - (m1*farpoint1[0]) + minmaxdist
        else:
            intercept1 = farpoint1[1] - (m1*farpoint1[0]) - minmaxdist
        if farpoint2==minsumpoint or farpoint2==maxdiffpoint:
            intercept2 = farpoint2[1] - (m2*farpoint2[0]) + minmaxdist
        else:
            intercept2 = farpoint2[1] - (m2*farpoint2[0]) - minmaxdist
        '''print("Intercept 1:",intercept1, m1, farpoint1)
        print("Intercept 2:",intercept2, m2, farpoint2)'''
        x = (intercept2-intercept1)/(m1-m2)
        y = (m1*x) + intercept1
    return [x, y]