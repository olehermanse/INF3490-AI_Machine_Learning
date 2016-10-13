# Evolutionary Computing

## Evolutionary Algorithms
 * Stochastic (random)
 * Population based
 * Variation/Diversity is created by recombination/mutation
 * Quality/Fitness is increased by selection, but at the cost of diversity.

### EA flow
 * INITIALIZE a Population
 * EVALUATION of all individuals - determine their fitness
 * LOOP
    1. SELECTION of parents - Select which individuals to reproduce
    2. RECOMBINE pairs - pairs of parents reproduce to generate offspring
    3. MUTATION of offspring - creates diversity (exploration)
    4. EVALUATION of offspring - determine fitness of children
    5. SELECTION of survivors - based on fitness (similarity, etc.?)
 * TERMINATE after some condition is met based on fitness, time, generations etc.

### Subtle differences in selection
 * Survivor selection is *simple*: live or die
    * Typically deterministic - kill the worst individuals (10%, 25%, 50%)
 * Parent selection chooses which parents are paired together
    * Typically probabilistic - High quality individuals are more likely
    * Same parent can be selected for reproduction multiple times.

### Flavors of EAs
 * Genetic Algorithm(GA)
 * Evolution Strategies(ES)
 * Evolutionary Programming(EP)
 * Genetic Programming(GP)
 * Best approach to EA design:
    1. Pick a representation
    2. Pick operators that suit the problem and the representation

### Representations
 * Binary
 * Integer
 * Real valued
 * Permutations
 * Tree
