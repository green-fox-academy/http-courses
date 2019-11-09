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
        System.out.println(fajlTartalom);

//        Parent root = FXMLLoader.load(getClass().getResource("sample.fxml"));
//        primaryStage.setTitle("Hello World");
//        primaryStage.setScene(new Scene(root, 300, 275));
//        primaryStage.show();
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
