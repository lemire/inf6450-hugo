---
title: "Variables et paramètres"
weight: 30
---
<h1>
 Variables et paramètres
</h1>
<h2>
 Les variables
</h2>
<p>
 Il est possible, en XSLT, de définir des variables, mais elles sont
    « immutables » (« dont la valeur ne peut être
    modifiée »).
    On peut se demander, à juste titre, si les mots variables et immutables vont
    bien
    ensemble, mais c'est ainsi que les inventeurs du XSLT se sont exprimés.
    Pour définir une variable nommée « test », on utilise
    l'élément
    « &lt;xsl:variable name="test" select="xxx" /&gt; ». La variable
    contiendra alors le résultat de l'expression XPath contenue dans l'attribut
    « select ». On fait référence à la variable dans d'autres
    expressions XPath en utilisant le symbole « $ ». Ainsi, si la variable se
    nomme test, l'expression $test aura comme valeur la valeur de la variable.
    L'exemple suivant peut être utilisé pour remplacer tous les éléments
    « produit » par le noeud de texte « bozo ».
</p>
<pre><span style="color:#004a43; ">&lt;?</span><span style="color:#800000; font-weight:bold; ">xml</span><span style="color:#004a43; "> </span><span style="color:#074726; ">version</span><span style="color:#808030; ">=</span><span style="color:#0000e6; ">"</span><span style="color:#7d0045; ">1.0</span><span style="color:#0000e6; ">"</span><span style="color:#004a43; ">
    </span><span style="color:#074726; ">encoding</span><span style="color:#808030; ">=</span><span style="color:#0000e6; ">"</span><span style="color:#0000e6; ">ISO-8859-1</span><span style="color:#0000e6; ">"</span><span style="color:#004a43; ">?&gt;</span>
    <span style="color:#a65700; ">&lt;</span><span style="color:#666616; ">xsl</span><span style="color:#800080; ">:</span><span style="color:#5f5035; ">stylesheet</span> <span style="color:#274796; ">version</span><span style="color:#808030; ">=</span><span style="color:#0000e6; ">"</span><span style="color:#0000e6; ">1.0</span><span style="color:#0000e6; ">"</span>
    <span style="color:#666616; ">xmlns</span><span style="color:#800080; ">:</span><span style="color:#074726; ">xsl</span><span style="color:#808030; ">=</span><span style="color:#0000e6; ">"</span><span style="color:#666616; ">http</span><span style="color:#800080; ">:</span><span style="color:#800000; font-weight:bold; ">//</span><span style="color:#5555dd; ">www.w3.org</span><span style="color:#40015a; ">/1999/XSL/Transform</span><span style="color:#0000e6; ">"</span><span style="color:#a65700; ">&gt;</span>
    <span style="color:#a65700; ">&lt;</span><span style="color:#666616; ">xsl</span><span style="color:#800080; ">:</span><span style="color:#5f5035; ">variable</span> <span style="color:#274796; ">name</span><span style="color:#808030; ">=</span><span style="color:#0000e6; ">"</span><span style="color:#0000e6; ">test</span><span style="color:#0000e6; ">"</span> <span style="color:#274796; ">select</span><span style="color:#808030; ">=</span><span style="color:#0000e6; ">"</span><span style="color:#0000e6; ">'bozo'</span><span style="color:#0000e6; ">"</span> <span style="color:#a65700; ">/&gt;</span>
    <span style="color:#a65700; ">&lt;</span><span style="color:#666616; ">xsl</span><span style="color:#800080; ">:</span><span style="color:#5f5035; ">template</span> <span style="color:#274796; ">match</span><span style="color:#808030; ">=</span><span style="color:#0000e6; ">"</span><span style="color:#0000e6; ">produit</span><span style="color:#0000e6; ">"</span><span style="color:#a65700; ">&gt;</span>
    <span style="color:#a65700; ">&lt;</span><span style="color:#666616; ">xsl</span><span style="color:#800080; ">:</span><span style="color:#5f5035; ">value-of</span> <span style="color:#274796; ">select</span><span style="color:#808030; ">=</span><span style="color:#0000e6; ">"</span><span style="color:#0000e6; ">$test</span><span style="color:#0000e6; ">"</span> <span style="color:#a65700; ">/&gt;</span>
    <span style="color:#a65700; ">&lt;/</span><span style="color:#666616; ">xsl</span><span style="color:#800080; ">:</span><span style="color:#5f5035; ">template</span><span style="color:#a65700; ">&gt;</span>
    <span style="color:#a65700; ">&lt;/</span><span style="color:#666616; ">xsl</span><span style="color:#800080; ">:</span><span style="color:#5f5035; ">stylesheet</span><span style="color:#a65700; ">&gt;</span>
