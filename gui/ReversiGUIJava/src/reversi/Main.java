package reversi;

import javafx.application.Application;
import javafx.fxml.FXMLLoader;
import javafx.scene.Group;
import javafx.scene.Parent;
import javafx.scene.Scene;
import javafx.stage.Stage;

public class Main extends Application {

    private static final int width = 400;
    private static final int height = 400;

    @Override
    public void start(Stage primaryStage) throws Exception{
        Tabla tabla = new Tabla("assets/allas.txt");
        Group root = new Group();
        primaryStage.setTitle("Reversi");
        primaryStage.setScene(new Scene(root, width, height));
        tabla.megjelenit(root, width, height);
        primaryStage.show();
    }


    public static void main(String[] args) {
        launch(args);
    }
}
