# Conta à mão — Radiação Extraterrestre ($R_a$) e $ET_0$ (Hargreaves-Samani)

- **Arquivo de origem:** `dados/clima_nova_cruz.csv` (linha 1)
- **Município / Data escolhida:** Nova Cruz (`NOVA`) — `2015-01-01`
- **Dia do ano ($J$):** `1`
- **Latitude ($\text{lat}$):** `-6.23°`
- **Temperaturas do dia:**
  - $T_{\text{máx}} = 33{,}79^\circ\text{C}$
  - $T_{\text{mín}} = 21{,}47^\circ\text{C}$
  - $T_{\text{média}} = 26{,}88^\circ\text{C}$

## Passo a passo na calculadora (FAO-56)

1. **Latitude em radianos ($\varphi$, Eq. 22):**
   $$\varphi = \frac{\pi}{180} \times (-6{,}23) = -0{,}1087\text{ rad}$$

2. **Distância relativa Terra–Sol ($d_r$, Eq. 23):**
   $$d_r = 1 + 0{,}033 \times \cos\left(\frac{2\pi}{365} \times 1\right) = 1{,}0330$$

3. **Declinação solar ($\delta$, Eq. 24):**
   $$\delta = 0{,}409 \times \sin\left(\frac{2\pi}{365} \times 1 - 1{,}39\right) = -0{,}4015\text{ rad}$$

4. **Ângulo horário do pôr do sol ($\omega_s$, Eq. 25):**
   $$\omega_s = \arccos\left(-\tan(-0{,}1087) \times \tan(-0{,}4015)\right) = 1{,}5243\text{ rad}$$

5. **Radiação extraterrestre ($R_a$, Eq. 21):**
   $$R_a = \frac{24 \times 60}{\pi} \times 0{,}0820 \times 1{,}0330 \times \left[1{,}5243 \sin(-0{,}1087)\sin(-0{,}4015) + \cos(-0{,}1087)\cos(-0{,}4015)\sin(1{,}5243)\right]$$
   $$R_a = 38{,}27\text{ MJ m}^{-2}\text{ dia}^{-1}$$

6. **Conversão para $\text{mm dia}^{-1}$ ($R_{a,\text{mm}}$, Eq. 20):**
   $$R_{a,\text{mm}} = 0{,}408 \times 38{,}27 = 15{,}62\text{ mm dia}^{-1}$$

7. **$ET_0$ por Hargreaves-Samani (Eq. 52):**
   $$ET_0 = 0{,}0023 \times (26{,}88 + 17{,}8) \times \sqrt{33{,}79 - 21{,}47} \times 15{,}62$$
   $$ET_0 = 0{,}0023 \times 44{,}68 \times \sqrt{12{,}32} \times 15{,}62$$
   $$ET_0 = 0{,}0023 \times 44{,}68 \times 3{,}50998 \times 15{,}62 = 5{,}63\text{ mm dia}^{-1}$$