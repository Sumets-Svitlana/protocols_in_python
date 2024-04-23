object main extends App {
  def add(x: Int, y: Int): Int = {
    x + y
  }

  def add(x: String, y: String): String = {
    x + y
  }

  println(add(2, 3))
  println(add("str1", "str2"))
}