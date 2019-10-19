package SOLID.OpenClosed;

public class Book {

  private String name;
  private String author;
  private String text;

  //constructor, getters es setters ideertendok

  // EZ ALATT NEM KELL

  // A VALTOZOKAT MODOSITO FUGGVENYEK
  public String replaceWordInText(String word){
    return text.replaceAll(word, text);
  }

  public boolean isWordInText(String word){
    return text.contains(word);
  }

  void printTextToConsole(){
    // our code for formatting and printing the text
  }
}
