import javax.xml.transform.*;
import javax.xml.transform.stream.StreamSource;
import javax.xml.transform.stream.StreamResult;
import java.io.File;
import java.io.StringWriter;

public class XmlVersConsole {

    public static void main(String[] args) {

        String xml  = "livres.xml";
        String xslt = "livres-vers-html.xsl";

        try {
            String resultat = transformer(xml, xslt);
            // Affichage direct du résultat
            System.out.println(resultat);

        } catch (TransformerException e) {
            System.err.println("Erreur lors de la transformation : " + e.getMessageAndLocation());
            e.printStackTrace();
        }
    }

    public static String transformer(String fichierXml, String fichierXslt) throws TransformerException {

        TransformerFactory fabrique = TransformerFactory.newInstance();

        // Sécurité recommandée
        fabrique.setFeature(javax.xml.XMLConstants.FEATURE_SECURE_PROCESSING, true);

        // Chargement de la feuille XSLT
        Transformer transformateur = fabrique.newTransformer(new StreamSource(new File(fichierXslt)));

        // Pour un résultat lisible dans la console
        transformateur.setOutputProperty(OutputKeys.INDENT, "yes");
        transformateur.setOutputProperty(OutputKeys.ENCODING, "UTF-8");
        // Pour les transformations HTML (facultatif mais souvent utile)
        transformateur.setOutputProperty(OutputKeys.METHOD, "xml"); // ou "html" ou "text"

        // Transformation vers une chaîne en mémoire
        StringWriter writer = new StringWriter();
        transformateur.transform(
            new StreamSource(new File(fichierXml)),
            new StreamResult(writer)
        );

        return writer.toString();
    }
}