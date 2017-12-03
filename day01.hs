import Data.Char

circularPairs :: [a] -> [(a, a)]
circularPairs [] = []
circularPairs xs = pairs xs
    where pairs [] = []
          pairs (y:ys) = (y, next):(pairs ys)
            where next = if length ys > 0 then head ys else head xs

pairMatches :: (Eq a) => (a, a) -> Bool
pairMatches (x, y) = x == y

main = putStrLn $ show result
    where input = "1122"
          nums = map digitToInt input
          matchingPairs = filter pairMatches (circularPairs nums)
          result = sum $ map fst matchingPairs
