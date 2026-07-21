# Mathematical Model

## La Pekillada

### Asymmetric Flow & Geometric Absorption Theory

---

# 1. Introduction

This document defines the mathematical foundation of **La Pekillada** and the **Theory of Asymmetric Flow**.

The mathematical model describes a dynamic multi-variable system where asymmetric redistribution, geometric progression, and state transitions interact to generate system evolution.

The objective is to provide a formal representation of the theoretical principles and establish a framework for computational analysis and future experimentation.

---

# 2. General System Model

The system is represented as a discrete dynamic transformation:

\[
S(t+1)=F(S(t),E(t))
\]

Where:

- \(S(t)\) = Current system state.
- \(S(t+1)\) = Next system state.
- \(E(t)\) = Event or transition input.
- \(F\) = Transformation function.

The next state depends on the interaction between the previous state and the event that modifies the system.

---

# 3. La Pekillada State Model

The reference implementation operates with three dynamic variables.

The system state is represented as:

\[
S(t)=(A(t),B(t),C(t))
\]

Where:

- \(A(t)\) = Exposure level of variable A.
- \(B(t)\) = Exposure level of variable B.
- \(C(t)\) = Exposure level of variable C.

Initial condition:

\[
S(0)=(1,1,1)
\]

Each variable starts with minimum exposure.

---

# 4. Asymmetric Transition Function

The system evolves through discrete events.

When one variable receives a favorable event, that variable returns to minimum exposure.

The remaining variables increase according to a geometric progression.

## Event A

\[
A(t+1)=1
\]

\[
B(t+1)=2B(t)
\]

\[
C(t+1)=2C(t)
\]

---

## Event B

\[
A(t+1)=2A(t)
\]

\[
B(t+1)=1
\]

\[
C(t+1)=2C(t)
\]

---

## Event C

\[
A(t+1)=2A(t)
\]

\[
B(t+1)=2B(t)
\]

\[
C(t+1)=1
\]

---

# 5. Geometric Exposure Model

Each variable follows a geometric progression:

\[
X_n=X_0 \times 2^n
\]

Where:

- \(X_n\) = Current exposure value.
- \(X_0\) = Initial exposure.
- \(n\) = Number of consecutive unsuccessful transitions.

The progression follows:

\[
1,2,4,8,16,32,64,128,...
\]

---

# 6. Asymmetric Flow Model

The asymmetric flow represents the non-uniform redistribution of exposure between system variables.

The flow can be represented as:

\[
A=f(D,M,R)
\]

Where:

- \(D\) = Direction component.
- \(M\) = Magnitude of flow.
- \(R\) = Resistance or restriction factor.

Unlike symmetrical systems, the distribution of exposure is not uniform.

The system continuously transfers accumulated exposure between active and inactive variables.

---

# 7. Flow Imbalance Factor

The degree of asymmetry can be represented as:

\[
AF=\frac{|F_1-F_2|}{F_1+F_2}
\]

Where:

- \(AF\) = Asymmetric Flow Factor.
- \(F_1\) = Primary flow component.
- \(F_2\) = Secondary flow component.

Values closer to zero represent more balanced states.

Higher values represent stronger asymmetry.

---

# 8. Geometric Absorption Model

Geometric absorption describes how accumulated exposure is redistributed through future system transitions.

The absorption function is represented as:

\[
G(a)=I \times C \times R_g
\]

Where:

- \(I\) = Incoming flow intensity.
- \(C\) = Geometric compatibility.
- \(R_g\) = Geometric response factor.

The resulting value represents the absorption response of the structure.

---

# 9. Interaction Model

The interaction between asymmetric flow and geometric absorption is defined as:

\[
T=A \times G
\]

Where:

- \(T\) = Total transformation effect.
- \(A\) = Asymmetric flow component.
- \(G\) = Geometric absorption component.

The evolution of the system depends on the interaction between both elements.

---

# 10. Total System Exposure

The global exposure of the system is defined as:

\[
E_{total}=A+B+C
\]

This value represents the accumulated exposure distributed across all variables.

The model studies how this value changes through repeated transitions.

---

# 11. Distribution Model

The distribution of exposure among variables can be represented as:

\[
C_i=\frac{E_i}{E_{total}}
\]

Where:

- \(C_i\) = Distribution coefficient.
- \(E_i\) = Exposure of variable i.
- \(E_{total}\) = Total system exposure.

Each variable may contain a different proportion of the total exposure due to asymmetric conditions.

---

# 12. Stability Model

A dynamic system maintains controlled variation when:

\[
|S(t+1)-S(t)|<\epsilon
\]

Where:

- \(\epsilon\) = Maximum acceptable variation.

If variation exceeds this value, the system enters a different dynamic state.

---

# 13. Simulation Parameters

The reference simulation evaluates:

- Initial state values.
- Number of iterations.
- Transition sequence.
- Exposure progression.
- Maximum exposure limits.
- Resource constraints.
- Statistical variation.

Possible simulation scales:

- 100 iterations.
- 1,000 iterations.
- 100,000 iterations.

---

# 14. Model Limitations

Current mathematical limitations:

- The model is experimental.
- Parameters require further calibration.
- Complex systems may require higher-dimensional representations.
- Additional analytical validation is required.

The model does not claim deterministic prediction of external events.

---

# 15. Future Extensions

Future mathematical developments may include:

- Multi-dimensional flow equations.
- Non-linear transition models.
- Advanced statistical analysis.
- Predictive simulations.
- Optimization methods.
- Higher-dimensional variable spaces.

---

# 16. Conclusion

The Mathematical Model establishes the formal structure behind **La Pekillada** and the **Theory of Asymmetric Flow**.

It defines the system state, transition rules, geometric progression, asymmetric redistribution, and simulation framework.

This model provides the mathematical foundation for future implementations, computational experiments, and theoretical development.

---

© 2026 Jaypsmall
