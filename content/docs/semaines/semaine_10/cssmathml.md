---
title: "Laboratoire CSS/MathML"
weight: 50
---

# Laboratoire CSS/MathML

Vous pouvez utiliser CSS pour modifier l'apparence du contenu MathML dans votre
navigateur.
  Je vous invite à éditer le code MathML dans la boîte suivante pour observer le résultat.

## Code MathML

<textarea id="mathmlCode" style="width:100%; height:400px">&lt;math xmlns="http://www.w3.org/1998/Math/MathML" display="block"&gt;
    &lt;mrow&gt;
        &lt;mi style="color: red; font-style: italic;"&gt;x&lt;/mi&gt;
        &lt;mo style="color: purple;"&gt;=&lt;/mo&gt;
        &lt;mfrac&gt;
            &lt;mrow&gt;
                &lt;mn style="color: green;"&gt;−1&lt;/mn&gt;
                &lt;mo style="color: purple;"&gt;±&lt;/mo&gt;
                &lt;msqrt&gt;
                    &lt;mn style="color: green;"&gt;1&lt;/mn&gt;
                    &lt;mo style="color: purple;"&gt;−&lt;/mo&gt;
                    &lt;mn style="color: green;"&gt;4&lt;/mn&gt;
                &lt;/msqrt&gt;
            &lt;/mrow&gt;
            &lt;mn style="color: green;"&gt;2&lt;/mn&gt;
        &lt;/mfrac&gt;
    &lt;/mrow&gt;
&lt;/math&gt;
</textarea>

<div class="render-container">
 <h2>
  Rendu MathML
 </h2>

 <div id="mathmlRender">
  <math display="block" xmlns="http://www.w3.org/1998/Math/MathML">
        <mrow>
            <mi style="color: red; font-style: italic;">x</mi>
            <mo style="color: purple;">=</mo>
            <mfrac>
                <mrow>
                    <mn style="color: green;">−1</mn>
                    <mo style="color: purple;">±</mo>
                    <msqrt>
                        <mn style="color: green;">1</mn>
                        <mo style="color: purple;">−</mo>
                        <mn style="color: green;">4</mn>
                    </msqrt>
                </mrow>
                <mn style="color: green;">2</mn>
            </mfrac>
        </mrow>
  </math>
 </div>
</div>
<script>
 const textarea = document.getElementById('mathmlCode');
    const renderDiv = document.getElementById('mathmlRender');
    textarea.addEventListener('input', () => {
        try {
            renderDiv.innerHTML = textarea.value;
        } catch (error) {
            console.error('Erreur MathML:', error);
        }
    });
</script>
