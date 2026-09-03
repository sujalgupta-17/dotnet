# Bayes' Theorem - Medical Test Example

# Given probabilities
P_disease = 0.01
P_positive_given_disease = 0.99
P_positive_given_no_disease = 0.05

# Probability of NOT having the disease
P_no_disease = 1 - P_disease

# True positive probability
P_disease_and_positive = (
    P_positive_given_disease * P_disease
)

# False positive probability
P_no_disease_and_positive = (
    P_positive_given_no_disease * P_no_disease
)

# Total probability of a positive test
P_positive = (
    P_disease_and_positive
    + P_no_disease_and_positive
)

# Bayes' theorem
P_disease_given_positive = (
    P_positive_given_disease * P_disease
) / P_positive

# Display results
print("P(Disease) =", P_disease)
print("P(Positive | Disease) =", P_positive_given_disease)
print("P(Disease ∩ Positive) =", P_disease_and_positive)
print("P(Not Disease ∩ Positive) =", P_no_disease_and_positive)
print("P(Positive) =", P_positive)
print(
    "P(Disease | Positive) =",
    P_disease_given_positive
)
print(
    "Probability of actually having the disease:",
    round(P_disease_given_positive * 100, 2),
    "%"
)
