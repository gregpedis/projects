package recfun

object RecFun extends RecFunInterface {
  def main(args: Array[String]): Unit = {
    println("Pascal's Triangle")
    for (row <- 0 to 10) {
      for (col <- 0 to row) {
        print(s"${pascal(col, row)} ")
      }
      println()
    }
  }

  /** Exercise 1
    */
  def pascal(c: Int, r: Int): Int = {
    val isCorner = (c == 0 || c == r)
    if (isCorner)
      then { 1 }
    else { pascal(c - 1, r - 1) + pascal(c, r - 1) }
  }

  /** Exercise 2
    */
  def balance(chars: List[Char]): Boolean = {
    def reqBalance(chars: List[Char], count: Int): Boolean = {
      if (count < 0) then { false }
      else if (chars.isEmpty)
        then { count == 0 }
      else {
        chars.head match {
          case '(' => reqBalance(chars.tail, count + 1)
          case ')' => reqBalance(chars.tail, count - 1)
          case _   => reqBalance(chars.tail, count)
        }
      }
    }
    reqBalance(chars, 0)
  }

  /** Exercise 3
    */
  def countChange(money: Int, coins: List[Int]): Int = {
    // coins: the types of coins to be used, in descending order
    // targetMoney: how much money is needed for this iteration
    def count(coins:List[Int], targetMoney: Int): Int = {
      // No money left, no coins used is 1 solution
      if (targetMoney == 0) then { 1 }
      // Target money was overshot, 0 solutions
      // OR
      // No coin left, 0 solutions
      else if (targetMoney < 0 || coins.length <= 0) then { 0 }
      else {
        // This is the count of solutions
        // that do NOT use the coins[coinsAvail-1] coin
        val dontUseLastOneCount = count(coins.tail, targetMoney)
        // This is the count of solutions
        // that use the biggest coin AT LEAST once.
        val useLastOneCount = count(coins, targetMoney - coins.head)
        // Solution is the mutually exclusive sums of the two counts.
        dontUseLastOneCount + useLastOneCount
      }
    }
    count(coins.sortBy(c => -c), money)
  }
}
