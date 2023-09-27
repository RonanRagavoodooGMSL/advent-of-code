import * as fs from "fs";

const part1: string[] = fs
  .readFileSync("typescript/2022/day2/test.txt", "utf-8")
  .split("\r\n")
  .map(
    (line: string) =>
      line.charCodeAt(2) -
      87 +
      ((line.charCodeAt(2) - line.charCodeAt(0) + 2) % 3) * 3
  )
  .reduce((total: number, curr: number) => total + curr);

part1;

const part2: string[] = fs
  .readFileSync("typescript/2022/day2/test.txt", "utf-8")
  .split("\r\n")
  .map(
    (line: string) =>
      (line.charCodeAt(2) - 88) * 3 +
      ((line.charCodeAt(0) - 151 + line.charCodeAt(2)) % 3) +
      1
  )
  .reduce((total: number, current: number) => total + current);

part2;
