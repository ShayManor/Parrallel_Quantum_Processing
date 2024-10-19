import random
import math
import csv

# Define the number of problems for each category
NUM_TRIG_SUB = 15
NUM_SERIES = 20
NUM_SEQUENCES = 20


# Helper functions for generating random integers and choices
def rand_int(a, b):
    return random.randint(a, b)


def rand_choice(lst):
    return random.choice(lst)


# Problem Templates and Generators

def generate_trig_sub_problem():
    substitution_type = rand_choice(['a2_minus_x2', 'a2_plus_x2', 'x2_minus_a2'])
    a = rand_int(2, 15)
    polynomial_degree = rand_choice(['linear', 'quadratic'])

    if substitution_type == 'a2_minus_x2':
        if polynomial_degree == 'linear':
            coeff = rand_int(1, 5)
            problem = f"Evaluate the integral ∫(3x + {coeff})√({a}² - x²) dx."
            solution = r"""**Step 1:** Use the substitution \( x = 7 \sin\theta \), so \( dx = 7 \cos\theta d\theta \).
**Step 2:** Substitute into the integral:
\[
\int (3x + 4)\sqrt{7^2 - x^2} \, dx = \int (3 \cdot 7 \sin\theta + 4) \times 7 \cos\theta \times 7 \cos\theta \, d\theta
\]
\[
= \int (21 \sin\theta + 4) \times 49 \cos^2\theta \, d\theta
\]
\[
= 1029 \int \sin\theta \cos^2\theta \, d\theta + 196 \int \cos^2\theta \, d\theta
\]
**Step 3:** Integrate each term separately using trigonometric identities.
**Step 4:** Apply the identity \( \cos^2\theta = \frac{1 + \cos 2\theta}{2} \) to simplify the integrals.
**Step 5:** After integration, substitute back using \( \theta = \arcsin(x/7) \) to express the answer in terms of \( x \).
**Final Answer:** [Expression in terms of \( x \)] + C"""
        else:  # quadratic
            problem = f"Evaluate the integral ∫x²√({a}² - x²) dx."
            solution = r"""**Step 1:** Use the substitution \( x = 7 \sin\theta \), so \( dx = 7 \cos\theta d\theta \).
**Step 2:** Substitute into the integral:
\[
\int x^2 \sqrt{7^2 - x^2} \, dx = \int (7^2 \sin^2\theta) \times 7 \cos\theta \times 7 \cos\theta \, d\theta
\]
\[
= 343 \int \sin^2\theta \cos^2\theta \, d\theta
\]
**Step 3:** Use the identity \( \sin^2\theta \cos^2\theta = \frac{1 - \cos 4\theta}{8} \) to simplify the integrand.
**Step 4:** Integrate the simplified expression.
**Step 5:** Substitute back using \( \theta = \arcsin(x/7) \) to express the answer in terms of \( x \).
**Final Answer:** [Expression in terms of \( x \)] + C"""
    elif substitution_type == 'a2_plus_x2':
        if polynomial_degree == 'linear':
            coeff = rand_int(1, 5)
            problem = f"Evaluate the integral ∫(5x - {coeff})√({a}² + x²) dx."
            solution = r"""**Step 1:** Use the substitution \( x = 7 \tan\theta \), so \( dx = 7 \sec^2\theta d\theta \).
**Step 2:** Substitute into the integral:
\[
\int (5x - 3)\sqrt{7^2 + x^2} \, dx = \int (5 \cdot 7 \tan\theta - 3) \times 7 \sec\theta \times 7 \sec^2\theta \, d\theta
\]
\[
= \int (35 \tan\theta - 3) \times 343 \sec^3\theta \, d\theta
\]
\[
= 12005 \int \tan\theta \sec^3\theta \, d\theta - 1029 \int \sec^3\theta \, d\theta
\]
**Step 3:** Integrate each term separately using trigonometric identities and integration techniques for \( \sec^3\theta \).
**Step 4:** After integration, substitute back using \( \theta = \arctan(x/7) \) to express the answer in terms of \( x \).
**Final Answer:** [Expression in terms of \( x \)] + C"""
        else:  # quadratic
            problem = f"Evaluate the integral ∫x³√({a}² + x²) dx."
            solution = r"""**Step 1:** Use the substitution \( u = x^2 + 7^2 \), so \( du = 2x \, dx \).
**Step 2:** Express \( x^3 \) as \( x^2 \times x = (u - 7^2) \times x \), and solve for \( x \) in terms of \( u \).
**Step 3:** Substitute into the integral and simplify:
\[
\int x^3 \sqrt{u} \times \frac{du}{2x} = \frac{1}{2} \int (u - 49) \sqrt{u} \, du
\]
\[
= \frac{1}{2} \int u^{3/2} - 49u^{1/2} \, du
\]
**Step 4:** Integrate using power rules:
\[
= \frac{1}{2} \left( \frac{2}{5} u^{5/2} - 49 \cdot \frac{2}{3} u^{3/2} \right) + C
\]
\[
= \frac{1}{5} u^{5/2} - \frac{49}{3} u^{3/2} + C
\]
**Step 5:** Substitute back using \( u = x^2 + 49 \) to express the answer in terms of \( x \).
**Final Answer:** \( \frac{1}{5} (x^2 + 49)^{5/2} - \frac{49}{3} (x^2 + 49)^{3/2} + C \)"""
    else:  # x2_minus_a2
        if polynomial_degree == 'linear':
            coeff = rand_int(1, 5)
            problem = f"Evaluate the integral ∫(2x + {coeff})√(x² - {a}²) dx."
            solution = r"""**Step 1:** Use the substitution \( x = 7 \sec\theta \), so \( dx = 7 \sec\theta \tan\theta d\theta \).
**Step 2:** Substitute into the integral:
\[
\int (2x + 3)\sqrt{x^2 - 7^2} \, dx = \int (2 \cdot 7 \sec\theta + 3) \times 7 \tan\theta \times 7 \sec\theta \tan\theta \, d\theta
\]
\[
= \int (14 \sec\theta + 3) \times 343 \sec\theta \tan^2\theta \, d\theta
\]
\[
= 4802 \int \sec^2\theta \tan^2\theta \, d\theta + 1029 \int \sec\theta \tan^2\theta \, d\theta
\]
**Step 3:** Expand and integrate each term separately using trigonometric identities.
**Step 4:** After integration, substitute back using \( \theta = \arcsec(x/7) \) to express the answer in terms of \( x \).
**Final Answer:** [Expression in terms of \( x \)] + C"""
        else:  # quadratic
            problem = f"Evaluate the integral ∫x²√(x² - {a}²) dx."
            solution = r"""**Step 1:** Use the substitution \( u = x^2 - 7^2 \), so \( du = 2x \, dx \).
**Step 2:** Express \( x^2 \) as \( u + 7^2 \).
**Step 3:** Substitute into the integral:
\[
\int x^2 \sqrt{u} \times \frac{du}{2x} = \frac{1}{2} \int (u + 49) \sqrt{u} \, du
\]
\[
= \frac{1}{2} \int u^{3/2} + 49u^{1/2} \, du
\]
**Step 4:** Integrate using power rules:
\[
= \frac{1}{2} \left( \frac{2}{5} u^{5/2} + 49 \cdot \frac{2}{3} u^{3/2} \right) + C
\]
\[
= \frac{1}{5} u^{5/2} + \frac{49}{3} u^{3/2} + C
\]
**Step 5:** Substitute back using \( u = x^2 - 49 \) to express the answer in terms of \( x \).
**Final Answer:** \( \frac{1}{5} (x^2 - 49)^{5/2} + \frac{49}{3} (x^2 - 49)^{3/2} + C \)"""
    return (problem, solution)


