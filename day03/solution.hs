import Data.List (transpose, elemIndices)

binaryToDecimal :: [Bool] -> Int
binaryToDecimal = foldl (\a x -> fromEnum x + 2*a) 0

stringToBinary :: String -> [Bool]
stringToBinary = map (== '1')

common :: (Num a, Ord a) => (a -> a -> Bool) -> String -> Bool
common compareFunc s = uncurry compareFunc zeroesOnesCount
    where zeroesOnesCount = foldr (\x (zeroes, ones) -> if x == '0' then (zeroes+1, ones) else (zeroes, ones+1)) (0, 0) s

mostCommon :: String -> Bool
mostCommon = common (<=)

leastCommon :: String -> Bool
leastCommon = common (>)

getRatingFromReport :: [String] -> Int -> (String -> Bool) -> String
getRatingFromReport [x] _ _ = x
getRatingFromReport lines pos f =
    let column = map (!! pos) lines
        mostOrLeastCommonOfColumn = f column
        indicesOfRowsThatHaveMostCommonValueAtPosition = elemIndices mostOrLeastCommonOfColumn $ stringToBinary column
    in getRatingFromReport (map (lines !!) indicesOfRowsThatHaveMostCommonValueAtPosition) (pos+1) f

part1 :: [String] -> Int
part1 lines =
    let columns = transpose lines
        gamma = map mostCommon columns
        epsilon = map not gamma
    in binaryToDecimal gamma * binaryToDecimal epsilon

part2 :: [String] -> Int
part2 [] = 0
part2 lines =
    let go compareFunc = binaryToDecimal $ stringToBinary $ getRatingFromReport lines 0 compareFunc
        oxygen = go mostCommon
        co2 = go leastCommon
    in oxygen * co2

main = do
    contents <- readFile "input"
    let ls = lines contents
    print $ part1 ls
    print $ part2 ls