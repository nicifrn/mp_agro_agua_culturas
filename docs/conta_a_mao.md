# Conta à mão — Radiação Extraterrestre ($R_a$) e $ET_0$ (Hargreaves-Samani)

- **Arquivo de origem:** `dados/clima_nova_cruz.csv` (linha 1)
- **Data escolhida:** `2016-01-01` *(substitua pela data da linha escolhida no seu CSV)*
- **Dia do ano ($J$):** `1`
- **Latitude ($\text{lat}$):** `-6.22°` *(substitua pelo valor exato de `dados/municipios.csv`)*
- **Temperaturas do dia:**
  - $T_{\text{máx}} = \text{[valor]}^\circ\text{C}$
  - $T_{\text{mín}} = \text{[valor]}^\circ\text{C}$
  - $T_{\text{média}} = \text{[valor]}^\circ\text{C}$

## Passo a passo na calculadora (FAO-56)

1. **Latitude em radianos ($\varphi$, Eq. 22):**
   $$\varphi = \frac{\pi}{180} \times (-6{,}22) = -0{,}1086\text{ rad}$$

2. **Distância relativa Terra–Sol ($d_r$, Eq. 23):**
   $$d_r = 1 + 0{,}033 \times \cos\left(\frac{2\pi}{365} \times 1\right) = 1{,}0330$$

3. **Declinação solar ($\delta$, Eq. 24):**
   $$\delta = 0{,}409 \times \sin\left(\frac{2\pi}{365} \times 1 - 1{,}39\right) = -0{,}4015\text{ rad}$$

4. **Ângulo horário do pôr do sol ($\omega_s$, Eq. 25):**
   $$\omega_s = \arccos\left(-\tan(-0{,}1086) \times \tan(-0{,}4015)\right) = 1{,}5243\text{ rad}$$

5. **Radiação extraterrestre ($R_a$, Eq. 21):**
   $$R_a = \frac{24 \times 60}{\pi} \times 0{,}0820 \times 1{,}0330 \times \left[1{,}5243 \sin(-0{,}1086)\sin(-0{,}4015) + \cos(-0{,}1086)\cos(-0{,}4015)\sin(1{,}5243)\right]$$
   $$R_a = 38{,}28\text{ MJ m}^{-2}\text{ dia}^{-1}$$

6. **Conversão para $\text{mm dia}^{-1}$ ($R_{a,\text{mm}}$, Eq. 20):**
   $$R_{a,\text{mm}} = 0{,}408 \times 38{,}28 = 15{,}62\text{ mm dia}^{-1}$$

7. **$ET_0$ por Hargreaves-Samani (Eq. 52):**
   $$ET_0 = 0{,}0023 \times (T_{\text{média}} + 17{,}8) \times \sqrt{T_{\text{máx}} - T_{\text{mín}}} \times 15{,}62 = \text{[resultado final]}\text{ mm dia}^{-1}$$