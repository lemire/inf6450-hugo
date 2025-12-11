<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet version="1.0"
                xmlns:xsl="http://www.w3.org/1999/XSL/Transform">

  <xsl:output method="html" encoding="UTF-8" indent="yes"/>

  <xsl:template match="/">
    <html>
      <head>
        <meta charset="utf-8"/>
        <title>Ma bibliothèque</title>
        <style>
          body { font-family: Arial, sans-serif; margin: 40px; }
          h1 { color: #2c3e50; }
          table { width: 100%; border-collapse: collapse; margin-top: 20px; }
          th, td { padding: 12px; text-align: left; border-bottom: 1px solid #ddd; }
          th { background-color: #3498db; color: white; }
          tr:nth-child(even) { background-color: #f9f9f9; }
          tr:hover { background-color: #f2f2f2; }
        </style>
      </head>
      <body>
        <h1>Ma petite bibliothèque</h1>
        <p>Nombre de livres : <xsl:value-of select="count(//livre)"/></p>

        <table>
          <thead>
            <tr>
              <th>Titre</th>
              <th>Auteur</th>
              <th>Année</th>
              <th>Prix</th>
            </tr>
          </thead>
          <tbody>
            <xsl:for-each select="bibliotheque/livre">
              <xsl:sort select="annee"/>
              <tr>
                <td><strong><xsl:value-of select="titre"/></strong></td>
                <td><xsl:value-of select="auteur"/></td>
                <td><xsl:value-of select="annee"/></td>
                <td><xsl:value-of select="prix"/> <xsl:value-of select="prix/@devise"/></td>
              </tr>
            </xsl:for-each>
          </tbody>
        </table>

        <p style="margin-top: 50px; color: #7f8c8d;">
          Transformé avec XSLT le <xsl:value-of select="current-date()"/>
        </p>
      </body>
    </html>
  </xsl:template>

</xsl:stylesheet>