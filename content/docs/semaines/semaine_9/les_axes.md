---
title: "Les axes"
weight: 60
---
<h1 class="">
 Les axes
</h1>
<h2 class="recall">
 Les axes
</h2>
<p>
 Par défaut, l'expression XPath « nom » désigne les éléments
    « nom » qui sont des enfants du nœud courant. On peut aussi
    écrire « child::nom ». De la même manière, « nom[2] » ou
    « child::nom[2] » désigne le second enfant du nœud courant.
    Il est possible
    de changer ce comportement en choisissant un axe différent.
</p>
<ul>
 <li>
  « child » : il s'agit de l'axe par défaut,
        « child::nom[3] » désigne le troisième élément
        « nom » enfant du nœud courant.
 </li>
 <li>
  « parent » : l'axe « parent » est pratiquement
        inutile, « parent::nom » désigne l'élément parent si celui-ci
        se nomme « nom ». En général, il est plus simple d'utiliser la
        syntaxe « .. » qui est équivalente à
        « parent::node() ».
 </li>
 <li>
  « attribute » : la syntaxe « attribute:: »
        n'est pas utilisée, on préfère la notation « @nom » qui
        signifie la même chose que « attribute::nom ».
 </li>
 <li>
  « ancestor » : la syntaxe « ancestor::nom »
        désigne les éléments de nom « nom » dans lesquels le nœud
        courant est contenu. On peut tester si le nœud courant est contenu dans
        un paragraphe avec la syntaxe &lt;xsl:if
        test="ancestor::paragraphe"&gt;...&lt;/xsl:if&gt;.
 </li>
 <li>
  « ancestor-or-self » : idem que l'axe ancestor exception
        faite que l'on inclut le nœud courant, on pourrait donc tester si nœud
        courant est contenu dans un paragraphe ou s'il est lui-même un
        paragraphe avec la syntaxe &lt;xsl:if
        test="ancestor-or-self::paragraphe"&gt;...&lt;/xsl:if&gt;.
 </li>
 <li>
  « preceding-sibling » : cet axe consulte en séquence les
        frères du nœud courant, c'est-à-dire les nœud ayant le même parent, qui
        apparaissent avant le nœud courant. Par exemple,
        « preceding-sibling::nom[2] » cherche le second élément-frère
        apparaissant avant le nœud courant.
 </li>
 <li>
  « following-sibling » : voir l'axe
        « preceding-sibling », mais à l'envers (
  <b>
   après
  </b>
  le nœud
        courant).
 </li>
 <li>
  « preceding » : cet axe est similaire à
        « preceding-sibling », mais on traverse tous les nœuds qui se
        sont terminés avant nœud courant. Par exemple,
        « preceding::nom[2] » cherche le second élément apparaissant
        avant le nœud courant, même s'il n'a pas le même parent.
 </li>
 <li>
  « following » : voir l'axe « preceding », mais
        à l'envers.
 </li>
 <li>
  « descendant  » : voir l'axe « ancestor », mais
        à l'envers.
 </li>
 <li>
  « descendant-or-self » : voir l'axe
        « ancestor-or-self », mais à l'envers.
 </li>
</ul>
