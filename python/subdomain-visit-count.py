# question can be found at leetcode.com/problems/subdomain-visit-count/
from Typing import List


class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        counting_dict = {}
        for domain in cpdomains:
            domain_pair = domain.split(" ")
            ctr = domain_pair[0]
            for subdomain in domain_pair[1]:
                sub = ".".join(
                    domain_pair[1][domain_pair[1].index(domain_pair[1]):])
                if sub in counting_dict:
                    counting_dict[sub] += ctr
                else:
                    counting_dict.update({sub: ctr})
        return [counting_dict.get(pair) + " " + pair for pair in counting_dict]
