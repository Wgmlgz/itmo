package l5

import java.io.*
import java.time.*
import java.time.format.DateTimeFormatter
import java.util.*
import kotlin.text.*

interface Input {
  fun hasNextLine(): Boolean
  fun nextLine(): String
}

class CsvInput(s: String) : Input {
  val splitted = s.split(",").iterator()
  override fun hasNextLine() = splitted.hasNext()
  override fun nextLine() = splitted.next()
}

class ScannerInput(f: File) : Input {
  var s = Scanner(f)
  override fun hasNextLine() = s.hasNext()
  override fun nextLine() = s.next()
}

interface Output {
  fun println(s: String) {}
  fun print(s: String) {}
}

class NullPrinter : Output {}

interface Io {
  abstract var scanner: Input
  abstract var printer: Output
}

class ConsoleIo : Io {
  override var scanner = Scanner(System.`in`)
  override var printer = PrintWriter(System.out)
}

class FileIo(file: String) : Io {
  var scanner = Scanner(File(file))
  var printer = NullPrinter()
}

// class Io(val input: Input, val output: Output) {
//   companion object {
//     fun fromStdIo(): Io = Io(Scanner(System.`in`), PrintWriter(System.out));
//   }
// }

public class Product(
    name: String,
    coordinates: Coordinates,
    price: Double,
    manufactureCost: Float,
    unitOfMeasure: UnitOfMeasure,
    owner: Person
) {
  companion object {
    var last_id: Long = 1
    fun getId() = last_id++

    fun read(io: Io): Product {
      val formatter = DateTimeFormatter.ofPattern("yyyy-MM-dd HH:mm")

      fun <T> readVal(prompt: String, parser: (s: String) -> T): T {
        var res: T? = null
        io.printer.print("$prompt: ")
        while (res == null) {
          if (!io.scanner.hasNextLine()) throw Exception("unexpected end of input")
          try {
            val line = io.scanner.nextLine()
            if (line != null) {
              res = parser(line)
            }
          } catch (e: Exception) {
            val msg = e.message
            io.printer.println("invalid value: $msg")
          }
        }
        return res
      }

      fun <T> readNested(prompt: String, parser: () -> T): T {
        io.printer.println("$prompt: ")
        return parser()
      }

      return Product(
          readVal("name", { s -> s }),
          readNested(
              "coordinates",
              {
                Coordinates(
                    readVal("coordinates.x", { s -> s.toFloat() }),
                    readVal("coordinates.y", { s -> s.toLong() })
                )
              }
          ),
          readVal("price", { s -> s.toDouble() }),
          readVal("manufactureCost", { s -> s.toFloat() }),
          readVal("unitOfMeasure", { s -> UnitOfMeasure.valueOf(s) }),
          readNested(
              "owner",
              {
                Person(
                    readVal("owner.name", { s -> s }),
                    readVal("owner.birthday", { s -> LocalDateTime.parse(s, formatter) }),
                    readVal("owner.nationality", { s -> Country.valueOf(s) }),
                )
              }
          ),
      )
    }

    // fun fromCsv(s: String): Product {}
  }
  val id = getId()
  val creationDate = ZonedDateTime.now()
}

// fun input(): Product {
//   val res = Product(

//   )
//   return res
// }
//     private Long id; //Поле не может быть null, Значение поля должно быть больше 0, Значение
// этого поля должно быть уникальным, Значение этого поля должно генерироваться автоматически
//     private String name; //Поле не может быть null, Строка не может быть пустой
//     private Coordinates coordinates; //Поле не может быть null
//     private java.time.ZonedDateTime creationDate; //Поле не может быть null, Значение этого поля
// должно генерироваться автоматически
//     private double price; //Значение поля должно быть больше 0
//     private float manufactureCost;
//     private UnitOfMeasure unitOfMeasure; //Поле может быть null
//     private Person owner; //Поле не может быть null
public class Coordinates(x: Float, y: Long) {
  // companion object {
  //   fun parse(input: String): Coordinates?
  // }
}

public class Person(name: String, birthday: LocalDateTime?, nationality: Country) {}

public enum class UnitOfMeasure {
  SQUARE_METERS,
  LITERS,
  GRAMS
}

