import javax.xml.xpath.*;
import javax.xml.namespace.QName;
import javax.xml.parsers.DocumentBuilder;
import javax.xml.parsers.DocumentBuilderFactory;
import org.w3c.dom.Document;
import java.io.File;

public class SimpleXPath {
    public static void main(String[] args) throws Exception {
        // Fichier XML à lire
        File xmlFile = new File("livres.xml");

        // Construire le document DOM
        DocumentBuilderFactory factory = DocumentBuilderFactory.newInstance();
        DocumentBuilder builder = factory.newDocumentBuilder();
        Document doc = builder.parse(xmlFile);

        // Créer l'objet XPath
        XPath xpath = XPathFactory.newInstance().newXPath();

        // === Exemples d'expressions XPath ===

        // 1. Tous les titres de livres
        String expr1 = "//livre/titre";
        printResult(xpath, doc, expr1, XPathConstants.NODESET);

        // 2. Le prix du premier livre
        String expr2 = "//livre[1]/prix";
        printResult(xpath, doc, expr2, XPathConstants.STRING);

        // 3. Tous les livres de plus de 30 €
        String expr3 = "//livre[prix > 30]";
        printResult(xpath, doc, expr3, XPathConstants.NODESET);

        // 4. Nombre total de livres
        String expr4 = "count(//livre)";
        printResult(xpath, doc, expr4, XPathConstants.NUMBER);
    }

    private static void printResult(XPath xpath, Document doc, String expression, QName returnType) throws XPathExpressionException {
        Object result = xpath.evaluate(expression, doc, returnType);

        System.out.print(expression + "  →  ");

        if (returnType == XPathConstants.NODESET) {
            var nodes = (org.w3c.dom.NodeList) result;
            for (int i = 0; i < nodes.getLength(); i++) {
                System.out.print(nodes.item(i).getTextContent());
                if (i < nodes.getLength() - 1) System.out.print(" | ");
            }
            System.out.println();
        } else if (returnType == XPathConstants.STRING) {
            System.out.println((String) result);
        } else if (returnType == XPathConstants.NUMBER) {
            System.out.println(((Number) result).doubleValue());
        } else {
            System.out.println(result);
        }
    }
}