def generate_series_problem():
    test_type = rand_choice(['limit_comparison', 'ratio', 'root', 'integral', 'alternating', 'absolute', 'cond_test'])
    if test_type == 'limit_comparison':
        # Generate a comparison test problem with non-trivial comparison
        p = rand_int(1, 4)
        a = rand_int(2, 10)
        problem = f"Use the Limit Comparison Test to determine the convergence of the series ∑(n^{{{p}}} + {a}^n) / (3n^{{{p}}} + {a}^{{n+1}})."
        solution = r"""**Step 1:** Choose a comparison series \( b_n = \frac{a^n}{3a^{n+1}} = \frac{1}{3a} \).
**Step 2:** Compute the limit \( L = \lim_{n \to \infty} \frac{a_n}{b_n} = \lim_{n \to \infty} \frac{n^p + a^n}{3n^p + a^{n+1}} \times 3a \).
**Step 3:** Simplify the limit:
\[
L = \lim_{n \to \infty} \frac{n^p/a^n + 1}{3n^p/a^n + a} = \frac{0 + 1}{0 + a} = \frac{1}{a}
\]
**Step 4:** Since \( L = \frac{1}{a} > 0 \) and \( \sum b_n = \sum \frac{1}{3a} \) is a convergent geometric series (because \( |\frac{1}{3a}| < 1 \) for \( a \geq 2 \)), by the Limit Comparison Test, the original series converges."""
    elif test_type == 'ratio':
        # Ratio test with more complex terms
        a = rand_int(2, 5)
        b = rand_int(1, 4)
        problem = f"Use the Ratio Test to determine the convergence of the series ∑(n^{{{b}}} * {a}^n) / (n! * 2^n)."
        solution = r"""**Step 1:** Apply the Ratio Test: 
\[
L = \lim_{n \to \infty} \left| \frac{a_{n+1}}{a_n} \right| = \lim_{n \to \infty} \left| \frac{(n+1)^b \cdot a^{n+1}}{(n+1)! \cdot 2^{n+1}} \times \frac{n! \cdot 2^n}{n^b \cdot a^n} \right|
\]
**Step 2:** Simplify the expression:
\[
L = \lim_{n \to \infty} \left| \frac{(n+1)^b \cdot a}{(n+1) \cdot 2} \right| = \lim_{n \to \infty} \frac{(n+1)^{b-1} \cdot a}{2}
\]
**Step 3:** Analyze based on the value of \( b \):
- If \( b < 1 \): \( L = 0 < 1 \) ⇒ Series converges absolutely.
- If \( b = 1 \): \( L = \frac{a}{2} \).
  - If \( \frac{a}{2} < 1 \) (i.e., \( a < 2 \)), Series converges absolutely.
  - If \( \frac{a}{2} > 1 \) (i.e., \( a > 2 \)), Series diverges.
- If \( b > 1 \): \( L = \infty > 1 \) ⇒ Series diverges.
**Conclusion:** Determine convergence based on the specific value of \( b \) and \( a \)."""
    elif test_type == 'root':
        # Root test with nested exponents
        a = rand_int(2, 4)
        problem = f"Use the Root Test to determine the convergence of the series ∑(n^3 / {a}^n)."
        solution = r"""**Step 1:** Apply the Root Test: 
\[
L = \lim_{n \to \infty} \sqrt[n]{|a_n|} = \lim_{n \to \infty} \sqrt[n]{\frac{n^3}{a^n}} = \lim_{n \to \infty} \frac{n^{3/n}}{a} = \frac{1}{a}
\]
**Step 2:** Compare \( L \) to 1:
- If \( L < 1 \) ⇒ Series converges absolutely.
- If \( L > 1 \) ⇒ Series diverges.
- If \( L = 1 \) ⇒ Test is inconclusive.
**Conclusion:** Since \( L = \frac{1}{a} < 1 \) (because \( a > 1 \)), the series converges absolutely."""
    elif test_type == 'integral':
        # Integral test with a more complex function
        problem = f"Use the Integral Test to determine the convergence of the series ∑1 / (n (\\log n)^2) for \( n \\geq 2 \)."
        solution = r"""**Step 1:** Consider the function \( f(x) = \frac{1}{x (\log x)^2} \), which is positive, continuous, and decreasing for \( x \geq 2 \).
**Step 2:** Evaluate the integral \( \int_{2}^{\infty} \frac{1}{x (\log x)^2} \, dx \).
**Step 3:** Use substitution \( u = \log x \), so \( du = \frac{1}{x} dx \).
**Step 4:** The integral becomes:
\[
\int_{\log 2}^{\infty} \frac{1}{u^2} \, du = \left[ -\frac{1}{u} \right]_{\log 2}^{\infty} = 0 - \left( -\frac{1}{\log 2} \right) = \frac{1}{\log 2}
\]
**Step 5:** Since the integral converges, by the Integral Test, the series \( \sum \frac{1}{n (\log n)^2} \) converges."""
    elif test_type == 'alternating':
        # Alternating series with non-trivial terms
        problem = f"Determine the convergence of the series ∑(-1)^n \\frac{{n}}{{n^2 + 1}}."
        solution = r"""**Step 1:** Apply the Alternating Series Test (Leibniz's Test).
**Step 2:** Let \( b_n = \frac{n}{n^2 + 1} \).
**Step 3:** Check if \( b_n \) is decreasing:
\[
b_{n+1} = \frac{n+1}{(n+1)^2 + 1} = \frac{n+1}{n^2 + 2n + 2} < \frac{n}{n^2 + 1} = b_n \quad \text{for all } n \geq 1
\]
**Step 4:** Compute \( \lim_{n \to \infty} b_n = \lim_{n \to \infty} \frac{n}{n^2 + 1} = 0 \).
**Conclusion:** Since \( b_n \) is decreasing and \( \lim_{n \to \infty} b_n = 0 \), the series \( \sum (-1)^n \frac{n}{n^2 + 1} \) converges conditionally."""
    elif test_type == 'absolute':
        # Absolute convergence involving multiple tests
        problem = f"Determine whether the series ∑(-1)^n \\frac{{n!}}{{2^n n^3}} converges absolutely, conditionally, or diverges."
        solution = r"""**Step 1:** Check for absolute convergence by considering the series \( \sum \frac{n!}{2^n n^3} \).
**Step 2:** Apply the Ratio Test to the absolute series:
\[
L = \lim_{n \to \infty} \left| \frac{a_{n+1}}{a_n} \right| = \lim_{n \to \infty} \frac{(n+1)!}{2^{n+1} (n+1)^3} \times \frac{2^n n^3}{n!} = \lim_{n \to \infty} \frac{(n+1) \cdot n^3}{2 (n+1)^3} = \lim_{n \to \infty} \frac{n^3}{2n^3 + 6n^2 + 6n + 2} = \frac{1}{2} < 1
\]
**Step 3:** Since \( L < 1 \), the series \( \sum \frac{n!}{2^n n^3} \) converges absolutely.
**Step 4:** Therefore, the original alternating series \( \sum (-1)^n \frac{n!}{2^n n^3} \) converges absolutely."""
    elif test_type == 'cond_test':
        # Conditional convergence with more complex alternating series
        problem = f"Determine whether the series ∑(-1)^n \\frac{{\\log n}}{{n}} converges absolutely, conditionally, or diverges."
        solution = r"""**Step 1:** Check for absolute convergence by considering the series \( \sum \frac{\log n}{n} \).
**Step 2:** Apply the Integral Test to \( \sum \frac{\log n}{n} \):
\[
\int_{2}^{\infty} \frac{\log x}{x} \, dx = \int_{\log 2}^{\infty} \frac{u}{x} \, du \quad \text{(with substitution } u = \log x, du = \frac{1}{x} dx)
\]
However, the correct substitution leads to:
\[
\int_{2}^{\infty} \frac{\log x}{x} \, dx = \int_{\log 2}^{\infty} u \, du = \infty
\]
**Step 3:** Since the integral diverges, the series \( \sum \frac{\log n}{n} \) diverges. Thus, the series does not converge absolutely.
**Step 4:** Next, apply the Alternating Series Test to the original series \( \sum (-1)^n \frac{\log n}{n} \).
**Step 5:** Let \( b_n = \frac{\log n}{n} \).
**Step 6:** Check if \( b_n \) is decreasing for \( n \geq 3 \) (which it is) and \( \lim_{n \to \infty} b_n = 0 \).
\[
\lim_{n \to \infty} \frac{\log n}{n} = 0
\]
**Conclusion:** Since \( b_n \) is decreasing and \( \lim_{n \to \infty} b_n = 0 \), the series \( \sum (-1)^n \frac{\log n}{n} \) converges conditionally."""
    return (problem, solution)


