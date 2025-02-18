## Descrição do Problema

A otimização da produção industrial é um desafio complexo que envolve a alocação eficiente de recursos escassos para maximizar os resultados desejados. Neste problema, uma fábrica manufatura dois produtos, **Produto A** e **Produto B**, utilizando dois recursos limitados: **horas de máquina** e **mão de obra**. A fábrica precisa encontrar a melhor estratégia de produção considerando múltiplos objetivos.

Os objetivos do problema são:
1. **Objetivo Primário**: **Maximizar o lucro total** derivado da produção dos dois produtos.
2. **Objetivo Secundário**: **Minimizar a produção total** para evitar superprodução desnecessária e otimizar a utilização dos recursos.

Para resolver este problema, é utilizada a ferramenta **Z3 Optimize**, que permite a formulação e solução de problemas de otimização multiobjetivo. As restrições do problema incluem:
- **Horas de máquina disponíveis**: Cada unidade do Produto A requer 3 horas e cada unidade do Produto B requer 2 horas, com um total de 100 horas disponíveis.
- **Mão de obra disponível**: Cada unidade do Produto A consome 2 horas de trabalho, enquanto cada unidade do Produto B consome 4 horas, com um total de 80 horas disponíveis.
- **Não negatividade**: Nenhuma quantidade produzida pode ser negativa.

O modelo de otimização define um conjunto de restrições e objetivos e busca uma solução ótima que atenda às limitações impostas. Além disso, o sistema implementa uma **verificação de solução ótima**, garantindo que não exista um conjunto alternativo de decisões que leve a um lucro maior.

Este problema serve como uma demonstração prática do poder do **Z3 Optimize** na resolução de problemas de otimização multiobjetivo, mostrando como ele pode ser utilizado para encontrar soluções eficientes e validar sua qualidade em um contexto industrial realista.