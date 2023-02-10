public class Product {
  private var id: Long,  //Поле не может быть null, Значение поля должно быть больше 0, Значение этого поля должно быть уникальным, Значение этого поля должно генерироваться автоматически
  private var name: String,  //Поле не может быть null, Строка не может быть пустой
  private var coordinates: Coordinates,  //Поле не может быть null
  private var creationDate: java.time.ZonedDateTime, //Поле не может быть null, Значение этого поля должно генерироваться автоматически
  private var price: double,  //Значение поля должно быть больше 0
  private var manufactureCost: float, 
  private var unitOfMeasure: UnitOfMeasure? = null,  //Поле может быть null
  private var owner: Person,  //Поле не может быть null

  constructor {
    
  }
}
public class Coordinates {
  private float x;
  private Long y; //Поле не может быть null
}
public class Person {
  private String name; //Поле не может быть null, Строка не может быть пустой
  private java.time.LocalDateTime birthday; //Поле может быть null
  private Country nationality; //Поле не может быть null
}
public enum UnitOfMeasure {
  SQUARE_METERS,
  LITERS,
  GRAMS;
}
public enum Country {
  CHINA,
  SOUTH_KOREA,
  JAPAN;
}

fun main(args : Array<String>) {
  println("Hello, World!")
}