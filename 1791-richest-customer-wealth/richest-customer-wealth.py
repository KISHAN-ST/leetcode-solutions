class Solution(object):
    def maximumWealth(self, accounts):
        max_wealth=0
        for acc in accounts:
           max_wealth=max(max_wealth,sum(acc))
        return max_wealth

        """
        :type accounts: List[List[int]]
        :rtype: int
        """
        