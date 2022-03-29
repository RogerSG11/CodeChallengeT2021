import javax.xml.soap.Text;
import java.io.*;
import java.time.DateTimeException;
import java.time.DayOfWeek;
import java.time.LocalDate;
import java.time.format.TextStyle;
import java.util.*;

public class Main {

    // Language tags
    static Map<String,String> langs = new HashMap<String,String>() {{
        put("CA", "ca-ES");
        put("CZ", "cs-CZ");
        put("DE", "de-DE");
        put("DK", "da-DK");
        put("EN", "en-US");
        put("ES", "es-ES");
        put("FI", "fi-FI");
        put("FR", "fr-FR");
        put("IS", "is-IS");
        put("GR", "el-GR");
        put("HU", "hu-HU");
        put("IT", "it-IT");
        put("NL", "nl-NL");
        put("VI", "vi-VN");
        put("PL", "pl-PL");
        put("RO", "ro-RO");
        put("RU", "ru-RU");
        put("SE", "sv-SE");
        put("SI", "sl-SI");
        put("SK", "sk-SK");
    }};

    public static void main(String[] args) {
        //System.out.println("Hello World!");
        try {
            String name = "submit";

            File fin = new File("textfiles/" + name + "Input.txt");
            Scanner input = new Scanner(fin);
            FileWriter fout = new FileWriter("textfiles/" + name + "Output.txt");

            int N = Integer.parseInt(input.nextLine());
            for (int n = 1; n <= N; ++n) {
                String[] data = input.nextLine().split(":");
                String[] dateFields = data[0].split("-");
                String lang = data[1];

                // Check language valid
                if (!langs.containsKey(lang)) {
                    //System.out.printf("Case #%d: INVALID_LANGUAGE\n", n);
                    fout.write(String.format("Case #%d: INVALID_LANGUAGE\n", n));
                    continue;
                }

                // Get day of week
                int year = Integer.parseInt(dateFields[0].length() == 4 ? dateFields[0] : dateFields[2]);
                int month = Integer.parseInt(dateFields[1]);
                int day = Integer.parseInt(dateFields[0].length() == 4 ? dateFields[2] : dateFields[0]);
                try {
                    LocalDate date = LocalDate.of(year, month, day);
                    DayOfWeek dayOfWeek = date.getDayOfWeek();
                    // Set language
                    Locale langLoc = Locale.forLanguageTag(langs.get(lang));
                    // Print result
                    String dow = dayOfWeek.getDisplayName(TextStyle.FULL, langLoc).toLowerCase();
                    fout.write(String.format("Case #%d: %s\n", n, dow));
                    //System.out.printf("Case #%d: %s\n", n, dayOfWeek.getDisplayName(TextStyle.FULL, langLoc).toLowerCase());
                } catch (DateTimeException e) {
                    //System.out.printf("Case #%d: INVALID_DATE\n", n);
                    fout.write(String.format("Case #%d: INVALID_DATE\n", n));
                }
            }

            input.close();
            fout.close();

        } catch (FileNotFoundException e) {
            System.out.println("File not found");
        } catch (IOException e) {
            System.out.println("Error writing");
        }
    }
}
