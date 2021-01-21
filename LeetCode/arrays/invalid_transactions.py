# A transaction is possibly invalid if:

# the amount exceeds $1000, or;
# if it occurs within (and including) 60 minutes of another transaction with the same name in a different city.
# Each transaction string transactions[i] consists of comma separated values representing the name, time (in minutes), amount, and city of the transaction.

# Given a list of transactions, return a list of transactions that are possibly invalid.  You may return the answer in any order.

 

# Example 1:

# Input: transactions = ["alice,20,800,mtv","alice,50,100,beijing"]
# Output: ["alice,20,800,mtv","alice,50,100,beijing"]
# Explanation: The first transaction is invalid because the second transaction occurs within a difference of 60 minutes, have the same name and is in a different city. Similarly the second one is invalid too.
# Example 2:

# Input: transactions = ["alice,20,800,mtv","alice,50,1200,mtv"]
# Output: ["alice,50,1200,mtv"]
# Example 3:

# Input: transactions = ["alice,20,800,mtv","bob,50,1200,mtv"]
# Output: ["bob,50,1200,mtv"]

class Solution:
    def invalidTransactions(self, transactions: List[str]) -> List[str]:
        res = []
        transactions = [x.split(',') for x in transactions]
        
        for i in transactions:
            for j in transactions:
                if int(i[2]) > 1000:
                    res.append(i)
                    break
                elif i[0] == j[0]:
                    if abs(int(i[1]) - int(j[1])) <= 60:
                        if i[3] != j[3]:
                            res.append(i)
                            break
        
        return [",".join(x) for x in res]