</pre>
<p>
 On peut aussi définir la valeur de la variable en omettant l'attribut
    « select » et en ajoutant du contenu à l'élément
    « xsl:variable ». Dans l'exemple suivant, on propose de remplacer
    tous les éléments «produit» par le contenu de la variable (qui est ici «
    &lt;produit&gt;x&lt;/produit&gt; »):
</p>
<pre><span style="color:#a65700; ">&lt;</span><span style="color:#666616; ">xsl</span><span style="color:#800080; ">:</span><span style="color:#5f5035; ">stylesheet</span> <span style="color:#274796; ">version</span><span style="color:#808030; ">=</span><span style="color:#0000e6; ">"</span><span style="color:#0000e6; ">1.0</span><span style="color:#0000e6; ">"</span>
    <span style="color:#666616; ">xmlns</span><span style="color:#800080; ">:</span><span style="color:#074726; ">xsl</span><span style="color:#808030; ">=</span><span style="color:#0000e6; ">"</span><span style="color:#666616; ">http</span><span style="color:#800080; ">:</span><span style="color:#800000; font-weight:bold; ">//</span><span style="color:#5555dd; ">www.w3.org</span><span style="color:#40015a; ">/1999/XSL/Transform</span><span style="color:#0000e6; ">"</span><span style="color:#a65700; ">&gt;</span>
    <span style="color:#a65700; ">&lt;</span><span style="color:#666616; ">xsl</span><span style="color:#800080; ">:</span><span style="color:#5f5035; ">variable</span> <span style="color:#274796; ">name</span><span style="color:#808030; ">=</span><span style="color:#0000e6; ">"</span><span style="color:#0000e6; ">test</span><span style="color:#0000e6; ">"</span> <span style="color:#a65700; ">&gt;</span>
    <span style="color:#a65700; ">&lt;</span><span style="color:#5f5035; ">produit</span><span style="color:#a65700; ">&gt;</span>x<span style="color:#a65700; ">&lt;/</span><span style="color:#5f5035; ">produit</span><span style="color:#a65700; ">&gt;</span>
    <span style="color:#a65700; ">&lt;/</span><span style="color:#666616; ">xsl</span><span style="color:#800080; ">:</span><span style="color:#5f5035; ">variable</span><span style="color:#a65700; ">&gt;</span>
    <span style="color:#a65700; ">&lt;</span><span style="color:#666616; ">xsl</span><span style="color:#800080; ">:</span><span style="color:#5f5035; ">template</span> <span style="color:#274796; ">match</span><span style="color:#808030; ">=</span><span style="color:#0000e6; ">"</span><span style="color:#0000e6; ">produit</span><span style="color:#0000e6; ">"</span><span style="color:#a65700; ">&gt;</span>
    <span style="color:#a65700; ">&lt;</span><span style="color:#666616; ">xsl</span><span style="color:#800080; ">:</span><span style="color:#5f5035; ">copy-of</span> <span style="color:#274796; ">select</span><span style="color:#808030; ">=</span><span style="color:#0000e6; ">"</span><span style="color:#0000e6; ">$test</span><span style="color:#0000e6; ">"</span> <span style="color:#a65700; ">/&gt;</span>
    <span style="color:#a65700; ">&lt;/</span><span style="color:#666616; ">xsl</span><span style="color:#800080; ">:</span><span style="color:#5f5035; ">template</span><span style="color:#a65700; ">&gt;</span>
    <span style="color:#a65700; ">&lt;/</span><span style="color:#666616; ">xsl</span><span style="color:#800080; ">:</span><span style="color:#5f5035; ">stylesheet</span><span style="color:#a65700; ">&gt;</span>
</pre>
<p>
 On peut déclarer la variable localement au sein d'un élément template.
    Pouvez-vous trouver ce que fait la transformation suivante?
