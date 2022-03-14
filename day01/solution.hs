import System.IO

countIncreasing :: [Int] -> Int
countIncreasing l = length $ filter id $ zipWith (<) l (tail l)

part1 = countIncreasing

part2 :: [Int] -> Int
part2 l =
    let triples = zip3 l (tail l) (tail $ tail l)
        tripleSums = map (\(x,y,z) -> x + y + z) triples
    in countIncreasing tripleSums

main = do
    contents <- readFile "input"
    let numbers = map read (lines contents)
    print $ part1 numbers
    print $ part2 numbers