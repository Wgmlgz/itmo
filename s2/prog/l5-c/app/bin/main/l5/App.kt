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

class ScannerInput(val s: Scanner) : Input {
  override fun hasNextLine() = s.hasNextLine()
  override fun nextLine() = s.nextLine()
}

interface Output {
  fun println(s: String) {}
  fun print(s: String) {}
}

class PrintWriterOutput(val p: PrintWriter) : Output {
  override fun println(s: String) {
    p.println(s)
    p.flush()
  }
  override fun print(s: String) {
    p.print(s)
    p.flush()
  }
}

class NullPrinter : Output {}

interface Io {
  val scanner: Input
  val printer: Output
}

class ConsoleIo : Io {
  override val scanner = ScannerInput(Scanner(System.`in`))
  override val printer = PrintWriterOutput(PrintWriter(System.out))
}

class FileIo(file: String) : Io {
  override var scanner = ScannerInput(Scanner(File(file)))
  override var printer = NullPrinter()
}

public class Product(
    val name: String,
    val coordinates: Coordinates,
    val price: Double,
    val manufactureCost: Float,
    val unitOfMeasure: UnitOfMeasure?,
    val owner: Person
) {
  companion object {
    var last_id: Long = 1
    fun getId() = last_id++

    fun read(input: Input, output: Output): Product {
      val formatter = DateTimeFormatter.ofPattern("yyyy-MM-dd HH:mm")

      fun <T> readVal(prompt: String, parser: (s: String) -> T): T {
        while (true) {
          output.print("$prompt: ")
          if (!input.hasNextLine()) throw Exception("unexpected end of input")
          try {
            return parser(input.nextLine())
          } catch (e: Exception) {
            output.println("error: ${e.message}}")
          }
        }
      }

      fun <T> readNested(prompt: String, parser: () -> T) =
          output.println("$prompt: ").let { parser() }

      return Product(
          readVal("name", { (if (it == "") throw Exception("can't be empty") else it) }),
          readNested(
              "coordinates",
              {
                Coordinates(
                    readVal("coordinates.x", { it.toFloat() }),
                    readVal("coordinates.y", { it.toLong() })
                )
              }
          ),
          readVal(
              "price",
              { (if (it.toDouble() > 0) it.toDouble() else throw Exception("must be > 0")) }
          ),
          readVal(
              "manufactureCost",
              { (if (it.toFloat() > 0) it.toFloat() else throw Exception("must be > 0")) }
          ),
          readVal(
              "unitOfMeasure (${enumValues<UnitOfMeasure>().joinToString { it.name }})",
              { (if (it == "") null else UnitOfMeasure.valueOf(it.uppercase())) }
          ),
          readNested(
              "owner",
              {
                Person(
                    readVal(
                        "owner.name",
                        { (if (it == "") throw Exception("can't be empty") else it) }
                    ),
                    readVal(
                        "owner.birthday (yyyy-MM-dd HH:mm)",
                        { (if (it == "") null else LocalDateTime.parse(it, formatter)) }
                    ),
                    readVal(
                        "owner.nationality (${enumValues<Country>().joinToString { it.name }})",
                        { Country.valueOf(it.uppercase()) }
                    ),
                )
              }
          ),
      )
    }

    fun getCsvHeader() =
        "id name coordinates.x coordinates.y price manufactureCost unitOfMeasure owner.name owner.birthday owner.nationality"
  }
  val id = getId()
  val creationDate = ZonedDateTime.now()
  override fun toString() =
      "$id $name ${coordinates.x} ${coordinates.y} $price $manufactureCost $unitOfMeasure ${owner.name} ${owner.birthday} ${owner.nationality}"
}

public class Coordinates(val x: Float, val y: Long)

public class Person(val name: String, val birthday: LocalDateTime?, val nationality: Country)

public enum class UnitOfMeasure {
  SQUARE_METERS,
  LITERS,
  GRAMS
}

public enum class Country {
  CHINA,
  SOUTH_KOREA,
  JAPAN
}

class Cmd(val save: String) {
  var io: Io = ConsoleIo()
  var alive = true
  val q = PriorityQueue<Product>()

  init {
    try {
      File(save).readLines().forEach {
        val product = Product.read(CsvInput(it), NullPrinter())
        q.add(product)
      }
    } catch (e: FileNotFoundException) {
      io.printer.println("file was'n found, skipping initialization")
    }
  }

  companion object {
    val id = "(\\d+)"
    val item = "(.+)"
  }

  fun help() = io.printer.println(commands.joinToString("\n") { (a, b, c) -> b })

  val commands: Array<Triple<String, String, (m: MatchResult) -> Unit>> =
      arrayOf(
          Triple("help", "help : вывести справку по доступным командам", { help() }),
          Triple(
              "info",
              "info : вывести в стандартный поток вывода информацию о коллекции (тип, дата инициализации, количество элементов и т.д.)",
              { m -> true }
          ),
          Triple(
              "show",
              "show : вывести в стандартный поток вывода все элементы коллекции в строковом представлении",
              {
                io.printer.println(Product.getCsvHeader())
                q.forEach { item -> io.printer.println(item.toString()) }
              }
          ),
          Triple(
              "add",
              "add {element} : добавить новый элемент в коллекцию",
              { q.add(Product.read(io.scanner, io.printer)) }
          ),
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
          Triple(
              "exit",
              "exit : завершить программу (без сохранения в файл)",
              {
                io.printer.println("finishing...")
                alive = false
              }
          ),
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
    if (alive) io.printer.print("-> ")
    while (alive && io.scanner.hasNextLine()) {
      cmd(io.scanner.nextLine())
      if (alive) io.printer.print("-> ")
    }
  }
}

fun main(args: Array<String>) {
  val file = "save.csv"
  if (args.size < 1) {
    println("no save file provided using default: $file")
  } else {
    println("using file path: $file")
  }

  val cmd = Cmd(file)
  cmd.cmd("help")
  cmd.cmd("update id 666")
  cmd.cmd("update id")
  cmd.cmd("update id 777")

  cmd.start()
}
