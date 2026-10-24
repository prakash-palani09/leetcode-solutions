class Solution(object):
    def countDaysTogether(self, arriveAlice, leaveAlice, arriveBob, leaveBob):
        """
        :type arriveAlice: str
        :type leaveAlice: str
        :type arriveBob: str
        :type leaveBob: str
        :rtype: int
        """
        hsh = {1:31,2:28,3:31,4:30,5:31,6:30,7:31,8:31,9:30,10:31,11:30,12:31}
        aam = int(arriveAlice[:2])
        aad = int(arriveAlice[3:])
        alm = int(leaveAlice[:2])
        ald = int(leaveAlice[3:])
        bam = int(arriveBob[:2])
        bad = int(arriveBob[3:])
        blm = int(leaveBob[:2])
        bld = int(leaveBob[3:])
        aaD = 0
        alD = 0
        baD = 0
        blD = 0
        for i in range(1,aam):
            aaD += hsh[i]
        aaD += aad
        for i in range(1,bam):
            baD += hsh[i]
        baD += bad
        for i in range(1,alm):
            alD += hsh[i]
        alD += ald
        for i in range(1,blm):
            blD += hsh[i]
        blD += bld

        AD = max(aaD,baD)
        DD = min(alD,blD)

        ans = DD-AD+1

        return ans if ans>0 else 0
        