</p>
<pre><span style="color:#004a43; ">&lt;?</span><span style="color:#800000; font-weight:bold; ">xml</span><span style="color:#004a43; "> </span><span style="color:#074726; ">version</span><span style="color:#808030; ">=</span><span style="color:#0000e6; ">"</span><span style="color:#7d0045; ">1.0</span><span style="color:#0000e6; ">"</span><span style="color:#004a43; ">
    </span><span style="color:#074726; ">encoding</span><span style="color:#808030; ">=</span><span style="color:#0000e6; ">"</span><span style="color:#0000e6; ">ISO-8859-1</span><span style="color:#0000e6; ">"</span><span style="color:#004a43; ">?&gt;</span>
    <span style="color:#a65700; ">&lt;</span><span style="color:#666616; ">xsl</span><span style="color:#800080; ">:</span><span style="color:#5f5035; ">stylesheet</span> <span style="color:#274796; ">version</span><span style="color:#808030; ">=</span><span style="color:#0000e6; ">"</span><span style="color:#0000e6; ">1.0</span><span style="color:#0000e6; ">"</span>
    <span style="color:#666616; ">xmlns</span><span style="color:#800080; ">:</span><span style="color:#074726; ">xsl</span><span style="color:#808030; ">=</span><span style="color:#0000e6; ">"</span><span style="color:#666616; ">http</span><span style="color:#800080; ">:</span><span style="color:#800000; font-weight:bold; ">//</span><span style="color:#5555dd; ">www.w3.org</span><span style="color:#40015a; ">/1999/XSL/Transform</span><span style="color:#0000e6; ">"</span><span style="color:#a65700; ">&gt;</span>
    <span style="color:#a65700; ">&lt;</span><span style="color:#666616; ">xsl</span><span style="color:#800080; ">:</span><span style="color:#5f5035; ">template</span> <span style="color:#274796; ">match</span><span style="color:#808030; ">=</span><span style="color:#0000e6; ">"</span><span style="color:#0000e6; ">/</span><span style="color:#0000e6; ">"</span><span style="color:#a65700; ">&gt;</span>
    <span style="color:#a65700; ">&lt;</span><span style="color:#666616; ">xsl</span><span style="color:#800080; ">:</span><span style="color:#5f5035; ">variable</span> <span style="color:#274796; ">name</span><span style="color:#808030; ">=</span><span style="color:#0000e6; ">"</span><span style="color:#0000e6; ">test</span><span style="color:#0000e6; ">"</span> <span style="color:#a65700; ">&gt;</span>
    <span style="color:#a65700; ">&lt;</span><span style="color:#5f5035; ">produit</span><span style="color:#a65700; ">&gt;</span>x<span style="color:#a65700; ">&lt;/</span><span style="color:#5f5035; ">produit</span><span style="color:#a65700; ">&gt;</span>
    <span style="color:#a65700; ">&lt;/</span><span style="color:#666616; ">xsl</span><span style="color:#800080; ">:</span><span style="color:#5f5035; ">variable</span><span style="color:#a65700; ">&gt;</span>
    <span style="color:#a65700; ">&lt;</span><span style="color:#666616; ">xsl</span><span style="color:#800080; ">:</span><span style="color:#5f5035; ">copy-of</span> <span style="color:#274796; ">select</span><span style="color:#808030; ">=</span><span style="color:#0000e6; ">"</span><span style="color:#0000e6; ">$test</span><span style="color:#0000e6; ">"</span> <span style="color:#a65700; ">/&gt;</span>
    <span style="color:#a65700; ">&lt;/</span><span style="color:#666616; ">xsl</span><span style="color:#800080; ">:</span><span style="color:#5f5035; ">template</span><span style="color:#a65700; ">&gt;</span>
    <span style="color:#a65700; ">&lt;/</span><span style="color:#666616; ">xsl</span><span style="color:#800080; ">:</span><span style="color:#5f5035; ">stylesheet</span><span style="color:#a65700; ">&gt;</span>
</pre>
<h3 class="recall">
 Les paramètres
</h3>
<p>
 Un fichier XSLT peut être utilisé comme un programme dans la mesure où on
    peut
    lui passer des paramètres. Rappelons qu'on appelle un fichier XSLT
    « xslt.xml » à partir d'un fichier XML qu'on veut transformer de
    cette manière :
