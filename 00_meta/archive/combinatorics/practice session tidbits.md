| Name                                                    | Counts                                                                                                              | Formula                                                                    |
| ------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------- |
| **Binomial coefficient**                                | Choose (k) objects from (n) distinct objects                                                                        | $(\displaystyle \binom{n}{k}=\frac{n!}{k!(n-k)!})$                         |
| **Multinomial coefficient** or **Multiset permutation** | Partition (n) sets possible for distinct objects into groups of specified sizes, or equivalently arrange a multiset | $(\displaystyle \binom{n}{n_1,n_2,\ldots,n_r}=\frac{n!}{n_1!\cdots n_r!})$ |
| **Multiset combination** (combination with repetition)  | Choose (k) items from (n) types, allowing repeats                                                                   | $(\displaystyle \binom{n+k-1}{k})$                                         |
|                                                         |                                                                                                                     |                                                                            |


We have two types of partitioning problems:

- **Partitioning distinct objects** → **Multinomial coefficient** -> multiset permutation
  - Partition distinct objects into labeled groups (sets) of given sizes. Think distrubting cards to disitnct people (labeled group)
  - $$\frac{n!}{n_1!\cdots n_r!}$$

- **Partitioning identical objects** → **Stars and Bars** (= integer compositions / positive integer solutions)
  - Partition identical objects into groups.
  - Equivalent to placing bars among identical stars, or solving
    $$x_1+\cdots+x_k=n,\qquad x_i>0.$$
  - $$\binom{n-1}{k-1}$$