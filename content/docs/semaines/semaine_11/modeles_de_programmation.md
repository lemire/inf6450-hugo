---
title: "Modèles de programmation"
weight: 20
---
<style>
 .codeblock {
            background:#282c34; color:#abb2bf; padding:18px; border-radius:8px; overflow-x:auto;
            font-family: Consolas, Monaco, 'Courier New', monospace; font-size:0.94em; line-height:1.5;
            margin:1.8em 0;
        }
        .xmlblock {
            background:#f8fafc; border:1px solid #cbd5e1; color:#2d3748; padding:18px; border-radius:8px;
            overflow-x:auto; font-family: Consolas, Monaco, 'Courier New', monospace; font-size:0.94em;
            margin:1.8em 0;
        }
        code {background:#e5e7eb; padding:3px 7px; border-radius:4px; font-size:0.95em;}
</style>
<h1>
 Modèles de programmation XML
</h1>
<p>
 Il y a plusieurs façons de traiter du XML. Chaque méthode a ses avantages et ses inconvénients. Bien que ce module s’intéresse surtout à l’approche DOM, il est important de connaître l’ensemble des méthodologies possibles et d’avoir une idée des forces et faiblesses relatives de chacune.
</p>
<h3>
 Traitement du XML comme du texte
</h3>
<p>
 Un fichier XML est d’abord un fichier texte. Comme certains langages, tel Java, savent bien traiter les fichiers en format texte, ils peuvent directement traiter le XML.
</p>
<pre><span style="color:#e06c75;">int</span> montant = <span style="color:#d19a66;">10</span><span style="color:#abb2bf;">;</span>
<span style="color:#e06c75;">String</span> nom = <span style="color:#98c379;">"Gérard Beauford"</span><span style="color:#abb2bf;">;</span>
<span style="color:#61afef;">System</span>.<span style="color:#61afef;">out</span>.<span style="color:#61afef;">println</span>(<span style="color:#98c379;">"&lt;?xml version=\"1.0\" ?&gt;\n&lt;facture&gt;&lt;montant&gt;"</span> + montant +
    <span style="color:#98c379;">"&lt;/montant&gt;&lt;nom&gt;"</span> + nom + <span style="color:#98c379;">"&lt;/nom&gt;&lt;/facture&gt;"</span>);</pre>
<p>
 Cependant, comment savoir si le XML produit est bien formé ? Dans l’exemple précédent, le document affiché ne sera pas du XML bien formé à cause de l’accent dans « Gérard » si l’environnement n’utilise pas UTF-8. Il est donc préférable d’utiliser des librairies dédiées au XML.
</p>
<div class="xmlblock">
 &lt;?xml version="1.0" encoding="ISO-8859-1" standalone="no"?&gt;
&lt;facture&gt;
  &lt;montant&gt;432&lt;/montant&gt;
  &lt;nom&gt;Gérard Beauford&lt;/nom&gt;
&lt;/facture&gt;
</div>
<div class="xmlblock">
 &lt;?xml version="1.0" encoding="ISO-8859-1" standalone="yes"?&gt;
&lt;!DOCTYPE facture [
  &lt;!ELEMENT facture (montant, nom)&gt;
  &lt;!ELEMENT montant (#PCDATA)&gt;
  &lt;!ELEMENT nom (#PCDATA)&gt;
  &lt;!ATTLIST nom surnom CDATA "Joe"&gt;
]&gt;
&lt;facture&gt;&lt;montant&gt;432&lt;/montant&gt;&lt;nom&gt;Gérard Beauford&lt;/nom&gt;&lt;/facture&gt;
</div>
<h3>
 Traitement événementiel
</h3>
<p>
 Le traitement événementiel (SAX, XNI…) lit le document séquentiellement et déclenche des événements.
</p>
<p>
 Pour le document suivant :
</p>
<div class="xmlblock">
 &lt;facture&gt;&lt;montant&gt;432&lt;/montant&gt;&lt;nom&gt;Maman&lt;/nom&gt;&lt;/facture&gt;
</div>
<p>
 Événements SAX générés :
</p>
<ol>
 <li>
  Début du document
 </li>
 <li>
  Début d’un élément « facture »
 </li>
 <li>
  Début d’un élément « montant »
 </li>
 <li>
  Texte « 432 »
 </li>
 <li>
  Fin d’un élément « montant »
 </li>
 <li>
  Début d’un élément « nom »
 </li>
 <li>
  Texte « Maman »
 </li>
 <li>
  Fin d’un élément « nom »
 </li>
 <li>
  Fin d’un élément « facture »
 </li>
 <li>
  Fin du document
 </li>
</ol>
<pre><span style="color:#c678dd;">import</span> <span style="color:#abb2bf;">java.io.*;</span>
<span style="color:#c678dd;">import</span> <span style="color:#abb2bf;">org.xml.sax.*;</span>
<span style="color:#c678dd;">import</span> <span style="color:#abb2bf;">org.xml.sax.helpers.*;</span>

<span style="color:#c678dd;">public</span> <span style="color:#c678dd;">class</span> <span style="color:#61afef;">MonApplicationSAX</span> <span style="color:#c678dd;">extends</span> DefaultHandler {

    <span style="color:#c678dd;">public</span> <span style="color:#abb2bf;">void</span> <span style="color:#61afef;">startElement</span>(String uri, String name, String qName, Attributes atts) {
        <span style="color:#c678dd;">if</span> (uri.length() &gt; <span style="color:#d19a66;">0</span>)
            System.out.<span style="color:#61afef;">println</span>(<span style="color:#98c379;">"Début de l’élément "</span> + uri + <span style="color:#98c379;">":"</span> + qName);
        <span style="color:#c678dd;">else</span>
            System.out.<span style="color:#61afef;">println</span>(<span style="color:#98c379;">"Début de l’élément "</span> + name);
    }

    <span style="color:#c678dd;">public</span> <span style="color:#abb2bf;">void</span> <span style="color:#61afef;">endElement</span>(String uri, String name, String qName) {
        <span style="color:#c678dd;">if</span> (uri.length() &gt; <span style="color:#d19a66;">0</span>)
            System.out.<span style="color:#61afef;">println</span>(<span style="color:#98c379;">"Fin de l’élément "</span> + uri + <span style="color:#98c379;">":"</span> + qName);
        <span style="color:#c678dd;">else</span>
            System.out.<span style="color:#61afef;">println</span>(<span style="color:#98c379;">"Fin de l’élément "</span> + name);
    }

    <span style="color:#c678dd;">public</span> <span style="color:#abb2bf;">void</span> <span style="color:#61afef;">characters</span>(<span style="color:#e06c75;">char</span>[] ch, <span style="color:#e06c75;">int</span> start, <span style="color:#e06c75;">int</span> length) {
        System.out.<span style="color:#61afef;">print</span>(<span style="color:#c678dd;">new</span> String(ch, start, length));
    }

    <span style="color:#c678dd;">public</span> <span style="color:#c678dd;">static</span> <span style="color:#abb2bf;">void</span> <span style="color:#61afef;">main</span>(String[] args) <span style="color:#c678dd;">throws</span> Exception {
        XMLReader xr = XMLReaderFactory.<span style="color:#61afef;">createXMLReader</span>();
        xr.<span style="color:#61afef;">setContentHandler</span>(<span style="color:#c678dd;">new</span> MonApplicationSAX());
        xr.<span style="color:#61afef;">parse</span>(<span style="color:#c678dd;">new</span> InputSource(<span style="color:#c678dd;">new</span> FileReader(args[<span style="color:#d19a66;">0</span>])));
    }
}</pre>
<h3>
 Traitement avec itérateurs (StAX)
</h3>
<p>
 StAX propose une approche « pull » plus intuitive.
</p>
<pre><span style="color:#c678dd;">import</span> <span style="color:#abb2bf;">javax.xml.stream.*;</span>
<span style="color:#c678dd;">import</span> <span style="color:#abb2bf;">java.net.*;</span>
<span style="color:#c678dd;">import</span> <span style="color:#abb2bf;">java.io.*;</span>

<span style="color:#c678dd;">public</span> <span style="color:#c678dd;">class</span> <span style="color:#61afef;">staxex</span> {
    <span style="color:#c678dd;">public</span> <span style="color:#c678dd;">static</span> <span style="color:#abb2bf;">void</span> <span style="color:#61afef;">main</span>(String[] args) {
        String input = args[<span style="color:#d19a66;">0</span>];
        <span style="color:#c678dd;">try</span> {
            URL u = <span style="color:#c678dd;">new</span> URL(input);
            InputStream in = u.<span style="color:#61afef;">openStream</span>();
            XMLInputFactory factory = XMLInputFactory.<span style="color:#61afef;">newInstance</span>();
            XMLStreamReader parser = factory.<span style="color:#61afef;">createXMLStreamReader</span>(in);
            <span style="color:#c678dd;">for</span> (<span style="color:#e06c75;">int</span> event = parser.<span style="color:#61afef;">next</span>();
                 event != XMLStreamConstants.END_DOCUMENT;
                 event = parser.<span style="color:#61afef;">next</span>()) {
                <span style="color:#c678dd;">switch</span> (event) {
                    <span style="color:#c678dd;">case</span> XMLStreamConstants.START_ELEMENT:
                        System.out.<span style="color:#61afef;">println</span>(parser.<span style="color:#61afef;">getLocalName</span>());
                        <span style="color:#c678dd;">break</span>;
                    <span style="color:#c678dd;">case</span> XMLStreamConstants.END_ELEMENT:
                        System.out.<span style="color:#61afef;">println</span>(parser.<span style="color:#61afef;">getLocalName</span>());
                        <span style="color:#c678dd;">break</span>;
                    <span style="color:#c678dd;">case</span> XMLStreamConstants.CDATA:
                        System.out.<span style="color:#61afef;">print</span>(parser.<span style="color:#61afef;">getText</span>());
                        <span style="color:#c678dd;">break</span>;
                }
            }
            parser.<span style="color:#61afef;">close</span>();
        } <span style="color:#c678dd;">catch</span> (Exception ex) { System.out.<span style="color:#61afef;">println</span>(ex); }
    }
}</pre>
<h3>
 Traitement avec modèle en arbre (DOM)
</h3>
<p>
 Un document XML peut être vu comme un arbre. Le DOM charge tout le document en mémoire sous forme d’objets.
</p>
<div class="xmlblock">
 &lt;?xml version="1.0" encoding="ISO-8859-1" standalone="yes"?&gt;
&lt;!DOCTYPE facture [...]&gt;
&lt;facture&gt;&lt;montant&gt;432&lt;/montant&gt;
&lt;nom&gt;Gérard Beauford&lt;/nom&gt;&lt;/facture&gt;
</div>
<p>
 Représentation en arbre :
</p>
<pre> Document
 └─ facture
     ├─ montant → "432"
     └─ nom (surnom="Joe") → "Gérard Beauford"</pre>
<h3>
 Transformations (XSLT)
</h3>
<p>
 XSLT est idéal pour les transformations simples (XML → HTML, XML → texte…). Pour des traitements complexes avec bases de données, il est insuffisant.
</p>
<h3>
 XPath
</h3>
<p>
 XPath permet d’extraire très simplement des données depuis Java :
</p>
<pre><span style="color:#c678dd;">import</span> <span style="color:#abb2bf;">javax.xml.parsers.*;</span>
<span style="color:#c678dd;">import</span> <span style="color:#abb2bf;">javax.xml.xpath.*;</span>

DocumentBuilder builder = DocumentBuilderFactory.<span style="color:#61afef;">newInstance</span>()
    .<span style="color:#61afef;">newDocumentBuilder</span>();
Document doc = builder.<span style="color:#61afef;">parse</span>(<span style="color:#98c379;">"http://www.mondomaine.com/monfichier.xml"</span>);

XPath xpath = XPathFactory.<span style="color:#61afef;">newInstance</span>().<span style="color:#61afef;">newXPath</span>();
String title = xpath.<span style="color:#61afef;">evaluate</span>(<span style="color:#98c379;">"//nom/text()"</span>, doc);</pre>
<h3>
 XML comme extension d’un langage (E4X)
</h3>
<p>
 JavaScript for XML permet d’écrire directement du XML dans le code :
</p>
<div class="xmlblock">
 var sales = &lt;sales vendor="John"&gt;
  &lt;item type="peas" price="4" quantity="6"/&gt;
  &lt;item type="carrot" price="3" quantity="10"/&gt;
  &lt;item type="chips" price="5" quantity="3"/&gt;
&lt;/sales&gt;;
</div>
<h3>
 Traitement par abstraction
</h3>
<p>
 De nombreuses bibliothèques (JAXB, bases de données, frameworks) manipulent du XML sans jamais vous forcer à écrire du XML à la main.
</p>
<h3>
 Sérialisation XML (Java Beans)
</h3>
<pre><span style="color:#c678dd;">import</span> <span style="color:#abb2bf;">java.beans.*;</span>
<span style="color:#c678dd;">import</span> <span style="color:#abb2bf;">java.io.*;</span>

<span style="color:#c678dd;">public</span> <span style="color:#c678dd;">class</span> <span style="color:#61afef;">Serialization</span> {
    <span style="color:#c678dd;">public</span> <span style="color:#c678dd;">static</span> <span style="color:#abb2bf;">void</span> <span style="color:#61afef;">main</span>(String[] args) <span style="color:#c678dd;">throws</span> IOException {
        String o = <span style="color:#c678dd;">new</span> String(<span style="color:#98c379;">"Un objet java"</span>);
        File f = <span style="color:#c678dd;">new</span> File(<span style="color:#98c379;">"test.xml"</span>);

        XMLEncoder e = <span style="color:#c678dd;">new</span> XMLEncoder(
            <span style="color:#c678dd;">new</span> BufferedOutputStream(<span style="color:#c678dd;">new</span> FileOutputStream(f)));
        e.<span style="color:#61afef;">writeObject</span>(o); e.<span style="color:#61afef;">close</span>();

        XMLDecoder d = <span style="color:#c678dd;">new</span> XMLDecoder(
            <span style="color:#c678dd;">new</span> BufferedInputStream(<span style="color:#c678dd;">new</span> FileInputStream(f)));
        Object lu = d.<span style="color:#61afef;">readObject</span>(); d.<span style="color:#61afef;">close</span>();
        System.out.<span style="color:#61afef;">println</span>(lu.<span style="color:#61afef;">equals</span>(o)); <span style="color:#5c6370;">// true</span>
    }
}</pre>
<div class="xmlblock">
 &lt;?xml version="1.0" encoding="UTF-8"?&gt;
&lt;java version="21" class="java.beans.XMLDecoder"&gt;
  &lt;string&gt;Un objet java&lt;/string&gt;
&lt;/java&gt;
</div>
<h3>
 Services web
</h3>
<p>
 Les services web REST utilisent simplement HTTP (GET, POST, PUT, DELETE).
</p>
<table>
 <tr>
  <th>
   Méthode
  </th>
  <th>
   Description
  </th>
 </tr>
 <tr>
  <td>
   GET
  </td>
  <td>
   Récupérer une ressource (sûre et idempotente)
  </td>
 </tr>
 <tr>
  <td>
   POST
  </td>
  <td>
   Créer ou modifier (non idempotente)
  </td>
 </tr>
 <tr>
  <td>
   PUT
  </td>
  <td>
   Créer/remplacer une ressource à l’URI donnée
  </td>
 </tr>
 <tr>
  <td>
   DELETE
  </td>
  <td>
   Supprimer une ressource
  </td>
 </tr>
</table>
<p>
 Exemple de requête SRU vers la Library of Congress :
</p>
<pre><span style="color:#c678dd;">import</span> <span style="color:#abb2bf;">org.w3c.dom.*;</span>
<span style="color:#c678dd;">import</span> <span style="color:#abb2bf;">javax.xml.parsers.*;</span>
<span style="color:#c678dd;">import</span> <span style="color:#abb2bf;">javax.xml.xpath.*;</span>

<span style="color:#c678dd;">public</span> <span style="color:#c678dd;">class</span> <span style="color:#61afef;">example</span> {
    <span style="color:#c678dd;">public</span> <span style="color:#c678dd;">static</span> <span style="color:#abb2bf;">void</span> <span style="color:#61afef;">main</span>(String[] args) <span style="color:#c678dd;">throws</span> Exception {
        String base = <span style="color:#98c379;">"http://z3950.loc.gov:7090/voyager?"</span>;
        String query = <span style="color:#98c379;">"operation=searchRetrieve&amp;version=1.1&amp;query=(dc.title=%22First Impressions of the New World%22)"</span>;
        Document doc = DocumentBuilderFactory.<span style="color:#61afef;">newInstance</span>()
            .<span style="color:#61afef;">newDocumentBuilder</span>().<span style="color:#61afef;">parse</span>(base + query);
        XPath xpath = XPathFactory.<span style="color:#61afef;">newInstance</span>().<span style="color:#61afef;">newXPath</span>();
        System.out.<span style="color:#61afef;">println</span>(<span style="color:#98c379;">"leader : "</span> + xpath.<span style="color:#61afef;">evaluate</span>(<span style="color:#98c379;">"//leader/text()"</span>, doc));
    }
}</pre>