def generate_sequence_problem():
    seq_type = rand_choice(
        ['nested', 'factorial', 'exponential', 'oscillatory', 'logarithmic', 'rational', 'recursive', 'limit_def'])
    if seq_type == 'nested':
        # Nested limits
        problem = r"Find the limit of the sequence \( a_n = \frac{(n^2 + 3n)^{1/n}}{2 + \frac{n}{n + 1}} \)."
        solution = r"""**Step 1:** Simplify the expression:
\[
a_n = \frac{(n^2 + 3n)^{1/n}}{2 + \frac{n}{n + 1}} = \frac{(n^2 (1 + \frac{3}{n}))^{1/n}}{2 + \frac{n}{n + 1}} = \frac{n^{2/n} (1 + \frac{3}{n})^{1/n}}{3}
\]
**Step 2:** Evaluate each part separately:
- \( \lim_{n \to \infty} n^{2/n} = 1 \) (since \( \lim_{n \to \infty} n^{1/n} = 1 \)).
- \( \lim_{n \to \infty} \left(1 + \frac{3}{n}\right)^{1/n} = 1 \) (since \( \left(1 + \frac{k}{n}\right)^n \) approaches \( e^k \), but here the exponent is \( \frac{1}{n} \)).
- \( \lim_{n \to \infty} \left(2 + \frac{n}{n + 1}\right) = 3 \).
**Step 3:** Combine the limits:
\[
\lim_{n \to \infty} a_n = \frac{1 \times 1}{3} = \frac{1}{3}
\]
**Final Answer:** \( \lim_{n \to \infty} a_n = \frac{1}{3} \)."""
    elif seq_type == 'factorial':
        # Factorial involving limits
        problem = r"Find the limit of the sequence \( a_n = \left( \frac{n!}{n^n} \right)^{1/n} \)."
        solution = r"""**Step 1:** Apply Stirling's approximation for \( n! \):
\[
n! \approx n^n e^{-n} \sqrt{2\pi n}
\]
**Step 2:** Substitute into \( a_n \):
\[
a_n = \left( \frac{n!}{n^n} \right)^{1/n} \approx \left( \frac{n^n e^{-n} \sqrt{2\pi n}}{n^n} \right)^{1/n} = \left( e^{-n} \sqrt{2\pi n} \right)^{1/n} = e^{-1} (2\pi n)^{1/(2n)}
\]
**Step 3:** Evaluate the limit:
\[
\lim_{n \to \infty} e^{-1} (2\pi n)^{1/(2n)} = e^{-1} \times 1 = \frac{1}{e}
\]
**Final Answer:** \( \lim_{n \to \infty} a_n = \frac{1}{e} \)."""
    elif seq_type == 'exponential':
        # Exponential involving limits
        a = rand_int(2, 5)
        problem = f"Find the limit of the sequence \( a_n = \\frac{{n^{{{a}}}}}{{e^n}} \)."
        solution = r"""**Step 1:** Compare the growth rates of the numerator and the denominator.
**Step 2:** Exponential growth (\( e^n \)) outpaces polynomial growth (\( n^a \)) for any fixed \( a \).
**Step 3:** Therefore:
\[
\lim_{n \to \infty} \frac{n^a}{e^n} = 0
\]
**Final Answer:** \( \lim_{n \to \infty} a_n = 0 \)."""
    elif seq_type == 'oscillatory':
        # Oscillatory sequences
        problem = r"Determine whether the sequence \( a_n = \frac{\sin n}{n^{1/2}} \) converges or diverges."
        solution = r"""**Step 1:** Observe that \( |\sin n| \leq 1 \) for all \( n \).
**Step 2:** Therefore:
\[
|a_n| = \left| \frac{\sin n}{n^{1/2}} \right| \leq \frac{1}{n^{1/2}}
\]
**Step 3:** Compute the limit of the bounding sequence:
\[
\lim_{n \to \infty} \frac{1}{n^{1/2}} = 0
\]
**Step 4:** By the Squeeze Theorem:
\[
\lim_{n \to \infty} \frac{\sin n}{n^{1/2}} = 0
\]
**Conclusion:** The sequence \( a_n \) converges to 0."""
    elif seq_type == 'logarithmic':
        # Logarithmic sequences
        problem = r"Find the limit of the sequence \( a_n = \frac{(\log n)^2}{n} \)."
        solution = r"""**Step 1:** Recognize that both the numerator and denominator tend to infinity as \( n \to \infty \).
**Step 2:** Apply L'Hospital's Rule since the limit is of the form \( \frac{\infty}{\infty} \).
**Step 3:** Differentiate the numerator and the denominator:
\[
\frac{d}{dn} [(\log n)^2] = 2 \log n \cdot \frac{1}{n} = \frac{2 \log n}{n}
\]
\[
\frac{d}{dn} [n] = 1
\]
**Step 4:** Apply L'Hospital's Rule:
\[
\lim_{n \to \infty} \frac{(\log n)^2}{n} = \lim_{n \to \infty} \frac{2 \log n}{n} = 0
\]
**Final Answer:** \( \lim_{n \to \infty} a_n = 0 \)."""
    elif seq_type == 'rational':
        # Complex rational sequences
        problem = r"Find the limit of the sequence \( a_n = \frac{3n^3 + 2n^2}{5n^3 - n + 4} \)."
        solution = r"""**Step 1:** Divide the numerator and the denominator by \( n^3 \), the highest power of \( n \) in the expression:
\[
a_n = \frac{3 + \frac{2}{n}}{5 - \frac{1}{n^2} + \frac{4}{n^3}}
\]
**Step 2:** Evaluate the limit as \( n \to \infty \):
\[
\lim_{n \to \infty} a_n = \frac{3 + 0}{5 - 0 + 0} = \frac{3}{5}
\]
**Final Answer:** \( \lim_{n \to \infty} a_n = \frac{3}{5} \)."""
    elif seq_type == 'recursive':
        # Recursive sequences
        problem = r"Given the recursive sequence \( a_{n+1} = \frac{a_n + \frac{3}{a_n}}{2} \) with \( a_1 = 2 \), find \( \lim_{n \to \infty} a_n \)."
        solution = r"""**Step 1:** Assume the sequence converges to \( L \), so \( \lim_{n \to \infty} a_n = L \).
**Step 2:** Take the limit on both sides of the recursive formula:
\[
L = \frac{L + \frac{3}{L}}{2}
\]
**Step 3:** Multiply both sides by \( 2L \) to eliminate the fraction:
\[
2L^2 = L^2 + 3
\]
**Step 4:** Simplify the equation:
\[
L^2 = 3
\]
**Step 5:** Solve for \( L \):
\[
L = \sqrt{3} \quad (\text{since } a_n > 0 \text{ for all } n)
\]
**Final Answer:** \( \lim_{n \to \infty} a_n = \sqrt{3} \)."""
    elif seq_type == 'limit_def':
        # Sequences defined by limits
        problem = r"Find \( \lim_{n \to \infty} \left(1 + \frac{2}{n}\right)^{3n} \)."
        solution = r"""**Step 1:** Recognize the limit as a form of the exponential function:
\[
\lim_{n \to \infty} \left(1 + \frac{2}{n}\right)^{3n} = \left[ \lim_{n \to \infty} \left(1 + \frac{2}{n}\right)^n \right]^3
\]
**Step 2:** Recall that \( \lim_{n \to \infty} \left(1 + \frac{k}{n}\right)^n = e^k \). Here, \( k = 2 \):
\[
\lim_{n \to \infty} \left(1 + \frac{2}{n}\right)^n = e^2
\]
**Step 3:** Apply the limit:
\[
\left( e^2 \right)^3 = e^6
\]
**Final Answer:** \( \lim_{n \to \infty} a_n = e^6 \)."""
    return (problem, solution)


# Generate Problems
problems = []

# Trigonometric Substitution Problems
for _ in range(NUM_TRIG_SUB):
    prob, sol = generate_trig_sub_problem()
    problems.append((prob, sol))

# Series Convergence and Divergence Problems
for _ in range(NUM_SERIES):
    prob, sol = generate_series_problem()
    problems.append((prob, sol))

# Sequence Convergence and Divergence Problems
for _ in range(NUM_SEQUENCES):
    prob, sol = generate_sequence_problem()
    problems.append((prob, sol))

# Export to CSV for Anki Import
with open('calculus2_challenging_problems.csv', 'w', newline='', encoding='utf-8') as csvfile:
    writer = csv.writer(csvfile, delimiter='\t')
    writer.writerow(['Front', 'Back'])  # Header
    for front, back in problems:
        writer.writerow([front, back])

print("Challenging problem generation complete! 'calculus2_challenging_problems.csv' has been created.")
