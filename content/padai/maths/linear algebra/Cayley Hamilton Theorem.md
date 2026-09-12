## Statement
Every **square matrix** satisfies its own **characteristic equation**.

## Example

Given $A = \begin{bmatrix} 1 & 3 \\ 4 & 2 \end{bmatrix}$, find $A^5$.

    $$ \lambda^2 - 3\lambda - 10 = 0 $$
$$ A^2 - 3A - 10I = 0 \implies A^2 = 3A + 10I $$

$$ A^4 = (A^2)^2 = (3A + 10I)^2 $$
        $$ = 9A^2 + 60A + 100I $$
$$ = 9(3A + 10I) + 60A + 100I$$
$$= 27A + 90I + 60A + 100I $$
$$ A^4 = 87A + 190I $$
$$ A^5 = A^4 \cdot A = (87A + 190I)A $$$$ = 87A^2 + 190A $$
        $$ = 87(3A + 10I) + 190A $$$$ A^5 = 451A + 870I $$