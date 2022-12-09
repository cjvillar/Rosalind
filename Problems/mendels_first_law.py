"""
https://rosalind.info/problems/iprb/

 NOTE: Looked up solutions below. revisite and think of other solutions.

Figure 2. The probability of any outcome (leaf) in a probability tree diagram is given by the product of probabilities from the start of the tree to the outcome. For example, the probability that X is blue and Y is blue is equal to (2/5)(1/4), or 1/10.
Probability is the mathematical study of randomly occurring phenomena. We will model such a phenomenon with a random variable, which is simply a variable that can take a number of different distinct outcomes depending on the result of an underlying random process.

For example, say that we have a bag containing 3 red balls and 2 blue balls. If we let X represent the random variable corresponding to the color of a drawn ball, then the probability of each of the two outcomes is given by Pr(X=red)=35 and Pr(X=blue)=25.

Random variables can be combined to yield new random variables. Returning to the ball example, let Y model the color of a second ball drawn from the bag (without replacing the first ball). The probability of Y being red depends on whether the first ball was red or blue. To represent all outcomes of X and Y, we therefore use a probability tree diagram. This branching diagram represents all possible individual probabilities for X and Y, with outcomes at the endpoints ("leaves") of the tree. The probability of any outcome is given by the product of probabilities along the path from the beginning of the tree; see Figure 2 for an illustrative example.

An event is simply a collection of outcomes. Because outcomes are distinct, the probability of an event can be written as the sum of the probabilities of its constituent outcomes. For our colored ball example, let A be the event "Y is blue." Pr(A) is equal to the sum of the probabilities of two different outcomes: Pr(X=blue and Y=blue)+Pr(X=red and Y=blue), or 310+110=25 (see Figure 2 above).

Given: Three positive integers k, m, and n, representing a population containing k+m+n organisms: k individuals are homozygous dominant for a factor, m are heterozygous, and n are homozygous recessive.

Return: The probability that two randomly selected mating organisms will produce an individual possessing a dominant allele (and thus displaying the dominant phenotype). Assume that any two organisms can mate.

Sample Dataset
2 2 2
Sample Output
0.78333

Some good resources:
http://saradoesbioinformatics.blogspot.com/2016/06/mendels-first-law.html
https://thagomizer.com/blog/2014/11/19/approaching-rosalind-problems.html
https://noobest.medium.com/rosalind-mendels-first-law-192864d81c45


"""
# https://docs.python.org/3/library/itertools.html
from itertools import product

# https://stackoverflow.com/questions/25119106/rosalind-mendels-first-law-iprb
def mendels_first_law(k, m, n):
    """k = AA  homozygous dominant , m = Aa heterozygous ,n = aa homozygous recessive"""

    pop = (["AA"] * k) + (["Aa"] * m) + (["aa"] * n)

    tot_children = []
    for p1 in pop:
        # remove selected parent from pop.
        chosen = pop[:]
        chosen.remove(p1)
        for p2 in chosen:
            # this will get all possible children from both parents punnett square.
            children = product(p1, p2)
            tot_children.extend(["".join(c) for c in children])

    dominants = filter(lambda c: "A" in c, tot_children)
    return len(list(dominants)) / len(tot_children)
   


# strategy to calc recessive alleles
# https://thagomizer.com/blog/2014/11/19/approaching-rosalind-problems.html
def calc_rec(k, m, n):
    dom, rec, het = k, m, n
    tot = dom + het + rec
    rr = (rec / tot) * ((rec - 1) / (tot - 1))
    hh = (het / tot) * ((het - 1) / (tot - 1))
    hr = (het / tot) * (rec / (tot - 1)) + (rec / tot) * (het / (tot - 1))
    rec_tot = rr + hh * 1 / 4 + hr * 1 / 2
    return 1 - rec_tot


# driver code
# k,m,n = 2,2,2
# ans --> 0.7833333
k, m, n = 29, 17, 19
# ans --> 0.8237
# print(calc_rec(k, m, n))
print(mendels_first_law(k, m, n))
