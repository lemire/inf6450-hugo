---
title: "Laboratoire XSLT"
weight: 80
---
<h1 class="">
 Laboratoire XSLT
</h1>
<p>
 Vous pouvez maintenant expérimenter avec un document XSLT un peu plus
    sophistiqué. Vous trouverez sur cette page un document DocBook et sa
    transformation. Nous vous invitons à modifier la transformation et le
    document XML d'origine afin de vous assurez que vous maîtrisez bien le XSLT.
</p>
<p>
 Instructions : il suffit de saisir un fichier XML source et une
    transformation
    XSLT valable et d'appuyer sur le bouton.
</p>
<p style="color: #4b5563; margin-bottom: 1rem; line-height: 1.5;">
 <strong>
  Instructions :
 </strong>
 <span>
  Saisissez un fichier XML source et une transformation XSLT valide, puis cliquez sur « Transformer ». Vous pouvez réinitialiser les champs avec le bouton « Réinitialiser ».
 </span>
 <br/>
</p>
<div style="margin-top: 1.5rem;">
 <div style="margin-bottom: 1.5rem;">
  <label for="xmlsource" style="display: block;  font-weight: 500; color: #374151; margin-bottom: 0.5rem;">
   Fichier XML :
  </label>
  <textarea aria-describedby="xmlsource-help" id="xmlsource" placeholder="Saisissez votre XML ici" rows="10" style="width: 100%; border: 1px solid #d1d5db; border-radius: 6px; padding: 12px; line-height: 1.5; resize: vertical; box-shadow: inset 0 1px 2px rgba(0, 0, 0, 0.05);">&lt;book&gt;
        &lt;bookinfo&gt;
        &lt;title&gt;Notre documentation&lt;/title&gt;
        &lt;author&gt;
        &lt;firstname&gt;Alexis&lt;/firstname&gt;
        &lt;surname&gt;Letrotteur&lt;/surname&gt;
        &lt;/author&gt;
        &lt;copyright&gt;&lt;year&gt;2004&lt;/year&gt;&lt;holder&gt;Bell
        Canada&lt;/holder&gt;&lt;/copyright&gt;
        &lt;/bookinfo&gt;
        &lt;chapter&gt;
        &lt;title&gt;Premier chapitre&lt;/title&gt;
        &lt;section&gt;
        &lt;title&gt;Première section du premier chapitre&lt;/title&gt;
        &lt;para&gt;Mettre ici le premier paragraphe de la première
        section.&lt;/para&gt;
        &lt;/section&gt;
        &lt;/chapter&gt;
        &lt;/book&gt;</textarea>
 </div>
 <div style="margin-bottom: 1.5rem;">
  <label for="xstlsource" style="display: block;  font-weight: 500; color: #374151; margin-bottom: 0.5rem;">
   Transformation XSLT :
  </label>
  <textarea aria-describedby="xstlsource-help" id="xstlsource" placeholder="Saisissez votre XSLT ici" rows="10" style="width: 100%; border: 1px solid #d1d5db; border-radius: 6px; padding: 12px;  line-height: 1.5; resize: vertical; box-shadow: inset 0 1px 2px rgba(0, 0, 0, 0.05);">&lt;?xml version="1.0"
        encoding="ISO-8859-1"?&gt;
        &lt;xsl:stylesheet version="1.0"
        xmlns:xsl="http://www.w3.org/1999/XSL/Transform"&gt;
        &lt;xsl:output method="html" indent="yes" encoding="ISO-8859-1" /&gt;
        &lt;xsl:template match="book"&gt; &lt;html&gt;
        &lt;head&gt;&lt;xsl:apply-templates select="bookinfo"/&gt;&lt;/head&gt;
        &lt;body&gt;&lt;h1&gt;&lt;xsl:value-of select="bookinfo/title"
        /&gt;&lt;/h1&gt;
        &lt;p style="text-indent:1em;"&gt;
        &lt;xsl:value-of select="bookinfo/author/firstname" /&gt;
        &lt;xsl:text&gt; &lt;/xsl:text&gt;
        &lt;xsl:value-of select="bookinfo/author/surname" /&gt;
        © &lt;xsl:value-of select="bookinfo/copyright/year" /&gt;
        &lt;/p&gt;&lt;h2&gt;Table des matières&lt;/h2&gt;
        &lt;ul&gt;&lt;xsl:apply-templates select="chapter"
        mode="tdm"/&gt;&lt;/ul&gt;
        &lt;xsl:apply-templates select="chapter"/&gt;
        &lt;/body&gt;&lt;/html&gt;
        &lt;/xsl:template&gt;
        &lt;xsl:template match="bookinfo"&gt;
        &lt;title&gt;&lt;xsl:value-of select="title" /&gt;
        par &lt;xsl:value-of select="author/firstname" /&gt;&lt;xsl:text&gt;
        &lt;/xsl:text&gt;&lt;xsl:value-of select="author/surname" /&gt;
        &lt;/title&gt;
        &lt;/xsl:template&gt;
        &lt;xsl:template match="chapter" mode="tdm"&gt;
        &lt;li&gt;&lt;a href="#{generate-id(.)}"&gt;
        &lt;xsl:number format="digit" lang="fr" count="chapter"/&gt;.
        &lt;xsl:value-of select="title" /&gt;&lt;/a&gt;&lt;/li&gt;
        &lt;ul&gt;&lt;xsl:apply-templates select="section"
        mode="tdm"/&gt;&lt;/ul&gt;
        &lt;/xsl:template&gt;
        &lt;xsl:template match="section" mode="tdm"&gt;
        &lt;li&gt;&lt;a href="#{generate-id(.)}"&gt;
        &lt;xsl:number format="digit" lang="fr"
        count="chapter"/&gt;.&lt;xsl:number format="digit" lang="fr"
        count="section"/&gt;
        &lt;xsl:text&gt; &lt;/xsl:text&gt;
        &lt;xsl:value-of select="title" /&gt;&lt;/a&gt;&lt;/li&gt;
        &lt;/xsl:template&gt;
        &lt;xsl:template match="chapter"&gt;
        &lt;h2&gt;&lt;a name="{generate-id(.)}" &gt;Chapitre
        &lt;xsl:number format="digit" lang="fr"
        count="chapter"/&gt;.&lt;xsl:text&gt; &lt;/xsl:text&gt;
        &lt;xsl:value-of select="title" /&gt;&lt;/a&gt;&lt;/h2&gt;
        &lt;div style="margin-left:1em"&gt;
        &lt;xsl:apply-templates select="section"/&gt; &lt;/div&gt;
        &lt;/xsl:template&gt;
        &lt;xsl:template match="section"&gt;
        &lt;h3&gt;&lt;a name="{generate-id(.)}"&gt;
        &lt;xsl:number format="digit" lang="fr"
        count="chapter"/&gt;.&lt;xsl:number format="digit" lang="fr"
        count="section"/&gt;
        &lt;xsl:text&gt; &lt;/xsl:text&gt;
        &lt;xsl:value-of select="title" /&gt;&lt;/a&gt;&lt;/h3&gt;
        &lt;div style="margin-left:1em"&gt;
        &lt;xsl:apply-templates/&gt;
        &lt;/div&gt;
        &lt;/xsl:template&gt;
        &lt;xsl:template match="itemizedlist"&gt;
        &lt;ul style="margin-left:1em"&gt;&lt;xsl:apply-templates
        /&gt;&lt;/ul&gt;
        &lt;/xsl:template&gt;
        &lt;xsl:template match="orderedlist"&gt;
        &lt;ol style="margin-left:1em"&gt;&lt;xsl:apply-templates
        /&gt;&lt;/ol&gt;
        &lt;/xsl:template&gt;
        &lt;xsl:template match="listitem"&gt;
        &lt;li style="text-indent:0.5em"&gt;&lt;xsl:apply-templates
        /&gt;&lt;/li&gt;
        &lt;/xsl:template&gt;
        &lt;xsl:template match="programlisting"&gt;
        &lt;pre style="color:blue;background-color:rgb(200,200,200);
        margin-left:1em"&gt;
        &lt;code&gt;
        &lt;xsl:apply-templates /&gt;
        &lt;/code&gt;&lt;/pre&gt;
        &lt;/xsl:template&gt;
        &lt;xsl:template match="para"&gt;
        &lt;xsl:choose&gt;
        &lt;xsl:when test="name(..) = 'listitem'"&gt;
        &lt;xsl:apply-templates /&gt;&lt;/xsl:when&gt;
        &lt;xsl:otherwise&gt;&lt;p&gt;&lt;xsl:apply-templates /&gt;&lt;/p&gt;
        &lt;/xsl:otherwise&gt;
        &lt;/xsl:choose&gt;
        &lt;/xsl:template&gt;
        &lt;xsl:template match="title" /&gt;
        &lt;/xsl:stylesheet&gt;</textarea>
 </div>
 <div style="margin-bottom: 1.5rem;">
  <p style=" font-weight: 500; color: #374151; margin-bottom: 0.5rem;">
   Résultat :
  </p>
  <div aria-live="polite" id="sol" style="min-height: 100px; background-color: #f9fafb; border: 1px solid #d1d5db; border-radius: 6px; padding: 12px;  color: #1f2937; overflow: auto;">
   émotion
  </div>
  <p aria-live="assertive" id="error" style="color: #dc2626;  margin-top: 0.5rem; display: none;">
   Erreur : Veuillez vérifier votre XML ou XSLT.
  </p>
 </div>
 <div style="text-align: center;">
  <button onclick="applyXSLT()" style="background-color: #3b82f6; color: white; font-weight: 600; padding: 8px 16px; border-radius: 6px; border: none; cursor: pointer;" type="button">
   Transformer
  </button>
  <button onclick="resetFields()" style="background-color: #6b7280; color: white; font-weight: 600; padding: 8px 16px; border-radius: 6px; border: none; cursor: pointer; margin-left: 10px;" type="button">
   Réinitialiser
  </button>
 </div>
