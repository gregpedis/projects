-- Resources

-- http://learn.hfm.io/
-- http://learnyouahaskell.com/chapters
-- https://www.haskell.org/tutorial/
-- http://book.realworldhaskell.org/read/

-- Types

-- Haskell is strongly, statically typed.

-- Type annotation on simple values, optional:
-- 42::Int, 'h'::Char, True::Bool

-- Type signature on simple values, optional:
-- someInt::Int, someChar::Char, someBool::Bool

-- Here are some primitives:

-- Numeric
intValue :: Int -- type signature
intValue = 42 :: Int -- variable definition

integerValue = 5 :: Integer -- same as Int, but arbitrary precision

floatValue = 42.69 :: Float

doubleValue = 3.14159 :: Double

-- Character
charValue = 'h'

-- [Char] and String are interchangable
stringValue = "hello" :: String

stringValue' = "hello" :: [Char]

-- Boolean

boolValue = True

-- Functions

-- Haskell functions tells us what something is.
-- They map something(s) to some other thing(s).

-- They have to start with lowercase letter or _
-- Can only contain alphanumeric, _ and ' characters

-- Here are some examples:

-- Maps a number to the next number.
inc x = x + 1 -- function declaration

-- Same method but with type signature.
-- Optional, but provides clarity.
inc2 :: Num a => a -> a -- type signature
inc2 x = x + 1 -- function declaration

-- This hides the Data.List.length function.
-- Be careful to not name functions with predefined names.
-- Might cause ambiguous execution on ghci/build.
length x = x

-- Multiple arguments
myAdd :: Num a => a -> a -> a
myAdd x y = x + y

-- As seen, type signatures do not separate arguments and return value.
-- Everything is separated by a "->", because haskell curries everything.
-- This is a fancy way of saying all functions take a single argument
-- and return either a value of a function that takes a single argument, etc.
-- This also allows partial application in every single function, out of the box.
-- Here is an example:

myAdd2 = myAdd 2

-- [myAdd 2] partially applies 2 to myAdd and returns a function.
-- When [myAdd2 y] is called, [myAdd 2 y] is called, which results in 2+y
-- This can also be written in a less idiomatic but more understandable way:
myAdd2' x = myAdd 2 x

-- Infix application
added = 1 + 2

added' = 1 `myAdd` 2

-- Infx is left-associative, meaning these two are the same:
-- x `fun1` y `fun2` z
-- (x `fun1` y) `fun2` z

-- Prefix application
added'' = (+) 1 2

added''' = myAdd 1 2

-- Typeclasses

-- Haskell groups sets of types in what is called typeclasses.
-- For example, float, double, int, and integer all belong to the Num typeclass.
-- That is useful because the Num typeclass contains functions for numeric ops.
-- For example, the following method can be used to any type that belongs to Num:
numericOperations :: Num a => a -> a -> a -> a -> a -> a
numericOperations a b c d e = a + b - c * d + abs e

-- As declared in the type signature,
-- this function takes 5 values belonging to a type 'a' that belongs to Num
-- and returns a value also belonging to 'a'.
-- Num is the typeclass, 'a' is called a type placeholder.
-- Because of typeclasses, 'numericOperations' is overloaded.
-- That means it can be called with arguments of any type belonging to Num.
-- Here is a demonstration:

numOpsResult = numericOperations 1 2 3 4 5

numOpsResult' = numericOperations 1 2 3 4 5 :: Int

numOpsResult'' = numericOperations 1.0 2 3 4 5

numOpsResult''' = numericOperations 1 2 3 4 5 :: Float

-- Some important typeclasses:
--Show, Read, Eq, Ord, Enum, Bounded
-- Num, Integral, Fractional, Floating, Complex