</p>
<pre><span style="color:#004a43; ">&lt;?</span><span style="color:#800000; font-weight:bold; ">xml</span><span style="color:#004a43; "> </span><span style="color:#074726; ">version</span><span style="color:#808030; ">=</span><span style="color:#0000e6; ">"</span><span style="color:#7d0045; ">1.0</span><span style="color:#0000e6; ">"</span><span style="color:#004a43; ">
    </span><span style="color:#074726; ">encoding</span><span style="color:#808030; ">=</span><span style="color:#0000e6; ">"</span><span style="color:#0000e6; ">ISO-8859-1</span><span style="color:#0000e6; ">"</span><span style="color:#004a43; ">
    </span><span style="color:#004a43; ">?&gt;</span>
    <span style="color:#004a43; ">&lt;?</span><span style="color:#800000; font-weight:bold; ">xml-stylesheet</span><span style="color:#004a43; "> </span><span style="color:#074726; ">href</span><span style="color:#808030; ">=</span><span style="color:#0000e6; ">"</span><span style="color:#40015a; ">xslt.xml</span><span style="color:#0000e6; ">"</span><span style="color:#004a43; "> </span>
    <span style="color:#004a43; ">  </span><span style="color:#074726; ">type</span><span style="color:#808030; ">=</span><span style="color:#0000e6; ">"</span><span style="color:#0000e6; ">application/xml</span><span style="color:#0000e6; ">"</span><span style="color:#004a43; ">?&gt;</span>
    <span style="color:#a65700; ">&lt;</span><span style="color:#5f5035; ">facture</span><span style="color:#a65700; ">&gt;</span>
    <span style="color:#a65700; ">&lt;</span><span style="color:#5f5035; ">montant</span><span style="color:#a65700; ">&gt;</span>10.10<span style="color:#a65700; ">&lt;/</span><span style="color:#5f5035; ">montant</span><span style="color:#a65700; ">&gt;</span>
    <span style="color:#a65700; ">&lt;</span><span style="color:#5f5035; ">personne</span><span style="color:#a65700; ">&gt;</span>Jean Rochond<span style="color:#a65700; ">&lt;/</span><span style="color:#5f5035; ">personne</span><span style="color:#a65700; ">&gt;</span>
    <span style="color:#a65700; ">&lt;</span><span style="color:#5f5035; ">raison</span><span style="color:#a65700; ">&gt;</span>Achat d'ordinateur<span style="color:#a65700; ">&lt;/</span><span style="color:#5f5035; ">raison</span><span style="color:#a65700; ">&gt;</span>
    <span style="color:#a65700; ">&lt;/</span><span style="color:#5f5035; ">facture</span><span style="color:#a65700; ">&gt;</span>
</pre>
<p>
 On peut enrichir cet appel avec les instructions « xslt-param »
    comme dans
    cet exemple.
</p>
<pre><span style="color:#004a43; ">&lt;?</span><span style="color:#800000; font-weight:bold; ">xml</span><span style="color:#004a43; "> </span><span style="color:#074726; ">version</span><span style="color:#808030; ">=</span><span style="color:#0000e6; ">"</span><span style="color:#7d0045; ">1.0</span><span style="color:#0000e6; ">"</span><span style="color:#004a43; ">
    </span><span style="color:#074726; ">encoding</span><span style="color:#808030; ">=</span><span style="color:#0000e6; ">"</span><span style="color:#0000e6; ">ISO-8859-1</span><span style="color:#0000e6; ">"</span><span style="color:#004a43; ">
    </span><span style="color:#004a43; ">?&gt;</span>
    <span style="color:#004a43; ">&lt;?</span><span style="color:#004a43; ">xslt-param</span><span style="color:#004a43; ">
        name="couleur" value="blue"</span><span style="color:#004a43; ">?&gt;</span>
    <span style="color:#004a43; ">&lt;?</span><span style="color:#004a43; ">xslt-param</span><span style="color:#004a43; ">
        name="taille" value="2"</span><span style="color:#004a43; ">?&gt;</span>
    <span style="color:#004a43; ">&lt;?</span><span style="color:#800000; font-weight:bold; ">xml-stylesheet</span><span style="color:#004a43; "> </span><span style="color:#074726; ">href</span><span style="color:#808030; ">=</span><span style="color:#0000e6; ">"</span><span style="color:#40015a; ">xslt.xml</span><span style="color:#0000e6; ">"</span><span style="color:#004a43; "> </span>
    <span style="color:#004a43; ">  </span><span style="color:#074726; ">type</span><span style="color:#808030; ">=</span><span style="color:#0000e6; ">"</span><span style="color:#0000e6; ">application/xml</span><span style="color:#0000e6; ">"</span><span style="color:#004a43; ">?&gt;</span>
    <span style="color:#a65700; ">&lt;</span><span style="color:#5f5035; ">facture</span><span style="color:#a65700; ">&gt;</span>
    <span style="color:#a65700; ">&lt;</span><span style="color:#5f5035; ">montant</span><span style="color:#a65700; ">&gt;</span>10.10<span style="color:#a65700; ">&lt;/</span><span style="color:#5f5035; ">montant</span><span style="color:#a65700; ">&gt;</span>
    <span style="color:#a65700; ">&lt;</span><span style="color:#5f5035; ">personne</span><span style="color:#a65700; ">&gt;</span>Jean Rochond<span style="color:#a65700; ">&lt;/</span><span style="color:#5f5035; ">personne</span><span style="color:#a65700; ">&gt;</span>
    <span style="color:#a65700; ">&lt;</span><span style="color:#5f5035; ">raison</span><span style="color:#a65700; ">&gt;</span>Achat d'ordinateur<span style="color:#a65700; ">&lt;/</span><span style="color:#5f5035; ">raison</span><span style="color:#a65700; ">&gt;</span>
    <span style="color:#a65700; ">&lt;/</span><span style="color:#5f5035; ">facture</span><span style="color:#a65700; ">&gt;</span>