</div>
<script>
 const defaultXML = `<?xml version="1.0" ?> 
<monmessage>
    <de>Jean</de> 
    <a>Pierre</a> 
    <titre type="émotion">Ouch!</titre> 
    <corps>Maman!</corps> 
</monmessage>`;
    const defaultXSLT = `<?xml version="1.0" ?> 
<xsl:stylesheet version="1.0" 
    xmlns:xsl="http://www.w3.org/1999/XSL/Transform">
    <xsl:template match="/">
                <xsl:value-of select="//titre/@type" />
    </xsl:template>
</xsl:stylesheet>`;
    function applyXSLT() {
        const xmlSource = document.getElementById('xmlsource').value;
        const xsltSource = document.getElementById('xstlsource').value;
        const resultDiv = document.getElementById('sol');
        const errorDiv = document.getElementById('error');
        // Reset previous state
        resultDiv.innerHTML = '';
        errorDiv.style.display = 'none';
        try {
            // Parse XML
            const xmlParser = new DOMParser();
            const xmlDoc = xmlParser.parseFromString(xmlSource, 'application/xml');
            if (xmlDoc.getElementsByTagName('parsererror').length > 0) {
                throw new Error('XML invalide');
            }
            // Parse XSLT
            const xsltDoc = xmlParser.parseFromString(xsltSource, 'application/xml');
            if (xsltDoc.getElementsByTagName('parsererror').length > 0) {
                throw new Error('XSLT invalide');
            }
            // Create XSLT processor
            const xsltProcessor = new XSLTProcessor();
            xsltProcessor.importStylesheet(xsltDoc);
            // Apply transformation
            const resultFragment = xsltProcessor.transformToFragment(xmlDoc, document);
            // Clear and append result
            resultDiv.innerHTML = '';
            if (resultFragment) {
                resultDiv.appendChild(resultFragment);
            }
            // If result is empty, show a fallback message
            if (!resultDiv.textContent.trim()) {
                resultDiv.textContent = 'Aucun contenu généré. Vérifiez votre XSLT.';
            }
        } catch (error) {
            errorDiv.textContent = `Erreur : ${error.message || 'Transformation échouée. Vérifiez votre XML ou XSLT.'}`;
            errorDiv.style.display = 'block';
        }
    }
    function resetFields() {
        const xmlSource = document.getElementById('xmlsource');
        const xsltSource = document.getElementById('xstlsource');
        const resultDiv = document.getElementById('sol');
        const errorDiv = document.getElementById('error');
        xmlSource.value = defaultXML;
        xsltSource.value = defaultXSLT;
        resultDiv.innerHTML = '';
        errorDiv.style.display = 'none';
    }
    // Real-time validation for XML
    document.getElementById('xmlsource').addEventListener('input', function() {
        const errorDiv = document.getElementById('error');
        try {
            const xmlParser = new DOMParser();
            const xmlDoc = xmlParser.parseFromString(this.value, 'application/xml');
            if (xmlDoc.getElementsByTagName('parsererror').length > 0) {
                errorDiv.textContent = 'Erreur : XML invalide';
                errorDiv.style.display = 'block';
            } else {
                errorDiv.style.display = 'none';
            }
        } catch {
            errorDiv.textContent = 'Erreur : XML invalide';
            errorDiv.style.display = 'block';
        }
    });
</script>
