package reversi;

import javafx.application.Application;
import javafx.fxml.FXMLLoader;
import javafx.scene.Group;
import javafx.scene.Parent;
import javafx.scene.Scene;
import javafx.scene.paint.Color;
import javafx.stage.Stage;

public class Main extends Application {

    @Override
    public void start(Stage primaryStage) throws Exception{
        Tabla tabla = new Tabla("allas.txt", primaryStage);
        Group tablaElemek = new Group();
        tabla.megjelenit(tablaElemek);

        primaryStage.setTitle("Reversi");
        int tablaSzelesseg = tabla.allas[0].length * Tabla.MEZO_MERET;
        int tablaMagassag = tabla.allas.length * Tabla.MEZO_MERET;
        primaryStage.setScene(new Scene(tablaElemek, tablaSzelesseg, tablaMagassag, Color.LIGHTGRAY));
        primaryStage.show();
    }


    public static void main(String[] args) {
        launch(args);
    }
}
