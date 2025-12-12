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
            System.out.println(resultat);

        } catch (TransformerException e) {
            System.out.println("Erreur lors de la transformation : " + e.getMessageAndLocation());
        }
    }

    public static String transformer(String fichierXml, String fichierXslt) throws TransformerException {
        TransformerFactory fabrique = TransformerFactory.newInstance();
        Transformer transformateur = fabrique.newTransformer(new StreamSource(new File(fichierXslt)));
        // Transformation vers une chaîne en mémoire
        StringWriter writer = new StringWriter();
        transformateur.transform(
            new StreamSource(new File(fichierXml)),
            new StreamResult(writer)
        );

        return writer.toString();
    }
}