</pre>
<p>
 Selon votre processeur XSLT, il peut y avoir d'autres façons de passer des
    paramètres
    à une feuille de style XSLT.
</p>
<p>
 On reçoit alors les paramètres avec un élément « xsl:param ».
    L'attribut
    « select » est utilisé pour spécifier une valeur par défaut.
</p>
<pre><span style="color:#004a43; ">&lt;?</span><span style="color:#800000; font-weight:bold; ">xml</span><span style="color:#004a43; "> </span><span style="color:#074726; ">version</span><span style="color:#808030; ">=</span><span style="color:#0000e6; ">"</span><span style="color:#7d0045; ">1.0</span><span style="color:#0000e6; ">"</span><span style="color:#004a43; ">
    </span><span style="color:#074726; ">encoding</span><span style="color:#808030; ">=</span><span style="color:#0000e6; ">"</span><span style="color:#0000e6; ">ISO-8859-1</span><span style="color:#0000e6; ">"</span><span style="color:#004a43; ">?&gt;</span>
    <span style="color:#a65700; ">&lt;</span><span style="color:#666616; ">xsl</span><span style="color:#800080; ">:</span><span style="color:#5f5035; ">stylesheet</span> <span style="color:#274796; ">version</span><span style="color:#808030; ">=</span><span style="color:#0000e6; ">"</span><span style="color:#0000e6; ">1.0</span><span style="color:#0000e6; ">"</span>
    <span style="color:#666616; ">xmlns</span><span style="color:#800080; ">:</span><span style="color:#074726; ">xsl</span><span style="color:#808030; ">=</span><span style="color:#0000e6; ">"</span><span style="color:#666616; ">http</span><span style="color:#800080; ">:</span><span style="color:#800000; font-weight:bold; ">//</span><span style="color:#5555dd; ">www.w3.org</span><span style="color:#40015a; ">/1999/XSL/Transform</span><span style="color:#0000e6; ">"</span><span style="color:#a65700; ">&gt;</span>
    <span style="color:#a65700; ">&lt;</span><span style="color:#666616; ">xsl</span><span style="color:#800080; ">:</span><span style="color:#5f5035; ">param</span> <span style="color:#274796; ">name</span><span style="color:#808030; ">=</span><span style="color:#0000e6; ">"</span><span style="color:#0000e6; ">couleur</span><span style="color:#0000e6; ">"</span> <span style="color:#274796; ">select</span><span style="color:#808030; ">=</span><span style="color:#0000e6; ">"</span><span style="color:#0000e6; ">red</span><span style="color:#0000e6; ">"</span>
    <span style="color:#a65700; ">/&gt;</span>
    <span style="color:#a65700; ">&lt;</span><span style="color:#666616; ">xsl</span><span style="color:#800080; ">:</span><span style="color:#5f5035; ">param</span> <span style="color:#274796; ">name</span><span style="color:#808030; ">=</span><span style="color:#0000e6; ">"</span><span style="color:#0000e6; ">taille</span><span style="color:#0000e6; ">"</span> <span style="color:#274796; ">select</span><span style="color:#808030; ">=</span><span style="color:#0000e6; ">"</span><span style="color:#0000e6; ">1</span><span style="color:#0000e6; ">"</span>
    <span style="color:#a65700; ">/&gt;</span>
    <span style="color:#a65700; ">&lt;</span><span style="color:#666616; ">xsl</span><span style="color:#800080; ">:</span><span style="color:#5f5035; ">template</span> <span style="color:#274796; ">match</span><span style="color:#808030; ">=</span><span style="color:#0000e6; ">"</span><span style="color:#0000e6; ">facture</span><span style="color:#0000e6; ">"</span><span style="color:#a65700; ">&gt;</span>
    <span style="color:#a65700; ">&lt;</span><span style="color:#5f5035; ">html</span><span style="color:#a65700; ">&gt;</span>
    <span style="color:#a65700; ">&lt;</span><span style="color:#5f5035; ">head</span><span style="color:#a65700; ">&gt;</span>
    <span style="color:#a65700; ">&lt;</span><span style="color:#5f5035; ">title</span><span style="color:#a65700; ">&gt;</span>Facture de <span style="color:#a65700; ">&lt;</span><span style="color:#666616; ">xsl</span><span style="color:#800080; ">:</span><span style="color:#5f5035; ">value-of</span> <span style="color:#274796; ">select</span><span style="color:#808030; ">=</span><span style="color:#0000e6; ">"</span><span style="color:#0000e6; ">personne</span><span style="color:#0000e6; ">"</span> <span style="color:#a65700; ">/&gt;</span><span style="color:#a65700; ">&lt;/</span><span style="color:#5f5035; ">title</span><span style="color:#a65700; ">&gt;</span>
    <span style="color:#a65700; ">&lt;/</span><span style="color:#5f5035; ">head</span><span style="color:#a65700; ">&gt;</span>
    <span style="color:#a65700; ">&lt;</span><span style="color:#5f5035; ">body</span><span style="color:#a65700; ">&gt;</span>
    <span style="color:#a65700; ">&lt;</span><span style="color:#5f5035; ">p</span> <span style="color:#274796; ">style</span><span style="color:#808030; ">=</span><span style="color:#0000e6; ">"</span><span style="color:#0000e6; ">color:{$couleur};
        font-size:{$taille}em</span><span style="color:#0000e6; ">"</span><span style="color:#a65700; ">&gt;</span>Ceci est
    une facture pour <span style="color:#a65700; ">&lt;</span><span style="color:#666616; ">xsl</span><span style="color:#800080; ">:</span><span style="color:#5f5035; ">value-of</span> <span style="color:#274796; ">select</span><span style="color:#808030; ">=</span><span style="color:#0000e6; ">"</span><span style="color:#0000e6; ">personne</span><span style="color:#0000e6; ">"</span> <span style="color:#a65700; ">/&gt;</span>
    de <span style="color:#a65700; ">&lt;</span><span style="color:#666616; ">xsl</span><span style="color:#800080; ">:</span><span style="color:#5f5035; ">value-of</span> <span style="color:#274796; ">select</span><span style="color:#808030; ">=</span><span style="color:#0000e6; ">"</span><span style="color:#0000e6; ">montant</span><span style="color:#0000e6; ">"</span> <span style="color:#a65700; ">/&gt;</span>$ pour:
    <span style="color:#a65700; ">&lt;</span><span style="color:#666616; ">xsl</span><span style="color:#800080; ">:</span><span style="color:#5f5035; ">value-of</span> <span style="color:#274796; ">select</span><span style="color:#808030; ">=</span><span style="color:#0000e6; ">"</span><span style="color:#0000e6; ">raison</span><span style="color:#0000e6; ">"</span> <span style="color:#a65700; ">/&gt;</span>.<span style="color:#a65700; ">&lt;/</span><span style="color:#5f5035; ">p</span><span style="color:#a65700; ">&gt;</span>
    <span style="color:#a65700; ">&lt;/</span><span style="color:#5f5035; ">body</span><span style="color:#a65700; ">&gt;</span>
    <span style="color:#a65700; ">&lt;/</span><span style="color:#5f5035; ">html</span><span style="color:#a65700; ">&gt;</span>
    <span style="color:#a65700; ">&lt;/</span><span style="color:#666616; ">xsl</span><span style="color:#800080; ">:</span><span style="color:#5f5035; ">template</span><span style="color:#a65700; ">&gt;</span>
    <span style="color:#a65700; ">&lt;/</span><span style="color:#666616; ">xsl</span><span style="color:#800080; ">:</span><span style="color:#5f5035; ">stylesheet</span><span style="color:#a65700; ">&gt;</span>
