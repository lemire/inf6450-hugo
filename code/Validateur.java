import org.xml.sax.SAXException;
import javax.xml.parsers.*;
import java.io.IOException;

public class Validateur {
    public static void main(String[] args) throws Exception {
        DocumentBuilderFactory factory = DocumentBuilderFactory.newInstance();
        factory.setValidating(true);
        DocumentBuilder parser = factory.newDocumentBuilder();
        parser.setErrorHandler(new org.xml.sax.ErrorHandler() {
            public void warning(SAXParseException ex) throws SAXException {
                System.err.println("Avertissement : " + ex.getMessage());
            }
            public void error(SAXParseException ex) throws SAXException {
                System.err.println("Erreur : " + ex.getMessage());
            }
            public void fatalError(SAXParseException ex) throws SAXException {
                System.err.println("Erreur fatale : " + ex.getMessage());
                throw ex;
            }
        });
        parser.parse("fichieravalider.xml");
        System.out.println("Le document est valide.");
    }
}
