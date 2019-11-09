package sample;

import javafx.application.Application;
import javafx.stage.Stage;

import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Paths;
import java.util.ArrayList;
import java.util.List;

public class Main extends Application {

    @Override
    public void start(Stage primaryStage) throws Exception{

        System.out.println("Hello");
        List<String> fajlTartalom = fajlbeolvasas("egyszamjatek1.txt");
        List<Jatekos> jatekosok = jatekosBeolvasas(fajlTartalom);
        
//        Parent root = FXMLLoader.load(getClass().getResource("sample.fxml"));
//        primaryStage.setTitle("Hello World");
//        primaryStage.setScene(new Scene(root, 300, 275));
//        primaryStage.show();
    }

    private List<Jatekos> jatekosBeolvasas(List<String> fajlTartalom) {
        List<Jatekos> jatekosok = new ArrayList<>();
        for (String jatekosSzoveg : fajlTartalom) {
            String[] jatekosAdatok = jatekosSzoveg.split(" ");
            String nev = jatekosAdatok[0];
            int[] tippek = jatekosTippekBegyujtese(jatekosAdatok);
            Jatekos jatekos = new Jatekos(nev, tippek);
            jatekosok.add(jatekos);
        }
        return jatekosok;
    }

    private int[] jatekosTippekBegyujtese(String[] jatekosAdatok) {
        int[] tippek = new int[jatekosAdatok.length - 1];
        for (int i = 1; i < jatekosAdatok.length; i++) {
            tippek[i - 1] = Integer.parseInt(jatekosAdatok[i]);
        }
        return tippek;
    }

    private List<String> fajlbeolvasas(String fajlNev) {
        try {
            return Files.readAllLines(Paths.get(fajlNev));
        } catch (IOException e) {
            System.err.println("Nem sikerult beolvasni a fajlt.");
            return new ArrayList<>();
        }
    }


    public static void main(String[] args) {
        launch(args);
    }
}
