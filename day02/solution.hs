getCommand :: String -> String
getCommand s = head $ words s

getCommandNum :: String -> Int
getCommandNum s = read $ last $ words s

commandNumList :: [String] -> String -> [Int]
commandNumList lines command = map getCommandNum $ filter (\x -> getCommand x == command) lines

part1 :: [String] -> Int
part1 lines =
    let sums = map (sum . commandNumList lines) ["forward", "down", "up"]
        horizontalPosition = head sums
        depth = sums !! 1 - (sums !! 2)
    in horizontalPosition * depth

part2 :: [String] -> Int
part2 lines = go lines 0 0 0
  where
    go [] _ depth pos = depth * pos
    go (x:xs) aim depth pos = case getCommand x of
      "forward" -> go xs aim (depth + aim * num) (pos + num)
      "down" -> go xs (aim + num) depth pos
      "up" -> go xs (aim - num) depth pos
      _ -> error "Invalid command"
      where
        num = getCommandNum x

main = do
    contents <- readFile "input"
    let ls = lines contents
    print $ part1 ls
    print $ part2 ls