</pre>
<p>
 On peut aussi passer des paramètres aux éléments « xsl:template »
    avec
    les éléments « xsl:call-template » comme dans cet exemple qui est
    une
    façon équivalente, mais plus compliquée, de formater notre document XML de
    type
    « facture » .
</p>
<pre><span style="color:#004a43; ">&lt;?</span><span style="color:#800000; font-weight:bold; ">xml</span><span style="color:#004a43; "> </span><span style="color:#074726; ">version</span><span style="color:#808030; ">=</span><span style="color:#0000e6; ">"</span><span style="color:#7d0045; ">1.0</span><span style="color:#0000e6; ">"</span><span style="color:#004a43; ">
    </span><span style="color:#074726; ">encoding</span><span style="color:#808030; ">=</span><span style="color:#0000e6; ">"</span><span style="color:#0000e6; ">ISO-8859-1</span><span style="color:#0000e6; ">"</span><span style="color:#004a43; ">?&gt;</span>
    <span style="color:#a65700; ">&lt;</span><span style="color:#666616; ">xsl</span><span style="color:#800080; ">:</span><span style="color:#5f5035; ">stylesheet</span> <span style="color:#274796; ">version</span><span style="color:#808030; ">=</span><span style="color:#0000e6; ">"</span><span style="color:#0000e6; ">1.0</span><span style="color:#0000e6; ">"</span>
    <span style="color:#666616; ">xmlns</span><span style="color:#800080; ">:</span><span style="color:#074726; ">xsl</span><span style="color:#808030; ">=</span><span style="color:#0000e6; ">"</span><span style="color:#666616; ">http</span><span style="color:#800080; ">:</span><span style="color:#800000; font-weight:bold; ">//</span><span style="color:#5555dd; ">www.w3.org</span><span style="color:#40015a; ">/1999/XSL/Transform</span><span style="color:#0000e6; ">"</span><span style="color:#a65700; ">&gt;</span>
    <span style="color:#a65700; ">&lt;</span><span style="color:#666616; ">xsl</span><span style="color:#800080; ">:</span><span style="color:#5f5035; ">template</span> <span style="color:#274796; ">match</span><span style="color:#808030; ">=</span><span style="color:#0000e6; ">"</span><span style="color:#0000e6; ">facture</span><span style="color:#0000e6; ">"</span><span style="color:#a65700; ">&gt;</span>
    <span style="color:#a65700; ">&lt;</span><span style="color:#666616; ">xsl</span><span style="color:#800080; ">:</span><span style="color:#5f5035; ">call-template</span> <span style="color:#274796; ">name</span><span style="color:#808030; ">=</span><span style="color:#0000e6; ">"</span><span style="color:#0000e6; ">monmotif</span><span style="color:#0000e6; ">"</span><span style="color:#a65700; ">&gt;</span>
    <span style="color:#a65700; ">&lt;</span><span style="color:#666616; ">xsl</span><span style="color:#800080; ">:</span><span style="color:#5f5035; ">with-param</span> <span style="color:#274796; ">name</span><span style="color:#808030; ">=</span><span style="color:#0000e6; ">"</span><span style="color:#0000e6; ">contenu</span><span style="color:#0000e6; ">"</span> <span style="color:#274796; ">select</span><span style="color:#808030; ">=</span><span style="color:#0000e6; ">"</span><span style="color:#0000e6; ">.</span><span style="color:#0000e6; ">"</span><span style="color:#a65700; ">/&gt;</span>
    <span style="color:#a65700; ">&lt;/</span><span style="color:#666616; ">xsl</span><span style="color:#800080; ">:</span><span style="color:#5f5035; ">call-template</span><span style="color:#a65700; ">&gt;</span>
    <span style="color:#a65700; ">&lt;/</span><span style="color:#666616; ">xsl</span><span style="color:#800080; ">:</span><span style="color:#5f5035; ">template</span><span style="color:#a65700; ">&gt;</span>
    <span style="color:#a65700; ">&lt;</span><span style="color:#666616; ">xsl</span><span style="color:#800080; ">:</span><span style="color:#5f5035; ">template</span> <span style="color:#274796; ">name</span><span style="color:#808030; ">=</span><span style="color:#0000e6; ">"</span><span style="color:#0000e6; ">monmotif</span><span style="color:#0000e6; ">"</span><span style="color:#a65700; ">&gt;</span>
    <span style="color:#a65700; ">&lt;</span><span style="color:#666616; ">xsl</span><span style="color:#800080; ">:</span><span style="color:#5f5035; ">param</span> <span style="color:#274796; ">name</span><span style="color:#808030; ">=</span><span style="color:#0000e6; ">"</span><span style="color:#0000e6; ">contenu</span><span style="color:#0000e6; ">"</span> <span style="color:#a65700; ">/&gt;</span>
    <span style="color:#a65700; ">&lt;</span><span style="color:#5f5035; ">html</span><span style="color:#a65700; ">&gt;</span>
    <span style="color:#a65700; ">&lt;</span><span style="color:#5f5035; ">head</span><span style="color:#a65700; ">&gt;</span>
    <span style="color:#a65700; ">&lt;</span><span style="color:#5f5035; ">title</span><span style="color:#a65700; ">&gt;</span>Facture de <span style="color:#a65700; ">&lt;</span><span style="color:#666616; ">xsl</span><span style="color:#800080; ">:</span><span style="color:#5f5035; ">value-of</span> <span style="color:#274796; ">select</span><span style="color:#808030; ">=</span><span style="color:#0000e6; ">"</span><span style="color:#0000e6; ">$contenu/personne</span><span style="color:#0000e6; ">"</span> <span style="color:#a65700; ">/&gt;</span><span style="color:#a65700; ">&lt;/</span><span style="color:#5f5035; ">title</span><span style="color:#a65700; ">&gt;</span>
    <span style="color:#a65700; ">&lt;/</span><span style="color:#5f5035; ">head</span><span style="color:#a65700; ">&gt;</span>
    <span style="color:#a65700; ">&lt;</span><span style="color:#5f5035; ">body</span><span style="color:#a65700; ">&gt;</span>
    <span style="color:#a65700; ">&lt;</span><span style="color:#5f5035; ">p</span><span style="color:#a65700; ">&gt;</span>Ceci est
    une facture pour <span style="color:#a65700; ">&lt;</span><span style="color:#666616; ">xsl</span><span style="color:#800080; ">:</span><span style="color:#5f5035; ">value-of</span> <span style="color:#274796; ">select</span><span style="color:#808030; ">=</span><span style="color:#0000e6; ">"</span><span style="color:#0000e6; ">$contenu/personne</span><span style="color:#0000e6; ">"</span> <span style="color:#a65700; ">/&gt;</span>
    de <span style="color:#a65700; ">&lt;</span><span style="color:#666616; ">xsl</span><span style="color:#800080; ">:</span><span style="color:#5f5035; ">value-of</span> <span style="color:#274796; ">select</span><span style="color:#808030; ">=</span><span style="color:#0000e6; ">"</span><span style="color:#0000e6; ">$contenu/montant</span><span style="color:#0000e6; ">"</span> <span style="color:#a65700; ">/&gt;</span>$ pour:
    <span style="color:#a65700; ">&lt;</span><span style="color:#666616; ">xsl</span><span style="color:#800080; ">:</span><span style="color:#5f5035; ">value-of</span> <span style="color:#274796; ">select</span><span style="color:#808030; ">=</span><span style="color:#0000e6; ">"</span><span style="color:#0000e6; ">$contenu/raison</span><span style="color:#0000e6; ">"</span> <span style="color:#a65700; ">/&gt;</span>.<span style="color:#a65700; ">&lt;/</span><span style="color:#5f5035; ">p</span><span style="color:#a65700; ">&gt;</span>
    <span style="color:#a65700; ">&lt;/</span><span style="color:#5f5035; ">body</span><span style="color:#a65700; ">&gt;</span>
    <span style="color:#a65700; ">&lt;/</span><span style="color:#5f5035; ">html</span><span style="color:#a65700; ">&gt;</span>
    <span style="color:#a65700; ">&lt;/</span><span style="color:#666616; ">xsl</span><span style="color:#800080; ">:</span><span style="color:#5f5035; ">template</span><span style="color:#a65700; ">&gt;</span>
    <span style="color:#a65700; ">&lt;/</span><span style="color:#666616; ">xsl</span><span style="color:#800080; ">:</span><span style="color:#5f5035; ">stylesheet</span><span style="color:#a65700; ">&gt;</span>
</pre>
<p>
 On peut aussi charger des documents distants avec la fonction XSLT
    « document » , cette instruction donne une copie du
    document situé à l'adresse @href :
    &lt;xsl:copy-of select="document(@href)"/&gt;. (L'élément
    « xsl:copy-of » sert
    ici à faire une copies des nœuds contenus dans le document distant.) Elle
    est cependant sujette à des contraintes
    de sécurité lorsqu'on l'utilise dans un navigateur : il n'est pas
    permis de charger
    des documents provenant d'autres serveurs que le serveur d'origine.
</p>
