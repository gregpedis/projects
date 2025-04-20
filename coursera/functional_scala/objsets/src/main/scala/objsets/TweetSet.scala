package objsets

import TweetReader.*

/** A class to represent tweets.
  */
class Tweet(val user: String, val text: String, val retweets: Int) {

  override def toString: String =
    "User: " + user + "\n" +
      "Text: " + text + " [" + retweets + "]"
}

/** This represents a set of objects of type `Tweet` in the form of a binary
  * search tree. Every branch in the tree has two children (two `TweetSet`s).
  * There is an invariant which always holds: for every branch `b`, all elements
  * in the left subtree are smaller than the tweet at `b`. The elements in the
  * right subtree are larger.
  *
  * Note that the above structure requires us to be able to compare two tweets
  * (we need to be able to say which of two tweets is larger, or if they are
  * equal). In this implementation, the equality / order of tweets is based on
  * the tweet's text (see `def incl`). Hence, a `TweetSet` could not contain two
  * tweets with the same text from different users.
  *
  * The advantage of representing sets as binary search trees is that the
  * elements of the set can be found quickly. If you want to learn more you can
  * take a look at the Wikipedia page [1], but this is not necessary in order to
  * solve this assignment.
  *
  * [1] http://en.wikipedia.org/wiki/Binary_search_tree
  */
abstract class TweetSet extends TweetSetInterface {
  // Implement this
  def filter(p: Tweet => Boolean): TweetSet = filterAcc(p, Empty())

  /** This is a helper method for `filter` that propagetes the accumulated
    * tweets.
    */
  def filterAcc(p: Tweet => Boolean, acc: TweetSet): TweetSet

  // Implement this in subclasses.
  def mostRetweeted: Tweet

  // Implement this in subclasses.
  def descendingByRetweet: TweetList

  /** Returns a new `TweetSet` which contains all elements of this set, and the
    * the new element `tweet` in case it does not already exist in this set.
    *
    * If `this.contains(tweet)`, the current set is returned.
    */
  def incl(tweet: Tweet): TweetSet

  /** Returns a new `TweetSet` which excludes `tweet`.
    */
  def remove(tweet: Tweet): TweetSet

  /** Tests if `tweet` exists in this `TweetSet`.
    */
  def contains(tweet: Tweet): Boolean

  /** This method takes a function and applies it to every element in the set.
    */
  def foreach(f: Tweet => Unit): Unit
}

class Empty extends TweetSet {
  // Implement this
  def filterAcc(p: Tweet => Boolean, acc: TweetSet): TweetSet = acc
  // Implement this
  def union(that: TweetSet): TweetSet = that
  // Implement this
  override def mostRetweeted: Tweet =
    throw java.util.NoSuchElementException("i am empty inside.")
  // Implement this
  override def descendingByRetweet: TweetList = Nil

  def contains(tweet: Tweet): Boolean = false

  def incl(tweet: Tweet): TweetSet = NonEmpty(tweet, Empty(), Empty())

  def remove(tweet: Tweet): TweetSet = this

  def foreach(f: Tweet => Unit): Unit = ()
}

class NonEmpty(elem: Tweet, left: TweetSet, right: TweetSet) extends TweetSet {
  // Implement this
  def filterAcc(p: Tweet => Boolean, acc: TweetSet): TweetSet = {
    val includeLeftAcc = left.filterAcc(p, acc)
    val includeBothAcc = right.filterAcc(p, includeLeftAcc)
    if (p(elem)) then { includeBothAcc.incl(elem) }
    else { includeBothAcc }
  }

  // Implement this
  def union(that: TweetSet): TweetSet = {
    val uniqueThat = that.filter(!contains(_))
    uniqueThat match {
      case empty: Empty => this
      case _: NonEmpty  => left.union(right).union(uniqueThat).incl(elem)
    }
  }

  private val _notRetweeted:Tweet = Tweet("","", -1)

  // Implement this
  override def mostRetweeted: Tweet = {
    def getMost(ts: TweetSet): Tweet = {
      ts match {
        case ne: NonEmpty => ne.mostRetweeted
        case _: Empty     => _notRetweeted
      }
    }

    val mostLeft = getMost(left)
    val mostRight = getMost(right)

    if (mostLeft.retweets > mostRight.retweets) then {
      if (mostLeft.retweets > elem.retweets) then { mostLeft }
      else { elem }
    } else if (mostRight.retweets > elem.retweets) then { mostRight }
    else { elem }
  }

  // Implement this
  override def descendingByRetweet: TweetList = {
    val winner = this.mostRetweeted
    val rest = remove(winner)
    rest match {
      case ne: NonEmpty => Cons(winner, rest.descendingByRetweet)
      case _: Empty     => Cons(winner, Nil)
    }
  }

  def contains(x: Tweet): Boolean =
    if (x.text < elem.text) then { left.contains(x) }
    else if (elem.text < x.text) then { right.contains(x) }
    else { true }

  def incl(x: Tweet): TweetSet =
    if (x.text < elem.text) then { NonEmpty(elem, left.incl(x), right) }
    else if (elem.text < x.text) then { NonEmpty(elem, left, right.incl(x)) }
    else { this }

  def remove(tw: Tweet): TweetSet =
    if (tw.text < elem.text) then { NonEmpty(elem, left.remove(tw), right) }
    else if (elem.text < tw.text) then {
      NonEmpty(elem, left, right.remove(tw))
    } else { left.union(right) }

  def foreach(f: Tweet => Unit): Unit = {
    f(elem)
    left.foreach(f)
    right.foreach(f)
  }
}

trait TweetList {
  def head: Tweet
  def tail: TweetList
  def isEmpty: Boolean
  def foreach(f: Tweet => Unit): Unit =
    if (!isEmpty) then {
      f(head)
      tail.foreach(f)
    }
}

object Nil extends TweetList {
  def head = throw java.util.NoSuchElementException("head of EmptyList")
  def tail = throw java.util.NoSuchElementException("tail of EmptyList")
  def isEmpty = true
}

class Cons(val head: Tweet, val tail: TweetList) extends TweetList {
  def isEmpty = false
}

object GoogleVsApple {
  val google = List("android", "Android", "galaxy", "Galaxy", "nexus", "Nexus")
  val apple = List("ios", "iOS", "iphone", "iPhone", "ipad", "iPad")

  // Helper method for brevity.
  def filterByKeywords(keywords: List[String], tweets: TweetSet): TweetSet = {
    tweets.filter(p => keywords.exists(kw => p.text.contains(kw)))
  }

  // Implement this
  lazy val googleTweets: TweetSet = filterByKeywords(google, allTweets)
  // Implement this
  lazy val appleTweets: TweetSet = filterByKeywords(apple, allTweets)
  // Implement this
  lazy val trending: TweetList =
    googleTweets.union(appleTweets).descendingByRetweet
}

object Main extends App {
  // Print the trending tweets
  GoogleVsApple.trending foreach println
}