// inline fun <reified T : Enum<T>> parseEnum(type: String): T? {
//   return try {
//     java.lang.Enum.valueOf(T::class.java, type)
//   } catch (e: IllegalArgumentException) {
//     null
//   }
// }

public enum class Country {
  CHINA,
  SOUTH_KOREA,
  JAPAN
}

// class RegexWhenArgument(val whenArgument: CharSequence) {
//   operator fun equals(other: String) = other is String && Regex(other).matches(whenArgument)

//   override operator fun equals(whenEntry: Any?) = (whenArgument == whenEntry)
// }

class Cmd(val save: String) {
  var io: Io = ConsoleIo()

  val q = PriorityQueue<Product>()

  init {
    val file = File(save)
    file.readLines().forEach { s ->
      io.scanner = CsvReader(s)
      val product = Product.parse(io)
      q.push(product)
    }
  }
  companion object {
    val id = "(\\d+)"
    val item = "(.+)"
  }

  fun help() {
    io.printer.println(commands.joinToString("\n") { (a, b, c) -> b })
  }
  val commands: Array<Triple<String, String, (m: MatchResult) -> Unit>> =
      arrayOf(
          Triple("help", "help : вывести справку по доступным командам", { m -> help() }),
          Triple(
              "info",
              "info : вывести в стандартный поток вывода информацию о коллекции (тип, дата инициализации, количество элементов и т.д.)",
              { m -> true }
          ),
          Triple(
              "show",
              "show : вывести в стандартный поток вывода все элементы коллекции в строковом представлении",
              { m -> true }
          ),
          Triple("add", "add {element} : добавить новый элемент в коллекцию", { m -> true }),
          Triple(
              "update $id",
              "update id {element} : обновить значение элемента коллекции, id которого равен заданному",
              { m -> true }
          ),
          Triple(
              "remove_by_id $id",
              "remove_by_id id : удалить элемент из коллекции по его id",
              { m -> true }
          ),
          Triple("clear", "clear : очистить коллекцию", { m -> true }),
          Triple("save", "save : сохранить коллекцию в файл", { m -> true }),
          Triple(
              "execute_script $item",
              "execute_script file_name : считать и исполнить скрипт из указанного файла. В скрипте содержатся команды в таком же виде, в котором их вводит пользователь в интерактивном режиме.",
              { m -> true }
          ),
          Triple("exit", "exit : завершить программу (без сохранения в файл)", { m -> true }),
          Triple(
              "remove_first",
              "remove_first : удалить первый элемент из коллекции",
              { m -> true }
          ),
          Triple(
              "and_if_max $item",
              "add_if_max {element} : добавить новый элемент в коллекцию, если его значение превышает значение наибольшего элемента этой коллекции",
              { m -> true }
          ),
          Triple(
              "remove_greater $item",
              "remove_greater {element} : удалить из коллекции все элементы, превышающие заданный",
              { m -> true }
          ),
          Triple(
              "min_by_manufacture_cost",
              "min_by_manufacture_cost : вывести любой объект из коллекции, значение поля manufactureCost которого является минимальным",
              { m -> true }
          ),
          Triple(
              "count_less_than_owner $item",
              "count_less_than_owner owner : вывести количество элементов, значение поля owner которых меньше заданного",
              { m -> true }
          ),
          Triple(
              "filter_contains_name $item",
              "filter_contains_name name : вывести элементы, значение поля name которых содержит заданную подстроку",
              { m -> true }
          ),
          Triple(".*", "", { m -> io.printer.println("unknown command") }),
      )

  fun runCmd(r: String, input: String, cb: (m: MatchResult) -> Unit): Boolean {
    var c = Regex(r).find(input)
    if (c == null) return false
    cb(c)
    return true
  }
  fun cmd(input: String) {

    for ((r, help, cb) in commands) if (runCmd(r, input, cb)) break
  }

  fun start() {
    while (io.scanner.hasNextLine()) {
      cmd(io.scanner.nextLine())
    }
  }
}

fun main() {
  val cmd = Cmd()
  cmd.cmd("help")
  cmd.cmd("update id 666")
  cmd.cmd("update id")
  cmd.cmd("update id 777")

  cmd.start()
}
