---
title: "Les tests"
weight: 100
---

# Les tests

## Utilisation des tests

Dans cette section, nous apprenons à utiliser les tests conditionnels en XSLT avec les éléments xsl:if et xsl:choose, permettant de contrôler le flux de transformation basé sur des conditions XPath.

Nous pouvons tester des conditions à l'aide d'expressions XPath contenant
   les symboles « < », « = », « != »,
   « or », « and », « > »,
   « >= », « <= ».
   Nous utilisons les tests en XSLT avec les éléments « xsl:choose »
   et « xsl:if ».
   Par exemple, faire quelque chose de particulier, si le nom de l'élément
   courant est « montant ».

```xml
<xsl:template match="*">
   <xsl:if test="name(.) = 'montant'">
   Il s'agit d'un élément nommé «montant».
   </xsl:if>
   </xsl:template>
```

La syntaxe de l'élément « xsl:if » est très simple; si la valeur de
   l'expression XPath
   contenue dans l'attribut « test » est vraie, le contenu de
   l'élément « xsl:if » s'applique,
   sinon, on l'omet. Notez qu'il n'y a pas d'élément « xsl:else »

Nous pouvons aussi traiter plusieurs tests dans un seul élément
   « xsl:choose » comme ceci :
```xml
<xsl:template match="*">
   <xsl:choose>
   <xsl:when test="name(.)='montant'">
   Il y a une balise "montant"
   </xsl:when>
   <xsl:when test="name(.)='facture'">
   J'ai trouvé une "facture"
   </xsl:when>
   <xsl:otherwise>
   Je ne connais pas cet élément
   </xsl:otherwise>
   </xsl:choose>
   </xsl:template>
```

On peut aussi combiner plusieurs tests avec les opérateurs logiques
   and, or et not comme le montre le prochain exemple.
```xml
<xsl:template match="*">
   <xsl:choose>
   <xsl:when test="name(.)='montant' or name(.)='facture'">
   Il y a une balise "montant" ou une
   balise "facture"
   </xsl:when>
   <xsl:when test="not(name(.)='argent')">
   Ce n'est ni montant, ni facture, ni argent.
   </xsl:when>
   <xsl:otherwise>
   Je ne connais pas cet élément.
   </xsl:otherwise>
   </xsl:choose>
   </xsl:template>
```

On peut aussi tester la langue d'un élément avec la fonction
   XPath « lang ». L'expression « count(//p[lang('en')]) »
   compte le nombre d'élément « p » ayant été déclaré comme contenant
   du
   texte en langue anglaise.

Observez qu'un élément « xsl:choose » contient plusieurs éléments
   « xsl:when »
   qui sont testés tour à tour, jusqu'à ce qu'une condition soit vraie;
   l'élément « xsl:otherwise »
   est présent pour l'éventualité où tous les tests échouent.
   Tous les tests sont réalisés en séquence et
   dès qu'une condition est vraie, les tests s'arrêtent et le contenu
   de l'élément « xsl:when » est évalué.

En XSLT, il ne faut pas abuser des tests; il est préférable
   d'utiliser des éléments « xsl:template » qui sont plus modulaires.
